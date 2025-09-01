import itertools

'''Approach
-k is not fixed
-after receiving value of k, we have to find all possible combination of k number of pokemons(use itertools)
-and then have to make a set of their maximum amount of types for each combination of k number of pokemons
-store the types in sets so common one doesnt get counted more than once and check the length of the set
-compare each set length and determine the strongest team'''
# Pokedex
pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground"),
}

def strongest_teams(pokedex, k):
    names = list(pokedex.keys())
    best_teams = []
    max_types = 0
    
    # generate all team combinations of size k
    print(itertools.combinations(names,k))
    for team in itertools.combinations(names, k):
        combined_types = set()
        for name in team:
            combined_types.update(pokedex[name])
        
        # check how many unique types this team has
        tcount = len(combined_types)
        
        if tcount > max_types:
            max_types = tcount
            best_teams = [(team, combined_types)]
        elif tcount == max_types:
            best_teams.append((team, combined_types))
    
    return max_types, best_teams

# Example: change k here
k = int(input("Enter the number of pokemons to build the strongest team"))
max_types, best = strongest_teams(pokedex, k)

print(f"Strongest teams with k={k}:")
print(f"Maximum unique types = {max_types}\n")

for team, types in best:
    print(f"Team: {', '.join(team)}")
    print(f"Combined Types ({len(types)}): {', '.join(types)}")

