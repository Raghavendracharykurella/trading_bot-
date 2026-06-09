import logging
from bot.client import BinanceClient

logger = logging.getLogger("trading_bot")

class OrderManager:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = BinanceClient(api_key, api_secret, testnet=testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        logger.info(f"Placing order: {symbol}, {side}, {order_type}, qty={quantity}, price={price}")
        try:
            order = self.client.place_order(symbol, side, order_type, quantity, price)
            logger.info(f"Order response: {order}")
            return order
        except Exception as e:
            logger.error(f"Order failed: {e}")
            raise
