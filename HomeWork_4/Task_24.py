n = int(input())
arr = [int(input()) for x in range(int(input()))]
mx = 0
for i in range(-1, len(arr) - 1):
    mx = max(mx, arr[i - 1] + arr[i] + arr[i + 1])
print(mx)
