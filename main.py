from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns
from src.viz import plot_graph


def main():
    df = load_csv(RAW_PATH)
    assert_columns(df, [
        'App', 'Category', 'Rating', 'Reviews',
        'Size_MB', 'Installs', 'Type', 'Price_$',
        'Content_Rating', 'Genres',
        'Last_Updated', 'Android_Version'
    ])
    df = clean(df)
    
    assert_columns(df, [
        'Android_Version',
        'Last_Updated',
        'Rating'
    ])

    df = build_features(df)

    assert_columns(df, [
        'Android_Version_Major',
        'Last_Updated_Year',
        'Last_Updated_Month',
        'Rating_Group',
    ])

    plot_graph(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
