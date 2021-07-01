G = int(input())
even_numbers = [n for n in list(range(1, G + 1)) if n % 2 == 0]
count = 0
for n in even_numbers:
    while n:
        if (n % 10) in [6, 8, 9]:
            count += 1
        n = n // 10

print(count)
