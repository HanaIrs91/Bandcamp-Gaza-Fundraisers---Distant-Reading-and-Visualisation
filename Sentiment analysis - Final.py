# Topic: distant reading of Bandcamp fundraisers/ sentiment analysis of supporter comments 
# Author: Hana Arshid
# Date: 04/10/2024

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from collections import Counter
import re

# Download the VADER lexicon 
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords

# Initialise the sentiment analyser
sia = SentimentIntensityAnalyzer()

# Load stop words
stop_words = set(stopwords.words('english'))

# Text
texts = [
    "A great cause that needs more support. Favorite track: Disloyal Times Dance Track.",
    "Please don't be afraid. Favorite track: Ytem & Chemist - Mantis Lords.",
    "Solidarity balm. So many gems here, hard to pick a favorite. Appreciate the covers—used to love that Jawbox song and now hearing it in a new way. Favorite track: That God Damn Paul McCartney Christmas Song. I haven't even listened through the whole thing and already it's helping me process all the feels. One of my first fave songs clicked at random is 'Candy' by Olive Mitra... why? I dunno I guess cuz it's round and has no words and those things are soothing right now. But damn all the songs I've heard so far have their own healing magic Favorite track: Candy.",
    "From The River To The Sea. Favorite track: The Sin of Human Frailty. An excellent initiative for a worthy cause. We are talking about the first genocide attempt of the 21st century, justified (or even militarily supported) by a lot of Western political 'leaders'. Palestine will be free, it is inevitable. Favorite track: Lonely Vigil (Demo). Sending help can be morally difficult, especially when money is involved and if it's middle east conflict. I searched online and in addition to this great tracklist, names like propagandhi and dave matthews band came up. Excellent cause that needs a lot of help, with some really amazing bands and tunes! From the river to the sea!! Favorite track: Tenderfoot. Great music and great initiative Favorite track: Sermon for Retribution. There is no reason for genocide EVER!!! No excuses, no cultural brainwashing can justify plain and simple MURDER and that is what we've been turning a blind eye to since 1947... This slow extermination must be stopped and every 'HUMAN!' should be ashamed of themselves, especially those egging it on! Monsters! (Also known as the RICH, RICH people have no Culture, NO SOULS Nor a trace of humanity! They are not Conscious life forms) FREEDOM FOR ALL Favorite track: The Sin of Human Frailty. Incredible roster compiled for a critical cause. Favorite track: Fencewalker Blues. A great initiative to support a crucial cause. Against imperialist occupation, Palestine will be free. Favorite track: Lie. From the river to the sea, Palestine will be free! Favorite track: Tenderfoot. فلسطين حرة!!! Favorite track: The Sin of Human Frailty. Perfect example of how the HC community can fight for a better world. Free Palestine and all oppressed peoples globally. Favorite track: The Wretched of the Earth / Military Issue (Live). So grateful hxc people are finally paying attention to Palestine and releasing BANGERS Favorite track: Dar Al-Qahr • دار القهر.",
    "HEAVY HITTERS to lift up an oppressed nation! Ty for making it clear that inclusion isn't limited to names on the lineup. Big love. Beautiful initiative, big up EQ50 and all the artists involved. From the river to the sea, Palestine WILL be free. Favorite track: Stars Are Calling.",
    "So many awesome people and bands coming together for a very important cause! Thanks to Edie for putting this together. Free Palestine! This is just absolutely awesome. Amazing bands coming together for a good cause. Free Palestine. Favorite track: Cadavers. This is great! Awesome people, awesome bands and for a great cause. Thanks a lot! Favorite track: Movimento Perpétuo.",
    "A good cause. Favorite track: Babe Martin - When They Look At Me.",
    "Rippin' weirdo grind for Gaza - what's not to love? Free Palestine from the scourge of zionism! Favorite track: RED TRIANGLES.",
    "Not only a great track but all of the proceeds go to an extremely worthwhile cause.",
    "Excellent mix of music by a variety of artists. There are numerous gems on it, I can’t pick just one. Well worth the money. Highly recommend it.",
    "Great music important cause. Favorite track: Frankie Cosmos - A Shit Show.",
    "Not gonna lie, I haven’t listened to anything after Insurrealista! Every song keeps topping the other one! Stoked to share ❤️🌎✊🏼🙏🏼🇵🇸 Favorite track: Insurrealista. This mixtape moves air, is a balm, is a witness to the massacres of Palestinians, and propels me to acts of solidarity! Favorite track: Folktronic Mafraq Haifa."
]

# Get the sentiment scores
sentiment_scores = []
sentiment_classes = []
word_list = []

for text in texts:
    sentiment = sia.polarity_scores(text)
    compound_score = sentiment['compound']
    
    # Classify sentiment
    if compound_score >= 0.05:
        sentiment_class = "Positive"
    elif compound_score <= -0.05:
        sentiment_class = "Negative"
    else:
        sentiment_class = "Neutral"
    
    # Store sentiment scores and classes for visualisation
    sentiment_scores.append(compound_score)
    sentiment_classes.append(sentiment_class)

    # Tokenise and filter words for frequency analysis
    words = nltk.word_tokenize(text.lower())
    # Exclude stop words
    word_list.extend([word for word in words if re.match("^[a-z]+$", word) and word not in stop_words])  # Only keep alphabetic words and not in stop_words

# Count word frequencies
word_counts = Counter(word_list)

# Separate words into positive, negative, and neutral based on their scores
positive_words = []
negative_words = []
neutral_words = []

for word, count in word_counts.items():
    word_sentiment = sia.polarity_scores(word)['compound']
    if word_sentiment > 0.05:
        positive_words.extend([word] * count)  
    elif word_sentiment < -0.05:
        negative_words.extend([word] * count)  
    else:
        neutral_words.extend([word] * count)  

# Get the top 5 most common words in each category
most_common_positive = Counter(positive_words).most_common(5)
most_common_negative = Counter(negative_words).most_common(5)
most_common_neutral = Counter(neutral_words).most_common(5)

# Print the results
print("Most Common Positive Words:", most_common_positive)
print("Most Common Negative Words:", most_common_negative)
print("Most Common Neutral Words:", most_common_neutral)

# Set default font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Visualisation of sentiment scores
plt.figure(figsize=(10, 6))
plt.barh(range(len(texts)), sentiment_scores, color=['green' if score >= 0.05 else 'red' if score <= -0.05 else 'grey' for score in sentiment_scores])
plt.yticks(range(len(texts)), [f"Comment {i+1}" for i in range(len(texts))])
plt.xlabel("Sentiment Score")
plt.title("Sentiment Analysis of Comments", fontweight='bold')
plt.axvline(0, color='black', linewidth=0.8)  
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Visualisation of word frequencies
positive_words_freq = [word[0] for word in most_common_positive]
positive_counts = [word[1] for word in most_common_positive]

negative_words_freq = [word[0] for word in most_common_negative]
negative_counts = [word[1] for word in most_common_negative]

neutral_words_freq = [word[0] for word in most_common_neutral]
neutral_counts = [word[1] for word in most_common_neutral]

# Plot the most common words
plt.figure(figsize=(15, 10))

# Positive Words
plt.subplot(3, 1, 1)
plt.barh(positive_words_freq, positive_counts, color='green')
plt.title('Most Common Positive Words', fontweight='bold')
plt.xlabel('Frequency')
plt.xlim(0, max(positive_counts) + 1)

# Negative Words
plt.subplot(3, 1, 2)
plt.barh(negative_words_freq, negative_counts, color='red')
plt.title('Most Common Negative Words', fontweight='bold')
plt.xlabel('Frequency')
plt.xlim(0, max(negative_counts) + 1)

# Neutral Words
plt.subplot(3, 1, 3)
plt.barh(neutral_words_freq, neutral_counts, color='grey')
plt.title('Most Common Neutral Words', fontweight='bold')
plt.xlabel('Frequency')
plt.xlim(0, max(neutral_counts) + 1)

plt.tight_layout()
plt.show()
