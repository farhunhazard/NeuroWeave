# modules/ipfs.py
# Handles IPFS file uploads via Pinata for NeuroWeave AI
import os
import requests
import json

PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")

def upload_to_pinata(filename: str, data: bytes, content_type: str):
    """
    Uploads a file to Pinata IPFS and returns (ipfs://CID, CID)
    """
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY,
    }
    files = {"file": (filename, data, content_type)}
    res = requests.post(url, headers=headers, files=files, timeout=60)

    if res.status_code != 200:
        raise RuntimeError(f"Pinata upload failed: {res.text}")

    j = res.json()
    cid = j.get("IpfsHash")
    if not cid:
        raise RuntimeError(f"Unexpected Pinata response: {j}")

    return f"ipfs://{cid}", cid


def upload_metadata_to_pinata(metadata: dict):
    """
    Uploads JSON metadata to Pinata
    """
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY,
        "Content-Type": "application/json",
    }
    res = requests.post(url, headers=headers, data=json.dumps(metadata), timeout=60)
    if res.status_code != 200:
        raise RuntimeError(f"Pinata metadata upload failed: {res.text}")

    j = res.json()
    cid = j.get("IpfsHash")
    return f"ipfs://{cid}", cid
