def phi(n):
    result = n
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            while n % i ==0:
                n//=i
            result = result // i * (i-1)
    if n > 1:
        result = result // n * (n-1)
    return result

results = []
while(1):
    number = int(input())
    if number == 0:
        break
    results.append(phi(number))
for result in results:
    print(result)


