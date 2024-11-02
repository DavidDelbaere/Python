import random
import math


def question_1(x):
    '''
    (number)--->(bool)
    '''
    start = random.randint(0,10)
    step = random.randint(1,2)
    end = start + random.randint(0,10)
    if x == 0:
        ans = input("Where does the following range function start? range(" + str(start) + ","+str(end)+","+str(step) + "): ")
        flag = False
        while flag == False:
            try:
                if int(ans) == start:
                    print(start)
                    return True
                else:
                    print(start)
                    return False
            except ValueError:
                    ans = input('Please enter a valid number: ')

    elif x == 1:
        ending= 0
        for i in range(start,end,step):
            ending = i
        ans = input("Where does the following range function end? range(" + str(start) + ","+str(end)+","+str(step) + "): ")
        flag = False
        while flag == False:
            try:
                if int(ans) == ending:
                    print(ending)
                    return True
                else:
                    print(ending)
                    return False
            except ValueError:
                    ans = input('Please enter a valid number: ')
    else:
        ans = input("How many steps does the range function take? range(" + str(start) + ","+str(end)+","+str(step) + "): ")
        flag = False
        while flag == False:
            try:
                if int(ans) == step:
                    print(step)
                    return True
                else:
                    print(step)
                    return False
            except ValueError:
                    ans = input('Please enter a valid number: ')
def question_2(x):
    
    if x == 0:
        flag = False
        total = 0
        b = random.randint(0,10)
        a = []
        for i in range(random.randint(0,3)):
            a += [random.randint(1,3)]
        
        for i in range(b):
            for j in range(len(a)):
                total += a[j]
        

        ans = input("Here is a function:\ndef xyx(a,b):\n'''\n(list)(int)->(number)\n'''\n\tfor i in range(b):\n\t\tfor j in range(len(a)):\n\t\t\ttotal += a[j]\nreturn total" + "\n\nThe following function will return what value when calling xyx("+str(a)+","+str(b)+"): ")
        
        while flag == False:
            try:
                if int(ans) == total:
                    print(ans)
                    return True
                else:
                    print(total)
                    return False
            except ValueError:
                    ans = input('Please enter a valid number: ') 
    else:
        flag = False
        total = []
        b = random.randint(1,2)
        a = []
        for i in range(random.randint(1,3)):
            a = a + [random.randint(1,3)]
        
        for i in range(b):
            for j in range(len(a)):
                total = total +  [a[j]]
        

        ans = input("Here is a function:\ndef xyx(a,b):\n'''\n(list)(int)->(list)\n'''\n\tfor i in range(b):\n\t\tfor j in range(len(a)):\n\t\t\ttotal += [a[j]]\nreturn total" + "\n\nThe following function will return a list when calling xyx("+str(a)+","+str(b)+")\nPlease write the numbers that will come out of the list\nNOTE: please separate numbers with a comma (ex: 2,1), if it returns nothing, just press enter ")
        
        while flag == False:
            try:
                ans = ("[" + ans + "]").replace(",",", ")
                if ans == str(total).strip():
                    print(ans,True)
                    return True
                else:
                    print(str(total).strip(),False)
                    return False
            except ValueError:
                    ans = input('Please enter a valid number: ') 
def question_3():
    return 0
def test():
    """
The following will be in this quiz:
The range function (all three formats). 


- arithmetic expressions in python (including +,-,*, /, exponentiation **, integer division //, mod %, ..)
- + operator on when applied on numbers, strings, lists
- == operator on numbers, strings, lists ...
- keywords/operators: pass, in,
- (compound) Boolean expressions and Boolean operators (==, !=, not ...)
- data types in Python (including None)
- function design
- function calls
- docstrings
- functions that return values vs. functions that do not
- if statements
- for loops
- while loops
- strings (including slicing)
- lists and tuples and operations on them including indexing, slicing, looping over elements of the list, looping over indices in the list
- order of execution
- mutable vs immutable objects (i.e. variables that refer to immutable objects like strings, numbers and tuples vs variables that refer to mutable objects like lists), memory, aliasing
- counting how many times something is printed
- LOGIC/ALGORITHMS/SOLVING COMPUTATIONAL PROBLEMS (understanding what a program/function does, writing programs etc) on all of the above data types: lists,  strings,  etc ...

******************



print, including print with end=" " 
range
.append (from list module)
.sort (from list module)
.count (from list and str modules)
len
. upper (from str module)

int(), str()


***************
Finally here some type of questions that appear frequently in the midterm:

What does the following code fragment print
or
Which of the options solves the problem correctly?
or
Which of the statements below is true about the following program?
or
What does the following function do?
or
Which of the following functions correctly computes ...
or
Which of the lines of code, when placed in the  indicated location, correctly solves the problem?
etc"""

    question_1(random.randint(0,2))
    print("\n\n")
    question_2(1)
    question_3()
test()
