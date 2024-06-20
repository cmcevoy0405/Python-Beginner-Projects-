#create item
stock = []

def add_item():
    while True:
            item = input("Item: ").lower()

            try:
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Invalid input. Price and quantity must be numerical")
                continue

            total = price * quantity

            entry = {
                "item": item,
                "price": price,
                "quantity": quantity,
                "total": total
                }

            stock.append(entry)
            print("Item added successfully")
            add_item = input("Too add item press y, to continue press enter: ")
            if add_item == "y":
                continue
            elif add_item == "":
                break


def print_stock():
    print(f"\nFinal stock:")
    print(f"{'item':<15} {'price':<10} {'quantity':<10} {'total':<10}")
    print(f"-" * 35)
    for entry in stock:
        print(f"{entry['item']:<15} £{entry['price']:<10.2f} {entry['quantity']:<10} £{entry['total']:<10.2f}")

def find_item():
    locate = input("what item do you want to find?: ").lower()
    for entry in stock:
        if locate == entry["item"]:
            print(f"\nItem details:")
            print(f"{'item':<15} {'price':<10} {'quantity':<10} {'total':<10}")
            print(f"-" * 35)
            print(f"{entry['item']:<15} £{entry['price']:<10.2f} {entry['quantity']:<10} £{entry['total']:<10.2f}")

def update_item():
    update = input("What item would you like to update?: ").lower()
    for entry in stock:
        if update == entry["item"]:
            new_item = input("item: ").lower()
            new_price = float(input("price:"))
            new_quantity = int(input("quantity: "))
            new_total = new_price * new_quantity

            entry["item"] = new_item
            entry["price"] = new_price
            entry["quantity"] = new_quantity
            entry["total"] = new_total
            print("Item updated")
            return
        else:
            print("Item not found")

def grand_total():
    grand_total = 0
    for entry in stock:
        grand_total += entry["total"]
        formatted_total = f"£{grand_total:.2f}"
        print("-" * 35)
        print(f"Grand Total: {formatted_total:>31}")


def sale():
    item_sold = input("What item has been sold?: ").lower()
    quantity_sold = int(input("How many were sold?: "))


    for entry in stock:
        if item_sold == entry["item"]:
            if quantity_sold <= entry["quantity"]:
                entry["quantity"] -= quantity_sold
                if entry["quantity"] == 0:
                    stock.remove(entry)
                new_total = entry["quantity"] * entry["price"]
                entry["total"] = new_total
                print(f"Updated stock for {item_sold}, remaining stock left is {entry['quantity']}")
            else:
                print(f"Not enough stock remaining, only {entry['quantity']} left")
            break
        elif item_sold != entry["item"]:
            print("Item not found")

def delete_item():
    delete = input("What item do you want to delete?: ").lower()
    for i, entry in enumerate(stock):
        if entry["item"] == delete:
            del stock[i]
            print("Item successfully deleted")
        else:
            print("Item not found")

def return_item():
    item_return = input("What item would you like to return?: ").lower()
    number_return = int(input("How many would you like to return?: "))
    for entry in stock:
        if entry["item"] == item_return:
            entry["quantity"] += number_return
            new_total = entry["quantity"] * entry["price"]
            entry["total"] = new_total
            print(f"Updated stock for {item_return}, stock is now {entry['quantity']}")
        else:
            print("We do not stock this item")

def main():
    while True:
        action = input("To add an item press [1], To view stock press [2], To find an item press [3], To update item press [4], To see total stock press [5], To make sale press [6], To delete item press [7], To return an item press [8], To exit press [q]: ")
        if action == "1":
            add_item()
        elif action == "2":
            print_stock()
            grand_total()
        elif action == "3":
            find_item()
        elif action == "4":
            update_item()
        elif action == "5":
            grand_total()
        elif action == "6":
            sale()
        elif action == "7":
            delete_item()
        elif action == "8":
            return_item()
        elif action == "q":
            break


if __name__ == "__main__":
    main()
