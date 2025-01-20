
while True:
    try:
        number_of_games = int(input("total numbner of games (Maximum 18 games each team): "))
        if 1<=number_of_games <=18:
            print(f"Number of games: {number_of_games}, successfully stored.")
            break
        else:
            print("Invalid number please enter correct number.")
            
    except ValueError:
        print("Invalid input! Please enter the correct number.")

num_of_teams = int(input("Enter the number of teams participating in the league: "))
teams=[]

for i in range(num_of_teams):
    team_name = input(f"Enter the name of the team {i+1}: ")
    teams.append(team_name)
    
print("\nTeams participating are:")
for index, team in enumerate(teams, start =1):
    print(f"{index}. {team}")

results =[]
points = []
for index, team in enumerate(teams, start =1):
    while True:
        try:
            print(f"Enter the result for {team}")
            won = int(input("Enter the number of games won: "))
            lost = int(input("Enter the number of games lost: "))
            draw = int(input("Enter the number of games draw: "))
            total_result = won + lost+ draw
            if total_result == number_of_games:
                results.append([won, lost, draw])
                print(f"Result for {team} is successfully stored.")
                point = (3*won) + (1*draw)
                points.append(point)
                print(f"Points for {team} is: {point}")
                break
            else:
                print("Incorret input! please re-enter the number of games won, lost and draw.")
        except ValurError:
            print("Invalid input! Please enter the correct number.")

for i in range(num_of_teams):
    print(f"{teams[i]}: Won = {results[i][0]}, Drawn = {results[i][1]}, Lost = {results[i][2]}")
    print(f"{teams[i]}: {points[i]} points")

combined = list(zip(points, teams, results))
print(combined)

combined.sort(reverse = True, key = lambda x:x[0])

points,teams,results = zip(*combined)

print("\nSorted team Results (by points): ")
for i in range(num_of_teams):
    print(f"{teams[i]}: points = {points[i]}, won = {results[i][0]}, draw = {results[i][1]}, lost = {results[i][2]}")




    