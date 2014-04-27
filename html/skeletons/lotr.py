"""
LotrSkeleton
Author: Tanner Baldus
Skeleton code for finding if a path exists between two Middle Earth 
(fictonal continent from lord of the rings series) cities. 

"""
import sys




def visitor(city,connections,visited):
	"""
	Visits every city connected to the city argument.

	The visitor will visit all neighbors of the city argument (the orginal city).
	Visitor will then recursively visit the neighbors of the nieghbirs of the orignal city.

	"""
	visited[city] = True	##label the city as visited
	neighbors = connections[city]
	for neighbor in neighbors:
		pass
		## your code here (remove the pass)
		## visit all unvisited neighbors



def main():

	## a list  of nested lists of teo city pairs
	middle_earth_connections = {'Angle': ['Mitheithel'],
	'Forlond': ['GreyHavens'],
	'Buckland': ['Bree'],
	'IthilianCrossroads': ['CrossingsofPoros', 'NorthBorderIthilien', 'EmenArnen'],
	'CairAndros': ['MinisTirith'],
	'Palargir': ['MinisTirith'],
	'Mitheithel': ['Angle'],
	'DeltaofGreyflood': ['Rivendell'],
	'Truckborough': ['Hobbiton', 'MichelDelving'],
	'Entwash': ['Edoras', 'Limlight'],
	'Tharbad': ['Bree', 'GapofRohan'],
	'Galadhan': ['Celebrant'],
	'EmenArnen': ['IthilianCrossroads'],
	'Bree': ['Buckland', 'Hobbiton', 'Tharbad'],
	'CrossingsofPoros': ['IthilianCrossroads'],
	'MinisTirith': ['CairAndros', 'Edoras', 'Barad-Dur', 'EmynArnen', 'HennethAnnun', 'Palargir'],
	'Barad-Dur': ['MinisTirith'],
	'EmynArnen': ['MinisTirith'],
	'Rivendell': ['DeltaofGreyflood'],
	'TowerHills': ['Greenholm', 'GreyHavens'],
	'HennethAnnun': ['MinisTirith'],
	'Tookbank': ['Tuckborough'],
	'Limlight': ['Entwash', 'Celebrant'],
	'BrandyHall': ['Hobbiton', 'Tuckborough'],
	'Isengard': ['Edoras'],
	'GapofRohan': ['Tharbad', 'Edoras'],
	'GreyHavens': ['Forlond', 'TowerHills'],
	'Greenholm': ['MichelDelving', 'TowerHills'],
	'NorthBorderIthilien': ['IthilianCrossroads'],
	'Celebrant': ['Limlight', 'Galadhan'],
	'Edoras': ['Isengard', 'MinisTirith', 'GapofRohan', 'GreatWestRoad', 'Entwash', 'Lothlorien'],
	'Lothlorien': ['Edoras'],
	'Tuckborough': ['BrandyHall', 'Tookbank'],
	'GreatWestRoad': ['Edoras'],
	'Hobbiton': ['BrandyHall', 'MichelDelving', 'Truckborough', 'Bree'],
	'MichelDelving': ['Hobbiton', 'Truckborough', 'Greenholm']}
	
	cities = sys.stdin.readline().strip()
	cities = cities.split()
	start_city = cities[0] 
	end_city = cities[1]

	visited_cities = {} ## initalizing our dictonary for visited cities 

	#call visitor function
	visitor(start_city,middle_earth_connections,visited_cities)

	#print end_city


	if end_city in visited_cities.keys():		## determine if there is a path between the points
		print("One can simply walk from "+start_city+" to "+end_city)

	else:
		print("One does not simply walk from "+start_city+" to "+end_city)

if __name__ == "__main__":
	main()