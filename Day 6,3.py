def max_chess_games(N):
    total_minutes = N * 6
    max_games = total_minutes // 20
    
    return max_games

N = int(input("Enter the number of hours of free time: "))
max_games = max_chess_games(N)
print("Chef can play a maximum of", max_games, "complete chess games.")
