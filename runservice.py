"""Gather sports content from ESPN"""
import sys
# add paths
sys.path.append('static')
sys.path.append('logic')

import sched
import time

from leagues import LEAGUES
from scraper import parse_html_page_by_team

def main():
    # start the scheduler
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(1, 1, run_scheduler, (schedule,))
    schedule.run()

def run_scheduler(schedule):
	pone()
	schedule.enter(1000, 1, run_scheduler, (schedule,))

def pone():
	for league in LEAGUES:
		for team in league.teams:
			parse_html_page_by_team(league.name, team.key, team.name)
		# sport_name = sport.get('name', '')
		# print sport_name
		# teams_in_sport = sport.get('teams', [])
		# print teams_in_sport
  #   	for team_data in teams_in_sport:
  #   		print team_data.get('name','') + '\n'
  #   		parse_html_page_by_team(sport_name, team_data)

if __name__ == '__main__':
    main()