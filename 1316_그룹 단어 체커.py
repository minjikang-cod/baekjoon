num = int(input())

group_check = 0
for i in range(num):
    alphabet = []
    word = list(input())
    for j in range(len(word)):
        if word[j] not in alphabet:
            alphabet.append(word[j])
        else:
            if word[j] != alphabet[-1]:
                alphabet.append(-1)
    if -1 not in alphabet:
        group_check += 1

print(group_check)