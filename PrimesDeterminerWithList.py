print("Press Ctrl + C to end any long-running primes")
testNumber = int(input("Please give the desired number:"))
divisor = 2
factorable = False
factorsList = list()
n = 0
while(testNumber>divisor) : 
    if testNumber%divisor == 0 :
        factorsList.insert(n,divisor)
        n += 1
        print("Thinking....")
    divisor += 1
if len(factorsList) == 0 :
    print(testNumber, "is prime")
else :
    print(testNumber,"is not prime with factors of", factorsList)
