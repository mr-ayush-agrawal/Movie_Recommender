# :moive: Movie Recommender
This is a basic Machine learning model Project. Which can be used to recommend the movie based on the mivie selected by the user.

## Running
There are bascially 2 ways to run the code. <br>
1. Running in the local web host.
1. Running the Jupyter notebook.

**Select any way you want** For Running it you have to do some of the below given basic steps for both of the process.

#### :copy_file: Forking
Fork the repostiory. For This you have to just click on the **FORK** option in the GitHub.

#### :open_folder: Cloning
After forking you will see the option of code and there you will see a link like<br>
`*/User_Name/Movie_Recommender`

Copy the link and go to the terminal in your local system.

Before Cloning you must make ensure that git is install in your system.Check it by running the given command.
```shell
git --version
```
If this throws an error then install git in your system.

Now, Get to the desired location where you want the copy of the code.
```shell
git clone <Paste_Your_Link> 
```

Now changing the location to the folder
```shell
cd Movie_Recommender
```
After successful completeion of these commands you decide which way you want to run the code.


### Local Web Host

For running the code in the local web host you need to get the API key of the [TMDB]() website. This API Key is used to fetch the poster of the Movies.

Run the following command to create the file for keeping your API Key as a private.

```shell
touch API_Key.txt
```
Now Open the file and Paste the API_KEY there.

After Pasting the Keys You need To run the following thing to generate the Dependency Files.

<!-- - Open [Analysis File](Analysis.ipynb) and click on ***Run All*** option -->
- Open [Model File](model.ipynb) and click on ***Run All*** option

Running These files would create the data for encoding the data of the movies on which we are making this project.


**Installing the Dependencies**<br>
Lets install all the Modules on the basis of which the model will be running
```shell

```

For Running the code and making a local web host  Now Run :
```shell
streamlit run app.py
```

**Getting Recommendation**

Select the movie on the basis of which you want the recommendation in the select box given.<br>
Click on Recommend button below. This shall produce the Movies suggestion based on the selected movie.


### Jupyter notebook

For Running the command in jupyter Notebook you just need to follow some of the basic steps.

The benefit of running through Jupyter is yoe dont need to create account with the TMDB to fetch the posters.

**Installing the Dependencies**<br>
Lets install all the Modules on the basis of which the model will be running
```shell
pip install numpy pandas nltk sklearn
```

Now open the [Model File](model.ipynb) click on Run-All button.<br>
This shall start the execution of the Code.

#### Changing Suggestion Name
For Changing the movie name for suggestion, goto `suggest('Avengers: Age of Ultron')` function call cell (Bottom third)<br>

Replace the name of Movie.

**Make sure that the Movie name is correct even all the spaces and the cases of letter**

## :caution: Caution
This old data and the latest movies are not updated in the database.<br>
If you Enter some movie which is not in the database this shall throw an error.