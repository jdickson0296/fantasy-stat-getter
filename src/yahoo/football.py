import os
import sys
from pathlib import Path

from yfpy import Data
from yfpy.query import YahooFantasySportsQuery

# set project directory
PROJECT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_DIR))
# set directory location of private.json for authentication
AUTH_DIR = PROJECT_DIR / "auth"
# set target directory for data output
DATA_DIR = Path(__file__).parent / "output"
# create YFPY Data instance for saving/loading data
DATA = Data(DATA_DIR)


class YahooFootball:
    """This class is used to interact with the Yahoo Fantasy Sports API.
    https://github.com/uberfastman/yfpy/blob/main/quickstart/quickstart.py
    """
    

    def __init__(self, league_id: int, game_id: int):
        self.league_id = league_id
        self.game_id = game_id
        self.game_code = "nfl"
        self.yahoo_query = YahooFantasySportsQuery(
            auth_dir=AUTH_DIR,
            league_id=self.league_id,
            game_code=self.game_code,
            game_id=self.game_id,
            offline=False,
            all_output_as_json_str=False,
            consumer_key=os.environ["YAHOO_CLIENT_ID"],
            consumer_secret=os.environ["YAHOO_CLIENT_SECRET"],
        )

    def get_yahoo_client(self):
        """Returns the Yahoo Fantasy Sports Query client instance."""
        return self.yahoo_query

    def get_teams(self):
        """Returns a list of teams in the league."""
        return self.yahoo_query.get_league_teams()

    def get_players(self, team_id: int):
        """Returns a list of players in a team."""
        return self.yahoo_query.get_team_roster_player_stats(team_id)

    def get_player_average_points(self, player_key: int):
        """Returns the average points per game for a player."""
        stats = self.yahoo_query.get_player_stats_for_season(player_key)
        player_stats = stats.player_stats.stats
        avg = sum(float(value.value) for value in player_stats) / len(player_stats)
        avg = round(avg, 2)
        return avg
