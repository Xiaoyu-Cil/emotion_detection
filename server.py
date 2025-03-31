"""
Flask web application for detecting emotions from input text using Watson NLP.

This app provides:
- A home route to render the main HTML interface.
- An /emotionDetector route that accepts a text input via GET request and returns
  a formatted string summarizing the detected emotions and dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the home page with the emotion detection UI.

    Returns:
        HTML template for the home page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion():
    """
    Handle the emotion detection request.

    Reads the input text from query parameters, uses the Watson NLP emotion
    detector to analyze the text, and returns a formatted result string.

    Returns:
        str: A summary of the emotion scores and the dominant emotion.
    """
    input_text = request.args.get("textToAnalyze", "")
    result = emotion_detector(input_text)

    if not result["dominant_emotion"]:
        return "Invalid text! Please try again!"

    output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return output

if __name__ == "__main__":
    # Run the Flask development server in debug mode
    app.run(debug=True)
