# Q. 2 What are the three different types of Boolean operators
def main():
    a = 100
    b = 200
    print(a > 50 and b > 100)       # Example of boolean and operator
    print(a > 200 or b > 100)       # Example of boolean or operator
    print(not(a > 10))              # Example of boolean mot operator

if __name__=="__main__":
    main()