# Q. 4 What are the values of the following expressions?

# (5>4) and (3==5)
# not (5>4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

def main():

    print("Ans : ", (5 > 4) and (3 == 5))
    print("Ans : ", not (5 > 4))
    print("Ans : ", (5 > 4) or (3 == 5))
    print("Ans : ", not ((5 > 4) or (3 == 5)))
    print("Ans : ", (True and True) and (True == False))
    print("Ans : ", (not False) or (not True))

if __name__=="__main__":
    main()
