import json
from collections import Counter
import matplotlib.pyplot as plt
import datetime

# Read the JSON file. You can choose by swapping the commented line
with open("ContemporaryChristian.json", "r") as file:
#with open("BaselineSongs.json", "r") as file:
    data = json.load(file)

#select a song by changing this index
index = 1

# Select a song
selected_song = data[index]
song_title = selected_song["song"]

# Extract the lyrics
lyrics = selected_song["lyrics"]

# Remove punctiation or anything that might throw off the word count
#lyrics = lyrics.replace("\n", " ")
lyrics = lyrics.replace(",", "")
lyrics = lyrics.replace("(", "")
lyrics = lyrics.replace(")", "")
lyrics = lyrics.replace(".", "")
lyrics = lyrics.replace("!", "")
lyrics = lyrics.replace(";", "")
lyrics = lyrics.replace(":", "")
lyrics = lyrics.replace("?", "")
lyrics = lyrics.replace("'", "")
lyrics = lyrics.replace('"', "")

# Split the lyrics into words
words = lyrics.lower().split()

# Count the occurrences of each word
word_counts = Counter(words)

# Order the words from least common to most common
ordered_word_counts = sorted(word_counts.items(), key=lambda x: x[1])

# Print the word counts
for word, count in ordered_word_counts:
    print(f"{word}: {count}")

# Print the count of unique words
unique_word_count = len(word_counts)
print("Unique Words:", unique_word_count)

#get the runtime of the song
runtime_string = selected_song["runtime"]

# Split the runtime string into minutes and seconds
minutes, seconds = runtime_string.split(":")

# Convert the minutes and seconds to integers
minutes = int(minutes)
seconds = int(seconds)

# Create a timedelta object representing the runtime
runtime = datetime.timedelta(minutes=minutes, seconds=seconds)

# Calculate the total minutes
total_minutes = runtime.total_seconds() / 60

print("Unique words per minute: " + str(unique_word_count/total_minutes))



# Create lists for histogram data
word_frequency_counts = [0 for _ in range(ordered_word_counts[len(ordered_word_counts)-1][1])]
x_axis = [i for i in range(1, ordered_word_counts[len(ordered_word_counts)-1][1] + 1)]

# Generate histogram data
for word, count in ordered_word_counts:
    word_frequency_counts[count-1] += 1


# Plot the histogram
plt.bar(x_axis, word_frequency_counts)
plt.xlabel("x")
plt.ylabel("Number of words appearing x times")
plt.title("Word Count Histogram for " + song_title)
plt.show()

