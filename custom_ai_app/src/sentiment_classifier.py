import pickle
import warnings
warnings.filterwarnings('ignore')


class Email_Sentiment_Classifier:
    def __init__(self, email):
        self.email = email

    def load_pickle_model(self, model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
            return model
        
    def predict_sentiment(self, le_model, tfidf_model, clf_model):
        tfidf_email = tfidf_model.transform([self.email])
        email_sentiment_label = clf_model.predict(tfidf_email)
        email_sentiment = le_model.inverse_transform(email_sentiment_label)[0]
        return email_sentiment





