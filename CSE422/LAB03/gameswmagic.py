def pacman_game(c):
    outcome = [3, 6, 2, 3, 7, 1, 2, 0]
    level_2_left = [min(outcome[0:2]),min(outcome[2:4])]
    level_2_right = [min(outcome[4:6]),min(outcome[6:8])]

    max_left = max(level_2_left)
    max_right = max(level_2_right)

    no_dark_magic = max(max_left, max_right)

    dark_magic_left = max(outcome[0:4]) - c
    dark_magic_right = max(outcome[4:8]) - c

    use_dark_magic = max(dark_magic_left, dark_magic_right)

    if use_dark_magic>no_dark_magic:
        return f"The new minimax value is {use_dark_magic}. Pacman uses dark magic."
    else:
        return f"The minimax value is {no_dark_magic}. Pacman does not use dark magic."
    
print(pacman_game(5))
# print(pacman_game(5))