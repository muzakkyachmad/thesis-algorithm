
def function2(x):

    return 2 * x

a = function2(3)

print(a)


b = function2(4)
print(b)

c = function2(5)

def function3(x, y):
    return x + y

e = function3(1, 2)
print(e)

def function4(x):
    print(x)

    return 3 * x

f = function4(4)
print(f)


#bmi

name1 = "YK "
height_m1 = 2
weight_kg1 = 90

name2 = "YK sister "
height_m2 = 1.8
weight_kg2 = 70

name3 = "bro "
height_m3 = 2.5
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)

    if bmi < 25:
        return name + "not over"
    else:
        return name + "over"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)





###### tutorial from mosh

def increment(number, by):
    x = number + by
    return x

print(increment(1, 2))

def increment2(number, by):
    return number + by

print(increment2(0, 2))


def multiply(*numbers):
    #to print the list using the function
    for number in numbers:
        print(number)

multiply(2, 3, 4, 5)

#to print arguments using for - a
def multiply1(*numbers):
    total = 1
    for number in numbers:
        total *= number
        print(total)
    return total

multiply1(2, 3, 4, 5)


#to print arguments using for - b
def multiply2(*numbers): #* is useful to let the function print all arguments
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply2(2, 3, 4, 5))


def save_user(**user): #the ** can help us to print the arguments in function into a dict
    print(user)

save_user(id=1, name="John", age=22)




def calculatetotalsum(*arguments):
    totalsum = 0
    for number in arguments:
        totalsum += number
    print(totalsum)


calculatetotalsum(5, 4, 3, 2, 1)



def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res



