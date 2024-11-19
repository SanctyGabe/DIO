T = int(input())

for i in range(T):

   i = input()
   i = i.split()

   N = int(i[0])
   K = int(i[1])
  
   garrafas_cheias = N // K
   garrafas_vazias = N % K
   total = garrafas_vazias + garrafas_cheias

   print(total)