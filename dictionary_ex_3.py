''' Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost. 
Store this information in a dictionary where the keys are the team names and the values are lists of the form [
wins, losses]. (a) Using the dictionary created above, allow the user to enter a team name and print out the team’s 
winning percentage. (b) Using the dictionary, create a list whose entries are the number of wins of each team. 
(c) Using the dictionary, create a list of all those teams that have winning records
'''
teams = {}

while True:
    team_name = input("Enter the name of the team (or enter 'done' to stop): ").strip()
    if team_name.lower() == 'done':
        break
   
    try:
        wins = int(input(f"Enter the number of games won {team_name} during this season: "))
        losses = int(input(f"Enter the number of games lost {team_name} during this season: "))
        teams[team_name] = [wins, losses]
   
    except ValueError:
        print("Please enter the correct value.")
   
while True:
    team_check = input("Enter the name of the team to find the winning percentage ('done' to skip: )").strip()
    if team_check.lower() == 'done':
        break
   
    if team_check in teams:
        wins, losses = teams[team_check]
        total_games = wins + losses
        if total_games == 0:
            print(f"{team_check} has not played any games.")
        else:
            win_percent = wins/total_games*100
            print(f"The winning percentage of team{team_check} is {win_percent}%.")
    else:
        print("Team not found")
       
#part (b): Wins list
wins_list = [record[0] for record in teams.values()]
print("\nList of wins for each team: ", wins_list)

#part (c): Teams with winning record
winning_teams = [team for team, record in teams.items() if record[0] > record[1]]
print("Teams with winning record:", winning_teams)