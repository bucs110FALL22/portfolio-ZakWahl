from nfl_games import NFLGames
from window import Window
from weather import Weather 
nfl_games = NFLGames()
get_teams = nfl_games.get_teams()
print(get_teams)
print('--------------------------------------------')
get_games = nfl_games.get_schedule(team_id=28, week=14)
