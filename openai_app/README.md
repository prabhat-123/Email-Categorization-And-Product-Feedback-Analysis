# 🚀 Usage

After installing the required dependencies and adding your OpenAI API key to `tm_api_key.txt`, follow these steps to run the Email Categorization and Product Feedback Analysis project:

## Prerequisites

Ensure that you have completed the initial setup and activated your virtual environment as described in the Installation and Setup section.

## Starting the FastAPI Server

1. **Navigate to the `src` directory:**
```
cd src
```

2. **Start the FastAPI server:**
Run the following command to launch the FastAPI server:
```
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The FastAPI server will start running and listen on port 8000.

## Launching the Streamlit UI

3. **Open a new terminal or command prompt.**

4. **Navigate to the `src` directory:**
```
cd src
```

5. **Activate the virtual environment:**
Ensure that your virtual environment is activated. If not, activate it using the appropriate command.

6. **Start the Streamlit UI:**
Run the following command to launch the Streamlit user interface:
```
streamlit run streamlit_app.py
```

The Streamlit UI will automatically open in your default web browser.

## Accessing the Application

You can now access and interact with the Email Categorization and Product Feedback Analysis application through the Streamlit UI in your web browser. Use the interface to input queries, analyze product sentiment, and explore the results.

Make sure to keep the FastAPI server running in the background to enable real-time communication with the Streamlit UI.

Enjoy exploring the project and analyzing customer emails with ease! 📧🔍


