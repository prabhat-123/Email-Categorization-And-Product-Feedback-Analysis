
## Creating Custom Datasets

To train text classification models and a custom NER model, you need to create your own email datasets. Collect emails related to your products and label them accordingly for sentiment analysis and product categorization.

## Building Text Classification Models

1. **Prepare and preprocess your dataset:** Use data preprocessing techniques to clean and prepare your email dataset.

2. **Build and train text classification models:** Implement text classification models to analyze email sentiments, such as customer satisfaction, anger, or requests for help.

## Training a Custom NER Model

To categorize emails into products (e.g., CRM, ERP, APPOINTMENT_BOOKING_SOFTWARE, OTHERS), you can train a custom Named Entity Recognition (NER) model.

1. **Create a labeled dataset:** Annotate your email dataset with product labels using a tool like Prodigy or spaCy's `Matcher`.

2. **Train the NER model:** Utilize spaCy's training pipeline to train a custom NER model on the labeled dataset.

## Running the `custom_ai_app`

After creating custom datasets and training the required models, you can run the `custom_ai_app`:

1. **Navigate to the `custom_ai_app` directory:**


The `custom_ai_app` will launch, allowing you to analyze email sentiments and categorize products based on your trained models.

## Custom AI App Features

- **Email Sentiment Analysis:** Analyze customer sentiments in emails, including happiness, anger, or requests for assistance.

- **Product Categorization:** Automatically categorize emails into product categories (e.g., CRM, ERP, APPOINTMENT_BOOKING_SOFTWARE, OTHERS) using the custom NER model.

Enjoy exploring and utilizing the Custom AI Application for Email Sentiment Analysis and Product Categorization! 🧠📊🔖

