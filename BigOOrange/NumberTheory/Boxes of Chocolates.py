num_cases = int(input())
results = []
for i in range(num_cases):
    N, B = map(int, input().split())
    sum_remainder = 0
    for j in range(B):
        numbers = list(map(int, input().split()))
        remainder = 1
        for number in numbers[1:]:
            temp = number % N
            remainder = (remainder*temp) % N
        sum_remainder = (sum_remainder + remainder) % N
    results.append(sum_remainder)
for result in results:
    print(result)
