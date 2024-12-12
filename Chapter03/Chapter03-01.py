n, m, k = map(int, input().split())

num_list = []
for i in range(n):
    num_list.append(input())

print(num_list)

num_list.sort(reverse=True)
num_list

num_1 = int(num_list[0])
num_2 = int(num_list[1])

result = 0

for i in range(m):
    result += num_1
    k -= 1
    if k == 0:
        result += num_2
        k == i - 1

result

print("test")