# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
water_tank = int(input())
water_info = [[] for _ in range(water_tank+1)]
for _ in range(water_tank):
	a, b = map(int, input().split())
	water_info[a].append(b)
	water_info[b].append(a)

while True:
	will_removed = 0
	for index in range(len(water_info)):
		if len(water_info[index]) == 1:
			water_info[water_info[index][0]].remove(index)
			water_info[index] = []
			will_removed += 1
	if will_removed == 0:
		break

answer01 = 0
answer02 = ''
for index in range(len(water_info)):
	if water_info[index] != []:
		answer01+=1
		answer02+=" "+str(index)
print(answer01)
print(answer02.strip())