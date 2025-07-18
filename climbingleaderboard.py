ranked=[100,90,90,80]
player=[70,80,105]
def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    result = []
    for score in player:
        while ranked and score >= ranked[-1]:
            ranked.pop()
        result.append(len(ranked) + 1)
    print(result) 
'''An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
Example



The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

int ranked[n]: the leaderboard scores
int player[m]: the player's scores
Returns

int[m]: the player's rank after each new score'''