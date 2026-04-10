def getIndex(num_list, target):
    return num_list.index(target)

def getMax(num_list):
    max = num_list[0]
    for num in num_list:
        if num > max:
            max = num
    return max

def getMin(num_list):
    min = num_list[0]
    for num in num_list:
        if num < min:
            min = num
    return min

def countGT(num_list, target):
    count = 0
    for num in num_list:
        if num > target:
            count += 1

    return count

def sumList(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

def swapList(num_list):
    num_list[::] = num_list[::-1]
    
    # for i in range(0, len(num_list)//2):
    #     num_list[i], num_list[-(i+1)] = num_list[-(i+1)], num_list[i]


number_list = [23, 45, 27, 11, 25, 65, 78]

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))
swapList(number_list)
print(number_list)