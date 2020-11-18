from factorial import factorial

def combination(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

def permutation(n, r):
    return int(factorial(n)/factorial(n-r))

def main():
    nums= input("Enter n,r: ")
    n, r=int(nums.split(",")[0]),int(nums.split(",")[1])
    print("Combination: ", str(combination(n,r)))
    print("Permutation: ", str(permutation(n,r)))

if __name__ == "__main__":
    main()