
from cluster.core.solana_client import SolanaClient

def test_transfer():
    client = SolanaClient("https://api.devnet.solana.com")
    balance = client.get_balance("YourPublicKeyHere")
    assert balance > 0, "Balance should be greater than zero"
