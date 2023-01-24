import pandas as pd
import math
import csv
import random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# 1. When each team does not have an ELO rating, give it a base ELO rating
base_elo = 1750
team_elos = {}
team_stats = {}
X = []
y = []

"""
2.
The Team statistics csv file
is initialized according to the
Miscellaneous, Opponent, and stats of each team
"""


def initialize_data(Mstat, Ostat, Tstat):
    new_Mstat = Mstat.drop(['Rk', 'Arena'], axis=1)
    new_Ostat = Ostat.drop(['Rk', 'G', 'MP'], axis=1)
    new_Tstat = Tstat.drop(['Rk', 'G', 'MP'], axis=1)

    team_stats1 = pd.merge(new_Mstat, new_Ostat, how='left', on='Team')
    team_stats1 = pd.merge(team_stats1, new_Tstat, how='left', on='Team')
    return team_stats1.set_index('Team', inplace=False, drop=True)


"""
3.
# When there is no ELO initially,
 assign base_elo initially to each team (look back to step 1)
"""


def get_elo(team):
    try:
        return team_elos[team]
    except:
        team_elos[team] = base_elo
        return team_elos[team]


# 4. Calculate the elo values for each team
def calc_elo(win_team, lose_team):
    winner_rank = get_elo(win_team)
    loser_rank = get_elo(lose_team)

    rank_diff = winner_rank - loser_rank
    exp = (rank_diff * -1) / 400
    odds = 1 / (1 + math.pow(10, exp))
    # modify the value of K based on the rank level
    if winner_rank < 2100:
        k = 32
    elif winner_rank >= 2100 and winner_rank < 2400:
        k = 24
    else:
        k = 16
    # update the value of rank level
    new_winner_rank = round(winner_rank + (k * (1 - odds)))
    new_loser_rank = round(loser_rank + (k * (0 - odds)))
    return new_winner_rank, new_loser_rank


"""
5. 
"""


def build_dataSet(all_data):
    print("Building data set..")
    X = []
    skip = 0
    for index, row in all_data.iterrows():

        Wteam = row['Wteam']
        Lteam = row['Lteam']

        # Get the original ELO or the original ELO value for each team
        team1_elo = get_elo(Wteam)
        team2_elo = get_elo(Lteam)

        # Add 200 ELO to the home team
        if row['Wloc'] == 'H':
            team1_elo += 150
        else:
            team2_elo += 150

        # Set ELO as the first eigenvalue to evaluate each team
        team1_features = [team1_elo]
        team2_features = [team2_elo]

        # Add the stats for each team we got from basketball reference.com
        for key, value in team_stats.loc[Wteam].items():
            team1_features.append(value)
        for key, value in team_stats.loc[Lteam].items():
            team2_features.append(value)

        """
        Randomly assign the eigenvalues of the two teams to the left and right sides of the data of each game
        and assign the corresponding 0/1 to the y 
        """

        if random.random() > 0.5:
            X.append(team1_features + team2_features)
            y.append(0)
        else:
            X.append(team2_features + team1_features)
            y.append(1)

        if skip == 0:
            print('X', X)
            skip = 1

        # 根据这场比赛的数据更新队伍的elo值
        new_winner_rank, new_loser_rank = calc_elo(Wteam, Lteam)
        team_elos[Wteam] = new_winner_rank
        team_elos[Lteam] = new_loser_rank

    return np.nan_to_num(X), y


# main action for training dataset

if __name__ == '__main__':
    folder = "dataset"
    Mstat = pd.read_csv(folder + '/advanced stats.csv')
    Ostat = pd.read_csv(folder + '/opponent per game stats.csv')
    Tstat = pd.read_csv(folder + '/nba team per game stats.csv')

    team_stats = initialize_data(Mstat, Ostat, Tstat)

    result_data = pd.read_csv(folder + '/21-22 result.csv')
    print(result_data)
    X, y = build_dataSet(result_data)

    # Training network model
    print("Fitting on %d game samples..." % len(X))

    model = linear_model.LogisticRegression()
    model.fit(X, y)

    # The training accuracy was calculated by 10-fold cross verification
    print("Doing cross-validation...")
    cvScore = cross_val_score(model, X, y, cv=10, scoring='accuracy', n_jobs=-1).mean()
    print(cvScore)


def predict_winner(team_1, team_2, model):
    features = []

    # team 1，Visit team
    features.append(get_elo(team_1))
    for key, value in team_stats.loc[team_1].items():
        features.append(value)

    # team 2，Home team (add ELO value 150 (10% of initial ELO value))
    features.append(get_elo(team_2) + 150)
    for key, value in team_stats.loc[team_2].items():
        features.append(value)

    features = np.nan_to_num(features)
    return model.predict_proba([features])


# Use the above trained model to make predictions in the 22- 23 NBA race

print('Predicting on new schedule..')
schedule1617 = pd.read_csv('dataset/22-23 schedule (excluding result).csv')
result = []

for index, row in schedule1617.iterrows():
    team1 = row['Vteam']
    team2 = row['Hteam']
    pred = predict_winner(team1, team2, model)
    prob = pred[0][0]
    if prob > 0.5:
        winner = team1
        loser = team2
        result.append([winner, loser, prob])
    else:
        winner = team2
        loser = team1
        result.append([winner, loser, 1 - prob])

with open('dataset/new 22-23 result.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['win', 'lose', 'probability'])
    writer.writerows(result)
    print('done.')

pd = pd.read_csv('dataset/new 22-23 result.csv', header=0)
print(pd)

