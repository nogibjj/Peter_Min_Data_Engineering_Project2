import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def read_spotify_data(filename):
    return pd.read_csv(filename, encoding="latin-1")


def generate_bar_chart_for_most_popular_artists(df: pd.DataFrame):
    # Handle missing & abnormal values
    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    df.dropna(subset=['streams'], inplace=True)

    # Create bar chart for 10 hottest songs reflected in stream counts
    top_artists = df.groupby('artist(s)_name')['streams'].sum().nlargest(10)
    plt.figure(figsize=(10, 6))
    top_artists.plot(kind='bar', color='blue')
    plt.title('10 Hottest Artists by Total Stream Count')
    plt.xlabel('Artists')
    plt.ylabel('Total Streams')
    plt.xticks(rotation=45)
    plt.show()


def main():
    spotify_df = read_spotify_data("spotify-2023.csv")
    generate_bar_chart_for_most_popular_artists(spotify_df)

main()