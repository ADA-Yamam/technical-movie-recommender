 import streamlit as st
from recommender_model import ContentBasedRecommender

st.set_page_config(
    page_title="Movie Recommendation Dashboard",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")
st.write("A data-driven movie recommender based on ratings and release year")

@st.cache_resource
def load_model():
    model = ContentBasedRecommender()
    model.load_data()
    model.build_model()
    return model

model = load_model()

top_n = st.slider("Number of recommendations", 1, 10, 5)

if st.button("🔍 Show Recommendations"):
    results = model.recommend_top_rated(top_n)

    if results:
        st.success("Recommendations loaded successfully")
        st.table(results)
    else:
        st.warning("No results found")
