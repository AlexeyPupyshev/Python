my_subject = {}
with open("Subject.txt", encoding="utf-8") as f:
    for line in f:
        name, qtr = line.split(':')
        name_sum = sum(map(int, "".join([i for i in qtr if i == ' ' or (i >= '0' and i <= '9')]).split()))
        my_subject[name] = name_sum
print(f"{my_subject}")
