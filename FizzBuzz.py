import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))

        
raw_num = raw_input("Input your numbers: ")
if(str.isdigit(raw_num)):
    num = int(raw_num)
elif(len(raw_num) == 0):
    num = 100
else:
    print("Input error..")
    exit()
    

a = range(1, num)
for b in a:
    if b % 3 == 0:
        print("fizz")
    elif b % 5 == 0:
        print("buzz")
    else:
        print b

    
    
        

