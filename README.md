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

🤖 As an alternative, we leveraged the power of large language models (LLMs) like OpenAI's GPT-3. We used prompt engineering techniques to harness the capabilities of GPT-3 for email categorization and feedback analysis.

**Key Advantages:**

- **Vast Knowledge:** LLMs have access to a vast amount of knowledge and context.
- **Rapid Prototyping:** Prompt engineering allows for rapid development and experimentation.

**Results:** Using GPT-3, we achieved impressive results in email categorization and feedback analysis.


## Getting Started

To explore this POC, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine. 🖥️

2. **Setup:** Follow the setup instructions in the `README` or `setup.md` file for any specific environment configurations. ⚙️

3. **Run the Prototype:** Execute the prototype code to see how email categorization and feedback analysis work. 🚀

## Feedback and Contributions

This is a proof of concept project, and we welcome feedback and contributions to help improve and extend its capabilities. Please feel free to open issues, provide suggestions, or submit pull requests. 🙌🤝

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 📜

## Acknowledgments

We would like to express our gratitude to the open-source community and all contributors who have made this POC project possible. 🙏✨

---

**Note:** This README serves as an introduction to the Email Categorization and Product Feedback Analysis POC project. Detailed instructions and documentation can be found within the repository. 📚📖
