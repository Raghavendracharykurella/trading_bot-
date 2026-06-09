import typer
from bot.logging_config import setup_logger
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price
from bot.orders import OrderManager

app = typer.Typer()

@app.command()
def order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    logger = setup_logger()

    # Replace with your Binance Testnet API credentials
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"

    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(order_type, price)

    manager = OrderManager(api_key, api_secret)
    try:
        order = manager.place_order(symbol, side, order_type, quantity, price)
        typer.echo("✅ Order placed successfully!")
        typer.echo(f"Order ID: {order['orderId']}")
        typer.echo(f"Status: {order['status']}")
        typer.echo(f"Executed Qty: {order.get('executedQty')}")
        typer.echo(f"Avg Price: {order.get('avgPrice')}")
    except Exception as e:
        typer.echo(f"❌ Failed to place order: {e}")

if __name__ == "__main__":
    app()
