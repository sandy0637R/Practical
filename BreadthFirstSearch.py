

from collections import deque
from rmp import dict_gn   


def bfs_search(start, goal):
    visited = []
    queue = deque([[start]])  
    print(f"Starting BFS from {start} to reach {goal}\n")

    while queue:
        path = queue.popleft()
        city = path[-1]

        print(f"Expanding city: {city} | Current path: {path}")

      
        if city == goal:
            print("\nGoal reached!")
            return path

      
        if city not in visited:
            visited.append(city)
            for neighbor in dict_gn.get(city, {}).keys(): 
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

        print(f"Queue size: {len(queue)}\n")

    return None


def main():
    start_city = "Arad"
    goal_city = "Bucharest"

    result_path = bfs_search(start_city, goal_city)

    print("\n--- RESULT ---")
    if result_path:
        print("Path found:", " → ".join(result_path))
        print("Total cities traversed:", len(result_path))
    else:
        print("No path found!")

if __name__ == "__main__":
    main()