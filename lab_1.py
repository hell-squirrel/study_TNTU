__author__ = 'Hulka Yuriy '
#Python 3.4.3
def heightToInch(data):
    while True:
        try:
            return format(float(data)*0.3937, '.4f')
            break
        except ValueError:
            print("Incorrect value")
            return -1
            break

if __name__=="__main__":
    print(heightToInch(input("Write a height:\n")))

