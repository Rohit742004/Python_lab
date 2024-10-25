#Write a python script to print numbers not divisible by 5 given between starting  range and ending range


Start = int(input("Enter the Starting range : "))
End = int(input("Enter the Ending range : "))
for i in range(Start,End):
    if(i%5==0):
        continue
    else:
        print(i)



Output:
Enter the Starting range :  10
Enter the Ending range :  20

11
12
13
14
16
17
18
19
