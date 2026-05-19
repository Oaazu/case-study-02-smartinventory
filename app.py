# This file sets up the Streamlit app to load and display data from the database.
import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product, Sale


def get_session() -> Session:
    return SessionLocal()


def load_products() -> list[Product]:
    session = get_session()
    try:
        return session.query(Product).order_by(Product.product_id).all()
    finally:
        session.close()


def load_sales() -> list[Sale]:
    session = get_session()
    try:
        return session.query(Sale).order_by(Sale.sale_date).all()
    finally:
        session.close()


def main() -> None:
    st.set_page_config(page_title="SmartInventory - QuickMart", layout="wide")

    st.title("SmartInventory: Sales Pattern Analysis")
    st.write("Analyze 90-day sales data to identify stock shortage risks at QuickMart.")

    # --- Sidebar filters ---
    st.sidebar.header("Filters")
    category_filter = st.sidebar.selectbox(
        "Filter by Category",
        ["All", "Dairy", "Meat", "Produce", "Bakery", "Beverages", "Frozen"],
    )

    # --- Load data ---
    sales = load_sales()
    sales_rows = [
        {
            "sale_date": s.sale_date,
            "day_of_week": s.day_of_week,
            "product_id": s.product_id,
            "product_name": s.product_name,
            "category": s.category,
            "units_sold": s.units_sold,
            "is_weekend": s.is_weekend,
        }
        for s in sales
    ]
    df = pd.DataFrame(sales_rows)

    if category_filter != "All":
        df = df[df["category"] == category_filter]

    # --- Products table ---
    st.subheader("Products")
    products = load_products()
    product_rows = [
        {
            "product_id": p.product_id,
            "product_name": p.product_name,
            "category": p.category,
            "base_sale_rate": p.base_sale_rate,
            "weekend_multiplier": round(p.weekend_multiplier, 2),
        }
        for p in products
    ]
    st.dataframe(pd.DataFrame(product_rows), use_container_width=True)

    # --- Sales table ---
    st.subheader("Sales Records")
    st.dataframe(df, use_container_width=True)

    # --- Weekend vs Weekday summary ---
    st.subheader("Weekend vs Weekday Average Sales")
    if not df.empty:
        summary = df.groupby("is_weekend")["units_sold"].mean().reset_index()
        summary["is_weekend"] = summary["is_weekend"].map({True: "Weekend", False: "Weekday"})
        summary.columns = ["Day Type", "Avg Units Sold"]
        st.dataframe(summary, use_container_width=True)


if __name__ == "__main__":
    main()

