import streamlit as st
import pandas as po
import plotly.express

st.title("India's Overview")

st.set_page_config(layout = "wide")

#python -m streamlit run app.py
#py -m streamlit run app.py

data = po.read_csv("india_info.csv")

st.dataframe(data)

st.sidebar.title("India's Dashbaord")

st.sidebar.subheader("Filters")

states=data["State"].unique().tolist()

states.insert(0,"India")

choose_state= st.sidebar.selectbox("Choose Your State",states)

gender=st.sidebar.radio("Choose Gender", ["Male","Female"])

sizes = st.sidebar.selectbox("Choose what to show with size", data.columns[6:])

color=st.sidebar.selectbox("Choose what to show using color",data.columns[6:])

if choose_state == "India":
    fig = plotly.express.scatter_map(data, lat = "Latitude", lon = "Longitude",height=800,zoom=4,size = sizes, hover_name="District")

else:
    data=data[data["State"] == choose_state]
    center_lat=data["Latitude"]
    fig=plotly.express.scatter_map(data, lat="Latitude", lon="Longitude", height=800,zoom=6,size=sizes, hover_name="District")

st.plotly_chart(fig)