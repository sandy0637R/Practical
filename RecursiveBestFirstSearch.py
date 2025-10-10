import queue as Q
from rmp import dict_gn, dict_hn

start = "Arad"
goal = "Bucharest"
result = None

def get_fn(citystr):
    cities = citystr.split(",")
    gn = 0
    for i in range(len(cities) - 1):
        gn += dict_gn[cities[i]][cities[i + 1]]
    hn = dict_hn[cities[-1]]
    return gn + hn

def expand(cityq):
    global result

    if cityq.empty():
        return

    
    tot, citystr, thiscity = cityq.get()

    if thiscity == goal:
        result = citystr + " :: " + str(tot)
        return

   
    nexttot = 999
    if not cityq.empty():
        nexttot, nextcitystr, nextthiscity = cityq.queue[0]

    print("Expanding city:", thiscity)
    print("Second best f(n):", nexttot)

    
    tempq = Q.PriorityQueue()
    for cty in dict_gn.get(thiscity, {}):
        new_path = citystr + "," + cty
        tempq.put((get_fn(new_path), new_path, cty))

   
    for _ in range(min(2, tempq.qsize())):
        f, path, node = tempq.get()
        if f < nexttot:
            cityq.put((f, path, node))

    
    expand(cityq)

def main():
    cityq = Q.PriorityQueue()
    cityq.put((999, "NA", "NA"))  
    cityq.put((get_fn(start), start, start))
    expand(cityq)

    print("\nThe RBFS path with total cost is:")
    print(result)

if __name__ == "__main__":
    main()
