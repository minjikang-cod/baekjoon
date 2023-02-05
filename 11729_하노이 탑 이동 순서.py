def move_hanoi(num, one, two, three):
    departure = []
    arrival = [] 
    
    if num ==1:
        departure.append(one)
        arrival.append(three)
        
    else:
        temp_departure, temp_arrival = move_hanoi(num-1,one, three, two)
        departure.extend(temp_departure)
        arrival.extend(temp_arrival)
        
        departure.append(one)
        arrival.append(three)
        
        temp_departure, temp_arrival = move_hanoi(num-1,two, one, three)
        
        departure.extend(temp_departure)
        arrival.extend(temp_arrival)
        
    return departure, arrival
    
    
if __name__ == '__main__':
    n = int(input())
    n_departure, n_arrival = move_hanoi(n,1,2,3)
    print(len(n_departure))
    for i in range(len(n_departure)):
        print(n_departure[i], end = ' ')
        print(n_arrival[i])