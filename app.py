import streamlit as st
from pickle import load
from pandas import DataFrame

# Loading all the movies through pkl files
movie_dict = load(open('movie_data_dict.pkl','rb'))
Similarity_Score = load(open('SimScr.pkl','rb'))
movies = DataFrame(movie_dict)

def recommend(movie):
    mov_Idx = movies[movies['title']==movie].index[0]
    distances = Similarity_Score[mov_Idx]
    movieList = sorted(list(enumerate(distances)), reverse=True, key=lambda x :x[1])[1:8]
    recommended = []

    for mv in movieList:
        recommended.append(movies.title.iloc[mv[0]])

    return recommended


st.title("Movie Recommender")

selected_movie = st.selectbox(
    'Select the Movie on the basis of which you want recommendation', 
    movies['title'].values
)

# placing a button
if st.button('Recommend'):
    recommended_movies = recommend(selected_movie)
    for mov in recommended_movies:
        st.write(mov)
