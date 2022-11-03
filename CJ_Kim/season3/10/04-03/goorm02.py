seq_num = int(input())
input_seq = input()
folder_keyboard = ['', '!1.,?', 'C2AB', 'F3DE', 'I4GH', 'L5JK', 'O6MN', 'S7PQR', 'V8TU', 'Z9WXY']

def default_press(key, num):
	if int(key) in [2, 3, 4, 5, 6, 8]:
		num = num%4
	elif int(key) in [1, 7, 9]:
		num = num%5
	return num


answer = ''
temp_stack = ''
for num in input_seq:
	if temp_stack == '':
		temp_stack += num
		continue
	if temp_stack[-1] != num:
		answer += folder_keyboard[int(temp_stack[-1])][default_press(int(temp_stack[-1]), len(temp_stack))]
		temp_stack = num
	else:
		temp_stack += num
if temp_stack != '':
	answer += folder_keyboard[int(temp_stack[-1])][default_press(int(temp_stack[-1]), len(temp_stack))]

print(answer)
	