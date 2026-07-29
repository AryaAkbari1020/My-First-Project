class Item:
    """Represents an item in the shopping cart."""
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price

class ShoppingCard:
    """Represents a shopping cart that holds items."""
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = [] # The shopping list, initially empty

    def add_item(self, item: Item):
        """Adds an item to the shopping cart.

        Args:
            item: An instance of the Item class.
        """
        if not isinstance(item, Item):
            raise TypeError("Only Item objects can be added to the cart.")
        self.items.append(item)
        print(f"'{item.name}' با قیمت {item.price:.2f} تومان به سبد خرید اضافه شد.")

    def get_total_cost(self) -> float:
        """Calculates and returns the total cost of all items in the cart.

        Returns:
            The total cost as a float.
        """
        total = sum(item.price for item in self.items)
        return total
if __name__ == "__main__":
    apple = Item("سیب", 15000.50)
    banana = Item("موز", 12000.00)
    orange = Item("پرتقال", 10000.75)


    my_card = ShoppingCard()


    my_card.add_item(apple)
    my_card.add_item(banana)
    my_card.add_item(orange)

   
    total_price = my_card.get_total_cost()
    print(f"\nمجموع هزینه سبد خرید شما: {total_price:.2f} تومان.")
   print(f"خطا در ساخت آیتم: {e}")
