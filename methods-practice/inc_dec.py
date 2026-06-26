def inp():
    try:
        num = int(input("Enter your number: "))
        ch = int(input("Enter 1 to increment.\nEnter 2 to decrement."))
        return num,ch
    except:
        print("No Valid input.")
        return 0

def increment(a):
    return a+1
def decrement(b):
    return b-1
def display(dis):
    print(dis)

def final():
    num,ch = inp()
    if(ch==1):
        num = increment(num)
    elif(ch==2):
        num = decrement(num)
    else:
        print("Wrong Choice")
    display(num)

final()