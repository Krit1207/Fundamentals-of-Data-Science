
# Q6 - Ranked Match History Analysis

# Given match history data
matches = [
    ("W", 10, 1, 5, "Layla"), ("W", 3, 2, 4, "Tigreal"), ("L", 2, 6, 3, "Layla"),
    ("W", 8, 0, 6, "Gusion"), ("W", 5, 2, 9, "Layla"), ("W", 1, 3, 12, "Tigreal"),
    ("L", 4, 5, 2, "Gusion"), ("W", 7, 2, 8, "Layla")
]

wins = 0
current_streak = 0
longest_streak = 0

# Dictionary to store each hero's KDA values
hero_kdas = {}

# Process each match using tuple unpacking
for result, kills, deaths, assists, hero in matches:

    # Count wins and longest winning streak
    if result == "W":
        wins += 1
        current_streak += 1

        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0

    # Use 1 when deaths are 0
    if deaths == 0:
        kda = (kills + assists) / 1
    else:
        kda = (kills + assists) / deaths

    # Store KDA for each hero
    if hero not in hero_kdas:
        hero_kdas[hero] = []

    hero_kdas[hero].append(kda)

# Calculate win rate safely
if len(matches) > 0:
    win_rate = wins / len(matches) * 100
else:
    win_rate = 0

# Print win rate and longest streak
print(f"Win rate: {win_rate:.1f}% Longest win streak: {longest_streak}")

# Print games played and average KDA for each hero
for hero, kdas in hero_kdas.items():
    games_played = len(kdas)
    average_kda = sum(kdas) / games_played

    print(f"{hero} games {games_played}, avg KDA {average_kda:.2f}")

# Find the most played hero
if hero_kdas:
    most_played = max(hero_kdas, key=lambda hero: len(hero_kdas[hero]))
    print("Most played hero:", most_played)
else:
    print("Most played hero: None")
