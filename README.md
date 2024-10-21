---
title: Europe Based Hotel Recommendation System
emoji: 😻
colorFrom: blue
colorTo: gray
sdk: streamlit
sdk_version: 1.38.0
app_file: Web_App.py
pinned: false
---

Status Badge: [![Sync to Hugging Face hub](https://github.com/Ahmad-Baseer/Europe-Based-Hotel-Recommendation-System/actions/workflows/CD_to_HuggingFace.yml/badge.svg)](https://github.com/Ahmad-Baseer/Europe-Based-Hotel-Recommendation-System/actions/workflows/CD_to_HuggingFace.yml/)

# How to run the application


## Follow the steps to configure this application:

1. Download all the files and place them in a specific folder. Open up Jupyter Notebook in your working folder.
2. Install the libraries first before running notebooks. Remove the ```#``` sign from the lines to allow nltk to download required files & to see if everything works fine or not.
3. Download the Hotel Reviews dataset from [here](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe)
4. Run the **Hotel_Recommendation_System** file first and then **Hotel Recommendation System Web App**, after running the second one you should see this: **Overwriting Web_App.py** in output.
5. Open up the terminal in the same folder and type this command: ```streamlit run Web_App.py```. It will open your application in your default browser.
6. Now, you can follow any YouTube video to deploy this application or you can enter your credentials to use my workflow as it is to deploy this application to your hugging face space.
7. You can use my application here: [Europe-based-hotel-recommendation-system](https://huggingface.co/spaces/AhmadHashim/Europe-based-hotel-recommendation-system)

## Complete working of this application:

### Data Preprocessing
Data preprocessing is a crucial first step in every project. It not only optimizes the performance of your application but also improves efficiency and accuracy.

To begin the preprocessing, use the following basic commands:
```bash
data.head()
data.tail()
data.info()
```
These commands help you visualize the dataset to understand its patterns and structure. The ```data.info()``` function provides details such as the count of non-null values and the data type of each column. This helps you decide whether the existing data types are appropriate for your application, or if any changes are required. Additionally, if there are many missing values, you can decide whether to drop those records or apply a strategy to handle them.

Based on this dataset, I follow these preprocessing steps:

1. Changing country names to alpha-2 codes for simplicity.
2. Extracting country information from the ```hotel_address``` column and storing it in a separate column.
3. Dropping unnecessary columns to focus only on relevant data.
4. Ensuring consistent formatting in the ```tags``` column, which is crucial for the application.
5. Removing punctuation (such as commas and apostrophes) to simplify data manipulation.

By performing these preprocessing steps, the dataset becomes cleaner and easier to work with, allowing for more accurate and efficient results.

### Hotel Recommender System Functionality
The hotel recommender system is designed to provide personalized hotel suggestions based on a user's location and description. Below are the steps followed in the recommendation process:

1. **Text Tokenization and Lowercasing:**
The user-provided description is first converted to lowercase and then split into individual words (tokens). This step ensures consistency in text comparison, as it treats words like "Hotel" and "hotel" as the same. Tokenization further helps break down the text into manageable units for analysis.

2. **Stopword Removal:**
Common English stopwords (e.g., "and," "the") are removed to eliminate irrelevant words from the analysis. This allows the system to focus on the most significant parts of the description, improving the accuracy of matching user preferences with hotel tags.

3. **Lemmatization:**
Lemmatization is applied to reduce words to their base form (e.g., "running" becomes "run"). This step is crucial because it ensures that different forms of the same word are treated equally, enhancing the system's ability to match the user’s description with relevant hotels.

4. **Filtering and Matching:**
After removing stopwords and lemmatizing the words, the system filters hotels based on the provided location. The filtered set of words from the user’s description is compared with the tags associated with each hotel. This step helps match hotels that best align with the user's preferences based on the location they are interested in.

5. **Cosine Similarity Calculation:**
The system calculates a similarity score for each hotel by finding the intersection between the user’s description and the hotel tags. Cosine similarity is used to measure how closely the two sets of words match, allowing the system to rank hotels based on relevance.

6. **Hotel Ranking and Selection:**
Hotels are ranked first by their similarity score and then by their average review score. The highest-rated hotels with the most relevant matches are recommended to the user. The system ensures that duplicate hotel entries are removed and returns the top 10 hotels, displaying their name, average score, and address.

By following these steps, the system provides a refined list of hotels that are both highly relevant to the user’s description and highly rated by other customers.

### Web Application
The front end is built with **Streamlit** for an interactive and responsive front-end experience. I have included the following features in it.

1. I started by allowing the user to select a country from a predefined list of European countries. For the description, instead of limiting the user to fixed options like "business trip" or "leisure trip," I give them the flexibility to type a custom description in a **dynamically growing text area**. This ensures that the user can provide a detailed and personalized input, which will later be processed for hotel recommendation.

2. After entering the country and trip description, the user can press the **Recommend** button. This triggers the recommendation system, which processes the input data by tokenizing, removing stopwords, and applying lemmatization, before calculating the similarity score between the user’s input and the hotel tags.

3. The system returns the top 10 hotel recommendations based on similarity score and rating. These hotels are sorted by their **Average Score** and filtered to remove duplicates. The final result is displayed in a **dataframe**, making it easy for users to view relevant details such as **Hotel Name**, **Average Score**, and **Hotel Address**.

4. To enhance user experience, the app features Lottie animations and interactive elements such as balloons and snow effects when the recommendations are generated. Additionally, a contact form is included at the bottom of the page, allowing users to get in touch with me directly.

This approach ensures that the app is both intuitive and engaging for users, while the underlying NLP techniques guarantee accurate recommendations based on user input.

# Thanks for reading

