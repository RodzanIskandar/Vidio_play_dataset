# Vidio stream dataset

## Overview
I am analyzing and build recommendation engine using real Vidio.com play dataset from 1 february 2020 to 16 february 2020. One of insights from the analytis is most play are 
in embed (not direct) with less play duration, play by non premium users coming from some refferers and campaigns. It shows there are still many opportunities to attract 
non-premium users to become premium users. In the build recommendation system I am using collaborative filtering method using K-Nearest Neighbors algorithm and completed play 
data by premium user.

## Algoritm and resource used
**Algorithm:** K-Nearest Neighbors

**Recommendation system refferences:** 
- [https://beckernick.github.io/music_recommender/](https://beckernick.github.io/music_recommender/)
- [https://towardsdatascience.com/how-did-we-build-book-recommender-systems-in-an-hour-part-2-k-nearest-neighbors-and-matrix-c04b3c2ef55c](https://towardsdatascience.com/how-did-we-build-book-recommender-systems-in-an-hour-part-2-k-nearest-neighbors-and-matrix-c04b3c2ef55c)
- [https://towardsdatascience.com/how-did-we-build-book-recommender-systems-in-an-hour-the-fundamentals-dfee054f978e](https://towardsdatascience.com/how-did-we-build-book-recommender-systems-in-an-hour-the-fundamentals-dfee054f978e)
- Example of Content based filtering recommendation system: [https://github.com/rustydigg918/movie_recommender/blob/master/Movie%20Recommender.ipynb](https://github.com/rustydigg918/movie_recommender/blob/master/Movie%20Recommender.ipynb)

## Dataset
The Dataset contains 41 columns as follows:
1. hash_content_id
2. hash_play_id
3. hash_visit_id
4. hash_watcher_id
5. hash_film_id
6. hash_event_id
7. is_login
8. playback_location: direct play in the Vidio.com website or embed
9. platform
10. play_time
11. end_time 
12. referrer: where the request to play Vidio player originated
13. average_bitrate
14. bitrate_range
15. total_bytes
16. buffer_duration
17. referrer_group
18. completed: completed play
19. utm_source: campaign resource
20. utm_medium: campaign resource
21. utm_campaign: campaign resource
22. player_name: Video player name
23. has_ad
24. flash_version
25. os_name
26. os_version
27. browser_name
28. browser_version 
29. app_name
30. autoplay
31. is_premium
32. app_version
33. city
34. play_duration 
35. content_type
36. stream_type
37. title
38. category_name
39. film_title
40. season_name
41. genre_name

## Data Cleaning
In order to get good data to do some analysis, here what I am doing in cleaning section:
1. Drop city column, cause not containing any data.
2. Fill na in boolean data type with False.
3. Fill na in categorical data type with unknown.
4. Transfrom date columns to datetime format.
5. Add new datetime columns based on 'play_time' column.
6. Transform boolean data type to object.
7. Filtering the data based on the 'end time' data happened after 'play_time' in the dataset.
8. Filtering the data based on the 'total_duration' as range of 'buffer_duration' and 'play_duration'.

## Data Analysis
Here is some facts and insights from the data, for complete analysis data please check the Data_Analysis_Vidio notebook above:
1. Total play mostly coming from another website (embed) not directly in the vidio webpage, with kapanlagi, merdeka, and liputan 6 as a top 3 referre_group streaming coming from. so thats why, most users are not login and not premium in the platform.
2. Premium Users tend to stream using web-desktop, tv-android and app android as platform to stream. Most of them coming from organic traffic, its proff by referrer_group dominated by empty, others, and internal, and campaign source dominated by unknown (nan data). Favorite content_type of premium users is VOD followed by livestreaming.
3. Total play in 15 days on February tends to be constant with peak at 12 february 2020. Sunday is the most play or stream happened followed by wednesday and thursday and at around 2PM at noon.
4. Bitrate tends to be good at app in android and smart tv version, but even with the good average bitrate, in tv-android buffer duration is still longer.
5. Most play are in embed (not direct) with less play duration, play by non premium users coming from some refferers and campaigns. It shows there are still many opportunities to attract non-premium users to become premium users. Whereas premium users tend to be play longer duration coming from organic traffic.

## Feature Importances using Random Forest Classifier
I analyzed some features (columns) that have the biggest impact to the 'is_premium' column whether the users is premium  or non premium using one of most popular algorithm, Random Forest Classifier. The result shows whether the vidio content is interesting, boring, good rating or bad rating and advertisement in Vidio player determines the user will premium or not, it shows by 'title' and 'has_ad' as top 2 of feature importances in Random Forest Classifier algorithm.
![](https://github.com/RodzanIskandar/Vidio_stream_dataset/blob/main/images/feature%20importance.png)

## Recommendation system
I am using collaborative filtering method to build recommendation system, here soem steps using K-Nearest Neighbors:
1. Filter data with only premium user and completed play.
2. Pick the user id, film (items) and completed feature to do a collaborative Filtering recommendation engine.
3. Make new columns total plays for each unique film_title.
4. Filter data to only popular film_title, to ensure statistical significance.
5. Reshape the data using pivot table function.
6. Transform Sparse matrix to Compressed Sparse Row (CSR).
7. Training the CSR data using K-Neares Neighbors using cosine similarity as metric.
8. Build the recommendation system by searching the 5 closest neighbors based on cosine similarity characteristic.

## Further Learning
In order to get more accurate recommendation engine, we can use complete dataset rather than using 20% sample dataset that we used in this notebook. And also it will be more proper result if using rating of the content by the user than completed watch by the user. But the basic idea of the collaborative filtering recommendation engine are the same.
