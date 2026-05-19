# This file seeds the database with generated product and sales data.
# Imports random to generate numbers and make random choices,
# Faker to generate realistic product names, and datetime to handle date-related operations.
import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product, Sale

fake = Faker()


def generate_products(session: Session) -> list:
    categories = ["Dairy", "Meat", "Produce", "Bakery", "Beverages", "Frozen"]
    grocery_words = ["Cheddar", "Salmon", "Spinach", "Yogurt", "Bagel", "Mango",
                     "Chicken", "Bread", "Butter", "Apple", "Pasta", "Milk",
                     "Beef", "Lettuce", "Orange", "Eggs", "Cheese", "Turkey",
                     "Tomato", "Cream","Grapes","Cereal","Ice Cream", "Juice","Fish","Rice","Beans","Carrots","Onions","Peppers"]

    products = []

    for _ in range(90):
        label = random.choice(["Premium", "Organic", "Classic", "Fresh"])
        product_name = f"{label} {random.choice(grocery_words)}"

        product = Product(
            product_name=product_name,
            category=random.choice(categories),
            base_sale_rate=random.randint(5, 40),
            weekend_multiplier=random.uniform(1.2, 2.5),
        )
        session.add(product)
        products.append(product)

    # Flush so each product gets its product_id assigned before we reference it in sales
    session.flush()
    return products


def generate_sales(session: Session, products: list) -> None:
    start_date = datetime(2024, 1, 1)

    for day in range(90):
        current_date = start_date + timedelta(days=day)
        day_of_week = current_date.strftime("%A")
        is_weekend = day_of_week in ["Saturday", "Sunday"]
        month = current_date.month

        for product in products:
            daily_sales = product.base_sale_rate * random.uniform(0.7, 1.3)

            if is_weekend:
                daily_sales *= product.weekend_multiplier

            if month in [7, 12]:
                daily_sales *= random.uniform(1.3, 1.8)

            sale = Sale(
                sale_date=current_date.date(),
                day_of_week=day_of_week,
                product_id=product.product_id,
                product_name=product.product_name,
                category=product.category,
                units_sold=int(daily_sales),
                is_weekend=is_weekend,
            )
            session.add(sale)


def main() -> None:
    session: Session = SessionLocal()
    try:
        # Clear existing data
        session.query(Sale).delete()
        session.query(Product).delete()

        products = generate_products(session)
        generate_sales(session, products)

        session.commit()
        print("Seeding complete!")
        print(f"  - {len(products)} products generated")
        print(f"  - {len(products) * 90} sales records generated")
    except Exception as e:
        session.rollback()
        print(f"Error during seeding: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()
