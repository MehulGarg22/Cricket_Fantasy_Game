import sqlite3
#connecting to Fantasy.db
db = sqlite3.connect("Fantasy.db")
cursor = db.cursor()
cursor.execute("SELECT * FROM Match")
row = cursor.fetchall()

def calculate_points(row):
    points = 0.0
    score = row[1]
    try:
        strike_rate = float(row[1]) / float(row[2])  # strike rate =runs/balls faced
    except:
        strike_rate = 0
    fours, sixes = float(row[3]), float(row[4])

    twos = int((score - 4 * fours - 6 * sixes) / 2)
    wickets = 10 * float(row[8])
    try:
        economy = float(row[7]) / (float(row[5]) / 6)
    except:
        economy = 0
    Fielding = float(row[9]) + float(row[10]) + float(row[11])

    # 1 point for hitting a boundary and 2 runs ,2 points for over boundary,10 points each for catch and wicket
    points += (fours + 2 * sixes + 10 * Fielding + twos + wickets)
    if score > 100:
        points += 10  # 10 points for century
    elif score >= 50:
        points += 5  # 5 points for half century
    if strike_rate > 1:  # for strike rate>100
        points += 4

    elif strike_rate >= 0.8:
        points += 2  # 2 points for strike rate >= 80
    if wickets >= 5:
        points += 10  # Additional 10 points for 5 wickets
    elif wickets > 3:
        points += 5  # Additional 5 points for 3 wickets
    if economy >= 3.5 and economy <= 4.5:
        points += 4  # 4 points for eco rate between 3.5 and 4.5
    elif economy >= 2 and economy < 3.5:
        points += 7  # 7 points for economy rate between 2 and 3.5
    elif economy < 2:
        points += 10  # 10 points for economy rate less than 2
    return points

player_points = {}
for i in row:
    player_points[i[0]] = calculate_points(i)

print(player_points)


