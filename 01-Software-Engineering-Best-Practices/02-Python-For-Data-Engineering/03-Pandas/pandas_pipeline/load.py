from pathlib import Path
import pandas as pd

def load_data(data_path: Path) -> pd.DataFrame:
    """
    Loads books data and ratings data from the specified path and returns a combined DataFrame.

    Parameters:
    - data_path (Path): Path to the directory containing the "books_data.csv" and "Books_rating.csv" files.

    Returns:
    - combined_df (pd.DataFrame): A DataFrame resulting from the inner merge of books data and ratings data on the "Title" column.

    Note:
    - "books_data.csv" should contain book details.
    - "Books_rating.csv" should contain book ratings.
    - Both CSVs are expected to have a "Title" column for the merge operation.
    - An inner merge is performed, so only books that exist in both datasets will be included in the result.

    Raises:
    - FileNotFoundError: If either of the CSV files is missing in the specified path.
    """
    if not (data_path / "books_data.csv").exists() or not (data_path / "Books_rating.csv").exists():
        raise FileNotFoundError("Missing files")

    books = pd.read_csv(data_path / "books_data.csv")
    ratings = pd.read_csv(data_path / "Books_rating.csv")
    combined_df = pd.merge(books, ratings, on="Title", how="inner")

    return combined_df

if __name__ == "__main__":
    load_data()
