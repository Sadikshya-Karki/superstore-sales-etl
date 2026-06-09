from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.validation import validate_data
from src.logger import setup_logger

logging = setup_logger()

def main():

    print("Starting ETL Pipeline...\n")
    logging.info("ETL Pipeline Started")

    # Extract
    df = extract_data("data/superstore.csv")
    initial_rows = df.shape[0]

    print(f"Initial rows: {initial_rows}")
    logging.info(f"Extract completed. Rows: {initial_rows}")

    # Transform
    print("Starting transformations...")
    df = transform_data(df)

    final_rows = df.shape[0]

    print("Transformations completed.")
    print(f"Final rows after transform: {final_rows}")

    logging.info(f"Transform completed. Rows: {final_rows}")

    # Load
    print("\nLoading data into database...")
    load_data(df)

    logging.info("Load completed successfully")

    print("Data loaded successfully.")
    print("\nETL Pipeline Completed Successfully!")

    logging.info("ETL Pipeline Finished Successfully")

if __name__ == "__main__":
    main()