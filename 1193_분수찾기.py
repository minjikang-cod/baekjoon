a = 1
b = 1
goal_number = int(input())
denu_sum = 1

while(goal_number - denu_sum > 0):
    goal_number = goal_number - denu_sum
    denu_sum = denu_sum + 1
denu_sum = denu_sum + 1

a = denu_sum-goal_number
b = goal_number

if denu_sum % 2 == 0:
    print(str(a)+'/'+str(b))
else:
    print(str(b)+'/'+str(a))
    
