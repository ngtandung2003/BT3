import streamlit as st
import pickle as pkl
import numpy as np

class_list = {'0': 'Negative', '1': 'Neutral', '2': 'Positive'}

st.title("Sentiment analysis from Vietnamese students' feedback")
