
# Anime Recommender System
---

## Problem Statement
---
The objective of this project is to create an accurate anime recommendation system that utilizes user-based anime reviews. This system will leverage a dataset of anime reviews to identify similarities between user preferences and provide personalized recommendations based on these similarities. The primary aim is to enhance the accuracy of the recommendation system, thereby enabling users to select the most suitable anime to watch with ease. The project's strategy involves building an anime recommendation model that relies solely on user viewing history as the basis for generating recommendations, as this approach is anticipated to yield optimal results.

## Executive Summary
---
### *Data Extraction*

The datasets were pulled form Kaggle using the Kaggle API for datasets:

-Anime dataset
(https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database?select=anime.csv#:~:text=calendar_view_week-,anime,-.csv)

-Anime rating dataset
(https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database?select=anime.csv#:~:text=calendar_view_week-,rating,-.csv)

#### *Data Preprocessing & EDA*

The two data set contains information on user preference data from 73,516 users on 12,294 anime. Each user was able to add anime to their completed list and give it a rating and merging the data sets made a compilation of those ratings. There were over 300 null values that we had to drop. Also ratings that we rated -1 were rows that were not rated. So for those columns they were drop as well. Overall both of the datsets were clean and not alot of cleaning was neccesary. Other datasets were to big to fit on Github.

##### Anime Type Count
![count](./vizualizations/movietypes.png)

###### Genre Type Count
![count](./vizualizations/generetypes.png)

##### Top 10 Anime Rated Movie
![count](./vizualizations/top10movie.png)

##### Top 10 Anime Rated TV Show
![count](./vizualizations/top10tv.png)


#### *Modeling*

For the modeling we were able to use Cosine similarity to help calculate the distances for similarites. In order to do that we had to create a pivot table consity of the name of the anime, the rating, and the userid. Recommendation systems for anime based on user reviews was created using collaborative filtering. These functions were included in a streamlit app for recommending anime books and tv shows.

## Conclusions and Recommendations

Recommendendation systems with collaborative filtering works great for finding the similarities and recommending to users. Recommendation systems are also great because we don't need knowledge of the particular field because the embeddings are automatically learned. One disadvantage could come for sparsity in some data leading to a recommendation not strong because of not enough data on a particular anime. However the model can help users discover new interests in anime they did not know they would have interest in. Next steps would consist of adding more filters to te recommender system and improving the model based on user feedback. 
