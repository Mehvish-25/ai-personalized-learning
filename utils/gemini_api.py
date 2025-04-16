import time
import json
import streamlit as st
import google.genai as genai

# Initialize Gemini client
_client = genai.Client(api_key="AIzaSyCckdLgRls8peSWOsNQhNKE5Rq1trJPf-8")

def generate_text(prompt: str) -> str | None:
    """Call Gemini API and wait up to 60s before surfacing any error."""
    start = time.time()
    try:
        resp = _client.models.generate_content(
            model="gemini-2.0-flash",  # Ensure this model is correct
            contents=prompt
        )
        return resp.text
    except Exception as e:
        elapsed = time.time() - start
        if elapsed < 60:
            time.sleep(60 - elapsed)
        st.error(f"⚠️ API request failed. Error: {str(e)}")
        return None

def generate_quiz(subject: str, n: int = 4) -> list[dict]:
    """Generate a quiz from Gemini API in a structured format."""
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
        return json.loads(text)  # Parse the generated text to ensure proper JSON
    except json.JSONDecodeError:
        st.error("⚠️ Failed to parse quiz JSON.")
        return []

def generate_syllabus(subject: str, score: int) -> str | None:
    """Generate syllabus for the subject, limit to 20 topics."""
    prompt = f"Generate a syllabus for learning '{subject}'. List the main topics as bullet points, with a maximum of 20 topics."
    return generate_text(prompt)

# Removed video generation since not needed for this use case
def generate_video_links(subject: str, n: int = 3) -> list[dict]:
    """Removed as we are only providing text-based content."""
    return []
