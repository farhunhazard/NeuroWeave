import os
import re
import requests
from urllib.parse import unquote, urlparse, parse_qs
from typing import List, Tuple
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
USE_OPENAI = bool(OPENAI_KEY)

_client = None
def _client_openai():
    global _client
    if _client is None:
        from openai import OpenAI
        _client = OpenAI(api_key=OPENAI_KEY)
    return _client

# ------------------- MULTI-AGENT SYSTEM -------------------
SYSTEM_PRIMERS = {
    "Creative": "You are CreativeAI. Generate bold, novel, visual ideas.",
    "Logic": "You are LogicAI. Structure, validate, and make plans.",
    "Empathy": "You are EmpathAI. Understand human perspectives and emotions.",
    "Data": "You are DataAI. Back insights with evidence and metrics.",
}

MODES = {
    "Planner (Structured)": ["Logic", "Data", "Empathy", "Creative"],
    "Debate (Critical)": ["Logic", "Creative", "Data"],
    "Brainstorm (Divergent)": ["Creative", "Empathy", "Data", "Logic"],
}

# ------------------- CORE LLM AGENTS -------------------
def _llm_call(prompt: str, temperature: float = 0.7, max_tokens: int = 900) -> str:
    """Run OpenAI call if available; otherwise return prompt preview."""
    if not USE_OPENAI:
        return prompt[:200] + " [...]"
    client = _client_openai()
    out = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Be concise, insightful, and actionable."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return out.choices[0].message.content

def _agent_step(role: str, context: str, user_prompt: str, temperature: float) -> str:
    primer = SYSTEM_PRIMERS[role]
    prompt = (
        f"{primer}\n"
        f"User: {user_prompt}\n"
        f"Context: {context[-1200:]}\n"
        f"Reply as {role} with concise, non-repetitive points."
    )
    return _llm_call(prompt, temperature=temperature, max_tokens=380)

def run_collective_session(user_prompt: str, mode: str, temperature: float, max_steps: int):
    roles = MODES.get(mode, MODES["Planner (Structured)"])
    latest_per_role, context = {}, ""

    for _ in range(max_steps):
        for role in roles:
            msg = _agent_step(role, context, user_prompt, temperature)
            latest_per_role[role] = msg
            context = (context + f"\n[{role}] {msg}")[-3000:]

    final_context = "\n".join(f"[{r}] {m}" for r, m in latest_per_role.items())
    final_answer = _llm_call(
        "Combine the agent insights below into ONE cohesive, complete final plan with:\n"
        "- Short executive summary (3–5 sentences)\n"
        "- Bullet points with concrete steps\n"
        "- Measurable goals/metrics\n"
        "- Clear next actions\n\n" + final_context,
        temperature=0.6,
        max_tokens=950,
    )
    ordered = [(r, latest_per_role[r]) for r in ["Logic", "Data", "Empathy", "Creative"] if r in latest_per_role]
    return ordered, final_answer

# ------------------- 🦆 DUCKDUCKGO ARTICLE SEARCH -------------------
def _decode_duck_url(url: str) -> str:
    """Convert DuckDuckGo redirect link (/l/?uddg=...) to real article URL."""
    if "uddg=" in url:
        try:
            qs = parse_qs(urlparse(url).query)
            return unquote(qs.get("uddg", [url])[0])
        except Exception:
            return url
    return url

def generate_concept_articles(concept_text: str, user_prompt: str = "") -> tuple:
    """
    Fetch one relevant article (title + URL) using DuckDuckGo (HTML scrape).
    """
    try:
        query = user_prompt or concept_text[:100]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        html_url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
        res = requests.get(html_url, headers=headers, timeout=20)
        soup = BeautifulSoup(res.text, "html.parser")

        a_tags = soup.select(".result__a, a.result__a")
        for a in a_tags:
            title = a.get_text(strip=True)
            href = _decode_duck_url(a.get("href", ""))
            if "http" in href:
                return (title, href)
    except Exception as e:
        print("🦆 DuckDuckGo article fetch error:", e)
    return ("No related article found", "#")

def fetch_more_articles(query: str) -> list:
    """
    Fetch 3–5 additional articles (title + URL) from DuckDuckGo.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        html_url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
        res = requests.get(html_url, headers=headers, timeout=20)
        soup = BeautifulSoup(res.text, "html.parser")

        results = []
        for a in soup.select(".result__a, a.result__a")[:6]:
            title = a.get_text(strip=True)
            href = _decode_duck_url(a.get("href", ""))
            if "http" in href:
                results.append((title, href))
        return results
    except Exception as e:
        print("🦆 DuckDuckGo 'More Articles' fetch error:", e)
        return []
