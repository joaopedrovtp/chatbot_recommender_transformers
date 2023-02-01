## Develop a recommender chatbot with fine-tuned transformer model

#### **What is this?**
This project consists in create a ChatBot with a recommendation system upon a fine-tuned transformer model. Deployed with streamlit.

Recommendation: Movies and books (or only movies)

#### Let's build that baby
*** Step by step:

Back:
> Recommendation 
    - Choose the dataset for fine tuning - ok 
    - pick a transformer model - ok 
    - fine-tune and see results? - ok

> Chatbot 
    - Build a conversational chatbot that will recommend a movie/series based on a descriptive tastes/interests user input

    - If asked about the movie/series, chatbot needs to give the full description.  

Front:
> Streamlit
    > Chatbot integratation


#### Draft






#### **What is included here?**

* `app/main.py`: Main app file and docker entrypoint. This defines the FastAPI logic;
* `app/model.py`: Utility file that defines the model's logic;
* `app/static/`: Contains the icons and CSS files
* `app/templates/`: Contains the `index.html` template file that will be modified at run time with the dialog HTML using jinja
* `Dockerfile`: Defines the steps needed to install all required libraries, and run the FastAPI app (`app.main.py`).
* `test/test_app.ipynb`: Testing notebook file

#### **How to run?**
1. Clone the repository to your local machine
2. Build the docker container `docker build . -t chatbot`
3. Run the container `docker run -p 8000:8000 chatbot`
4. Type http://0.0.0.0:8000/ in your favorite browser to interact with the app
