
# Q3 - Cricket Innings Score Calculator

# Given ball-by-ball data
balls = "1 4 . W 6 wd 2 1 . 4 nb 1 . . W 6 1 lb2"

# Convert the string into a list
ball_list = balls.split()

# Initialize counters
runs = 0
wickets = 0
legal_balls = 0
extras = 0
fours = 0
sixes = 0
dot_balls = 0
boundary_runs = 0

# Process each delivery
for ball in ball_list:

    # Wides and no-balls are not legal deliveries
    if ball == "wd" or ball == "nb":
        runs += 1
        extras += 1
        continue

    # Count legal deliveries
    legal_balls += 1

    if ball == "W":
        wickets += 1

    elif ball == ".":
        dot_balls += 1

    elif ball.startswith("lb"):
        extra_runs = int(ball[2:])
        runs += extra_runs
        extras += extra_runs

    else:
        bat_runs = int(ball)
        runs += bat_runs

        if bat_runs == 4:
            fours += 1
            boundary_runs += 4

        elif bat_runs == 6:
            sixes += 1
            boundary_runs += 6

# Calculate overs using integer division and modulus
overs = legal_balls // 6
remaining_balls = legal_balls % 6

# Calculate run rate safely
if legal_balls > 0:
    run_rate = runs * 6 / legal_balls
else:
    run_rate = 0

# Calculate boundary percentage safely
if runs > 0:
    boundary_percentage = boundary_runs / runs * 100
else:
    boundary_percentage = 0

# Display final results
print(f"Score: {runs}/{wickets} in {overs}.{remaining_balls} overs")
print(f"Extras {extras}, Fours {fours}, Sixes {sixes}, Dot balls {dot_balls}")
print(f"Run rate {run_rate:.2f}, Boundary runs {boundary_runs} ({boundary_percentage:.1f}% of total)")
