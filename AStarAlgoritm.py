import queue as Q
from rmp import dict_gn, dict_hn

start = "Arad"
goal = "Bucharest"
result = ""

def get_fn(city_str):
    cities = city_str.split(", ")
    g_n = 0
    for i in range(len(cities) - 1):
        g_n += dict_gn[cities[i]][cities[i + 1]]
    h_n = dict_hn[cities[-1]]
    return g_n + h_n

def expand(city_q):
    global result
    if city_q.empty():
        return

    tot, city_str, this_city = city_q.get()
    if this_city == goal:
        result = city_str + " :: " + str(tot)
        return

    for next_city in dict_gn.get(this_city, {}):
        new_path = city_str + ", " + next_city
        city_q.put((get_fn(new_path), new_path, next_city))

    expand(city_q)

def main():
    global result
    city_q = Q.PriorityQueue()
    city_q.put((get_fn(start), start, start))
    expand(city_q)

    print("The A* path with the total cost is:")
    print(result)

if __name__ == "__main__":
    main()
