import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import string
import sys
from colorama import init, Fore, Style

init(autoreset=True)

print("Hey User! Welcome to Sentiment Analysis tool")
print("Type 'exit' anytime to quit.\n")

sia = SentimentIntensityAnalyzer()

while True:
    text = input("Enter a prompt: ").strip()
    
    if text.lower() == 'exit':
        print("Goodbye!")
        sys.exit()
    
    if not text:
        print(Fore.YELLOW + "Please enter some text or type 'exit' to quit.")
        continue

    tokens = text.lower().split()
    ftext = []
    for word in tokens:
        if word in string.punctuation:
            continue
        elif word[-1] in string.punctuation:
            ftext.append(word[:-1])
        else:
            ftext.append(word)
      
    cleaned_text = " ".join(ftext)
    scores = sia.polarity_scores(cleaned_text)

    if scores['compound'] > 0.05:
        print(Fore.GREEN + "Sentiment: Positive 😊")
    elif scores['compound'] < -0.05:
        print(Fore.RED + "Sentiment: Negative 😠")
    else:
        print(Fore.YELLOW + "Sentiment: Neutral 😐")

    print(f"Scores: {scores}\n")
