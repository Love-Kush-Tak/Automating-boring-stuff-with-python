import sqlite3

def batting(runs, four, six, balls, field):
    points = runs//2
    if(runs>=50):
        points += 5
    if(runs>=100):
        points += 10
    if(runs/balls*100 >=80 and runs/balls*100 <=100):
        points += 2
    if(runs/balls*100 >100):
        points += 4
    points += 1*four
    points += 2*six
    points += 10*field
    return points

def bowling(wkts, overs, runs):
    points = 0
    points += wkts*10
    if(wkts>=3):
        points += 5
    if(wkts>=5):
        points += 10
    if(runs/overs >3.5 and runs/overs <=4.5):
        points += 4
    if(runs/overs >=2 and runs/overs <=3.5):
        points += 7
    if(runs/overs <2):
        points += 10
    points += 10*field
    return points


Match = sqlite3.connect('match')
Stats = sqlite3.connect('stats')
Teams = sqlite3.connect('teams')



sql_stats = "SELECT player from stats;"



curmatch = Match.cursor()
curmatch.execute(sql_match)
curstats = Stats.cursor()
curstats.execute(sql_stats)
players = []
while True:
    record = curstats.fetchone()
    if record == None:
        break
    players.append(record)
    print(players)
#calculate score
score = 0
sql_scores_match = "SELECT * from match;"
while True:
    record_match = curmatch.fetchone()
    if record_match == None:
        break
    score += batting(record_match(1), record_match(3), record_match(4), record_match(2), record_match(9)) + bowling(record_match(8) ,record_match(5)//6, record_match(7))  
    print(record_match(1), record_match(3), record_match(4), record_match(2), record_match(9), record_match(8) ,record_match(5)//6, record_match(7)) 
print(score)

curteams=Teams.cursor()
curteams.execute("INSERT INTO teams (name, players, value) VALUES('Internshala','kk', score);")
Teams.commit()
                 
