import streamlit as st
import pickle
import pandas as pd

# Load movie data and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Extract movie titles
movies_list = movies['title'].values


# Function to fetch poster
def fetch_poster(movie_id):
    # Replace this with actual poster URL logic if available
    return f"https://image.tmdb.org/t/p/w500/{movie_id}.jpg"


# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    # Get top 5 recommendations
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies_list
)

# Button to trigger recommendations
if st.button("Recommend"):
    recommended_names, recommended_posters = recommend(selected_movie_name)

    # Display recommendations in Streamlit
    for name, poster in zip(recommended_names, recommended_posters):
        st.subheader(name)
        st.image(poster)
