total_sum = 0  
ammount = 0
sum = 0
for n in range(2, 10000000):
    for d in str(n):
        sum += int(d) ** 5
    if sum == n:
        ammount += 1
        total_sum += n
        print(f'№{ammount}--{n}| Total sum={total_sum}')
    sum = 0