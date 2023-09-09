# 📧 Email Categorization and Product Feedback Analysis (POC) 🚀

## Overview

Welcome to the Email Categorization and Product Feedback Analysis POC project. This repository showcases a prototype solution designed to address the challenge of categorizing customer emails and analyzing feedback related to various software products. 💌🔍

## Problem Statement

**Problem:** Our company receives a vast number of emails from customers, covering a range of topics related to our software products, including CRM, ERP, appointment booking software, and more. These emails contain valuable insights, such as customer support requests, bug reports, and feature requests, among others. However, with millions of emails pouring in, it's becoming increasingly challenging to manually categorize and analyze them. 😓

**Objective:** The goal of this POC project is to demonstrate a solution that can automatically categorize incoming customer emails into different categories, each associated with a specific software product. Additionally, we aim to derive meaningful titles for each category, making it easier for our executive team to understand and act on the feedback. 🎯

**Scope:** This POC is a demonstration of the core concept and is not intended as a final product. It serves as a starting point for exploring the feasibility of automating email categorization and feedback analysis. 🌱

## Prototype Features

The prototype includes the following key features: 🧩

1. **Email Categorization:** Incoming emails are automatically categorized into relevant software product categories. 📥🗂️

2. **Feedback Analysis:** The content of emails is analyzed to identify sentiments, such as customer satisfaction or dissatisfaction. 📊📈

3. **Title Generation:** Meaningful titles are derived for each category, summarizing the key feedback themes. 📌📝

## Approaches

### 1. Custom AI Model Approach

**Source Code:** [custom_ai_app](/custom_ai_app)

🧠 We initially attempted to create our custom AI model to address the problem. However, we encountered challenges in obtaining a sufficiently large and diverse real dataset to achieve the desired accuracy.

**Challenges Faced:**

- **Data Availability:** Finding a good enough real dataset proved to be challenging.
- **Model Training:** Training a custom model required significant computational resources.

**Results:** Despite the challenges, our custom model showcases the potential for solving the problem statement.

### 2. OpenAI's Language Model Approach

**Source Code:** [openai_app](/openai_app)

🤖 As an alternative, we leveraged the power of large language models (LLMs) like OpenAI's GPT-3.5. We used prompt engineering techniques to harness the capabilities of GPT-3.5 for email categorization and feedback analysis.

**Key Advantages:**

- **Vast Knowledge:** LLMs have access to a vast amount of knowledge and context.
- **Rapid Prototyping:** Prompt engineering allows for rapid development and experimentation.

**Results:** Using GPT-3, we achieved impressive results in email categorization and feedback analysis.

# 🛠️ Technology & Tech Stacks Used

The Email Categorization and Product Feedback Analysis POC project was built using Python 3.8.0 and leveraged various libraries and frameworks to achieve its objectives. 🐍💻

## Technologies Used

1. **Python 3.8.0** 🐍
   - Python served as the core programming language for developing the project. Its versatility and rich ecosystem of libraries made it an ideal choice.

## Python Libraries & Frameworks

2. **uvicorn==0.22.0** 🚀
3. **pandas==1.3.5** 🐼
4. **fastapi==0.97.0** 🚀
5. **streamlit==1.24.0** 🌟
6. **python-multipart==0.0.6** 📦
7. **openai==0.27.8** 🤖
8. **spacy==3.5.3** 🌐
9. **gdown==4.7.1** 📥
10. **scikit-learn==1.2.2** 🧠
11. **seaborn==0.12.2** 📊
    
## Python Environment

To reproduce the results of this project, it is recommended to set up a Python 3.8.0 environment, as the project has not been tested on other Python versions.

These technologies and libraries collectively empowered Email Categorization and Product Feedback Analysis POC, enabling efficient data processing, analysis, and interaction.


## Getting Started

To explore this POC, follow these steps:

### Installation and Setup

1. Clone the repository:
   ```
   https://github.com/prabhat-123/Email-Categorization-And-Product-Feedback-Analysis.git
   ```

2. Before running any files, you have to set up  virtual environment.

   ##### i) First of all you have to install virtual environment tool to create one.
   For installation:   
      python -m pip install --user virtualenv
      
      
   ##### Recommended
   For installing a virtual environment on Anaconda Prompt(Windows):

       conda install -c anaconda virtualenv

   ```
   python -m venv env
   ```

4. Activate the virtual environment:
   - For Windows:
     ```
     env\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source env/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 📜

## Acknowledgments

We would like to express our gratitude to the open-source community and all contributors who have made this POC project possible. 🙏✨

---

**Note:** This README serves as an introduction to the Email Categorization and Product Feedback Analysis POC project. Detailed instructions and documentation can be found within the repository. 📚📖
