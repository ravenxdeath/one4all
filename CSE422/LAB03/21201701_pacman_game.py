def minimax(node, depth, alpha, beta, mini_player, outcome_ls):
    if depth == 0:
        return outcome_ls[node]

    if mini_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = minimax(node * 2 + i, depth - 1, alpha, beta, False, outcome_ls)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = minimax(node * 2 + i, depth - 1, alpha, beta, True, outcome_ls)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
    
## here the minimax func calculates the minimax values of the game recusively
## as well as implements the alpha, beta pruning 

def mypacman_game(c):
    outcome_ls = [3, 6, 2, 3, 7, 1, 2, 0]
 
    minimax_val = minimax(0, 3, float('-inf'), float('inf'), True, outcome_ls)
 
    dark_magic_left = max(outcome_ls[0:4]) - c
    dark_magic_right = max(outcome_ls[4:8]) - c

    zero_dark_magic = minimax_val
    using_dark_magic = max(dark_magic_left, dark_magic_right)
    
    if using_dark_magic > zero_dark_magic:
        return f"The new minimax value is {using_dark_magic}. Pacman uses dark magic."
    else:
        return f"The minimax value is {zero_dark_magic}. Pacman does not use dark magic."

print(mypacman_game(1))
print(mypacman_game(2))

print(mypacman_game(5))
