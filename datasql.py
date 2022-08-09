from cgi import print_directory
from importlib.resources import path
import pandas as pd
import sqlite3

path = r'C:\Users\USMAN JOIYA\Documents\Data'
db = path + '\database.sqlite'
conn = sqlite3.Connection(db)
tables = pd.read_sql("""SELECT * FROM sqlite_master
                            WHERE type='table';
                                    """, conn)
print (tables)

players = pd.read_sql(""" SELECT * FROM Player ORDER BY height;
                        """, conn)

print(players)

countries = pd.read_sql(""" SELECT * FROM Country;
                        """, conn)
print(countries)
print (players.columns)

leagues = pd.read_sql(""" SELECT * FROM League;
                        """, conn)
print(leagues.columns)

league_countries = pd.read_sql(""" SELECT League.name, Country.name FROM League 
                                    JOIN COUNTRY ON Country.id=League.country_id
                                    ;""", conn)

print(league_countries)


match_details = pd.read_sql(""" SELECT Match.id, 
                                        Country.name AS country_name, 
                                        League.name AS league_name, 
                                        season, 
                                        stage, 
                                        date,
                                        HT.team_long_name AS  home_team,
                                        AT.team_long_name AS away_team,
                                        home_team_goal, 
                                        away_team_goal   
                            FROM Match
                            JOIN Country on Country.id=Match.country_id 
                            JOIN League on League.id=Match.League_id
                            LEFT JOIN Team AS HT on HT.team_api_id=Match.home_team_api_id
                            LEFT JOIN Team AS AT on AT.team_api_id=Match.away_team_api_id

                            WHERE Country.name = 'Spain'
                            ORDER BY date
                            ;""", conn)

print (match_details.head)

leagues_season = pd.read_sql("""SELECT Country.name AS country, League.name AS league, season, 
                                count(distinct stage) AS Total_Stages, 
                                count(distinct HT.team_long_name) AS Total_Teams,
                                sum (home_team_goal) AS Total_Home_Team_Goals,
                                sum (away_team_goal) AS Total_Away_Team_Goals,
                                avg (home_team_goal) AS Avg_Home_Team_Goals,
                                avg (away_team_goal) AS Avg_Away_Team_Goals,
                                avg (home_team_goal-away_team_goal) AS Avg_Goal_Diff,
                                avg (home_team_goal + away_team_goal) AS Avg_Goals,
                                sum(home_team_goal + away_team_goal) AS Total_Goals
                                FROM Match
                                INNER JOIN Country ON Country.id = Match.country_id
                                INNER JOIN League ON League.id = Match.league_id
                                LEFT JOIN Team AS HT ON HT.team_api_id = Match.home_team_api_id
                                LEFT JOIN Team AS AT ON AT.team_api_id = Match.away_team_api_id 
                                GROUP BY Country.name, League.name, season
                                HAVING count(distinct stage) > 10
                                ORDER BY Country.name, League.name, season DESC
                                    ;""", conn)

print(leagues_season)