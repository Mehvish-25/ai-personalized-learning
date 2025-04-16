from .gemini_api import generate_subject_content

def get_learning_path(subject):
    content = generate_subject_content(subject)
    return content
