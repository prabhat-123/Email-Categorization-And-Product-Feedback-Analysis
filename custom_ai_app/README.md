# Hybrid Approach for Product Categorization, Email Sentiment Analysis, and Product Title Generation 🚀

Welcome to our hybrid approach repository! Here, we've combined the power of custom models for product categorization and email sentiment analysis with OpenAI's capabilities for title generation.

## Custom Model Development 🤖

For **product categorization** and **email sentiment analysis**, we've developed a custom model tailored to our unique requirements. This model is a prototype model to demonstrate product categorization and identify customer sentiments in emails. 📈

## The Perfect Dataset 📊

To construct our custom model, we needed the right dataset that aligned perfectly with our problem statement. After an exhaustive search, we stumbled upon the "Customer Support Ticket Dataset" on Kaggle, which turned out to be a goldmine for our purposes. 🕵️‍♂️

### Customer Support Ticket Dataset 💬

This remarkable dataset covers customer support tickets related to various tech products. It includes inquiries regarding hardware issues, software bugs, network problems, account access, data loss, and other support-related topics. 🌐💻

#### Key Information 📋

- Customer details 🧑🏽‍💼
- Product information 🛒
- Ticket types 📝
- Ticket channels 📬
- Ticket statuses ✅❌
- And other pertinent details 📊

## Access the Dataset 📦

You can access this valuable dataset using the following link: [Customer Support Ticket Dataset](https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset). 📂

## Data Utilization 🧐

We found this dataset to be a perfect fit for modeling our problem statement, especially when dealing with customer inquiries seeking assistance. Moreover, we identified a specific ticket type for software bugs within the dataset, which became the foundation for generating emails expressing frustration and anger from customers. 🤬😡

# Data Generation Notebook 📊

In our notebooks section, you'll discover the 'data_creation_from_ticket_dataset.ipynb' notebook file. This notebook plays a crucial role in our project as it effectively utilizes the customer support ticket dataset to craft a dataset that aligns perfectly with our use case.

## Dataset Creation 📈

Upon successfully running this notebook, you'll be rewarded with the freshly minted 'product_sentiment_analysis.csv' dataset. We've conveniently organized this dataset within a dedicated 'data' folder for effortless access and seamless integration into our project.

## Leveraging OpenAI for Dataset Generation 🌐

In our innovative approach, we rely on OpenAI's advanced capabilities to generate datasets tailored to our unique use case. We create two types of emails: those expressing frustration and anger from customers, and those conveying happiness and satisfaction. 

# Leveraging OpenAI for Dataset Generation 🌐

In our innovative approach, we rely on OpenAI's advanced capabilities to generate datasets tailored to our unique use case. We create two types of emails: those expressing frustration and anger from customers, and those conveying happiness and satisfaction.

## Data Generation Process 🧠

Located inside the 'src' folder, you'll find the 'data_generator.py' file. This file employs prompt engineering techniques to harness OpenAI's power in creating datasets. It generates a dataset with 450 rows and compiles them into an 'email.txt' file, providing us with a diverse set of emails for different use cases.

**Folder Name:** 'src'

**Python File Name:** 'data_generator.py'

**Output Generated:** 'email.txt'

## Enhancing Data Variability 🔄

Within the same 'src' folder, you'll discover the 'data_preprocessing.py' file. This script plays a vital role in processing our generated data, introducing variations to mitigate the repetition of phrases that can occur during email generation by OpenAI. The outcome of this process is the 'prod_email.csv' file, a rich dataset that we utilize to train our custom models for both email sentiment analysis and product categorization.

**Folder Name:** 'src'

**Python File Name:** 'data_preprocessing.py'

**Output Generated:** 'prod_email.csv'

# Custom Model Training 🧠

In our project, we've developed two distinct models: one for product categorization and another for customer sentiment analysis.

## Customer Sentiment Analysis Model 📊

To train the customer sentiment analysis model, follow these steps:

1. Navigate to the 'notebooks' directory.
2. Open the 'email_sentiment_classification_using_tfidf.ipynb' notebook.
3. Execute the notebook meticulously to train the custom model.

Upon successful execution, the following three models will be generated and stored inside the 'models' directory:

- `classifier_model.pkl`: The trained model for customer sentiment analysis.
- `label_encoder.pkl`: A label encoder for mapping sentiment labels.
- `tfidf_vectorizer.pkl`: The TF-IDF vectorizer used for text feature extraction.

These models collectively enable the analysis of customer sentiment in emails.
Please ensure that you follow the instructions in the notebook diligently to train the model effectively.

# Model Inference for Email Sentiment Analysis 📝

After successfully training the customer sentiment analysis model using the 'email_sentiment_classification_using_tfidf.ipynb' notebook, you can perform inference using the 'email_sentiment_classification_inference.ipynb' notebook.

To utilize the trained model for sentiment analysis, follow these steps:

1. **Location**: Navigate to the **'notebooks' directory**.
2. **Notebook File Name**: Open the **'email_sentiment_classification_inference.ipynb'** notebook.
   
Upon executing the notebook, you will generate:

- **Output**: Sentiment analysis results for emails.

This notebook is designed to facilitate the practical application of the trained model for analyzing the sentiment of emails.

Feel free to use this notebook to gain insights into email sentiments after training the model.




By combining our custom model with OpenAI's expertise, we've crafted a prototype solution to handle product categorization, email sentiment analysis, and even generate compelling product titles. 🌈💼



## 🧩 Our Approach

- **Hybrid Model**: We developed a custom model for product categorization and email sentiment analysis, harnessing the strengths of both.

- **Title Generation**: Leveraging OpenAI's capabilities, we utilized title generation for certain tasks.

