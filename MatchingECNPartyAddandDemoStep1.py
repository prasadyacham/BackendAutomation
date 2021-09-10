# Step 1: Script to find matching ECNs between PartyAddress and Demographics
PartyAddress = {}

with open("C:\\Users\\Prasad.Yacham\\PartyAddress.txt", "r") as fs1:
    for line in fs1:
        currentlinef1 = line.split("|")
        PartyAddress[currentlinef1[0]] = currentlinef1[0] + '|' + currentlinef1[7] + '|' + currentlinef1[9]

print("\n")
print(len(PartyAddress))
print("End of PartyAddress_2M")

DemoG = {}
Match = {}

with open("C:\\Users\\Prasad.Yacham\\PartyDemographics_2M.txt", "r") as fs2:
    for line2 in fs2:
        currentlinef2 = line2.split("|")
        DemoG[currentlinef2[0]] = currentlinef2[1] + '|' + currentlinef2[2] + '|' + currentlinef1[7]

print("\n")
print(len(DemoG))
print("End of PartyDemographics_2M")

for keyAddress in PartyAddress:
    if keyAddress in DemoG.keys():
        Match[keyAddress] = DemoG[keyAddress] + '|' + PartyAddress[keyAddress]
print("Matching ECN's " + str(len(Match)))

with open("C:\\Users\Prasad.Yacham\FinalECNMatch.txt", "w") as fs3:
    for ECNS in Match:
        str1 = str(Match[ECNS])
        fs3.write(str1 + "\n")
