my_list = [1,2,3,5.1,5.2,5.3,"aaaa","bbb","cccc", ["ddd",2,3.5],[4,5.5,"eeee",True],[7,"hhh",9.5],True,False]
totalint = 0
sumint = 0
totalfloat = 0
sumfloat = 0
boolean = 0
strings = 0
for i in my_list:
    if type(i) == int:
        totalint += 1
        sumint += i
    elif type(i) == float:
        totalfloat += 1
        sumfloat += i
    elif type(i) == bool:
        boolean += 1
    elif type(i) == str:
        strings += 1
    if type(i) == list:
        for j in i:
            if type(j) == float:
                totalfloat += 1
                sumfloat += j
            elif type(j) == bool:
                boolean += 1
            elif type(j) == str:
                strings += 1
    
print("Total integers: ", totalint)
print("Sum of integers: ", sumint)
print("Total boolean: ", boolean)
print("Total floats: ", totalfloat)
print("Sum of floats: ", sumfloat)
print("Total strings: ", strings)


