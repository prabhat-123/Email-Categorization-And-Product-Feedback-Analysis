import openai
import json
from json.decoder import JSONDecodeError
import config as cfg 

class ProductTitleGenerator:
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

    def generate_product_title(self, query):
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
                I want you to act as a Topic Modeller or a Title Generator for the query email.  
                Instructions:
                The email can have multiple paragraphs and of various writing styles.
                You must generate a short title for the query email and the output must be in a JSON format.
                The key of the generated json output will be product_title.
                """
                }
            ],
            max_tokens=128,
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
            print(final_json_response)
            return final_json_response
        except JSONDecodeError as e:
            return e
            # return {"query": self.query}
