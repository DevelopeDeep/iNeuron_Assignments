# Q. 8 What should the values of the following two terms be

def main():
    Mango = "Sweet"         # Valid variable initialization
    100 = "Number"          # Invalid variable initialization
    print(Mango)
    print(100)
try:
    print(eval('100 = Number'))
except SyntaxError as err:
    print('Syntax error')
    print (err)

if __name__=="__main__":
    main()