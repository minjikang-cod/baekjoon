words = input()

for w in words:
    ascii = list(str(ord(w)))
    cnt = 0
    for a in ascii:
        cnt += int(a)
    print(w*cnt)
    