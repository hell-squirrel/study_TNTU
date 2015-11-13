__author__ = 'Hulka Yuriy'
#Python 3.4.3
def harmonicMean():
    while True:
        try:
            data1=float(input("Write a number 1:\n"))
            if data1==0:
                break
            data2=float(input("Write a number 2:\n"))
            if data2==0:
                break
            if type(data1)==float and type(data2)==float:
                result=(2.0*data1*data1)/(data1+data2)
                print(result)
        except ValueError:
            print("Wrong input")
    return result
if __name__=="__main__":
    harmonicMean()
    print('hello motherfucker')