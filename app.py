import streamlit as st

from tutor_engine import explain_concept
from quiz_generator import generate_quiz
from gamification_engine import add_points, get_level, get_badges
from study_plan_generator import generate_study_plan

from utils.helpers import (
    calculate_accuracy,
    calculate_progress,
    format_study_plan
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Gamified AI Study Companion",
    layout="wide",
    page_icon="🎓"
)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "points" not in st.session_state:
    st.session_state.points = 0

if "level" not in st.session_state:
    st.session_state.level = "Beginner"

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []

if "score" not in st.session_state:
    st.session_state.score = 0

if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = 0

if "quizzes_taken" not in st.session_state:
    st.session_state.quizzes_taken = 0


# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown(
"""
<div style="background: linear-gradient(120deg,#4f46e5,#22c55e);
padding:40px;border-radius:12px;color:white;margin-bottom:30px">

<h1>🎓 Gamified AI Study Companion</h1>
<p>Your intelligent AI tutor for learning concepts, quizzes and study planning.</p>

</div>
""",
unsafe_allow_html=True
)

# ---------------------------------------------------
# NAVIGATION TABS
# ---------------------------------------------------

tabs = st.tabs([
    "Dashboard",
    "AI Tutor",
    "Generate Quiz",
    "Attempt Quiz",
    "Progress",
    "Study Plan"
])

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

with tabs[0]:

    st.session_state.level = get_level(st.session_state.points)
    badges = get_badges(st.session_state.points)

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("⭐ Points", st.session_state.points)
    col2.metric("🏆 Level", st.session_state.level)
    col3.metric("❓ Questions Asked", st.session_state.questions_asked)
    col4.metric("📝 Quizzes Taken", st.session_state.quizzes_taken)

    st.divider()

    st.subheader("Weekly Learning Progress")

    progress = calculate_progress(st.session_state.points)

    st.progress(progress)

    st.caption("Earn points by asking AI questions and completing quizzes.")

    st.divider()

    st.subheader("Badges")

    if badges:
        for b in badges:
            st.write("🏅", b)
    else:
        st.write("No badges yet")

# ---------------------------------------------------
# AI TUTOR
# ---------------------------------------------------

with tabs[1]:

    st.header("AI Tutor")

    question = st.text_input(
        "Ask a question",
        placeholder="Explain Neural Networks"
    )

    if st.button("Ask AI"):

        if question:

            with st.spinner("AI thinking..."):

                response = explain_concept(question)

                st.markdown(response)

                st.session_state.points = add_points(
                    st.session_state.points,
                    "ask_question"
                )

                st.session_state.questions_asked += 1


# ---------------------------------------------------
# GENERATE QUIZ
# ---------------------------------------------------

with tabs[2]:

    st.header("Generate Quiz")

    topic = st.text_input("Topic")

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy","Medium","Hard"]
    )

    num_questions = st.slider(
        "Number of Questions",
        3,10,5
    )

    if st.button("Generate Quiz"):

        with st.spinner("Generating quiz..."):

            quiz = generate_quiz(topic,difficulty,num_questions)

            if quiz:

                st.session_state.quiz_questions = quiz

                st.success("Quiz generated successfully")

            else:

                st.error("Quiz generation failed")


# ---------------------------------------------------
# ATTEMPT QUIZ
# ---------------------------------------------------


with tabs[3]:

    st.header("Attempt Quiz")

    quiz = st.session_state.quiz_questions

    if not quiz:
        st.warning("Generate a quiz first.")
    else:

        answers = []

        for i, q in enumerate(quiz):

            st.markdown(f"### Q{i+1}. {q['question']}")

            ans = st.radio(
                "Select one option",
                q["options"],
                key=f"quiz{i}"
            )

            answers.append(ans)

            st.write("")

        submit = st.button("Submit Quiz")

        if submit:

            score = 0

            st.session_state.answers = answers

            for i, q in enumerate(quiz):

                if answers[i] == q["answer"]:
                    score += 1

                    st.session_state.points = add_points(
                        st.session_state.points,
                        "correct_answer"
                    )

            st.session_state.points = add_points(
                st.session_state.points,
                "finish_quiz"
            )

            st.success(f"You scored {score}/{len(quiz)}")

            st.divider()

            st.subheader("Quiz Review")

            for i, q in enumerate(quiz):

                user_answer = answers[i]
                correct_answer = q["answer"]

                st.markdown(f"### Q{i+1}. {q['question']}")

                # show options with color
                for option in q["options"]:

                    if option == correct_answer:
                        st.markdown(
                            f"<span style='color:green;font-weight:bold'>✔ {option}</span>",
                            unsafe_allow_html=True
                        )

                    elif option == user_answer:
                        st.markdown(
                            f"<span style='color:red;font-weight:bold'>✘ {option}</span>",
                            unsafe_allow_html=True
                        )

                    else:
                        st.write(option)

                st.write("")

            if score / len(quiz) >= 0.7:
                st.balloons()

            st.session_state.quizzes_taken += 1
            st.session_state.score = score
# ---------------------------------------------------
# PROGRESS
# ---------------------------------------------------

with tabs[4]:

    st.header("Learning Analytics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Questions Asked",
        st.session_state.questions_asked
    )

    col2.metric(
        "Quizzes Taken",
        st.session_state.quizzes_taken
    )

    accuracy = calculate_accuracy(
        st.session_state.score,
        len(st.session_state.quiz_questions)
    )

    col3.metric(
        "Accuracy",
        f"{accuracy}%"
    )

    st.divider()

    st.subheader("Performance Overview")

    progress = calculate_progress(st.session_state.points)

    st.progress(progress)

    st.caption("Overall learning progress based on your points.")

    st.divider()

    st.subheader("Weekly Activity")

    activity_data = {
        "Mon": 2,
        "Tue": 3,
        "Wed": 5,
        "Thu": 4,
        "Fri": 6,
        "Sat": 3,
        "Sun": 4
    }

    st.bar_chart(activity_data)

    st.divider()

    st.subheader("Achievements")

    badges = get_badges(st.session_state.points)

    if badges:

        cols = st.columns(len(badges))

        for i, badge in enumerate(badges):
            cols[i].success(badge)

    else:

        st.info("No badges yet. Keep learning!")


# ---------------------------------------------------
# STUDY PLAN
# ---------------------------------------------------

with tabs[5]:

    st.header("AI Study Plan Generator")

    subject = st.text_input(
        "Subject",
        placeholder="Machine Learning"
    )

    days = st.slider("Days",3,30,10)

    if st.button("Generate Study Plan"):

        if subject:

            with st.spinner("Generating plan..."):

                plan = generate_study_plan(subject,days)

                plan_lines = format_study_plan(plan)

                for p in plan_lines:
                    st.write("📅",p)