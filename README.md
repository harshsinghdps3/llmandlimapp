# Gemini Q&A and Vision Apps

This project contains two simple web applications built with Streamlit and Google's Generative AI.

## Features

*   **Q&A App (`app.py`):** A text-based chatbot that answers your questions using the Gemini model.
*   **Vision App (`vision.py`):** An application that lets you upload an image and ask questions about it.

## Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd llmandlimapp
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    Create a file named `.env` in the project root and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY"
    ```

5.  **Run the applications:**

    For the Q&A app:
    ```bash
    streamlit run app.py
    ```

    For the Vision app:
    ```bash
    streamlit run vision.py
    ```
