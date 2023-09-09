import openai
import json
from json.decoder import JSONDecodeError
import config as cfg 

class ProductSentimentAnalyzer:
    openai.api_key = open(cfg.OPENAI_API_PATH, "r").read().strip('\n')
    def __init__(self):
        """
        Initialize the ProductSentimentAnalyzer with model settings and API key.
        """
        self.model_name = "gpt-3.5-turbo"
        self.role = "user"

    def extract_json_content(self, text):
        """
        Extracts JSON content from a given text.

        Args:
            text (str): The input text containing JSON content.

        Returns:
            str: The extracted JSON content as a string.
        """
        start_pos = text.find("{")
        end_pos = text.rfind("}") + 1
        json_string = text[start_pos:end_pos]
        return json_string

    def analyze_product_query(self, query):
        """
        Analyze a product query email and extract relevant information.

        Args:
            query (str): The input query email text.

        Returns:
            dict: A dictionary containing the extracted information, including product sentiment, titles, and categories.
        """
        self.query = query
        completion = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": self.role,
                "content": f"""
                ### Query Email: "{self.query}"
                Context 1: I want you to act as a Named entity extractor for identifying the names of the products that have been mentioned
                in the query email. Additionally, you also need to categorize the product into the 
                following categories:
                1) ERP,
                2) Appointment Booking Software,
                3) CRM,
                4) Others

                Context 2: I want you to act as a Topic Modeller or a Title Generator for the query email.  

                Context 3: I want you to act as an Email Sentiment Analyzer for the given query email. You need to identify the following sentiments:
                1) Emails asking for help -> Help Request
                2) Angry emails when they see bugs -> Angry Request
                3) Happy emails praising the new feature -> Happy Response

                Instructions:
                The email can be one paragraph and multiple paragraphs.
                You need to generate an output response for all three contexts and the output must be in a JSON Format.
                Combine the output generated from all context1, context2, and context3 in a single JSON response.
                The output of a JSON response should be like this:
                "customer_sentiment": ""
                "product_title": ,
                "product": "product_name": "",  "product_category": "",
                """
                }
            ],
            max_tokens=256,
            temperature=0.05,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response = completion['choices'][0]['message']['content']
        tokens_used = completion['usage']['total_tokens']
        try:
            json_response = self.extract_json_content(response)
            json_response = json.loads(json_response)
            final_json_response = {key: value for key, value in json_response.items() if value is not None and value != ""}
            return final_json_response
        except JSONDecodeError as e:
            return {"query": self.query}
