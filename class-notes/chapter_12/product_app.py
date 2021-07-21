from goods_property import Goods

'''
Create an terminal application that user can:

1. add products and prica
2. delete product from list
3. show list with all products

'''

products_list = []


def add_product(x, y):
    products_list.append(Goods(x, y))


while True:
    menu_option = input("1. Add  2.DeleteOne  3.ShowAll 4.Quit \n-->")

    if menu_option == "4":
        break

    if menu_option == "1":
        while True:
            product = input("Enter product \n--> ")

            if product == "q":
                break

            value = int(input("Enter value \n--> "))

            add_product(product, value)

    if menu_option == "3":
        print(f"Total: {len(products_list)}")
        for obj in products_list:
            print(obj.mynumber, obj.name, obj.price)

    if menu_option == "2":
        item_to_delete = input("Enter product number to delete \n-->")

        if item_to_delete in products_list:
            item_to_delete = int(item_to_delete)
            products_list.pop(item_to_delete)
