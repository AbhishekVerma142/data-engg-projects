import pandas as pd
from pathlib import Path


def write_category_distribution(combined_df: pd.DataFrame, data_path: Path) -> None:
    """
    Generates a CSV file of the book categories distribution.

    Criteria:
    - Categories with a proportion less than 1% of the total count will be grouped into the "Other" category.
    - Removes any surrounding brackets from the category names.
    - The column names in the output will be lowercase.

    Parameters:
    - combined_df (pd.DataFrame): DataFrame resulting from the merge of ratings and book details.
    - data_path (Path): pathlib.Path object indicating where the result should be saved.

    Output File:
    - "category_distribution.csv" saved in the specified `data_path`.

    Output Columns:
    - category: The name of the book category, with any surrounding brackets removed.
    - count: The number of books in that category.

    Returns:
    - None: Writes the result to the specified path.
    """
    total_books = combined_df.shape[0]
    threshold = total_books * 0.01

    category_counts = combined_df["categories"].value_counts()

    main_categories = category_counts[category_counts >= threshold]
    other_categories = category_counts[category_counts < threshold]

    other_count = other_categories.sum()

    main_categories_df = main_categories.reset_index()
    main_categories_df.columns = ["category", "count"]

    main_categories_df["category"] = main_categories_df["category"].str.replace(r"\[|\]|'", "", regex=True)

    other_df = pd.DataFrame([["Other", other_count]], columns=["category", "count"])
    final_category_distribution = pd.concat([main_categories_df, other_df], ignore_index=True)

    final_category_distribution.to_csv(data_path / "category_distribution.csv", index=False)
