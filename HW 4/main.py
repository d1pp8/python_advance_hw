from services.enter_data import seed_data
from services.services import get_all_categories, update_product_price, count_products_by_category, categories_with_many_products
from db.connection import engine, Base

if __name__ == "__main__":

    Base.metadata.create_all(engine)

    seed_data()

    while True:
        print("\n\n")
        print("1.📋All categories with goods")
        print("2.✏️Update")
        print("3.📊Number of products")
        print("4.🔥Categories with more than 1 product")
        print("0.🚪Exit")

        choice = int(input("Enter your choice: "))


        if choice == 1:
            categories = get_all_categories()

            print("\n📦Categories and products:")
            for c in categories:
                print(f"\n{c.name}:")
                for p in c.products:
                    print(f" - {p.name}: {p.price}")

        elif choice == 2:
            # It would be possible to make it so the user could select a product and change the price,
            # but validation would also be needed, and the program is already stretched.
            # name = input("Enter the product: ")
            # new_price = input("Enter new price: ")
            update_product_price()

        elif choice == 3:
            print("\n📊Number of products:")
            for name, count in count_products_by_category():
                print(f"{name}: {count}")

        elif choice == 4:
            print("\n🔥Categories with more than 1 product:")
            for name, count in categories_with_many_products():
                print(f"{name}: {count}")

        elif choice == 0:
            print("\n\nThanks for work!")
            break




