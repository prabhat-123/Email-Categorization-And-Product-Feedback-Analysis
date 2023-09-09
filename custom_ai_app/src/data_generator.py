import openai
import pandas as pd
from tqdm import tqdm
import config as cfg 

class DataGenerator:
    openai.api_key = open(cfg.OPENAI_API_PATH, "r").read().strip('\n')
    def __init__(self):
        """
        Initialize the ProductSentimentAnalyzer with model settings and API key.
        """
        self.model_name = "gpt-3.5-turbo"
        self.role = "user"


    def generate_angry_email(self, query):
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
                I want you to write an email as an angry customer who seems angry because of the 
                software bugs or technical issues you are facing associated with the product.
                The name of the product will be mentioned in the ticket to be provided below.
                ### Query Email: "{self.query}"
                ### Instructions: 
                Name of the product should be included in the generated email. The product name is provided 
                in the ticket above.
                You can just take ideas from the description provided while generating an email.
                The email generation should be based upon the products mentioned in the ticket.
                The output must be in a string format.
                Donot generate anything extra besides the email.
                There should be variations in the output email generated.
                Try different ways that a customer can respond whenever they are angry.
                Donot Generate email consisting of more than 400 tokens. Try to finish the email within 450 tokens.
                Some emails can also have a shorter length than the desired lenghth.
                """
                }
            ],
            max_tokens=500,
            temperature=0.05,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response = completion['choices'][0]['message']['content']
        return response
        
    def generate_help_email(self, query):
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
                I want you to write an email as a customer asking for help regarding the product 
                setup, installation support, product related issues and queries, and inquiry about the
                usage of products and so on. The name of the product will be mentioned in the ticket 
                to be provided below.
                ### Query Email: "{self.query}"
                ### Instructions: 
                Name of the product should be included in the generated email. The product name is provided 
                in the ticket above.
                You can just take ideas from the description provided while generating an email.
                The email generation should be based upon the products mentioned in the ticket.
                The output must be in a string format.
                Donot generate anything extra besides the email.
                There should be variations in the output email generated.
                Try different ways that a customer can use when asking for help.
                Donot Generate email consisting of more than 400 tokens. Try to finish the email within 450 tokens.
                Some emails can also have a shorter length than the desired lenghth.
                """
                }
            ],
            max_tokens=300,
            temperature=0.05,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response = completion['choices'][0]['message']['content']
        return response

    def generate_happy_email(self, product):
        """
        Analyze a product query email and extract relevant information.

        Args:
            query (str): The input query email text.

        Returns:
            dict: A dictionary containing the extracted information, including product sentiment, titles, and categories.
        """
        self.product = product
        completion = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": self.role,
                "content": f"""
                I want you to write an email as a satisfied customer praising the 
                new features of the product. The name of the products will be provided. You have to 
                generate happy customer email praising the features of that particular product.'
                ### Product Name: "{self.product}"
                ### Instructions: 
                The email generation should be based upon the products mentioned in the query.
                The output must be in a string format.
                Donot generate anything extra besides the email.
                There should be variations in the output email generated.
                Try different ways of expressions that a customer show while 
                responding whenever they are happy regarding the release of new features, upgrades, proper maintainance and others.
                Donot Generate email consisting of more than 450 tokens. Try to finish the email within 450 tokens.
                Some emails can also have a shorter length than the 200 tokens as well.
                """
                }
            ],
            max_tokens=500,
            temperature=0.05,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response = completion['choices'][0]['message']['content']
        return response

    def text_writer(self, text):
        file = open(cfg.TEXT_FILE_PATH, 'a')
        file.write(text)
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')        


    def generate_data(self):
        df = pd.read_csv(cfg.RAW_DATA_PATH)
        df = df.iloc[442:]
        new_data = {"ticket_subject": [], "product_name": [],
                    "product_type": [], "email": []}
        for item in tqdm(df.values):
            new_data['ticket_subject'].append(item[1])
            new_data['product_name'].append(item[-2])
            new_data['product_type'].append(item[-1])
            if item[1] == "Software bug":
                # angry emails
                angry_email = self.generate_angry_email(item[2])
                new_data['email'].append(angry_email)
                self.text_writer(angry_email)

            elif item[1] == "Awesome Addition":
                # happy emails
                happy_email = self.generate_happy_email(item[2])
                new_data['email'].append(happy_email)
                self.text_writer(happy_email)

            else:
                # asking for help
                help_email = self.generate_help_email(item[2])
                new_data['email'].append(help_email)
                self.text_writer(help_email)


if __name__ == "__main__":
    datagen_obj = DataGenerator()
    email_df = datagen_obj.generate_data()
