#Write a python script to generate the following multiplication table format:

for i in range(1,6):
    print('Multiplication table of ',i)
    for m in range(1,6):
        if i >= 5 and m >= 5:
            break 
        print(i * m,end=' ')
    print('')


Output:

Multiplication table of  1
1 2 3 4 5 
Multiplication table of  2
2 4 6 8 10 
Multiplication table of  3
3 6 9 12 15 
Multiplication table of  4
4 8 12 16 20 
Multiplication table of  5
5 10 15 20 
