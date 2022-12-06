# Q. 3 What are the three different types of Boolean operators
def main():
    a = 100
    b = 200
    print("\nThe Truth tables for the boolean tables are as follows:")
    print("\nTruth table for and operator")

    print("\nTrue and True is     : ", a > 50 and b > 100)       # Example of boolean and operator
    print("True and False is    : ", a > 50 and b < 100)         # Example of boolean and operator
    print("False and True is    : ", a < 50 and b > 100)         # Example of boolean and operator
    print("False and False is   : ", a < 50 and b < 100, '\n')    # Example of boolean and operator

    print("Truth table for or operator")

    print("\nTrue or True is     : ", a > 50 or b > 100)        # Example of boolean or operator
    print("True or False is    : ", a > 50 or b < 100)          # Example of boolean or operator
    print("False or True is    : ", a < 50 or b > 100)          # Example of boolean or operator
    print("False or False is   : ", a < 50 or b < 100, '\n')     # Example of boolean or operator

    print("Truth table for not operator")

    print("\nTrue not is   : ", not(a > 10))                    # Example of boolean mot operator
    print("False not is  : ", not(a < 10))                      # Example of boolean mot operator

if __name__=="__main__":
    main()
