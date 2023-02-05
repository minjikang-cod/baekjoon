total = int(input())
count5 = total//5
bag_list = []
for i in range(count5+1):
    residual = total - 5*(count5-i)
    sum3 = 0
    j=0
    while sum3<residual:
        j += 1
        sum3 = j*3
    if sum3 == residual:
        bag_list.append(count5-i+j)

if not bag_list:
    print(-1)
else: 
    bag_list.sort()
    print(bag_list[0])