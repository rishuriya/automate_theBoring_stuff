# chapter 2
### 1. What are the two values of the Boolean data type? How do you write them?
True and false are two values of boolean data type. We have to right T and F in uppercase and rest in lower.

### 2. What are the three Boolean operators?
and, or and not are three boolean operators.

### 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
True and True is true
True and False is false
False and True is false
False and False is false
true or true is true
true or false is true
False or True is true
False or False is False
not True is False.
not False is True.

### 4. What do the following expressions evaluate to?
False, False, True, False, False, True

### 5. What are the six comparison operators?
<,>,==,<=,>= and !=

### 6. What is the difference between the equal to operator and the assignment operator?
Equal operator compare while assignment operator assign value to variable.

### 7. Explain what a condition is and where you would use one.
Condition is a statement which give boolean value as result and it use in flow of control.

### 8. Identify the three blocks in this code:
1 block contain other two block
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')

### 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam=int(input())
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
### 10. What keys can you press if your program is stuck in an infinite loop?
Ctrl+C to stop programm if it struck in infinite loop.

### 11. What is the difference between break and continue?
break statement immediately stop the loop while continue statement start loop from starting.

### 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
range(10) start range from 0 to 10 where 10 not include, range(0,10) start from 0 to 10 but if we replace 0 from less than 10 then it will start from that number to 10 where 10 is not included and range(0,10,1) start from 0 to 10 and it increase by difference of 1.

### 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(10):
    print(i+1)

i=1
while i<11:
    print(i)
    i=i+1

### 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
to call bacon(), i use spam.bacon()