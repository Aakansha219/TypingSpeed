from time import time
#calculating errors9
def tyerror(prompt):
    global inwords
    words = prompt.split()
    errors = 0
    for i in range(len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors+1
        else:
            if inwords[i] == words[i]:
                if(inwords[i-1] == words[i - 1]) & (inwords[i-1]==words[i-1]):
                    continue
                else:errors+=1
            else:
                errors+=1
    return errors
#to calculate speed
def speed(inprompt,stime,etime):
    global time
    global inwords

    inwords = inprompt.split()
    Twords = len(inwords)
    speed = Twords / time
    return speed
#calculate the total elapsed time
def elapsedtime(stTime,endTime):
    time = endTime - stTime
    return time

if __name__ == '__main__':
    prompt = '''Touch typing improves the accuracy of the work a typist produces. This is because they are extremely
    familiar with the location of all the letters on the keyboard. Thus, there are fewer mistakes, and mistakes are 
    much more quickly corrected. It also increases employees’ confidence in their work and is important to a 
    company’s productivity.'''
    #text to be typed
    print("type this:- " , prompt)
    input("Press Enter when you are ready to start typing")
    stTime = time()
    inprompt = input()
    endTime =  time()
    time = round(elapsedtime(stTime, endTime), 2)
    speed = speed(inprompt,stTime,endTime)
    errors = tyerror(prompt)
    print("Total Time ELAPSED: ", time, "seconds")
    print("Your typing speed is ", speed," words per minute" )
    print("You made ", errors, " errors")