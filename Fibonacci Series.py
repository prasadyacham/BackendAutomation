input_n = int(input("Enter the size of Fibonacci Series: "))

def Fibonacci (input):
    fibseries = []
    if input == 0:
        fibseries.append(0)
        return fibseries
    if input == 1:
        fibseries.append(0,1)
        return fibseries
    fibseries = [0,1]
    for n in range (2,input+1):
        fibseries.append(fibseries[n-1]+fibseries[n-2])
        return fibseries

series = Fibonacci(input_n)
print (series)