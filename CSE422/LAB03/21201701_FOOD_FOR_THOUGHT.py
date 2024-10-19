# Is the first player always a maximizer node?

#ans: it all depends on the specific game context and the roles assigned to the players at the init.
# eg. If the first player is the one trying to maximize their utility, they are the maximizer.

# Can alpha-beta pruning handle stochastic environments?

#ans: No, alpha-beta pruning is not designed for stochastic environments. Stochastic environments deals with rolling dice, drawing cards, or random events etc. However, alpha-beta pruning relies on the assumption that there are only two types of nodes (maximizing and minimizing)