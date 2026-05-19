# This file exports the sales table as a CSV file to be used in Lovable.
import pandas as pd
from database import engine


def main() -> None:
    df = pd.read_sql_table("sales", con=engine)
    df.to_csv("quickmart_sales.csv", index=False)
    print(f"CSV exported successfully: {len(df)} sales records saved to quickmart_sales.csv")


if __name__ == "__main__":
    main()

