# Topic: distant reading of Bandcamp fundraisers/genres frequencies
# Author: Hana Arshid
# Date: 06/10/2024

import nltk
nltk.download('punkt_tab')

# pip install nltk matplotlib

import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Download resources from nltk

nltk.download('punkt')
nltk.download('stopwords')

# text provided 
texts = [
    """Berlin 
    alternative Stockholm
    electronic funk hip hop house breaks dub electronica jazz minimal techno Beirut
    electronic house ambient electronic drone noise techno Kilkenny
    electronic house midwest tech house techno trance Pittsburgh
    e.b.m. electronic artpop darkwave ethereal synthpop Berlin
    folk gaza meca middle east middle east children's alliance palestine love multi-genre pop psychedelic rock soul San Francisco
    electronic palestine techno uk techno bass breakbeat breaks jungle leftfield leftfield techno London
    experimental palestine ambient fundraiser gaza Germany
    punk anarcho punk benefit compilation crust dbeat gaza hardcore punk palestine political punk post-punk punk rock synth Philadelphia
    ambient experimental gaza strip oud music palestine palestinian world gaza middle east middle eastern noise noise ambient oud philistine Buffalo
    extreme metal metal metalcore palestine punk grindcore hardcore hardcore punk metallic hardcore post-metal screamo Lyon
    alternative rock ambient electro ethnic experimental folk jazz poetry poetry and music rock spoken word Rome
    electronic gaza strip palestine world benefit compilation benefits gaza gazal global bass global bass music global beat world beat world music Turin
    140 electronic garage house uk garage ukg acid house breakbeat breaks dubstep garage United Kingdom
    drum & bass electronic footwork jungle jungle dnb drum and bass jungle London
    punk emo post hardcore screamo skramz Indiana
    alternative aotearoa electronic new zealand electronic genre-fluid New Zealand

    antimusic black metal diy death metal experimental punk xenojazz ambient experimental goregrind grindcore hardcore noise noise wall xenojazz Apache Junction
    jazz instrumental spoken word poetry Dublin
    ambient dark ambient drone field recordings soundscape
    punk free gaza hardcore punk post-punk Italy
    doom. folk metal punk-rock ska world blues doom folk poetry punk rock ska Spain
    electronic experimental electronic hardcore techno Turin
    electronic experimental ambient compilation harsh noise industrial noise power electronics Rouen
    world New York
    electronic gaza jazz palestine alternative ceasefire free never again nu-jazz soul London
    world benefit benefit compilation compilation free gaza free palestine Palestine
    hip-hop palestine rap rock world international multilingual political world music New York"""
]

# Combine all the texts into a single string
combined_text = " ".join(texts)

# Tokenise the text 
genres = nltk.word_tokenize(combined_text)

# Convert to lowercase and remove punctuation
genres = [genre.lower() for genre in genres if genre.isalpha()]  # Removes non-alphabetical tokens like punctuation

# List of acceptable genres
acceptable_genres = [
    'alternative', 'ambient', 'artpop', 'bass', 'breakbeat', 'crust', 'dbeat', 
    'darkwave', 'death', 'dj', 'drone', 'dub', 'dubstep', 'electro', 
    'electronic', 'folk', 'funk', 'garage', 'goregrind', 'grindcore', 'hardcore',
    'house', 'jazz', 'leftfield', 'metal', 'metalcore', 'minimal', 
    'multi-genre', 'nu-jazz', 'pop', 'post-hardcore', 'post-punk', 'psychedelic',
    'punk', 'rock', 'screamo', 'synthpop', 'tech house', 'techno', 
    'trance', 'ukg', 'world', 'jungle', 'emo', 'experimental', 'ethnic', 
    'breaks', 'hip-hop', 'ska', 'blues', 'ambient', 'footwork', 'xenojazz'
]

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_genres = [genre for genre in genres if genre not in stop_words and genre in acceptable_genres]

# Count genre frequencies
genre_counts = Counter(filtered_genres)

# Get the 20 most common genres
most_common_genres = genre_counts.most_common(20)

# Visualisation: Bar Chart
# Separate genres and counts for plotting
labels, values = zip(*most_common_genres)

# Define shades of purple for each bar
colors = ['#EDE7F6', '#D1C4E9', '#B39DDB', '#9575CD', '#7E57C2', '#673AB7', '#5E35B1', '#512DA8', '#4527A0', '#311B92']

# Create a new figure for the bar chart with adjusted size
plt.figure(figsize=(9, 5), dpi=300)  

# Create bar chart
bars = plt.bar(labels, values, color=colors[:len(labels)], edgecolor='black', alpha=0.8)  # Add edgecolor and transparency

# Add title and labels 
plt.title('Top 20 Most Common Genres', fontsize=12, fontname='Times New Roman', fontweight='bold', pad=15)  # Title in bold, slightly further from the chart
plt.text(0.5, 1.05, 'October 2023 - October 2024', fontsize=7, fontname='Times New Roman', transform=plt.gca().transAxes, ha='center', va='center')
plt.xlabel('Genres', fontsize=6, fontname='Times New Roman', fontweight='bold', labelpad=3)  # Smaller font size for labels, closer to the chart
plt.ylabel('Frequency', fontsize=6, fontname='Times New Roman', fontweight='bold')  # Smaller font size for labels

# Set x-ticks to be vertical
plt.xticks(rotation=90, ha='center', fontsize=6, fontname='Times New Roman')  # Rotate to 90 degrees for vertical display

# Set y-ticks font to Times New Roman 
plt.yticks(fontsize=5, fontname='Times New Roman')

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)  

# Use tight_layout() 
plt.tight_layout(pad=4.0)  

# Save the chart as a high-resolution JPEG file
plt.savefig('genre_frequency_chart.jpeg', format='jpeg', dpi=300)

# Show the bar chart
plt.show()
