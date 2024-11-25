
import sys
from cluster.core.utils import load_env
from cluster.commands import transfer, dex, snipe, portfolio, market

COMMANDS = {
    "transfer": transfer.execute,
    "dex": dex.execute,
    "snipe": snipe.execute,
    "portfolio": portfolio.execute,
    "market": market.execute,
}

def main():
    load_env()
    if len(sys.argv) < 2:
        print("Usage: python -m cluster <command> [options]")
        sys.exit(1)

    command = sys.argv[1]
    if command in COMMANDS:
        COMMANDS[command](sys.argv[2:])
    else:
        print(f"Unknown command: {command}")
        print("Available commands: transfer, dex, snipe, portfolio, market")

if __name__ == "__main__":
    main()
