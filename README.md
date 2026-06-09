# Trading Bot – Binance Futures Testnet

## Setup
1. Clone repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
Add your Binance Testnet API key and secret in cli.py.

Usage
Place a MARKET order:

bash
python cli.py order BTCUSDT BUY MARKET 0.001
Place a LIMIT order:

bash
python cli.py order BTCUSDT SELL LIMIT 0.001 --price 65000
