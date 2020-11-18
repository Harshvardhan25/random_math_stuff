from shift import shift

def all_shift(string):
    shifts=[]
    for i in range(26):
        shifts.append(shift(string,i))
    return shifts

def main():
    string=input("Enter a string: ")
    shifts=all_shift(string)
    print("All 26 shifts:")
    for shifted in shifts:
        print(shifted)

if __name__=="__main__":
    main()