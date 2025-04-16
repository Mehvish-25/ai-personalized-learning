# 🎓 AI‑Powered Personalized Learning

This project aims to provide an AI-powered personalized learning experience, enabling users to learn topics based on their selected subject. The app generates a customized syllabus, explains topics in a detailed yet simple manner, and tests users with a quiz to evaluate their learning progress. Additionally, the app tracks performance and helps learners visualize their progress.

## Features

- **Personalized Learning Path**: Choose a subject and generate a syllabus tailored to your learning needs.
- **Topic Selection**: From the generated syllabus, select topics to learn in-depth.
- **Content Generation**: Get detailed explanations of the topics in simple, understandable language.
- **Quiz Generation**: After learning, take a quiz to test your understanding of the selected topic.
- **Performance Tracking**: Track your test scores and performance on each topic.

## Tech Stack

- **Streamlit**: For the frontend to create a user-friendly interface.
- **Google Gemini API (Gemini-2.0)**: For generating text-based content like syllabus, topic explanations, and quizzes.
- **Python**: For backend processing and integration with the Gemini API.
  
## Installation

### Prerequisites

1. Python 3.x
2. Streamlit
3. Google Gemini API (API key required)

### Steps to Install

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repository-name/ai-personalized-learning.git
    cd ai-personalized-learning
    ```

2. **Set up the environment**:
    It is recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate  # For Windows
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Gemini API client**:
    - Obtain your API key from Google Cloud.
    - Add your API key in the code (`gemini_api.py` file) or store it as an environment variable.

5. **Run the app**:
    ```bash
    streamlit run app.py
    ```

6. Open your browser and navigate to `http://localhost:8501` to access the app.

## How to Use

1. **Step 1: Subject Entry**
   - Enter the subject you want to learn (e.g., "Mathematics", "Physics", etc.).
   - Click on the "Start" button to begin your personalized learning journey.

2. **Step 2: Syllabus Generation**
   - Once the subject is selected, the app will generate a syllabus with topics for that subject.
   - The syllabus is broken down into bullet points for easy reading.
   - You can select up to 20 topics based on the syllabus to start learning.

3. **Step 3: Content Delivery**
   - After selecting a topic, the app will generate detailed content explaining the topic in a simple, easy-to-understand manner.

4. **Step 4: Test**
   - After reading the content, you can proceed to take a quiz to assess your understanding of the topic.
   - Answer the questions and submit your responses.

5. **Step 5: Performance Tracking**
   - The app will display your performance on the quiz, showing your score out of the total questions.
   - Visualize your learning progress with performance graphs.

## Files Overview

- **app.py**: Main Streamlit app file that handles the user interface and app flow.
- **gemini_api.py**: Handles interaction with the Google Gemini API to generate content, syllabus, and quizzes.
- **performance.py**: Contains the function to plot the performance chart based on quiz results.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the changes to your fork (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io) for creating a powerful tool for building web apps easily.
- [Google Gemini API](https://cloud.google.com/gen-ai) for providing state-of-the-art AI models for content generation.
