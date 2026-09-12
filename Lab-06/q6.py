''' 6. Print the following table to display the square, cube and square root of the numbers from 1
to 15. Round the value to keep four digits after the decimal point.
N N^2 N^3 Square Root
1 1 1 1.0000
2 4 8 1.4142
3 9 27 1.7321
...
14 196 2744 3.7417
15 225 3375 3.8730 '''

# ill change this into something....
for i in range(1, 16):
    square = i ** 2
    cube = i ** 3
    sqrt = i ** 0.5
    print(f"{i} {square} {cube} {sqrt:.4f}")


print("n\t n^2\t n^3\t √n\t ")
for i in range(1,16):
    print(i,
          "\t", i**2,
          "\t", i**3,
          "\t", f"{i ** .5:.4f}")