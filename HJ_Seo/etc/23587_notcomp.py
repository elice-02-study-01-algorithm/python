# ! 정수론 수학 문제...  어떻게 접근해야할 지 모르겠다.

from sys import stdin,stdout

n = int(input())

print(*range(1,n+1)), stdout.flush()

random_set = tuple(map(int,stdin.readline().strip().split()))



# for i in range(10):
#     print(i)
#     if i == 5:
#         print ("Flushing buffer")
#         sys.stdout.flush()
#     time.sleep(1)
    
# for i in range(10):
#     print(i)
#     if i == 5:
#         print("Flushing buffer")
#         sys.stdout.flush()

# ? ==> output : 
# ? 0 1 2 3 4 5 Flushing buffer
# ? 6 7 8 9 0 1 2 3 4 5 Flushing buffer
# ? 6 7 8 9
#  