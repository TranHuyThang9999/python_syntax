def sum_odd():
    sum = 0
    n = int(input("Nhap N: "))
    for i in range(1, n + 1):
        sum += i
    return sum

def SumExponential():
    sum = 0
    n = int(input("Nhap N: "))
    for i in range(1,n):
        sum+=(pow(i,2))
    return  sum
def sum_fraction():
    sum = 0
    n = int(input("Nhap N: "))
    for i in range (1,n):
        sum+= (1/i)
    return sum

def sum_fraction_odd():
    sum = 0
    n = int(input("Nhap N: "))
    for i in range(1,n):
        sum+=(1/(i*2)) #phép chia nguyên // để lấy từng chữ số của n
    return sum
def countNumberInt():
    count = 0
    n = int(input("Nhap N: "))
    while n>0:
        n=n//10
        count=count+1
    return count

if __name__ == "__main__":
    print("Process ....")
    #print("Tong cac so le tu 1 den N la:", sum_odd())
    #print("sum Exponential =   ",Exponential())
    #print("sum fraction = ",sum_fraction())
   #print("sum fraction odd = ",sum_fraction_odd())
    #num_digits = len(str(n))
    print("count len number = ",countNumberInt())

