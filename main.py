# Üçgen

def DrawTriangle(step):
    total = step * 2

    for letterCount in range(1, total+1, 2):
        spaceCount = int((total - letterCount) / 2)
    
        space = ""
        for j in range(spaceCount):
            space += " "
    
        letters = ""
        for x in range(letterCount):
            letters += "*"
    
        print(space + letters + space)

digit = int(input("Enter digit number: "))
DrawTriangle(digit)