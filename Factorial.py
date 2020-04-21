'''
    [Factorial.py]
    By : Nasir Ali
'''
def fact(n):
   k = 1
   for j in range(1,n+1):
        k*=j
   return k


while True:
   c = input("Enter a Number : ")
   print("{}! = {}".format(c,fact(int(c))))
