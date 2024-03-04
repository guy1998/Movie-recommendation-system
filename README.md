# Movie-recommendation-system

***

## General description of the project
This is a project with focus on recommendation systems and how they function. The information used is based on the movie dataset provided by kaggle which can be found at the link in resources section. The program designed is a hybrid recommendation system which employs both collaborative filtering and content filtering. This is manifested in the two main features of the program which are providing a personal recommendation and providing trending recommendations. To provide personal recommendation the system relies on previous movies the user has interacted with to generate a list of similar movies from the dataset using cosine similarity. For each movie in the interaction list about 35 similar movies are picked and the recommendation is created by taking the intersection of each movie list. This way the user is likely to get movies that he will enjoy. On the other hand, to provide the trending recommendation the system relies on the interaction list of each user. It generates the personal recommendation of each user and then takes the intersaction of the personal recommendations. On the next version of the system this feature will be updated so that the first 10 movies on each personal recommendation are joined an the other movies are intersected to create the final trending recommendation. <br>
Since the system currently has the goal of simply simulating a hybrid recommendation system, the interaction of the user with the movies is minimal. The user can search for the movies and put them in his interaction list by pressing like. In the next version of the app the dislike feature will also be provided. The application currently maintains states of previous recommendations. This is done because creating a new recommendation is a time-consuming task so it should be avoided if the interaction lists of users have not changed in a while.

## GUI

The user interface for this program is developed using python and tkinter library especially. More information on tkinter library can be found at: https://docs.python.org/3/library/tkinter.html . The goal of the interface is to visualize the work of a recommendation system. A login system is provided to differentiate between users just like it would be in a real recommending system.
<p align="center">
  <img width="960" alt="image" src="https://github.com/guy1998/Movie-recommendation-system/assets/104024859/8ee0dfd2-6500-499d-a4cf-7a24478d6577">
  <p align="left">
    The image above displays the login page. Is obviously a simple login page with the text field corresponding to username and the password field. 
  </p>
  <img width="960" alt="image" src="https://github.com/guy1998/Movie-recommendation-system/assets/104024859/c823a4f4-f4be-4900-957c-6de03bd6a845">
  <p align="left">
    The user is allowed to search movies and is displayed the information for each movie he searches. This is displayed on the image above. The image below shows how the program displays the recommendation when the user requests one.
  </p>
  <img width="959" alt="image" src="https://github.com/guy1998/Movie-recommendation-system/assets/104024859/b278bb36-f965-4f87-9e9b-a88b61274c9f">
</p>

## Resources

The dataset for this project can be found at: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
