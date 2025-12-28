"""
Movie Platform API

FastAPI REST API for the movie recommendation system.
Provides endpoints for retrieving recommendations and movie data.

Endpoints:
- GET /docs - Swagger UI documentation
- GET /api/movies - Get all movies
- GET /api/recommend/{movie_title} - Get recommendations for a movie
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from recommender_model import MovieRecommender

# Initialize FastAPI app
app = FastAPI(
    title="Movie Recommendation API",
    description="REST API for content-based movie recommendations",
    version="1.0.0"
)

# Add CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize recommender
recommender = MovieRecommender()


# Pydantic models for request/response
class Movie(BaseModel):
    """Movie data model."""
    MovieID: int
    Title: str
    ReleaseYear: int
    Rating: float


class Recommendation(BaseModel):
    """Recommendation response model."""
    title: str
    similarity_score: float


class RecommendationResponse(BaseModel):
    """Complete recommendation response."""
    reference_movie: str
    recommendations: List[Recommendation]
    count: int


# API Endpoints

@app.get("/", tags=["Health"])
async def root():
    """Health check endpoint."""
    return {
        "status": "✅ Movie Recommendation API is running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/api/movies", response_model=List[Movie], tags=["Movies"])
async def get_all_movies():
    """
    Get all movies in the database.

    Returns:
        List of all movies with their metadata
    """
    try:
        movies_df = recommender.get_all_movies()
        if movies_df.empty:
            raise HTTPException(status_code=404, detail="No movies found")

        movies = [
            Movie(
                MovieID=int(row['MovieID']),
                Title=row['Title'],
                ReleaseYear=int(row['ReleaseYear']),
                Rating=float(row['Rating'])
            )
            for _, row in movies_df.iterrows()
        ]
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get(
    "/api/recommend/{movie_title}",
    response_model=RecommendationResponse,
    tags=["Recommendations"]
)
async def get_recommendations(
    movie_title: str,
    n: int = Query(5, ge=1, le=20, description="Number of recommendations")
):
    """
    Get movie recommendations based on similarity.

    Args:
        movie_title: Title of the reference movie
        n: Number of recommendations (1-20)

    Returns:
        Recommendations with similarity scores
    """
    try:
        recommendations = recommender.get_recommendations(movie_title, n)

        if not recommendations:
            raise HTTPException(
                status_code=404,
                detail=f"Movie '{movie_title}' not found"
            )

        recommendation_list = [
            Recommendation(title=title, similarity_score=score)
            for title, score in recommendations
        ]

        return RecommendationResponse(
            reference_movie=movie_title,
            recommendations=recommendation_list,
            count=len(recommendation_list)
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/stats", tags=["Statistics"])
async def get_statistics():
    """
    Get database statistics.

    Returns:
        Statistics about the movie database
    """
    try:
        movies_df = recommender.get_all_movies()
        return {
            "total_movies": len(movies_df),
            "avg_rating": float(movies_df['Rating'].mean()),
            "min_year": int(movies_df['ReleaseYear'].min()),
            "max_year": int(movies_df['ReleaseYear'].max()),
            "rating_range": {
                "min": float(movies_df['Rating'].min()),
                "max": float(movies_df['Rating'].max())
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
