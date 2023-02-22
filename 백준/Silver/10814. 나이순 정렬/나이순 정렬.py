n = int(input())

pe_li = []

for _ in range(n):
    age, name = input().split()
    pe_li.append((int(age), name))

pe_li.sort(key=lambda a: a[0], reverse=False)

for pe in pe_li:
    print(pe[0], pe[1])
