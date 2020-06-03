from random import randint
import math

q = int(input("Enter the quantity of numbers: "))
arr = []
for i in range(q):
    arr.append(randint(0, 40))

def squareTriangle(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    s = float('{:.2f}'.format(s))
    return s

print("Array of random numbers:", arr)
count = 0
resArray = []
resStr = ''
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if(arr[i] < (arr[j] + arr[k]) and arr[j] < (arr[i] + arr[k]) and arr[k] < (arr[i] + arr[j])):
                count += 1
                resArray.append(str(arr[i]))
                resArray.append(str(arr[j]))
                resArray.append(str(arr[k]))

if resArray:
    print("Existing triangles -", count, "pcs :")
    for res in range(0, len(resArray), 3):
        a = int(resArray[res])
        b = int(resArray[res + 1])
        c = int(resArray[res + 2])
        print("Triangle with sides in cm:", "a =", a, "b =", b, "c =", c, "\nSquare of the triangle:", squareTriangle(a, b, c), "cm2")
        print("")

else:
    print("Triangles does NOT exist")