letters=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',)
def shift(string, shift_val):
    s=""
    shift_val==shift_val%26
    if shift_val==0:
        return string
    for char in string:
        if char.isalpha():
            i=letters.index(char.lower())
            if char.isupper():
                s+=letters[(i+shift_val)%26].upper()
            else:
                s+=letters[(i+shift_val)%26]
        else:
            s+=char
    return s

def main():
    string=input("Enter string: ")
    shift_val=int(input("Enter shift: "))
    print(shift(string,shift_val))
        
if __name__=="__main__":
    main()
