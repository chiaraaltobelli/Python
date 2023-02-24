"""
Chiara Altobelli
Programming Exerecise 11.3 Expo
December 8, 2020

Program Description:

Big O Notation: O(n) where n is represented by the exponent
"""

def expo(base, exponent):
    # Write your function here
    if exponent == 0:
        total = 1 #if exponent is 0 return 1
    else:
        counter = exponent - 1 #because total starts as "base"
        total = base #set beginning balue equal to given base (2)
        while counter > 0:
            total *= base 
            counter -= 1
    return total

def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print("Exponent: ", exponent, "Result : ", expo(2, exponent))

if __name__ == "__main__":
    main()

