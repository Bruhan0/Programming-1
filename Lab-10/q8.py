n = int(input())
hash_map = {}
for i in range(n):
    c , cap = input().split()
    hash_map[c] = cap
there = input()
print(hash_map.get(there, "Not found"))