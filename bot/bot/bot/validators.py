import typer

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise typer.BadParameter("Side must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise typer.BadParameter("Order type must be MARKET or LIMIT")
    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise typer.BadParameter("Quantity must be greater than 0")
    return quantity

def validate_price(order_type: str, price: float) -> float:
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise typer.BadParameter("Price must be provided and greater than 0 for LIMIT orders")
    return price
