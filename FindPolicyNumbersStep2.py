#Step 2: Script to find Policy Numbers from ECN in PartyRel
ECN = []
with open("C:\\Prasad.Yacham\\FinalECNMatch.txt","r") as fs1:
    for line1 in fs1:
        currentlinef1 = line1.split("|")
        ECN.append(currentlinef1[3])

ECN.sort()
PolicyDict = {}

print(len(ECN))

with open ("C:\\Prasad.Yacham\\PartyPolicyRel_2M.txt","r") as fs2:
    for line2 in fs2:
        currentlinef2 = line2.split("|")
        PolicyDict[currentlinef2[0]] = currentlinef2[2]

with open ("C:\\Prasad.Yacham\\FinalECNPolicy.txt","w") as fs3:
    for ECNS in ECN:
        if ECNS in PolicyDict.keys():
            str1 = ECNS + "|" + PolicyDict[ECNS] + "\n"
            fs2.write(str1)
        else:
            PolicyDict[ECNS] = "Blank"
            str1 = ECNS + "|" + PolicyDict[ECNS] + "\n"
            fs2.write(str1)