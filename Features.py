"""
Authour: Dhiraj Meenavilli
Date: July/17/2019
Title: Features
"""

"""
Alright first things first there are a few base things which need to be devolped such as being able to add different
people, each with different capacities and abilities.
"""

# --- Functions --- #

class Person(object):
	def __init__(self, name):
		self.name = name

	def returnName(self):
		print(self.name)


def addPerson(team,name):
	team.append(Person(name))

# --- Variables --- #
team = []

addPerson(team,"Bill")
addPerson(team,"Linda")

for i in range(len(team)):
	team[i].returnName()
