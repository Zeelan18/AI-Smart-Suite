# 🤖 AI Smart Suite

> **One Platform • Multiple AI Solutions**

AI Smart Suite is a modern AI-powered web application developed using **Python** and **Streamlit**. It combines multiple AI tools into a single platform with a clean dashboard, authentication system, and usage analytics.

This project was developed as part of **Task 04 – AI Multi-Tool Platform**.

---

## 📌 Features

* 🔐 User Login Authentication (Temporary Session-Based)
* 🏠 Professional Dashboard
* 💬 AI Chat Assistant
* 📝 AI Text Summarizer
* 😊 Sentiment Analysis
* 📄 AI Resume Analyzer
* 📊 Usage Analytics Dashboard
* 🎨 Modern Responsive UI

---

## 🚀 AI Modules

### 💬 AI Chat Assistant

* Ask questions in natural language
* Powered by Google Gemini AI
* Interactive chat interface

### 📝 Text Summarizer

* Generate concise summaries from long text
* Multiple summary styles
* Fast AI-powered responses

### 😊 Sentiment Analysis

* Detects Positive, Negative, or Neutral sentiment
* Provides confidence and explanation

### 📄 Resume Analyzer

* Upload PDF resumes
* ATS compatibility analysis
* Resume score
* Strengths & weaknesses
* Missing skills
* Improvement suggestions

### 📊 Analytics Dashboard

* Tracks AI tool usage
* Interactive charts
* Module usage statistics

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI

* Google Gemini API

### Libraries

* Streamlit
* Google Generative AI
* Plotly
* Pandas
* PDFPlumber
* Python Dotenv

---

## 📂 Project Structure

```text
AI-smart-suite/

│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── assets/
│
├── models/
│   ├── gemini_config.py
│   ├── chat_model.py
│   ├── summarizer.py
│   ├── sentiment.py
│   └── resume.py
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_AI_Chat.py
│   ├── 3_Text_Summarizer.py
│   ├── 4_Sentiment_Analysis.py
│   ├── 5_Resume_Analyzer.py
│   └── 6_Analytics.py
│
└── utils/
    ├── session.py
    └── styles.py
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Zeelan18/AI-smart-suite.git
```

Move into the project

```bash
cd AI-smart-suite
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📊 Project Workflow

```text
User Login
      │
      ▼
Dashboard
      │
      ▼
Select AI Module
      │
      ▼
Gemini AI Processing
      │
      ▼
Display Result
      │
      ▼
Update Analytics
```

---

## 📸 Screenshots

* Login Page
* Dashboard
* AI Chat Assistant
* Text Summarizer
* Sentiment Analysis
* Resume Analyzer
* Analytics Dashboard

---

## 🌟 Future Enhancements

* Image Classification
* AI Content Generator
* Voice Assistant
* User Database
* Chat History Storage
* Export Reports
* Multi-language Support

---

## 👨‍💻 Developer

**Zeelan I**

* Final Year B.Tech – Artificial Intelligence and Data Science
* Government College of Engineering, Bargur

GitHub: https://github.com/Zeelan18

---

## 📄 License

This project is developed for educational and internship purposes.
