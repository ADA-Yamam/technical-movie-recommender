
from fastapi import FastAPI
from recommender_model import ContentBasedRecommender

app = FastAPI(title="Movie Recommendation API")

model = ContentBasedRecommender()
model.load_data()
model.build_model()


@app.get("/")
def root():
    return {"message": "Movie Recommendation API is running"}


@app.get("/recommend")
def recommend(top_n: int = 5):
    return model.recommend_top_rated(top_n)
uvicorn movie_platform_api:app --reload
