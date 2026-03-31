def getIndex(num_list, target):
    return num_list.index(target)

def getMax(num_list):
    return max(num_list)

def getMin(num_list):
    return min(num_list)

def countGT(num_list, target):
    count = 0
    for num in num_list:
        if num > target:
            count += 1

    return count

def sumList(num_list):
    return sum(num_list)

def swapList(num_list):
    num_list.reverse()


number_list = [23, 45, 27, 11, 25, 65, 78]

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))
swapList(number_list)
print(number_list)