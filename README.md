# Recommender Chatbot with Fine-Tuned Transformer Model

## What is this?

This project implements an intelligent chatbot that provides movie and tv series recommendations based on user preferences expressed through natural language conversation. It leverages a fine-tuned transformer model for both understanding user input and generating relevant recommendations. The application is deployed using Streamlit, providing an interactive and user-friendly experience.

## Description

This project combines the power of conversational AI with a robust recommendation system. Users interact with the chatbot to describe their tastes and interests in movies and tv series. The chatbot, powered by the "facebook/blenderbot-400M-distill" model, is designed to understand these descriptions, even if they are complex or nuanced.  It can also provide detailed information about recommended items if requested.  This conversational approach allows for a more personalized and dynamic recommendation experience compared to traditional methods.

The recommendation engine utilizes Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.  This model generates high-quality sentence embeddings, enabling the system to capture the semantic meaning of user input and match it with relevant movies or books in the database.  This ensures that recommendations are not just based on keywords, but on a deeper understanding of the user's preferences.

The front-end is built with Streamlit, making the application accessible and easy to use.  The Streamlit Chatbot component provides a seamless interface for interacting with the chatbot and viewing recommendations.

## Key Features

* **Conversational Recommendations:**  Users can express their preferences in natural language, leading to more personalized and accurate recommendations.
* **Chat-bot Model:** The "facebook/blenderbot-400M-distill" model is used for natural language understanding and generation, enabling engaging and informative conversations.
* **Semantic Recommendation Engine:** Sentence-BERT provides semantically rich embeddings for user input and items, ensuring relevant recommendations.
* **Movie and series Recommendations:** The system can be configured to recommend either movies and books or just movies, depending on the dataset used.
* **Streamlit Deployment:** The Streamlit interface makes the application easy to use and accessible through a web browser.

## Technical Details

* **Chatbot Model:** "facebook/blenderbot-400M-distill"
* **Recommendation Model:** Sentence-BERT (Sentence Embeddings using Siamese BERT-Networks)
* **Front-end:** Streamlit, Streamlit Chatbot component
* **Back-end:** Python
* **Libraries/Frameworks:** sentence_transformers, transformers, Pytorch
