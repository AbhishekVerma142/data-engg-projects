import pandas as pd
from pathlib import Path


def write_best_performing_books(combined_df: pd.DataFrame, data_path: Path) -> None:
    """
    Generates a CSV file of the top 10 best performing books based on their average review score.

    Criteria:
    - Books should have at least 25 reviews.
    - Removes any surrounding brackets from the author names.

    Parameters:
    - combined_df (pd.DataFrame): DataFrame resulting from the merge of ratings and book details.
    - data_path (Path): pathlib.Path object indicating where the result should be saved.

    Output File:
    - "best_performing_books.csv" saved in the specified `data_path`.

    Output Columns:
    - title: The title of the book.
    - average_review_score: The average score of reviews received by the book.
    - number_of_reviews: The total number of reviews received by the book.
    - author: The author(s) of the book, with any surrounding brackets removed.

    Returns:
    - None: Writes the result to the specified path.
    """

    book_perf = combined_df.groupby("Title").filter(lambda x: len(x) >= 25)

    book_perf["authors"] = book_perf["authors"].str.replace(r"\[|\]|'", "", regex=True)

    book_perf = (
        book_perf.groupby("Title")
        .agg(
            average_review_score=("review/score", "mean"),
            number_of_reviews=("User_id", "size"),
            author=("authors", "first"),
        )
        .reset_index()
    )

    top_books = book_perf.nlargest(10, "average_review_score")

    top_books.columns = ["title", "average_review_score", "number_of_reviews", "author"]

    top_books.to_csv(data_path / "best_performing_books.csv", index=False)
