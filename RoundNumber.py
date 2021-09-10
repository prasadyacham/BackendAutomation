A = input("Enter Number 1: ")
B = input("Enter Number 2: ")

FirstFlag = True
if len(A)!= len(B):
    FirstFlag = False
length = len(A)

Loop = []

for j in range(2):
    for i in range(length):
        Loop.append(i)

print (Loop)

counterinitiate= 0

Flag = True

for i in range(len(A)):
    if Flag == True:
        for x in range(len(B)):
            if (B[x]==A[i]):
                offset = x
                print ("{} {}".format("Offset is: ", offset))
                counterinitiate  = Loop.index(offset)
                Flag = False
                break
            else:
                pass
    else:
        break

SecondFlag = True

for a in range(5):
    if (A[a]==B[Loop[a+counterinitiate]]):
        pass
    else:
        SecondFlag = False

if FirstFlag == True and SecondFlag == True:
    print("It is a round number")
else:
    print("It is not a round number")