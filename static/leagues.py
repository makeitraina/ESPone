class Team(object):
	def __init__(self, key, name):
		self.key = key
		self.name = name


class League(object):
	def __init__(self, name, teams):
		self.name = name
		self.teams = teams


MLB_TEAMS = [
	Team('sf', 'san-francisco-giants'),
	Team('tor', 'toronto-blue-jays')
]
MLB = League('mlb', MLB_TEAMS)

NFL_TEAMS = [
	Team('gb', 'green-bay-packers')
]
NFL = League('nfl', NFL_TEAMS)

LEAGUES = [
	MLB,
	NFL
]
