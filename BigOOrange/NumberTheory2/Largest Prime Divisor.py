def phi(n):
    count = 0
    prime = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            count+=1
            prime=i
            while n % i ==0:
                n//=i
            # result = result // i * (i-1)
    if n > 1:
        prime=n
        count+=1
        # result = result // n * (n-1)
    return count, prime

results = []
while(1):
    number = int(input())
    if number < 0:
        number = -number
    if number == 0:
        break
    count, largest = phi(number)
    if(count==1):
        results.append(-1)
    else:
        results.append(largest)
for result in results:
    print(result)


