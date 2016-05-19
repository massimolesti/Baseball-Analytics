#Use a calculation of each player's stats on a team to estimate their contributed wins each season. Tally those numbers up to find total number of wins the team should have a year.
#WAR = Wins above Replacement
#batters' WAR = ((Rbat + Rbaser + Rdp + Rfield + Rpos)+Rrep)/10
#Starters' WAR = ((4.78 - Player FIP)/9.9 + .500 - .380)*innings/10
#relievers' WAR = ((4.78-players FIP)/9.9+.500-.470)*innings/10
#Default win percentage for team = .294 = 48 wins/162 games
#Source: https://docs.python.org/3/library/csv.html#csv.DictReader
import csv
team_name_list = ['dbacks','rockies','dodgers','padres','giants','cubs','reds','pirates','brewers','cardinals','braves','mets','phillies','marlins','nationals','toronto','orioles','devilrays','yankees','redsox','whitesox','indians','royals','tigers','twins','mariners','rangers','athletics','angels','astros']
for team_name in team_name_list:
#Arizona Diamondbacks
    with open('%shit.csv'%team_name, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        hit=0
        for row in reader:
            if row['Year']=='2015':
                hit+=(float(row['Rbat'])+float(row['Rbaser'])+float(row['Rdp'])+float(row['Rfield'])+float(row['Rpos'])+float(row['Rrep']))/10
    with open('%spitch.csv'%team_name, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        pitch=0
        for row in reader:
            if row['Year']=='2015':
                pitch+=(((4.78-float(row['FIP']))/9.9+.500-.380)*float(row['IP']))/10
    with open('%srelief.csv'%team_name, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        relief=0
        for row in reader:
            if row['Year']=='2015':
                relief+=(((4.78-float(row['FIP']))/9.9+.500-.470)*float(row['IP']))/10
    Wins=40+hit+pitch+relief
    print "%s are estimated to have won %f games in 2015" %(team_name,Wins)
