import pyinputplus as pyip
import random, time
question=10
correct=0
while question>=1:
    no=11-question
    n1=random.randint(0,9)
    n2=random.randint(0,9)
    ans=n1*n2
    attempt=3
    print("{}.: What is the result of {}x{}".format(no,n1,n2))
    while attempt>0:
        try:
            answer=pyip.inputStr(allowRegexes=['{}'.format(ans)],timeout=8)
        except pyip.TimeoutException:
            print("Oh!! Too Late, TimeOut")
            break
        else:
            if int(answer)==ans:
                correct=correct+1
                print("Brilliant!! You Got it.")
                break;
            else:
                attempt=attempt-1
                
                if attempt>0:
                    print("Wrong Answer! You have {} tries left".format(attempt))
                else:
                    print("Sad!! out of tries")
    time.sleep(1)
    question=question-1
print("Your Total score is {}".format(correct))