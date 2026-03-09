import streamlit as st

st.set_page_config(
    page_title="AI Study Companion",
    layout="wide"
)

st.title("🎓 Gamified AI Study Companion")

menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "AI Tutor",
        "Generate Quiz",
        "Quiz Attempt",
        "Progress Dashboard",
        "Study Plan Generator"
    ]
)

if menu == "AI Tutor":
    st.header("AI Tutor")

    question = st.text_input("Ask a question")

    if st.button("Ask AI"):
        st.write("AI response will appear here.")

elif menu == "Generate Quiz":
    st.header("Quiz Generator")

elif menu == "Quiz Attempt":
    st.header("Quiz Attempt")

elif menu == "Progress Dashboard":
    st.header("Progress Dashboard")

elif menu == "Study Plan Generator":
    st.header("Study Plan Generator")