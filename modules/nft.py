# modules/nft.py
# Handles NFT minting operations for NeuroWeave AI on Celo
import os
import json
from web3 import Web3

CELO_RPC = os.getenv("CELO_RPC", "https://alfajores-forno.celo-testnet.org")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
CONTRACT_ABI_PATH = os.getenv("CONTRACT_ABI_PATH", "contract_abi.json")

web3 = Web3(Web3.HTTPProvider(CELO_RPC))
account = web3.eth.account.from_key(PRIVATE_KEY)

try:
    with open(CONTRACT_ABI_PATH, "r") as f:
        CONTRACT_ABI_JSON = json.load(f)
except Exception:
    CONTRACT_ABI_JSON = []

def mint_nft(recipient: str, metadata_uri: str):
    """
    Mints NFT on Celo Alfajores Testnet with metadata URI (IPFS link)
    """
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI_JSON)
    nonce = web3.eth.get_transaction_count(account.address)
    gas_estimate = contract.functions.safeMint(recipient, metadata_uri).estimate_gas({"from": account.address})

    txn = contract.functions.safeMint(recipient, metadata_uri).build_transaction({
        "from": account.address,
        "nonce": nonce,
        "gas": int(gas_estimate * 1.2),
        "gasPrice": web3.to_wei("2", "gwei"),
        "chainId": 44787  # Alfajores Testnet
    })

    signed_tx = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash.hex(), tx_receipt
