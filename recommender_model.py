"""
Movie Recommendation Model

This module implements a content-based recommendation system using cosine similarity.
It demonstrates ML integration in a production-like system.

Features used:
- Movie rating (0-10 scale)
- Release year

Algorithm:
- Feature scaling with StandardScaler
- Cosine similarity for movie-to-movie similarity
- K-nearest neighbors for recommendations
"""

import sqlite3
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple


class MovieRecommender:
    """Content-based movie recommendation system."""

    def __init__(self, db_path: str = "movies.db"):
        """
        Initialize the recommender system.

        Args:
            db_path: Path to SQLite database
        """
        self.db_path = db_path
        self.movies_df = None
        self.feature_matrix = None
        self.similarity_matrix = None
        self.scaler = StandardScaler()
        self._load_data()
        self._build_model()

    def _load_data(self):
        """Load movie data from database."""
        try:
            conn = sqlite3.connect(self.db_path)
            self.movies_df = pd.read_sql_query(
                "SELECT MovieID, Title, ReleaseYear, Rating FROM movies",
                conn
            )
            conn.close()
            print(f"✅ Loaded {len(self.movies_df)} movies from database")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            raise

    def _build_model(self):
        """Build the recommendation model."""
        if self.movies_df is None or len(self.movies_df) == 0:
            print("⚠️ No data available to build model")
            return

        # Select features for recommendation
        features = self.movies_df[['Rating', 'ReleaseYear']].values

        # Scale features
        self.feature_matrix = self.scaler.fit_transform(features)

        # Compute similarity matrix
        self.similarity_matrix = cosine_similarity(self.feature_matrix)
        print("✅ Recommendation model built successfully")

    def get_recommendations(
        self,
        movie_title: str,
        n_recommendations: int = 5
    ) -> List[Tuple[str, float]]:
        """
        Get movie recommendations based on similarity.

        Args:
            movie_title: Title of the reference movie
            n_recommendations: Number of recommendations to return

        Returns:
            List of (movie_title, similarity_score) tuples
        """
        if self.similarity_matrix is None:
            return []

        # Find the movie
        movie_matches = self.movies_df[
            self.movies_df['Title'].str.lower() == movie_title.lower()
        ]

        if movie_matches.empty:
            print(f"❌ Movie '{movie_title}' not found")
            return []

        movie_idx = movie_matches.index[0]

        # Get similarity scores
        similarities = self.similarity_matrix[movie_idx]

        # Get top N recommendations (excluding the movie itself)
        top_indices = np.argsort(similarities)[::-1][1:n_recommendations + 1]

        recommendations = [
            (
                self.movies_df.iloc[idx]['Title'],
                float(similarities[idx])
            )
            for idx in top_indices
        ]

        return recommendations

    def get_all_movies(self) -> pd.DataFrame:
        """Get all movies in the database."""
        return self.movies_df.copy() if self.movies_df is not None else pd.DataFrame()


# Example usage
if __name__ == "__main__":
    recommender = MovieRecommender()
    print("\n📊 Recommendation Model Loaded")
    print(f"Total movies: {len(recommender.get_all_movies())}")
