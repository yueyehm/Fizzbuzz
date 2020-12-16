import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))

retryCount = 0
retryLimit = 5
raw_num = 0
num = 0
while True:
    raw_num = raw_input("Input your numbers: ")
    if(str.isdigit(raw_num)):
        num = int(raw_num)
        break
    elif(len(raw_num) == 0):
        print("No input deteced. Use 100 as default.")
        num = 100
        break
    else:
        print("Input error. Plrease re-enter.")
        retryCount += 1
        if(retryCount >= retryLimit):
            print("Error too much. Exit.")
            break
        
    

a = range(1, num)
for b in a:
    if b % 3 == 0:
        print("fizz")
    elif b % 5 == 0:
        print("buzz")
    else:
        print b




    
    
        

