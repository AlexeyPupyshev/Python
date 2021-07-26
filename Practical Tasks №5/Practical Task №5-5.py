import random
with open('Result.txt', mode='w+', encoding='utf-8') as f:
    f.write(" ".join([str(random.randint(1, 50)) for _ in range(10)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))
