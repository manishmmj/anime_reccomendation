import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
    
# https://drive.google.com/file/d/12inLzbTbbKFGKXdCMZrZWb65HwWRExo6/view?usp=drive_link

# Load the precomputed similarity model and anime dataset
anime_df = joblib.load(open('anime_data.pkl', 'rb'))  # Replace with your anime dataset file

# Train content-based model using anime descriptions
tfidf = TfidfVectorizer(stop_words='english')
anime_tfidf = tfidf.fit_transform(anime_df['genre'])
cosine_sim = cosine_similarity(anime_tfidf, anime_tfidf)

# Streamlit App Title
st.title("Anime Recommendation System")

# User Input for Anime Preferences
st.write("### Enter Your Favorite Anime or Filters Below:")

anime_list = anime_df['name'].tolist()
selected_anime = st.selectbox('Select an Anime:', anime_list)

num_recommendations = st.slider('Number of Recommendations:', min_value=1, max_value=10, value=5)

if st.button('Recommend Anime'):
    # Function to recommend anime based on cosine similarity
    def recommend_anime(title, n_recommendations=5):
        # Find the index of the anime in the dataframe
        indices = pd.Series(anime_df.index, index=anime_df['name']).drop_duplicates()
        idx = indices[title]
        
        # Get similarity scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Fetch top n recommendations (excluding the selected anime)
        sim_scores = sim_scores[1:n_recommendations + 1]
        anime_indices = [i[0] for i in sim_scores]
        
        return anime_df[['name','genre','episodes','rating']].iloc[anime_indices]

    # Generate Recommendations
    recommendations = recommend_anime(selected_anime, num_recommendations)

    # Display Recommendations
    st.write(f"### Recommended Anime Similar to '{selected_anime}':")
    st.dataframe(recommendations)

st.write("##Explore More Anime Recommendations!")
