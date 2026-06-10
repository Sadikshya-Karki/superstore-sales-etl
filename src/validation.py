def validate_data(df):

    required_columns = ["Order Date", "Ship Date", "Sales"]

    # Check missing columns
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise Exception(f"Missing columns: {missing}")

    # Check empty dataset
    if df.empty:
        raise Exception("Dataset is empty")

    return True
