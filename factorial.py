def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)

def main():
    num= int(input("Enter num:"))
    print(factorial(num))

if __name__=="__main__":
    main()