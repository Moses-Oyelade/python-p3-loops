#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        
        print(f"{i}")
        i -= 1
        
    print(f"Happy New Year!")
    
    
print(happy_new_year())

list = [1, 2, 3, 4, 5]

def square_integers(list):
    # code goes here!
    new_list = []
    for num in list:
        new_list.append(num**2)
    return new_list


# print(square_integers(list))



def fizzbuzz():
    # code goes here!
    i = 100
    for i in range(1, 101):
        if i%3==0 and i%5==0 :
            print(f"FizzBuzz")
        elif i%3==0:
            print(f"Fizz")
        elif i%5==0:
            print(f"Buzz")
        else:
            print(i)
    return i
    
# print(fizzbuzz())
        


