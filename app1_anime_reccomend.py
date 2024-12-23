import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the precomputed similarity model and anime dataset
cosine_sim = pickle.load(open('readme.md', 'rb'))  # Replace with your similarity file
anime_df = pickle.load(open('anime_data.pkl', 'rb'))  # Replace with your anime dataset file

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
        
        return anime_df[['Title', 'Genre', 'Type', 'Episodes', 'Rating']].iloc[anime_indices]

    # Generate Recommendations
    recommendations = recommend_anime(selected_anime, num_recommendations)

    # Display Recommendations
    st.write(f"### Recommended Anime Similar to '{selected_anime}':")
    st.dataframe(recommendations)

st.write("##Explore More Anime Recommendations!")
