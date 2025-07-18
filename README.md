💬 Sentiment Analysis App (CLI + Web)
This project analyzes the sentiment of input text (positive 😊, negative 😞, or neutral 😐) using NLTK's VADER sentiment analysis model. It includes:

✅ A Command Line Interface (CLI) tool

🌐 A Streamlit Web App version with UI and visualization

🔧 Features
🖥️ CLI Tool
Input sentences in the terminal

Emoji-based sentiment output (😍 😊 😐 😞 😡)

Color-coded feedback using Colorama

Gracefully handles punctuation and empty input

🌐 Streamlit Web App
Textbox for user input ✍️

Upload and analyze .txt files 📄

Emoji + Markdown output for better UX 🎨

VADER score bar chart visualization 📊

"Try Another" button for multiple attempts 🔁

🚀 Tech Stack
Python 3

NLTK (VADER Sentiment Analyzer)

Streamlit (for Web UI)

Colorama (for colorful CLI output)

📦 Installation
Install Python 3 if not already installed.

Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/sentiment-analysis-app.git
cd sentiment-analysis-app
Install dependencies:

bash
Copy
Edit
pip install nltk streamlit colorama
(First-time only) Download VADER lexicon:

python
Copy
Edit
>>> import nltk
>>> nltk.download('vader_lexicon')
▶️ How to Run
CLI Version
bash
Copy
Edit
python main.py
Streamlit Web App
bash
Copy
Edit
streamlit run sentiment.py
Then open http://localhost:8501 in your browser.

🧪 Sample Input
"I absolutely love the way this app works! It's super smooth and efficient."

🎯 Output: Sentiment: Ecstatic 😍
📊 Scores:

json
Copy
Edit
{'neg': 0.0, 'neu': 0.375, 'pos': 0.625, 'compound': 0.8946}
☁️ Deploy Online (Optional)
You can deploy the Streamlit app for free on Streamlit Community Cloud.

🙌 Acknowledgements
NLTK Team for VADER

Streamlit Team for simplifying data apps
