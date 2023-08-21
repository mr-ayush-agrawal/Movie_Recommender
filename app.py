import streamlit as st
from pickle import load
from pandas import DataFrame

# Loading all the data through pkl files
movie_dict = load(open('movie_data_dict.pkl','rb'))
movies = DataFrame(movie_dict)

st.title("Movie Recommender")

selected_movie = st.selectbox(
    'Select the Movie on the basis of which you want recommendation', 
    movies['title'].values
)

# placing a button
if st.button('Recommend'):
    st.write(selected_movie)
