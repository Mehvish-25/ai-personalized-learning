import streamlit as st
from utils.gemini_api import (
    generate_syllabus,
    generate_text,
    generate_video_links,  # kept for other steps, but unused now
    generate_quiz
)
from utils.performance import plot_performance

# Initialize session state
for key, default in {
    'step': 'Subject',
    'subject': None,
    'syllabus': None,
    'topics': None,
    'selected_topic': None,
    'content_text': None,
    'test_qs': None,
    'test_score': None
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Sidebar navigation
st.sidebar.title("🔖 Navigation")
steps = ["Subject", "Syllabus", "Content", "Test", "Performance"]
current = st.session_state.step
choice = st.sidebar.radio("Go to step:", steps, index=steps.index(current))
st.session_state.step = choice

# App title
st.title("🎓 AI‑Powered Personalized Learning")

# 1) Subject entry
if st.session_state.step == "Subject":
    subj = st.text_input("Enter subject you want to learn:", value=st.session_state.subject or "")
    if st.button("Start"):
        if subj.strip():
            st.session_state.subject = subj.strip()
            st.session_state.syllabus = None
            st.session_state.topics = None
            st.session_state.step = "Syllabus"
        else:
            st.warning("Please enter a valid subject.")

# 2) Syllabus generation
elif st.session_state.step == "Syllabus":
    st.header("📑 Choose a Topic to Learn")

    if st.session_state.syllabus is None:
        # Expecting generate_syllabus() to return a plain text with bullets
        raw_text = generate_syllabus(st.session_state.subject, 0)
        lines = raw_text.splitlines() if raw_text else []

        topics = [
            line.strip('-•* ').strip()
            for line in lines
            if line.strip().startswith(('-', '*', '•'))
        ]
        st.session_state.syllabus = raw_text
        st.session_state.topics = topics[:20]  # Limit to 20

    selected = None
    if st.session_state.topics:
        for i, topic in enumerate(st.session_state.topics):
            if st.button(topic, key=f"topic_{i}"):
                selected = topic

    if selected:
        st.session_state.selected_topic = selected
        st.session_state.content_text = None
        st.session_state.step = "Content"
        st.rerun()

# 3) Text-only Content delivery
elif st.session_state.step == "Content":
    st.header(f"📚 Topic: {st.session_state.selected_topic}")

    if st.session_state.content_text is None:
        with st.spinner("Generating content..."):
            st.session_state.content_text = generate_text(
                f"Explain the topic '{st.session_state.selected_topic}' in simple and detailed manner."
            )

    st.subheader("📝 Explanation")
    st.write(st.session_state.content_text)

    if st.button("Proceed to Test"):
        st.session_state.step = "Test"
        st.session_state.test_qs = None
        st.rerun()

# 4) Final Test
elif st.session_state.step == "Test":
    st.header(f"🧪 Final Test: {st.session_state.selected_topic}")

    if st.session_state.test_qs is None:
        st.session_state.test_qs = generate_quiz(
            st.session_state.subject, st.session_state.selected_topic, 4
        )

    tanswers = []
    for i, q in enumerate(st.session_state.test_qs or []):
        st.subheader(f"Q{i+1}: {q['question']}")
        tanswers.append(st.radio("", q['options'], key=f"test_{i}"))

    if st.button("Submit Final Test"):
        tscore = sum(1 for a, q in zip(tanswers, st.session_state.test_qs) if a == q['answer'])
        st.session_state.test_score = tscore
        st.success(f"You scored {tscore}/{len(st.session_state.test_qs)}")
        st.session_state.step = "Performance"
        st.rerun()

# 5) Performance
elif st.session_state.step == "Performance":
    st.header("📊 Performance Analysis")
    fig = plot_performance(
        st.session_state.assessment_score,
        st.session_state.test_score,
        st.session_state.selected_topic
    )
    st.pyplot(fig)
