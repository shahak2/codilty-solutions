The problem:
A rectangular map consisting of N rows and M columns of square areas is given. Each area is painted with a certain color.
Two areas on the map belong to the same country if both coditions are met:
1. they have the same color.
2. you can move from one to another by going west/south/north/east (meaning, not diagonally).

Write a function that counts the number of countries.

For example:


<img src="https://user-images.githubusercontent.com/47245335/136171825-08d21e48-cd14-4fc9-9d51-0f2807ba9af7.png" width="200" height="400">




Time complexity O(N x M)

Side note: my first given solution used recursion. I added it as it is much more intuitive. However, when the given matrix is large
the depth of the program's stack is too large. 
My other and correct solution uses a stack instead, to keep track of the country's relevant borders.
Each time a cell is popped out of the stack, we add its neighbors if they have the same color.
