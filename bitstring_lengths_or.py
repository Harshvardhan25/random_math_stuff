def bitstring(n):
    return 2**n

def main():
    nums=input("Enter lengths separated by commas: ")
    nums=[int(n) for n in nums.split(",")]
    count=0
    for n in nums:
        count+=bitstring(n)
    print("Count:", str(count))
if __name__ == "__main__":
    main()