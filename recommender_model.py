
       import sqlite3
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

DB_PATH = "movies.db"


class ContentBasedRecommender:
    def __init__(self):
        self.df = None
        self.similarity_matrix = None
        self.scaled_features = None

    def load_data(self):
        conn = sqlite3.connect(DB_PATH)

        query = """
        SELECT 
            m.MovieID,
            m.Title,
            m.ReleaseYear,
            m.Rating,
            GROUP_CONCAT(g.GenreName, ' ') AS Genres
        FROM Movies m
        LEFT JOIN MovieGenres mg ON m.MovieID = mg.MovieID
        LEFT JOIN Genres g ON mg.GenreID = g.GenreID
        GROUP BY m.MovieID
        """

        self.df = pd.read_sql(query, conn)
        conn.close()

        self.df["Genres"] = self.df["Genres"].fillna("")
        self.df["Rating"] = self.df["Rating"].fillna(0)
        self.df["ReleaseYear"] = self.df["ReleaseYear"].fillna(0)

    def build_model(self):
        features = self.df[["Rating", "ReleaseYear"]]
        scaler = StandardScaler()
        self.scaled_features = scaler.fit_transform(features)
        self.similarity_matrix = cosine_similarity(self.scaled_features)

    def recommend_top_rated(self, top_n=5):
        top_movies = (
            self.df.sort_values(by="Rating", ascending=False)
            .head(top_n)
            [["Title", "Rating", "ReleaseYear", "Genres"]]
        )
        return top_movies.to_dict(orient="records")

      
       
