import streamlit as st
import pickle
import pandas as pd
import numpy as np


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaper.dog/large/17116088.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 



anime = pd.read_csv('../datasets/anime.csv')
anime = anime[anime['members'] >= 10000]
anime = anime[anime['type'] == 'Movie']
st.title("Anime Recommendatation System")
#movie_df=pickle.load(open("../datasets/movie_recm.pkl","rb"))
#similarity=pickle.load(open("../datasets/dists.pkl","rb"))
#list_movie=np.array(movie_df["name"])
rec_df = pd.read_pickle('../datasets/recmovie.plk')



col1, col2 = st.columns(2)
col1.header("Top Rated Movies")

ar = anime.sort_values('rating', ascending=False)
ar.set_index('name', inplace=True)
col1.table(ar['rating'].head(10))

col2.header("Top Watched Movies")

ac = anime.sort_values('members', ascending=False)
ac.set_index('name', inplace=True)
col2.table(ac['members'].head(10))

option = st.selectbox(
"Select Movie ", rec_df[81:])

if st.button('Recommend Me'):
     st.write('Movies Recomended for you are:')
     def recom(option):
        return 1 - rec_df[option].sort_values(ascending = True).head(10)
     df = pd.DataFrame(1 - rec_df[option].sort_values(ascending= True).head(12))
     df['url'] = 'https://www.justwatch.com/us/search?q=' + df.index.astype(str).str.replace(' ' , '%20')
     st.table(df.drop(columns = 'url').iloc[:11])
     url0 = df.reset_index().loc[0]['url']
     urlname = df.reset_index().loc[0]['name']
     st.write(f"Check out: '{urlname}' here [link]({url0})")
     url1 = df.reset_index().loc[1]['url']
     urlname = df.reset_index().loc[1]['name']
     st.write(f"Check out: '{urlname}' here [link]({url1})")
     
     url2 = df.reset_index().loc[2]['url']
     urlname = df.reset_index().loc[2]['name']
     st.write(f"Check out: '{urlname}' here [link]({url2})")
     
     url3 = df.reset_index().loc[3]['url']
     urlname = df.reset_index().loc[3]['name']
     st.write(f"Check out: '{urlname}' here [link]({url3})")
     
     url4 = df.reset_index().loc[4]['url']
     urlname = df.reset_index().loc[4]['name']
     st.write(f"Check out: '{urlname}' here [link]({url4})")
     
     url5 = df.reset_index().loc[5]['url']
     urlname = df.reset_index().loc[5]['name']
     st.write(f"Check out: '{urlname}' here [link]({url5})")
     
     url6 = df.reset_index().loc[6]['url']
     urlname = df.reset_index().loc[6]['name']
     st.write(f"Check out: '{urlname}' here [link]({url6})")
     
     url7 = df.reset_index().loc[7]['url']
     urlname = df.reset_index().loc[7]['name']
     st.write(f"Check out: '{urlname}' here [link]({url7})")
     
     url8 = df.reset_index().loc[8]['url']
     urlname = df.reset_index().loc[8]['name']
     st.write(f"Check out: '{urlname}' here [link]({url8})")
     
     url9 = df.reset_index().loc[9]['url']
     urlname = df.reset_index().loc[9]['name']
     st.write(f"Check out: '{urlname}' here [link]({url9})")
     
     url10 = df.reset_index().loc[10]['url']
     urlname = df.reset_index().loc[10]['name']
     st.write(f"Check out: '{urlname}' here [link]({url10})")
     