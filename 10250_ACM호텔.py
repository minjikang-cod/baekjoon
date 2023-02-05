import math

count = int(input())
room_list = []
for i in range(count):
    hotel_info = input()
    hotel_info_list = list(map(lambda x : int(x),hotel_info.split(' ')))

    floor = hotel_info_list[-1] % hotel_info_list[0]
    if floor == 0:
        floor = hotel_info_list[0]
    room = math.ceil(hotel_info_list[-1] / hotel_info_list[0])
    
    room_list.append(floor*100+room)

for r in room_list:
    print(r)   