from binance.client import Client
import logging

class BinanceClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = logging.getLogger("trading_bot")
        base_url = "https://testnet.binancefuture.com" if testnet else None
        self.client = Client(api_key, api_secret, testnet=testnet)
        if base_url:
            self.client.API_URL = base_url

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")

            self.logger.info(f"Order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing order: {e}")
            raise
