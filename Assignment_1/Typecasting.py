# Q. 9 .What three functions can be used to get the integer,floating-point number,or string version of a value?

def main():
    A = 10.0
    a = int(A)
    b = float(A)
    c = str(A)
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)

    print("\nSecond Method")
    print('int(10.0) -> ', int(10.0))   # int() function converts given input to int
    print('float(10) -> ', float(10))   # float() function converts given input to float
    print('str(10.0)   -> ', str(10.0))     # str() function converts given input to string

if __name__ == "__main__":
    main()
