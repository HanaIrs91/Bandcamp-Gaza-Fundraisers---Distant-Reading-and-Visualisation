# Topic: distant reading of Bandcamp fundraisers/words associated with Palestinians 
# Author: Hana Arshid
# Date: 07/10/2024

import pandas as pd
import spacy
from collections import Counter
import matplotlib.pyplot as plt

# Load spaCy model for English
nlp = spacy.load('en_core_web_sm')

# Load the Excel file from the path
file_path = '/Users/hanairshaid/Desktop/Data analysis and visualisation py/Textual Data - BC Gaza Fundraisers.xlsx'
df = pd.read_excel(file_path)

# Extract the text column
texts = df['Statements '].tolist()

# Preprocess the text using spaCy
def preprocess(text):
    doc = nlp(text.lower())
    return [token for token in doc if token.is_alpha and not token.is_stop]

# Define target terms related to Palestinians and Gazans
target_terms = ['palestinian', 'palestinians', 'gazan', 'gazans', 'palestinian people']

# Define demography-related words
demography_terms = ['men', 'women', 'children', 'elderly', 'youth', 'families', 'boys', 'girls']

# Define aid-related words
aid_terms = ['aid', 'relief', 'support', 'donations', 'assistance', 'charity', 'humanitarian']

# Function to extract adjectives, demography-related, and aid-related words
def get_associated_words(doc, target_terms, demography_terms, aid_terms, window_size=2):
    associated_words = []
    for i, token in enumerate(doc):
        if token.text in target_terms:
            start = max(0, i - window_size)
            end = min(len(doc), i + window_size + 1)
            context_words = doc[start:i] + doc[i+1:end]
            for context_word in context_words:
                if context_word.pos_ == 'ADJ':  
                    associated_words.append(context_word.text)
                elif context_word.text in demography_terms:  
                    associated_words.append(context_word.text)
                elif context_word.text in aid_terms:  
                    associated_words.append(context_word.text)
    return associated_words

# Process each text and extract adjectives, demography-related, and aid-related terms
associated_words = []
for text in texts:
    doc = preprocess(text)
    associated_words.extend(get_associated_words(doc, target_terms, demography_terms, aid_terms))

# Count the most frequent words
word_counts = Counter(associated_words)

# Get the 20 most common words
most_common_words = word_counts.most_common(20)
word_labels = [word for word, _ in most_common_words]
word_values = [count for _, count in most_common_words]

# Set up colours for the chart
colors = ['#E8F5E9', '#C8E6C9', '#A5D6A7', '#81C784', '#66BB6A', '#4CAF50', '#43A047', '#388E3C', '#2E7D32', '#1B5E20']

# Visualise the most associated adjectives, demography-related, and aid-related words as a bar chart
plt.figure(figsize=(9, 5), dpi=300)
bars = plt.bar(word_labels, word_values, color=colors[:len(word_labels)], edgecolor='black', alpha=0.8)

# Add title and labels 
plt.title('Words Associated with Palestinians', fontsize=14, fontname='Times New Roman', fontweight='bold', pad=20)
plt.text(0.5, 1.1, 'October 2023 - October 2024', fontsize=7, fontname='Times New Roman', transform=plt.gca().transAxes, ha='center', va='center')
plt.xlabel('Words', fontsize=6, fontname='Times New Roman', fontweight='bold')
plt.ylabel('Frequency', fontsize=6, fontname='Times New Roman', fontweight='bold')

# Rotate x-ticks 
plt.xticks(rotation=45, ha='right', fontsize=4, fontname='Times New Roman')

# Adjust the font size 
plt.yticks(fontsize=4, fontname='Times New Roman')

# Add gridlines to the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Use tight_layout() 
plt.tight_layout(pad=6.0)

# Save the associated words frequency chart
plt.savefig('associated_words_palestinians.png', format='png', dpi=300)

# Show the chart
plt.show()

