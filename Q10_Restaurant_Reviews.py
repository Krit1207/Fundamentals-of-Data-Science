
# Q10 - Restaurant and Cafe Review Analysis

# Given review data
reviews = [
    ("Momo Magic", 5, "Delicious momo and friendly staff, very clean place"),
    ("Momo Magic", 4, "Tasty food but slow service"),
    ("Thakali Kitchen", 2, "Food was cold and the place was dirty"),
    ("Thakali Kitchen", 3, "Good dal bhat but expensive and slow"),
    ("Lakeside Cafe", 5, "Amazing view, delicious coffee, friendly owner"),
]

positive = {"delicious", "friendly", "clean", "tasty", "good", "amazing"}
negative = {"slow", "cold", "dirty", "expensive", "rude"}

# Store ratings for each place
place_ratings = {}

# Count opinion word frequency
word_counts = {}

# Process each review
for place, stars, review in reviews:

    # Clean review text
    cleaned = review.lower().replace(",", "")

    # Split text into words
    words = cleaned.split()

    # Convert words into a set
    word_set = set(words)

    # Find positive and negative words
    positive_words = word_set & positive
    negative_words = word_set & negative

    pos_count = len(positive_words)
    neg_count = len(negative_words)

    # Determine review mood
    if pos_count > neg_count:
        mood = "Positive"
    elif pos_count < neg_count:
        mood = "Negative"
    else:
        mood = "Mixed"

    # Print each review's result
    print(
        f"{place:<18} {stars}* "
        f"pos={pos_count} neg={neg_count} -> {mood}"
    )

    # Store ratings by place
    if place not in place_ratings:
        place_ratings[place] = []

    place_ratings[place].append(stars)

    # Count opinion word frequencies
    for word in words:
        if word in positive or word in negative:
            if word not in word_counts:
                word_counts[word] = 0

            word_counts[word] += 1

# Print average rating per place
print("Average rating:")

for place, ratings in place_ratings.items():
    average = sum(ratings) / len(ratings)

    print(
        f"  {place:<18} {average:.1f} "
        f"from {len(ratings)} reviews"
    )

# Sort opinion words by frequency (highest first)
# Alphabetical order is used for ties
sorted_words = sorted(
    word_counts.items(),
    key=lambda item: (-item[1], item[0])
)

# Print the top 3 opinion words
print("Top opinion words:", sorted_words[:3])
