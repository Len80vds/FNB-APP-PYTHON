
try:
    print(X)
except NameError:
    print("Variable X is not defined")
else:
    print("Everything is fine")
#except NameError:
    #print("Variable X is not defined")
#except:
    #print("An exception occurred")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero allowed")