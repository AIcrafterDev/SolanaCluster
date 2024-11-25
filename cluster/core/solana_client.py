
from solana.rpc.api import Client

class SolanaClient:
    def __init__(self, rpc_url):
        self.client = Client(rpc_url)

    def get_balance(self, public_key):
        response = self.client.get_balance(public_key)
        if "result" in response:
            return response["result"]["value"]
        raise ValueError("Failed to fetch balance")

    def send_transaction(self, transaction, signers):
        return self.client.send_transaction(transaction, signers)
