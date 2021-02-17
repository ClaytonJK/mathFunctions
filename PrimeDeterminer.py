
testNumber = int(input("Please give the desired number:"))
divisor = 2
factorable = False
while(testNumber>divisor) : 
    if testNumber%divisor == 0 :
        print(testNumber,"is not prime with a factor of", divisor)
        factorable = True
    divisor = divisor + 1
if factorable == False : 
    print(testNumber, "is prime")
    