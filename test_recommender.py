from recommender_model import ContentBasedRecommender

model = ContentBasedRecommender()
model.load_data()
model.build_model()

results = model.recommend_top_rated(top_n=5)
for r in results:
    print(r)
