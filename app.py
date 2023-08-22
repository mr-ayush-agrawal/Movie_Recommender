import streamlit as st
from pickle import load
from pandas import DataFrame
import requests as req

# Loading all the movies through pkl files
movie_dict = load(open('movie_data_dict.pkl','rb'))
Similarity_Score = load(open('SimScr.pkl','rb'))
movies = DataFrame(movie_dict)

with open('API_Key.txt', 'r') as file:
    API_KEY = file.readline()

def fetch_poster(movie_id):
    URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&&language=en-US'
    response = req.get(URL)
    return "https://image.tmdb.org/t/p/original" + response.json()['poster_path']


def recommend(movie):
    mov_Idx = movies[movies['title']==movie].index[0]
    distances = Similarity_Score[mov_Idx]
    movieList = sorted(list(enumerate(distances)), reverse=True, key=lambda x :x[1])[1:8]
    recommended = []
    poster = []

    for mv in movieList:
        recommended.append(movies.title.iloc[mv[0]])
        poster.append(fetch_poster(movies.iloc[mv[0]].id))

    return recommended, poster


st.title("Movie Recommender")

selected_movie = st.selectbox(
    'Select the Movie on the basis of which you want recommendation', 
    movies['title'].values
)

# placing a button
if st.button('Recommend'):
    names, poster = recommend(selected_movie)

    col = st.columns(7)
    for i in range(7) :
        with col[i]:
            st.text(names[i])
            st.image(poster[i])
            