from src.logger import setup_logger
from src.validation import validate_data
import pandas as pd

logging = setup_logger()

def transform_data(df):

    logging.info("Starting transformations")

    # Validate data FIRST
    validate_data(df)
    logging.info("Validation passed")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Remove duplicates
    df = df.drop_duplicates()
    logging.info(f"Duplicates removed. Shape: {df.shape}")

    # Remove missing critical values
    df = df.dropna(subset=["Order Date", "Ship Date", "Sales"])

    # Convert dates safely
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

    # Drop invalid dates
    df = df.dropna(subset=["Order Date", "Ship Date"])

    # Feature engineering
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month
    df["Order Day"] = df["Order Date"].dt.day

    df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    df["Sales Category"] = pd.cut(
        df["Sales"],
        bins=[0, 100, 500, float("inf")],
        labels=["Low", "Medium", "High"]
    )

    df["High Value Order"] = df["Sales"].apply(
        lambda x: "Yes" if x > 500 else "No"
    )

    logging.info(f"Transformations completed. Final shape: {df.shape}")

    return df