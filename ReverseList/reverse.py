"""
Chiara Altobelli
Programming Exercise 11.2 Reverse
December 8, 2020

Program description: This program takes a given list and reverses the order by swapping the values at each end.
Big O notation: 0(n) - complexity is expected to double as the length of the list increases

"""

def reverse(lyst):
    # Define your reverse function here without using the reverse function.
    for index in range(len(lyst) // 2): #only need to go through half of the list to swap all 
        lyst[index], lyst[-index-1] = lyst [-index-1], lyst[index]

def main():
    """Tests with two lists."""
    lyst = list(range(4))
    print("List 1 before reversing: ", lyst,"\n")
    reverse(lyst)
    print("List 1 after reversing: ", lyst, "\n")
    lyst = list(range(3))
    print("List 2 before reversing: ", lyst,"\n")
    reverse(lyst)
    print("List 2 after reversing: ", lyst,"\n")

if __name__ == "__main__":
    main()

