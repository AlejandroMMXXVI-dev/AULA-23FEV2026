T = int(input())
N = [i % T for i in range(10)]

for i, j in enumerate(N):
    print(f'N[{i}] = {j}')