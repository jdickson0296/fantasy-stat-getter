"""Module for populating data from Yahoo Fantasy Football API into structured formats."""
from pathlib import Path

from src.yahoo.football import YahooFootball
from src.utils.utils import write_df_to_csv


DATA_PATH = Path('src/data/')
YEAR = "2024"
# Get league IDs from https://profiles.sports.yahoo.com/#
LEAGUE_ID = "1055167"
LEAGUE_NAME = {'1055167': 'LinkedIn'}
# Game ID found in https://github.com/uberfastman/yfpy/blob/main/quickstart/quickstart.py
YAHOO_FB_CLIENT = YahooFootball(league_id=LEAGUE_ID, game_id=449)


def populate_players(league_id: int):
    """Collects player data from Yahoo Fantasy Football league and formats it for storage.

    Args:
        league_id (int): The Yahoo league ID
        league_name (str): The name of the league
    """
    player_data = []
    for team in YAHOO_FB_CLIENT.get_teams():
        team_name = team.name.decode("utf-8")
        team_id = team.team_id
        for player in YAHOO_FB_CLIENT.get_players(team_id):
            # player_key = player.player_key
            player_data.append({
                'name': player.name.full,
                'position': player.primary_position,
                'team': player.editorial_team_abbr.upper(),
                'owner': team_name,
                'total_points': player.player_points.total,
                'league_id': league_id,
                'league_name': LEAGUE_NAME[league_id]
            })
    file = f'{DATA_PATH}/players_yahoo_{YEAR}.csv'
    write_df_to_csv(player_data, file)


if __name__ == "__main__":
    populate_players(LEAGUE_ID)
