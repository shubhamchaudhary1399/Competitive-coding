# def isAnagram(string1, string2):
# 	if len(string1) != len(string2):
# 		return False
# 	count = [0]* 26
# 	for i in range(len(string1)):
# 		count[ord(string1[i]) - ord('a')] += 1

# 	for j in range(len(string2)):
# 		count[ord(string2[j]) - ord('a')] -= 1

# 	for k in range(len(count)):
# 		if count[k] != 0:
# 			return False
# 	return True

# def fibonacci(num):
# 	if num == 0:
# 		return
# 	if num == 1:
# 		print(0)
# 		return
# 	if num == 2:
# 		print(0, 1)
# 		return
# 	lastTwo = [0, 1]
# 	for i in range(2):
# 		print(lastTwo[i], end = ' ')
# 	for i in range(2, num):
# 		third = lastTwo[0] + lastTwo[1]
# 		print(third, end = ' ')
# 		lastTwo[0], lastTwo[1] = lastTwo[1], third

# # print(isAnagram('abc', 'bcd'))
# fibonacci(2)

# def arrays():
# 	n = int(input())
# 	array = []
# 	for i in range(n):
# 		lst = list(map(int, input().split()))
# 		array.append(lst)
	
# 	for i in range(n):
# 		mn = array[i][0]
# 		mx = array[i][0]
# 		for j in range(len(array[i])):
# 			if array[i][j] > mx:
# 				mx = array[i][j]
# 			if array[i][j] < mn:
# 				mn = array[i][j]
# 		print(mx, mn)

# arrays()

# def sortingString():
# 	n = int(input())
# 	bigStr = []
	
# 	for i in range(n):
# 		string = input()
# 		bigStr.append(string)

# 	for i in range(n):

# 	# for i in range(n):
# 	# 	count = [0]*26
# 	# 	ansStr = ''
# 	# 	for j in range(len(bigStr[i])):
# 	# 		count[ord(bigStr[i][j]) - ord('a')] += 1
# 	# 	for k in range(len(count)):
# 	# 		if count[k] != 0:
# 	# 			ansStr += chr(ord('a') + k)
# 	# 	print(ansStr)

# sortingString()

# def secondMaxArray(array):
# 	if len(array) == 0:
# 		return None
# 	if len(array) == 1:
# 		return None
# 	firstMax = array[0]
# 	secondMax = array[1]
# 	for i in range(1, len(array)):
# 		if array[i] > firstMax:
# 			secondMax = firstMax
# 			firstMax = array[i]
		
# 	return secondMax

# # print(secondMaxArray([6,5,3,2,5,8,9]))
# # print(secondMaxArray([10, 11,3,5,6,7,8]))
# print(secondMaxArray([8 ,9]))
# print(secondMaxArray([9,8]))
# print(secondMaxArray([12, 37, 1, 10, 35, 1]))
# print(secondMaxArray([12, 12, 12, 12, 12]))

def missingNumber(array):
	if len(array) == 0:
		return
	if len(array) == 1:
		return
	array.sort()
	ans = 1
	for i in array:
		if ans != i:
			return ans
		ans += 1

print(missingNumber([5,6,2,7,3]))
print(missingNumber([3, 1]))
print(missingNumber([3, 1]))

