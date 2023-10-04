import csv

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.product} from {self.country} (Code: {self.code}) - Cost: {self.cost}, Quantity: {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("/home/makgera/Documents/HYPE DEV/LT01T30/inventory.txt", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                country = row["Country"]
                code = row["Code"]
                product = row["Product"]
                cost = int(row["Cost"])
                quantity = int(row["Quantity"])
                shoe_list.append(Shoe(country, code, product, cost, quantity))
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("File not found!")

def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = int(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print("Shoe data captured and added to the list.")

def view_all():
    print("\n======= Inventory =======")
    for shoe in shoe_list:
        print(shoe)
    print("==========================")

def re_stock():
    min_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe with the lowest quantity is: {min_quantity_shoe}")
    restock_quantity = int(input("Enter the quantity to be added for restocking: "))
    min_quantity_shoe.quantity += restock_quantity
    print(f"Restocked {restock_quantity} units for {min_quantity_shoe.product}.")

def search_shoe():
    search_code = input("Enter the shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == search_code:
            print(f"Found shoe: {shoe}")
            return
    print("Shoe not found!")

def value_per_item():
    print("\n====== Value per Item ======")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: {value}")
    print("============================")

def highest_qty():
    max_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe with the highest quantity is: {max_quantity_shoe}")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main_menu():
    print("\n===== Nike Warehouse Inventory Management =====")
    print("1. Capture New Shoe Data")
    print("2. View All Shoes")
    print("3. Re-stock Shoes")
    print("4. Search Shoe by Code")
    print("5. Calculate Value per Item")
    print("6. Show Shoe with Highest Quantity")
    print("0. Exit")

def main():
    read_shoes_data()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
