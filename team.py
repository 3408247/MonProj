from Strategies import*
from soccersimulator import SoccerTeam, Player

#### Mes tests
Priya_1a = SoccerTeam("Priya_1a",[Player("f1",FonceurStrat)])
Priya_1b =SoccerTeam("Priya_1b",[Player("GARDIEN",AllignerStrat)])

Priya_2a = SoccerTeam("Priya_2a",[Player("DEF1",DefStrat),Player("GARDIEN1",AllignerStrat)])
Priya_2b =SoccerTeam("Priya_2b",[Player("ATTACK2",FonceurStrat),Player("GARDIEN2",AllignerStrat)])

Priya_4a = SoccerTeam("Priya_4a",[Player("f1",FonceurStrat),Player("gk1",AllignerStrat)])
Priya_4b =SoccerTeam("Priya_4b",[Player("f2",FonceurStrat),Player("gk2",GkStrat)])


### Pour le tournoi
team1 = SoccerTeam("team1",[Player("f1",FonceurStrat)])
team2 = SoccerTeam("team2",[Player("f2",FonceurStrat),Player("gk2",GkStrat)])

