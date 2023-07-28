user_entries = ['10', '19.1', '20']
i=0
total =0
sum_run=0
while  i <= len(user_entries)-1:

    sum_run = total + float(user_entries[i])
    total = sum_run
    i = i+1

print(total)

# with list compprehension

float_num = [float(num) for num in user_entries]
print(sum(float_num))