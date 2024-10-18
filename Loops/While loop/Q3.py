#Q3.Write a python script to print N's multiplication table using while loop

num = int(input("Enter the number")) #Q3.printing tables of given number.
n=1
while n<=10:
    print (f"{num} x {n} = {n * num}") # can also written as print(num ," * ", n ," = ",(num*n))
    n=n+1

Output : 
    Enter the number 2

    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    2 x 4 = 8
    2 x 5 = 10
    2 x 6 = 12
    2 x 7 = 14
    2 x 8 = 16
    2 x 9 = 18
    2 x 10 = 20
