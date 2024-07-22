N = int(input())

for _ in range(N):
    A, B = input().split()

    # Inverte as strings para comparar do final para o início
    if A[::-1].startswith(B[::-1]):
        print("encaixa")
    else:
        print("nao encaixa")