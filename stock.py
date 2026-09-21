import sqlite3

conexao = sqlite3.connect("stock.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, quantity INTEGER NOT NULL, price REAL NOT NULL)""")
conexao.commit()

def add_produtos(name, quantity, price):
    cursor.execute(""" INSERT INTO products (name, quantity, preice) VALUES (?, ?, ?)""", (name, quantity, price))
    conexao.commit()
    print(f"✅ '{name}' added succesfully!")

def sub_produtos(prod_id):
    cursor.execute(""" DELETE FROM products WHERE id = ? """, (prod_id))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Product ID {prod_id} was removed from stock.")
    else:
        print(f"Product ID {prod_id} not found.")

def list_produtos():
    cursor.execute("""SELECT * FROM products""")
    products = cursor.fetchall()
    print("\n-----Stock-----")
    if not products:
        print("Empty Stock :)))")
    else:
        for p in products:
            print(f"ID: {p[0]} | Name: {p[1]} | Qtt: {p[2]} | Price: {p[3]:.2f}€")
    print("-" * 20)

def add_prod():
    name = input("Insert Product Name: ")
    quantity = int(input("Insert Product Quantity: "))
    price = float(input("Insert Product Price: "))
    add_produtos(name, quantity, price)

def sub_prod():
    prod_id = int(input("Insert Product ID: "))
    sub_produtos(prod_id)

def main():
    while True:
        print("1 - Add a Product \n2 - List All Products \n3 - Remove Product \n4 - Exit")
        option = int(input("What do you need? "))
        if option == 1:
            add_prod()
        elif option == 2:
            list_produtos()
        elif option == 3:
            sub_prod()
        elif option == 4:
            break
        else:
            print("Option Not Found")

main()