# ML: Analyzed past matches to predict the winning probability of each team by using ELO function ratings

In this project, I used statistical data from Basketball Reference.com. In this site, we could see the basic statistics of different players, teams, seasons and league games, such as points scored, fouls, wins and losses.

**Key words: Machine Learning, The Elo score function, Feature vector, Logistic regression**


# Introduction
 

------------------------------

Steps of Contents

------------------------------

- Get game statistics
- Match data analysis, to get the representation of each team in each match
- The machine learning method is used to learn the relationship between each match and the winning team, and the prediction of the 2022-2023 match is made
- Compare data from the first half of the 22-23 season, analyze the data, and visualize the data.


## 1. Get NBA game statistics

(--- When using SR data, please cite us and provide a link and/or a mention. 

**https://www.basketball-reference.com/leagues/NBA_2022_standings.html**)
<div align=center>
<img src="https://github.com/manzitlo/ML_22-23NBA_predictions-/blob/master/screenshot(results)/nba_data.png" width="550px">
</div>

-------------------------------

## 2. Match data analysis, to get the representation of each team in each match
<div align=center>
<img src="https://github.com/manzitlo/ML_22-23NBA_predictions-/blob/master/screenshot(results)/match%20all%20the%20data.png" width="550px">
<img src="https://github.com/manzitlo/ML_22-23NBA_predictions-/blob/master/screenshot(results)/list%20of%20dataset.png" width="345px">
</div>

# Data analysis

In evaluating each team's past games, Data from three tables, Team Per Game Stats, Opponent Per Game Stats and Miscellaneous Stats (hereinafter referred to as T, O and M tables for short), are used to represent the game characteristics of a team in a match. Our goal is to predict, for each game, which team is going to win, but not to give an absolute win or loss, but to predict what the winning team's probability of winning is. So we're going to set up an eigenvector that represents the race. It consists of the previous competition statistics of the two teams (T, O and M tables) and the respective Elo ratings of the two teams.

Elo was originally used to better rank different players in chess. At present, many competitive sports or games will adopt the Elo rating system to grade players or players, such as football, basketball, baseball games or LOL, DOTA and other games.

citation:
    <a href="https://medium.com/purple-theory/what-is-elo-rating-c4eb7a9061e0#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImFmYzRmYmE2NTk5ZmY1ZjYzYjcyZGM1MjI0MjgyNzg2ODJmM2E3ZjEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NzQ1ODAwNTcsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExMTc4MDE4OTQ1MjE1NTM0MTUxNiIsImVtYWlsIjoiaGVsbG9sd3oxMTIwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJuYW1lIjoiTWFueml0IExvIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FFZEZUcDRPNzdVbDhOQ19rcmdycnFEY2V5eHFRTlBJblE4OWlNZEczNzBNSkE9czk2LWMiLCJnaXZlbl9uYW1lIjoiTWFueml0IiwiZmFtaWx5X25hbWUiOiJMbyIsImlhdCI6MTY3NDU4MDM1NywiZXhwIjoxNjc0NTgzOTU3LCJqdGkiOiIyZTgzNzlmODI3NTU4MGM2ZTU3YjA3NzJlY2Y3NjcxMTkwM2Y4YTQ1In0.ivM7I-IDVYLVV27IC_AkLa24EtpNbnxdRLE4lsGktZ2OkqHSgks0yz6MYp8ya_4ooKTeryvyVsdrCi3Ipi1Z6FMcYuQlTmf9aD9K4dQ3Ob6GOEtZhvBj4wKOg7UIJPOLcm8i0n8lH1GLpTCaW1M6KAzpZWjY1PHDgPyyRUYS16SfwMz9PFbhaBDO0bq6yA4NMsiqcc0bbhxSEYBPr2VUcvBAYHp3odgBGafjEbOv9nsHd5vSUg6Mf0ZKW_XvqEwSTub2N951wAujPP2Jula1vVrHJKkVQDgBUofsruggCQtUuYKBdl06I809BTq87CsW9uG_r5avxRW-F_2LXPQM3A" class="button">Click Here to know <What is an ELO Rating?></a>
    
## Result from visulazition:

**！！The data are for reference only. The purpose of this experiment is to explore the accuracy of prediction results of ELO function！！**


<div align=center>
<img src="https://github.com/manzitlo/ML_22-23NBA_predictions-/blob/master/screenshot(results)/total.png" width="550px">
</div>

West:
<div align=center>
<img src="https://github.com/manzitlo/ML_22-23NBA_predictions-/blob/master/screenshot(results)/west.png" width="550px">
</div>

East:
<div align=center>
<img src="https://github.com/manzitlo/ML_22-23NBA_predictions-/blob/master/screenshot(results)/east.png" width="550px">
</div>

