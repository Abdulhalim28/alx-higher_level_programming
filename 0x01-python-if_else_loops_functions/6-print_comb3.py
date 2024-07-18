#!/usr/bin/python3
for i in range(1, 10):
 for j in range(i+1, 10):
 print("{:02d}".format(i*10+j), end=', ')
 print()  # This print statement should be indented to match the inner loop
 print()  # This print statement should not be indented, to print a newline at the end


