# Q. 7. Identify the three blocks in this code

# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')

# Ans: In Python, code block refers to a collection of code that is in the same block or indent.
# This is most commonly found in classes, functions, and loops.
# e = is that assignment operator that stores a value in a variable.


def main():
    spam = 0
    if spam == 10:
        print("eggs")  # Block 1
    if spam > 5:
        print("becon") # Block 2
    else:
        print("ham")   # Block 3
    print("spam")
    print("spam")

if __name__=="__main__":
    main()
