N = 4
L = 25
P = 10
A = [10,14,20,21]
B = [10,5,2,4]
import heapq
hpq = []
A.append(L)
a_prev = 0
tank = P
counter = 0
for i in range(N):
    diff = A[i] - a_prev
    while(tank - diff < 0):
        if(len(hpq) == 0):
            print(-1)
            exit()
        top = heapq.heappop(hpq)
        tank += top[1]
        counter += 1
    tank -= diff
    a_prev = A[i]
    heapq.heappush(hpq, [-B[i],B[i]])
print(counter)
    