
from cluster.core.solana_client import SolanaClient

def execute(args):
    if len(args) < 3:
        print("Usage: transfer <amount> <recipient>")
        return

    amount = float(args[0])
    recipient = args[1]

    solana = SolanaClient("https://api.mainnet-beta.solana.com")
    print(f"Sending {amount} SOL to {recipient}...")
    print("Transaction submitted! Hash: fake_transaction_hash")
