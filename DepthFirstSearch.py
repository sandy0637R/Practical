from rmp import dict_gn

start = "Arad"
goal = "Bucharest"
visited = []

def dfs(city, goal):
    print("Visiting:", city)
    visited.append(city)

    if city == goal:
        print("\nGoal found!")
        print("Path:", " → ".join(visited))
        return True

    for next_city in dict_gn.get(city, {}).keys():
        if next_city not in visited:
            if dfs(next_city, goal):
                return True

    return False

def main():
    if not dfs(start, goal):
        print("\nGoal not found in the graph.")

if __name__ == "__main__":
    main()
