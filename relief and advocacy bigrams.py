# Topic: distant reading of Bandcamp fundraisers/ advocacy and relief bigrams
# Author: Hana Arshid
# Date: 04/10/2024

import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from nltk import bigrams

# Download resources from nltk
nltk.download('punkt')
nltk.download('stopwords')

# Load the Excel file from the path
file_path = '/Users/hanairshaid/Desktop/Data analysis and visualisation py/Textual Data - BC Gaza Fundraisers.xlsx'
df = pd.read_excel(file_path)

# Extract the text column
texts = df['Statements '].tolist()  

# Preprocess the text
stop_words = set(stopwords.words('english'))
bigrams_list = []

for text in texts:
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    bigrams_list += list(bigrams(words))

# Define advocacy and relief keywords
advocacy_keywords = ['justice', 'freedom', 'solidarity', 'rights', 'liberation', 'support']
relief_keywords = ['aid', 'relief', 'donations', 'humanitarian', 'funds', 'charity']

# Filter bigrams by advocacy and relief keywords
def filter_bigrams_by_keywords(bigrams_list, keywords):
    return [(w1, w2) for w1, w2 in bigrams_list if w1 in keywords or w2 in keywords]

# Get advocacy-related and relief-related bigrams
advocacy_bigrams = filter_bigrams_by_keywords(bigrams_list, advocacy_keywords)
relief_bigrams = filter_bigrams_by_keywords(bigrams_list, relief_keywords)

# Count the frequency of the filtered bigrams
advocacy_bigram_counts = Counter(advocacy_bigrams)
relief_bigram_counts = Counter(relief_bigrams)

# Get the 20 most common advocacy bigrams
most_common_advocacy_bigrams = advocacy_bigram_counts.most_common(20)
advocacy_labels = [f'{w1} {w2}' for (w1, w2), _ in most_common_advocacy_bigrams]
advocacy_values = [count for _, count in most_common_advocacy_bigrams]

# Get the 20 most common relief bigrams
most_common_relief_bigrams = relief_bigram_counts.most_common(20)
relief_labels = [f'{w1} {w2}' for (w1, w2), _ in most_common_relief_bigrams]
relief_values = [count for _, count in most_common_relief_bigrams]

# Set up colours for the charts
colors = ['#E8F5E9', '#C8E6C9', '#A5D6A7', '#81C784', '#66BB6A', '#4CAF50', '#43A047', '#388E3C', '#2E7D32', '#1B5E20']

# Advocacy Bigram Frequency Bar Chart
plt.figure(figsize=(9, 5), dpi=300)
bars = plt.bar(advocacy_labels, advocacy_values, color=colors[:len(advocacy_labels)], edgecolor='black', alpha=0.8)

plt.title('Top 20 Advocacy-Related Bigrams', fontsize=14, fontname='Times New Roman', fontweight='bold', pad=20)
plt.text(0.5, 1.1, 'October 2023 - October 2024', fontsize=7, fontname='Times New Roman', transform=plt.gca().transAxes, ha='center', va='center')

plt.xlabel('Bigrams', fontsize=6, fontname='Times New Roman', fontweight='bold')
plt.ylabel('Frequency', fontsize=6, fontname='Times New Roman', fontweight='bold')

plt.xticks(rotation=45, ha='right', fontsize=4, fontname='Times New Roman')
plt.yticks(fontsize=4, fontname='Times New Roman')

# Add gridlines to the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Padding 
plt.tight_layout(pad=6.0)

# Save the advocacy bigram frequency chart
plt.savefig('advocacy_bigram_frequency_chart.png', format='png', dpi=300)

# Show the advocacy bigram frequency chart
plt.show()

# Relief Bigram Frequency Bar Chart
plt.figure(figsize=(9, 5), dpi=300)
bars = plt.bar(relief_labels, relief_values, color=colors[:len(relief_labels)], edgecolor='black', alpha=0.8)

plt.title('Top 20 Relief-Related Bigrams', fontsize=14, fontname='Times New Roman', fontweight='bold', pad=20)
plt.text(0.5, 1.1, 'October 2023 - October 2024', fontsize=7, fontname='Times New Roman', transform=plt.gca().transAxes, ha='center', va='center')

plt.xlabel('Bigrams', fontsize=6, fontname='Times New Roman', fontweight='bold')
plt.ylabel('Frequency', fontsize=6, fontname='Times New Roman', fontweight='bold')


plt.xticks(rotation=45, ha='right', fontsize=4, fontname='Times New Roman')
plt.yticks(fontsize=4, fontname='Times New Roman')

# Add gridlines to the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Padding
plt.tight_layout(pad=6.0)

# Save the relief bigram frequency chart
plt.savefig('relief_bigram_frequency_chart.png', format='png', dpi=300)

# Show the relief bigram frequency chart
plt.show()
