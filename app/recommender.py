# Import libs 
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util
import torch
from pathlib import Path


class Recommender: 
    def __init__(self, model_name='paraphrase-multilingual-MiniLM-L12-v2'):
        self.BASE_DIR = Path(__file__).resolve().parent
        self.model, self.des_embeddings = self.load_model(model_name)
  
    # Sentence Transformer model and saved embeddings
    def load_model(self, model_name):
        model = SentenceTransformer(model_name)
        
        des_embeddings = np.load(str(Path(self.BASE_DIR, '../input/descriptions-multiLM-embeddings/des_embeddings.npy')))
        return model, des_embeddings

    def data_processing(self):
        # path of csv files
        netflix_csv_path = str(Path(self.BASE_DIR, "../data/netflix_titles.csv"))
        amazon_csv_path = str(Path(self.BASE_DIR, "../data/amazon_titles.csv"))

        # Read CSV files from List
        df = pd.concat(map(pd.read_csv, [netflix_csv_path, amazon_csv_path]))
        data = df[['id','title', 'type', 'genres', 'description']]

        # removing missing movies/shows without descriptions
        data = data[~data['description'].isnull()].reset_index()

        # Concat genres and description
        data['genres_and_description'] = data['genres'].str.cat(data['description'], sep=', ')
        
        return data

    def recommend(self, query, type_query):
        #Compute cosine-similarities with all embeddings
        query_embedd = self.model.encode(query)
        cosine_scores = util.pytorch_cos_sim(query_embedd, self.des_embeddings)
        matches = torch.argsort(cosine_scores, dim=-1, descending=True).tolist()[0][1:50]


        # Get top 5 matches from database (our case from csv)
        data = self.data_processing()
        type_query = 'MOVIE' if type_query == 'movie' else 'SHOW'
        df = data.iloc[matches,:][data.type == type_query][:5][['title','genres_and_description','type']]
        df.index = np.arange(1, len(df) + 1)

        return df