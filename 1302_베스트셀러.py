import sys
input = sys.stdin.readline

N = int(input())
books = {}

for _ in range(N):
  b = input()
  if b in books:
    books[b] += 1
  else:
    books[b] = 1

max_books = [key for key, value in books.items() if value == max(books.values())]
print(sorted(max_books)[0])