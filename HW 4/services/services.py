from sqlalchemy.orm import joinedload
from sqlalchemy import func

from db.models import Category, Product
from utilities.context_manager import get_session

from decimal import Decimal


def get_all_categories():
    with get_session() as session:
        return session.query(Category).options(joinedload(Category.products)).all()


def update_product_price():
    with get_session() as session:
        product = session.query(Product).filter(Product.name == "Smartphone").first()
        if product:
            product.price = Decimal(349.99)

def count_products_by_category():
    with get_session() as session:
        return session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).all()

def categories_with_many_products():
    with get_session() as session:
        return session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()