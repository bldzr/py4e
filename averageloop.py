count = 0
sum = 0
run_avg = 0
print('Before', count, sum, run_avg)
for value in [9, 41, 12, 74, 15, 52, 98]:
    count = count + 1
    sum = sum + value
    run_avg = sum / count
    print(count, sum, value, run_avg)
print('After', count, sum, run_avg)

