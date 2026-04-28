from db.models import Category, Product
from utilities.context_manager import get_session
from decimal import Decimal

def seed_data():
    with get_session() as session:
        electronics  = Category(name="Electronics", description="Gadgets and devices.")
        books = Category(name="Books", description="Printed books and e-books.")
        clothing = Category(name="Clothing", description="Clothing for men and women.")

        session.add_all([electronics, books, clothing])
        session.flush()

        products  = [
            Product(name="Smartphone", price=Decimal("299.99"), category_id=electronics.id),
            Product(name="Laptop", price=Decimal("499.99"), category_id=electronics.id),
            Product(name="Science fiction novel", price=Decimal("15.99"), category_id=books.id),
            Product(name="Jeans", price=Decimal("40.50"), category_id=clothing.id),
            Product(name="T-shirt", price=Decimal("20.00"), category_id=clothing.id),
        ]
        
        session.add_all(products)