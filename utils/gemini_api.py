import time
import json
import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyCckdLgRls8peSWOsNQhNKE5Rq1trJPf-8")

# Default model used throughout
DEFAULT_MODEL = "gemini-2.0-flash"

def generate_text(prompt: str, model_name: str = DEFAULT_MODEL) -> str | None:
    """Call Gemini API with a prompt and return the generated text."""
    start = time.time()
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        elapsed = time.time() - start
        if elapsed < 60:
            time.sleep(60 - elapsed)
        st.error(f"⚠️ API request failed. Error: {str(e)}")
        return None

def generate_quiz(subject: str, n: int = 4) -> list[dict]:
    """Generate a quiz in JSON format from Gemini API."""
    prompt = (
        f"Generate a quiz of {n} questions for the subject '{subject}'. "
        f"Return each question as a dictionary with 'question' (string), "
        "'options' (list of strings), and 'answer' (string). "
        f"Example output: "
        f"[{{'question': 'What is X?', 'options': ['A', 'B', 'C', 'D'], 'answer': 'B'}}]"
    )
    text = generate_text(prompt)
    if not text:
        return []
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        st.error("⚠️ Failed to parse quiz JSON.")
        return []

def generate_syllabus(subject: str, score: int) -> str | None:
    """Generate a syllabus with up to 20 bullet-point topics."""
    prompt = f"Generate a syllabus for learning '{subject}'. List the main topics as bullet points, with a maximum of 20 topics."
    return generate_text(prompt)

def generate_video_links(subject: str, n: int = 3) -> list[dict]:
    """Removed video generation. Placeholder returning empty list."""
    return []


# Removed video generation since not needed for this use case
def generate_video_links(subject: str, n: int = 3) -> list[dict]:
    """Removed as we are only providing text-based content."""
    return []
