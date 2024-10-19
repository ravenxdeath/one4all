import random

def round_wins():
    return random.choice([1, -1])  

def minimax(dep, figher, α, β, maxi):
    
    if dep == 5:
        return round_wins()

    if maxi:
        max_eval = -float('inf')
        for _ in range(2):
            eval = minimax(dep + 1, figher, α, β, False)
            max_eval = max(max_eval, eval)
            α = max(α, eval)
            if β <= α:
                break
        return max_eval 
    else:
        min_eval = float('inf')
        for _ in range(2):
            eval = minimax(dep + 1, figher, α, β, True)
            min_eval = min(min_eval, eval)
            β = min(β, eval)
            if β <= α:
                break
        return min_eval

def play_game(starting_figher):
    rounds = 5
    round_winners = []
    current_figher = starting_figher
    
    scorpion_wins = 0
    subzero_wins = 0
    
    for round_num in range(1, rounds + 1):
        maxi = (current_figher == 1)
        round_winner = minimax(0, current_figher, -float('inf'), float('inf'), maxi)
        
        if round_winner == 1:
            round_winners.append("Sub-Zero")
            subzero_wins += 1
        else:
            round_winners.append("Scorpion")
            scorpion_wins += 1
        
                                                        # If any figher wins 3 rounds ; we break no need for further matches
        if scorpion_wins == 3 or subzero_wins == 3:
            break
        
        current_figher = 1 - current_figher
    
    if scorpion_wins > subzero_wins:
        game_winner = "Scorpion"
    else:
        game_winner = "Sub-Zero"
    
    return game_winner, round_winners

starting_figher = int(input("Enter who starts the battle (0 for Scorpion, 1 for Sub-Zero): "))

game_winner, round_winners = play_game(starting_figher)

print(f"Game Winner: {game_winner}")
print(f"Total Rounds Played: {len(round_winners)}")
for i, winner in enumerate(round_winners, 1):
    print(f"Round {i} wins: {winner}")
