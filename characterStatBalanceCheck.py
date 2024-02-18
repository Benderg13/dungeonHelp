

#variable 
point_buy = [-9, -6, -4, -2, -1, 0, 1, 2, 3, 4, 5, 7, 9, 12, 15, 19]

def calculateBalance(statArray):
    point_total = 0
        
    for stat in statArray:
        if(2 < stat and stat < 19):
            point_total = point_total + point_buy[stat-3]
        else:
            print("invalid stat value: ", stat)         
    print("Point total using point buy value: ", point_total)

    if(point_total < 18):
        print("reroll stats")
    elif(point_total >= 18 and point_total < 24):
        print("Point total low, highly consider rerolling")
    elif(point_total >= 24 and point_total < 27):
        print("Below standard distribution, consider rerolling stats")
    elif(point_total > 45):
        print("Unusually high stats")
    else:
        print("Looks good!")
        
def main():
    stats = input("please enter the 6 stats of your character seperated by spaces:\n")
    statArray = stats.split(sep=" ")
    statArray = [int(stat) for stat in statArray]
    
    while(len(statArray) != 6):
        stats = input("please enter the 6 stats of your character seperated by spaces:\n")
        statArray = stats.split(sep=" ")
    
    calculateBalance(statArray)
    
main()