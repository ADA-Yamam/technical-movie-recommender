"""
Movie Recommendation Dashboard

Interactive Streamlit dashboard for the movie recommendation system.
Allows users to select movies and view personalized recommendations.
"""

import streamlit as st
import pandas as pd
from recommender_model import MovieRecommender

# Page configuration
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
@st.cache_resource
def load_recommender():
    """Load the recommendation model (cached)."""
    return MovieRecommender()


# Header
st.title("🎬 Movie Recommendation System")
st.markdown("""
    **Technical Data Engineering Portfolio Project**
    
    This dashboard demonstrates a content-based recommendation system built with Python, 
    FastAPI, and Streamlit. Select a movie to get personalized recommendations.
""")

# Load recommender
recommender = load_recommender()
all_movies = recommender.get_all_movies()

if all_movies.empty:
    st.error("❌ No movies found in database. Please run prepare_db.py first.")
    st.stop()

# Sidebar
st.sidebar.header("⚙️ Configuration")
selected_movie = st.sidebar.selectbox(
    "Select a Movie:",
    options=all_movies['Title'].tolist(),
    help="Choose a movie to get recommendations"
)

n_recommendations = st.sidebar.slider(
    "Number of Recommendations:",
    min_value=1,
    max_value=10,
    value=5,
    help="How many recommendations to display"
)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Movie Information")
    selected_movie_data = all_movies[all_movies['Title'] == selected_movie].iloc[0]
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.metric("Title", selected_movie)
    with col_info2:
        st.metric("Rating", f"{selected_movie_data['Rating']:.1f}/10")
    
    col_info3, col_info4 = st.columns(2)
    with col_info3:
        st.metric("Release Year", int(selected_movie_data['ReleaseYear']))
    with col_info4:
        st.metric("Movie ID", int(selected_movie_data['MovieID']))

with col2:
    st.subheader("📈 Database Statistics")
    
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    with col_stat1:
        st.metric("Total Movies", len(all_movies))
    with col_stat2:
        st.metric("Avg Rating", f"{all_movies['Rating'].mean():.2f}")
    with col_stat3:
        st.metric("Year Range", f"{int(all_movies['ReleaseYear'].min())}-{int(all_movies['ReleaseYear'].max())}")

# Get recommendations
st.subheader("🎯 Recommendations")

recommendations = recommender.get_recommendations(selected_movie, n_recommendations)

if recommendations:
    # Display recommendations as a table
    rec_data = {
        "Movie Title": [title for title, _ in recommendations],
        "Similarity Score": [f"{score:.4f}" for _, score in recommendations]
    }
    rec_df = pd.DataFrame(rec_data)
    
    st.dataframe(rec_df, use_container_width=True, hide_index=True)
    
    # Display as expandable cards
    st.markdown("---")
    st.subheader("📋 Detailed Recommendations")
    
    for idx, (title, score) in enumerate(recommendations, 1):
        with st.expander(f"{idx}. {title} (Score: {score:.4f})"):
            movie_info = all_movies[all_movies['Title'] == title].iloc[0]
            col_detail1, col_detail2, col_detail3 = st.columns(3)
            
            with col_detail1:
                st.metric("Rating", f"{movie_info['Rating']:.1f}/10")
            with col_detail2:
                st.metric("Release Year", int(movie_info['ReleaseYear']))
            with col_detail3:
                st.metric("Similarity", f"{score:.4f}")
else:
    st.error(f"❌ Could not generate recommendations for '{selected_movie}'")

# Footer
st.markdown("---")
st.markdown("""
    **Technical Details:**
    - Model Type: Content-Based Recommendation
    - Features: Movie Rating, Release Year
    - Algorithm: Cosine Similarity
    - Framework: Streamlit, FastAPI, Scikit-learn
    
    This is a **portfolio project** demonstrating data engineering and system integration skills.
""")
