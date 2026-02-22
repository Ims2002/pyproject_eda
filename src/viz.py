import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(df: pd.DataFrame) -> None:
    hist_grapg(df, 'Price_$')
    bar_graph_price_proportion(df)
    apps_per_genre(df)
    genre_distribution(df)
    heatmap_category_android_version(df)
    genre_by_avg_paid_app_price(df)
    avg_installs_by_android_version(df)
    avg_paid_price_rating_group(df)
    crosstab_viz(df, 'Category', 'Type')
    crosstab_viz(df, 'Category', 'Content_Rating')

def hist_grapg(df: pd.DataFrame, column: str) -> None:
    df[column].value_counts().plot(kind='bar')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.title(f'Distribution del {column}')
    plt.show()

def bar_graph_price_proportion(df: pd.DataFrame) -> None:
    type_counts = df['Type'].value_counts(normalize=True) * 100

    plt.figure()
    plt.bar(type_counts.index, type_counts.values)
    plt.xlabel('App Type')
    plt.ylabel('Percentage (%)')
    plt.title('Free vs Paid Apps Distribution')
    plt.show()

def apps_per_genre(df: pd.DataFrame) -> None:
    genre_counts = df['Category'].value_counts()
    colors = plt.cm.viridis(np.linspace(0, 1, len(genre_counts)))

    genre_counts.plot(kind='bar', color=colors, figsize=(12,6))
    plt.xticks(rotation=45)
    plt.ylabel('Count')
    plt.title('Number of Apps per Genre')
    plt.show()

def genre_distribution(df: pd.DataFrame) -> None:
    genre_counts = df['Genres'].value_counts().head(10)
    plt.figure(figsize=(8,8))
    plt.pie(
        genre_counts.values,
        labels=genre_counts.index,
        autopct='%1.1f%%',
        startangle=140
    )
    plt.title('Top 10 Genres Distribution (%)')
    plt.show()

def heatmap_category_android_version(df: pd.DataFrame) -> None:
    pivot = df.pivot_table(index='Category', columns='Android_Version_Major', values='App', aggfunc='count', fill_value=0)
    plt.figure(figsize=(15,8))
    sns.heatmap(pivot, cmap='Oranges', annot=True, fmt='d')
    plt.title('Number of Apps per Category and Android Version')
    plt.show()

def genre_by_avg_paid_app_price(df: pd.DataFrame) -> None:
    paid_df = df[df['Type'] == 'Paid']

    price_mean_genre = (
        paid_df.groupby('Genres', as_index=False)['Price_$']
        .mean()
        .sort_values('Price_$', ascending=False)
    )

    top_genres = price_mean_genre.head(6)

    plt.figure(figsize=(12,6))
    sns.barplot(data=top_genres, x='Genres', y='Price_$', palette='pastel')
    plt.xticks(rotation=90)
    plt.title('Top 10 Genres by Average Paid App Price')
    plt.show()

def avg_installs_by_android_version(df: pd.DataFrame) -> None:
    mean_installs = df.groupby('Android_Version_Major')['Installs'].mean().sort_index()
    installs_percent = mean_installs / mean_installs.sum() * 100

    installs_df = installs_percent.reset_index()
    installs_df.columns = ['Android_Version_Major', 'Percent']

    plt.figure(figsize=(12,6))
    sns.barplot(data=installs_df, x='Android_Version_Major', y='Percent', palette='pastel')

    plt.xticks(rotation=45)
    plt.xlabel('Android Version')
    plt.ylabel('Average Installs (%)')
    plt.title('Average Installs Distribution by Android Version')
    plt.show()

def avg_paid_price_rating_group(df: pd.DataFrame) -> None:
    paid_df = df[df['Type'] == 'Paid']

    sns.barplot(
        data=paid_df,
        x='Rating_Group',
        y='Price_$',
        order=['Low','Mid','High','Top'],
        palette='viridis'
    )
    plt.title('Average Price by Rating Group (Paid Apps)')
    plt.show()

def crosstab_viz(df: pd.DataFrame, col1: str, col2: str) -> None:
        
    ct = pd.crosstab(
        df[col1],
        df[col2],
        normalize='index'
    )
    
    print(f"{ct} + \n") 