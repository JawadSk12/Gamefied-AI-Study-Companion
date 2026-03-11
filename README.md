# 🎓 Gamified AI Study Companion

An AI-powered learning assistant that helps students **understand concepts, generate quizzes, and track learning progress** through a gamified system.

This project demonstrates how **Large Language Models (LLMs)** can be integrated into an educational platform to create a **24×7 AI tutor experience**.

---

# 🚀 Project Overview

The **Gamified AI Study Companion** is a GenAI-powered platform designed to assist students in learning technical concepts more effectively.

The system allows students to:

- Ask AI for concept explanations
- Generate quizzes on any topic
- Attempt quizzes and receive instant feedback
- Track progress and learning analytics
- Generate personalized study plans

Gamification elements such as **points, levels, and badges** help keep students engaged while learning.

---

# ✨ Features

## 🤖 AI Tutor
Students can ask conceptual questions such as:

```
Explain Neural Networks
Explain TCP vs UDP
Explain Linear Regression
```

The AI generates **student-friendly explanations** using a Large Language Model.

---

## 📝 AI Quiz Generator

Students can generate quizzes by selecting:

- Topic
- Difficulty
- Number of questions

Example:

```
Topic: Machine Learning
Difficulty: Medium
Questions: 5
```

The system generates **multiple-choice questions dynamically** using an AI model.

---

## 🎯 Quiz Attempt & Instant Feedback

Students can attempt quizzes and receive immediate feedback.

- Correct answers → highlighted in **green**
- Incorrect answers → highlighted in **red**

This helps reinforce learning through instant evaluation.

---

## 🏆 Gamification System

The application includes a simple gamification mechanism.

### Points System

| Action | Points |
|------|------|
Ask AI question | +5  
Correct quiz answer | +10  
Finish quiz | +20  

### Levels

| Points | Level |
|------|------|
0–50 | Beginner  
50–150 | Intermediate  
150+ | Advanced  

Badges are unlocked as students progress.

---

## 📊 Learning Analytics Dashboard

The progress page provides insights into:

- Questions asked
- Quizzes taken
- Accuracy percentage
- Weekly learning activity

This allows students to monitor their learning progress.

---

## 📅 AI Study Plan Generator

Students can generate structured study plans.

Example input:

```
Subject: Machine Learning
Days: 10
```

Example output:

```
Day 1 → Introduction to Machine Learning
Day 2 → Linear Regression
Day 3 → Logistic Regression
Day 4 → Decision Trees
Day 5 → Random Forest
```

---

# 🏗️ System Architecture

The project follows a **modular architecture** to separate UI, AI logic, and application logic.

```
Frontend Layer
Streamlit UI

Application Layer
Python Backend (app.py)

AI Layer
LLM APIs via LangChain

Logic Layer
Quiz Engine
Gamification Engine

Utility Layer
Helper Functions

Data Layer
Session State / JSON Memory
```

---

# 📂 Project Structure

```
AI-Study-Companion
│
├── app.py
│
├── tutor_engine.py
├── quiz_generator.py
├── gamification_engine.py
├── study_plan_generator.py
│
├── utils
│   └── helpers.py
│
├── notebooks
│   ├── prompt_engineering.ipynb
│   ├── quiz_generation.ipynb
│   ├── gamification_simulation.ipynb
│   └── learning_analytics.ipynb
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Integration
- LangChain
- Groq / OpenAI / Gemini APIs

### Data Handling
- JSON
- Session State

### Visualization
- Streamlit Charts

---

# 🧠 AI Components

The system integrates AI models for multiple tasks.

### Concept Explanation
Uses LLM prompts to generate **clear educational explanations**.

### Quiz Generation
LLM generates structured MCQs in JSON format.

### Study Plan Generation
LLM produces **daily study schedules** based on user goals.

---

# 🔧 Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/AI-Study-Companion.git
cd AI-Study-Companion
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate environment.

### Mac / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔑 API Setup

Set your API key for the LLM provider.

Example for Groq.

### Mac / Linux

```bash
export GROQ_API_KEY="your_api_key"
```

### Windows

```bash
set GROQ_API_KEY=your_api_key
```

---

# ▶️ Run the Application

Start the Streamlit server.

```bash
streamlit run app.py
```

Open the application.

```
http://localhost:8501
```

---

# 🧪 Machine Learning Notebooks

The repository includes notebooks for experimentation.

| Notebook | Purpose |
|--------|--------|
prompt_engineering.ipynb | LLM prompt experiments |
quiz_generation.ipynb | Quiz generation experiments |
gamification_simulation.ipynb | Gamification system testing |
learning_analytics.ipynb | Learning progress analysis |

---

# 📈 Future Improvements

Possible enhancements include:

- User authentication
- Persistent learning history
- Adaptive quizzes based on performance
- Personalized AI tutoring
- Leaderboards and streak systems
- Mobile app integration

---

# 🎥 Demo

A demo video explaining the application, architecture, and code walkthrough is included with the submission.

---

# 👨‍💻 Author

**Jawad SK**

Computer Engineering Student  
Interested in AI Engineering, LLM Applications, and Intelligent Systems.

---

# 📜 License

This project is for educational and demonstration purposes.
