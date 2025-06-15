import streamlit as st
import pandas as pd
import pickle
import requests


# Helper Function

def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=60baad01bd7eaac7cf470aa6c82a70d9&language=en-US"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get("poster_path", "")

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Load Data

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


# Page Configuration

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")


# Custom CSS Styling

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-attachment: fixed;
        background-color: rgb(9, 7, 63, 34%);
        background-size: cover;
        color: white;
    }
    
    .stApp.stAppEmbeddingId-sxuo0lgh8m99.streamlit-wide.st-emotion-cache-fg4pbf.erw9t6i1{
        position: absolute;
        background: rgb(255, 255, 255);
        color: rgb(49, 51, 63);
        inset: 0px;
        overflow: hidden;
    }

    .title-style {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        color: black;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    .subtext {
        text-align: center;
        font-size: 1.2rem;
        color: #dcdcdc;
        margin-bottom: 2rem;
    }

    .movie-card {
        background: linear-gradient(to right, #fc466b, #3f5efb);
        padding: 12px;
        border-radius: 15px;
        transition: 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        text-align: center;
    }

    .movie-card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
    }

    .movie-title {
        margin-top: 10px;
        font-weight: bold;
        font-size: 1rem;
        color:black;
    }

    .stButton > button {
        background: linear-gradient(to right, #fc466b, #3f5efb);
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        border-radius: 10px;
        font-weight: bold;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(63, 94, 251, 0.4);
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #3f5efb, #fc466b);
        transform: scale(1.05);
        cursor: pointer;
    }

    .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- App Content ----------
st.markdown("<div class='title-style'>🎬 Movie Recommender System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Discover the best movies based on your taste 🍿</div>", unsafe_allow_html=True)


# Select Movie

selected_movie_name = st.selectbox("Select a movie you like:", movies["title"].values)


# Recommend Button & Output

if st.button("🎥 Recommend Movies"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                <div class='movie-card'>
                    <img src="{posters[i]}" width="100%" style="border-radius: 10px;">
                    <div class='movie-title'>{names[i]}</div>
                </div>
            """, unsafe_allow_html=True)
