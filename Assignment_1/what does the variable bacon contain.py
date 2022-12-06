# Q. After running the following code, what does the variable bacon contain?
def main():
    become = 22
    become+1
    print('Explanation: The variable bacon is set to 22 .The expression bacon + 1 does not reassign the value in bacon'
          '(\nthat would the case if the expression is like bacon = bacon + 1 instead of bacon + 1)'
          '\nAns :', become)

if __name__=="__main__":
    main()
