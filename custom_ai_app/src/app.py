import spacy
import uvicorn
import config as cfg
from fastapi import FastAPI, Request
from utils import clean_text, remove_stopwords
from product_title_generator import ProductTitleGenerator
from sentiment_classifier import Email_Sentiment_Classifier

app = FastAPI()

def classify_email_sentiment(clean_query):
    """
    Classify the sentiment of a cleaned email query using pre-trained models.
    Parameters:
    clean_query (str): The cleaned email query to classify sentiment for.
    Returns:
    str: The predicted sentiment of the email query, which can be one of the following:
         - 'Happy Email' (e.g., emails praising new features).
         - 'Help Request' (e.g., emails asking for help).
         - 'Angry Email' (e.g., emails reporting bugs).
    """
    sentiment_classifier = Email_Sentiment_Classifier(clean_query)
    tfidf_model = sentiment_classifier.load_pickle_model(cfg.TFIDF_VECTORIZER_PATH)
    clf_model = sentiment_classifier.load_pickle_model(cfg.CLASSIFIER_PATH)
    le_model = sentiment_classifier.load_pickle_model(cfg.LABEL_ENCODER_PATH)
    sentiment = sentiment_classifier.predict_sentiment(le_model, tfidf_model, clf_model)
    return sentiment

def classify_product(clean_query):
    """
    Extract and classify product information from a cleaned query using named entity recognition.

    Parameters:
    clean_query (str): The cleaned query containing product information.

    Returns:
    dict: A dictionary containing the extracted product name and category.

    Example:
    If the 'clean_query' contains information about a software product like 'Calendly' or other appointment booking softwares,
    this function will return a dictionary like:
    {'product_name': 'Calendly', 'product_category': 'APPOINTMENT_BOOKING_SOFTWARE'}

    Note:
    The function categorizes products into specific categories such as 'CRM', 'ERP', 'APPOINTMENT_BOOKING_SOFTWARE', or 'OTHERS'
    based on the recognized named entities in the input query.
    """
    prediction_result = {}
    nlp = spacy.load(cfg.NER_MODEL_PATH)
    doc = nlp(clean_query)
    for ent in doc.ents:
        if ent.text not in prediction_result:
            prediction_result[ent.label_] = ent.text
    product_name = list(prediction_result.values())[0]
    product_category = list(prediction_result.keys())[0]
    output_response = {"product_name": product_name, 
                        "product_category": product_category}
    return output_response

@app.post("/analyze_product_sentiment")  
async def analyze_product_sentiment(request: Request): 
    """
    Analyze the sentiment of a product-related query and generate a product title.

    Parameters:
    request (Request): A FastAPI Request object containing the user's query.

    Returns:
    dict: A dictionary containing the following information:
        - 'customer_sentiment': The sentiment of the query.
        - 'product': Extracted product details including name and category.
        - 'title': The generated product title.

    Example:
    When a user submits a query, this function processes it by cleaning the text,
    classifying customer sentiment, extracting product details, and generating a product title.
    The result is returned as a dictionary containing the sentiment, product details, and title.
    """
    form_data = await request.form()
    query = form_data.get("query")
    clean_query = clean_text(query)
    clean_query = remove_stopwords(clean_query)
    # Classify email sentiment
    sentiment_response = classify_email_sentiment(clean_query)
    # Clasify product 
    product_details = classify_product(clean_query)
    # Generate Title
    title_generator = ProductTitleGenerator()  
    output_response = title_generator.generate_product_title(query) 
    output_response['customer_sentiment'] = sentiment_response
    output_response['product'] = product_details
    return output_response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# uvicorn app:app --reload --host 0.0.0.0 --port 8000
