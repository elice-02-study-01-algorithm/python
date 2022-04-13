'''
입력
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 다음 N개의 줄에는 비용 행렬이 주어진다. 
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. 
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
============
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
==> 35 ()
'''

# def isAnagram(str1, str2):
#     dict1 = {}
#     dict2 = {}
    
#     for i in str1:
#         if i not in dict1.keys():
#             dict1[i]=1
#         else:
#             dict1[i] += 1
            
#     for i in str2:
#         if i not in dict2.keys():
#             dict2[i]=1
#         else:
#             dict2[i] += 1
    
#     if dict1 == dict2:
#         return True
#     else:
#         return False

# def main():
#     print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
#     print(isAnagram('cat', 'cap')) #should return False
    

# if __name__ == "__main__":
#     main()


#a = <3, 5, 7> 없는 타입.. print할 때 join등을 이용해서 박아주기..
