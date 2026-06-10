import random, time, csv
from collections import defaultdict

players = []
with open("players.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    players = [row["player"].strip() for row in reader]

pots = {}

with open("teams.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        pot_num = int(row["pot"])
        teams = [team.strip() for team in row["teams"].split(",")]
        pots[pot_num] = teams

if len(players) < 2 or len(players) > 12:
    raise ValueError("2-12 players required")

for i in range(1,5):
    if len(pots[i]) != 12:
        raise ValueError(f"Pot {i} must contain 12 teams")
    
draw = defaultdict(list)
random.shuffle(players)

for pot_num in range(1,5):
    random.shuffle(pots[pot_num])

    rotated_players = players[pot_num % len(players):] + players[:pot_num % len(players)]

    for i, team in enumerate(pots[pot_num]):
        player = rotated_players[i % len(players)]
        draw[player].append((pot_num, team))

print("\nWORLD CUP 2026 SWEEPSTAKE\n")
print("=" * 25)

print("STARTING DRAW")
print("=" * 13)
time.sleep(2)

for player, teams in draw.items():
    print(f"\n{player}")
    print("-" * len(player))
    time.sleep(1)

    for pot_num, team in teams:
        print(f"Pot {pot_num}: {team}")
        time.sleep(0.7)

with open("draw_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["player", "pot", "team"])

    for player, teams in draw.items():
        for pot, team in teams:
            writer.writerow([player, pot, team])