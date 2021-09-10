Str = input("Enter the String: ")
Result = {}
FirstElement = False
for s in Str:
    if (s not in Result):
        Result[s]=Str.count(s)
        if (Str.count(s)>1):
            if(FirstElement==False):
                FirstDupChar = s
                FirstElement = True

print (Result)
print ("First Repeating Character: " +FirstDupChar)