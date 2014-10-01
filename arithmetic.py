def add(nums):
    result = 0
    for i in nums:
        result = result + i
    return result

def subtract(*nums):
    result = 0
    for i in nums:
        result = result - i
    return result
        
def multiply(*nums):
    result = 1
    for i in nums:
        result = result * i
    return result

def divide(*nums):
    first = nums[0] 
    second = nums[1]
    rest = nums[2:]      
    result = first/second
    for num in rest:
        if num != 0:
            result = result / num
    print result

def square(*nums):
    result = nums[0] ** 2
    return result
    print "The square of your first value is %d." % (result)   
    return result

def cube(*nums):
    result = nums[0] ** 3
    return result
    print "The cube of your first value is %d." % (result)   
    return result

def power(*nums):
    result = nums[0]
    for i in nums[1:]:
        result = result ** i 
    return result

def mod(*nums):
    result = nums[0]
    for i in nums[1:]:
        if i != 0:
            result = result % i 
    return result

