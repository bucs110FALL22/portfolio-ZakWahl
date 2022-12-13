import requests, json, f
from collections import OrderedDict
import datetime


class NFLGames():

    def get_teams(self):
        url = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams'
        response = json.loads(requests.get(url)._content.decode('utf-8'))
        team_data = {}
        for sport in response['sports']:
            for leagues in sport['leagues']:
                for team in leagues['teams']:
                    team_data[int(
                        team['team']['id'])] = team['team']['displayName']
        team_data = OrderedDict(sorted(team_data.items()))
        return team_data

    def get_schedule(self, team_id=1, week=None):
        url = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team_id}/schedule'
        response = json.loads(requests.get(url)._content.decode('utf-8'))
        sched = {}
        game_week = 1
        for r in response['events']:
            wk = datetime.datetime.strptime(
                r['date'], '%Y-%m-%dT%H:%M%z').isocalendar()[1] - 35
            if week != None:
                print('Week = ', week, game_week)
                if game_week == week:
                    sched[game_week] = {
                        'title': r['name'],
                        "zip":
                        r['competitions'][0]['venue']['address']['zipCode']
                    }
            else:
                sched[game_week] = {
                    'title': r['name'],
                    "zip": r['competitions'][0]['venue']['address']['zipCode']
                }
            game_week += 1
        if week == None:
            sched_data = OrderedDict(sorted(sched.items()))
        else:
            sched_data = sched
        print(sched_data)
        return sched_data
