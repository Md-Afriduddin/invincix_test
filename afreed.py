def compound(string):
    n = len(string)
    maximumLen = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            flag = 1
            for k in range(0, ((j - i) // 2) + 1):
                if (string[i + k] != string[j - k]):
                    flag = 0

            if (flag != 0 and (j - i + 1) > maximumLen):
                start = i
                maximumLen = j - i + 1
                
    print("Best Drug from the complex is : ", end = "")
    end = start + maximumLen - 1
    for i in range(start, end+1):
        print(string[i], end = "")

if __name__ == '__main__':

    string = input("Enter Name of Complex Compound :")
    compound(string)