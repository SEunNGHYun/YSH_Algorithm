import sys
input = sys.stdin.readline

c_val1 = {
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 1000,
    'yellow': 10000,
    'green': 100000,
    'blue': 1000000,
    'violet': 10000000,
    'grey': 100000000,
    'white': 1000000000
}
c_val2 = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}
total_r = 0
val = 10
for _ in range(2):
    color = input().rstrip()
    total_r += (val * c_val2[color])
    val = 1
color = input().rstrip()
total_r *= c_val1[color]
print(total_r)
