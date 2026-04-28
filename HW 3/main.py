from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# 1
engine = create_engine("sqlite:///:memory:")

Base = declarative_base()

# 2
Session = sessionmaker(bind=engine)
session = Session()

# 4
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))

    products = relationship("Product", back_populates="category")


# 3
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    in_stock = Column(Boolean, default=True)

    # 5
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)