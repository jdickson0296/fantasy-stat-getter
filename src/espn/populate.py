""" Populate the database with data from ESPN. """
from pathlib import Path
from os import environ

from src.espn.football import ESPNFootball
from src.utils.utils import write_df_to_csv


# Get Environment Variables
ESPN_S2 = environ.get("ESPN_S2")
SWID = environ.get("SWID")
LEAGUE_ID = environ.get("LEAGUE_ID")
YEAR = environ.get("YEAR")

# Constants
DATA_PATH = Path('src/data/')
LEAGUE_NAME = {'499904937': 'Sunday Funday',
               '244658114': 'Johnson\'s'}

# Create ESPN Client
ESPN_CLIENT = ESPNFootball(
    league_id=LEAGUE_ID,
    year=int(YEAR),
    private=True,
    espn_s2=ESPN_S2,
    swid=SWID,
)


def populate_teams():
    """Create CSV for Teams Data.

    """
    teams_data = []
    teams = ESPN_CLIENT.get_teams()
    for team in teams:
        team_dict = {
            'name': team.team_name,
            'wins': team.wins,
            'losses': team.losses,
            'league_id': LEAGUE_ID,
            'league_name': LEAGUE_NAME[LEAGUE_ID]
        }
        teams_data.append(team_dict)
    file = f'{DATA_PATH}/teams_espn_{YEAR}.csv'
    write_df_to_csv(teams_data, file)


def populate_box_scores():
    """Create CSV for weekly score data.

    """
    box_score_data = []
    weeks = ESPN_CLIENT.get_reg_season_count()
    for week in range(1, weeks + 1):
        box_scores = ESPN_CLIENT.get_league().box_scores(week)
        for box_score in box_scores:
            box_score_dict = {
                'week': week,
                'home_team': box_score.home_team.team_name,
                'away_team': box_score.away_team.team_name,
                'home_score': round(box_score.home_score, 2),
                'away_score': round(box_score.away_score, 2),
                'home_projected': round(box_score.home_projected, 2),
                'away_projected': round(box_score.away_projected, 2),
                'league_id': LEAGUE_ID,
                'league_name': LEAGUE_NAME[LEAGUE_ID]
            }
            box_score_data.append(box_score_dict)
    file = f'{DATA_PATH}/box_scores_espn_{YEAR}.csv'
    write_df_to_csv(box_score_data, file)


def populate_players():
    """Create CSV for individual player data.

    """
    player_data = []
    teams = ESPN_CLIENT.get_teams()
    for team in teams:
        roster = team.roster
        for player in roster:
            player_dict = {
                'name': player.name,
                'position': player.position,
                'team': player.proTeam,
                'owner': team.team_name,
                'total_points': round(player.total_points, 2),
                'total_projected_points': round(player.projected_total_points, 2),
                'avg_points': round(player.avg_points, 2),
                'projected_avg_points': round(player.projected_avg_points, 2),
                'league_id': LEAGUE_ID,
                'league_name': LEAGUE_NAME[LEAGUE_ID]
            }
            player_data.append(player_dict)
    file = f'{DATA_PATH}/players_espn_{YEAR}.csv'
    write_df_to_csv(player_data, file)


if __name__ == "__main__":
    populate_teams()
    populate_box_scores()
    populate_players()
