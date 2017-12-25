# O(n^2) rectangle search
**input ... digital matrix**<br>

```
1000
1111
0001
```

**output ... list of rectangle**<br>
(0, 0, 0, 1)<br>
(0, 1, 3, 1)<br>
(3, 1, 3, 2)<br>

output "rectangle" is not included by aother rectangle.<br>
This code would not recognize a following region as rectangle.<br>
(1, 1, 2, 1)<br>

Because (1, 1, 2, 1) is included by (0, 1, 3, 1).<br>

<br>

# original source code
The original source code is below, written in C language.<br>
For understanding the algorithm, I have rewrote it in Python.<br> 
https://www.ipsj.or.jp/07editj/promenade/4304.pdf<br>

<br>

# usage
## 1. with optimization
```
$ python -O rectangle_search.py
1111110
1101101
1110110
0111101
1111110
1111111
0010010
(0, 0, 0, 5)
(0, 3, 1, 4)
(1, 6, 1, 6)
(0, 0, 2, 1)
(2, 0, 2, 2)
(2, 4, 2, 5)
(3, 6, 3, 6)
(0, 1, 5, 1)
(2, 1, 5, 2)
(0, 4, 5, 4)
(3, 1, 5, 4)
(4, 0, 5, 5)
(5, 0, 5, 6)
(2, 2, 6, 2)
(4, 5, 6, 5)
```



## 2. without optimization
Without optimization, you can see the interim progresss of this code.<br>
The code print variables when it detect a rectangle.<br>

```
$ python rectangle_search.py < digital_matrix.txt
right bottom corner detect...
-----
  num_of_rectangle = 1
  row, col+1 = 1, 7
  row0, col0, row1, col1, s =(1, 1, 1, 6, 6)
-----
extended_board = 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]
                      [0, 1, 1, 1, 1, 1, 1, 0]

lst_max_0_row       = [8, 0, 0, 0, 0, 0, 0, 1, 0]
lst_left_0_wall_col = [0, 0, 0, 0, 0, 0, 0, 0, 0]
height_col          =                    6
left_0_wall_col     =                       7
```

<br>

# Basic Proceadure
**basic concept**<br>
0 is tangent with one or more rectangles.<br>

**basic proceadure**<br>
1. Look for right bottom corner.<br>
2. Look for upper left corner.<br>

## 1. 
Let's think about digital matrix below.

```
1111110
1101101
1110110
0111101
1111110
1111111
0010010
```

## 2.
Let's think about a rectangle tangent with (3, 4) of 0.
```
1111 1 | 1 0
1101 1 | 0 1
1110 1 | 1 0
0111 1 |[0]1
1111 1 | 1 0
1111 1 | 1 1
0010 0 | 1 0
```


## 3. bottom right corner
What is a bottom right corner<br>
of the rectangle tangent with (3, 4) of 0?<br>

You can find it easily by looking down for 0, (6, 4).<br>

The right bottom corner would be (5, 4).

```
1111 1 | 1 0
1101 1 | 0 1
1110 1 | 1 0
0111 1 |[0]1
1111 1 | 1 0
1111 1 | 1 1
-------|----
0010[0]| 1 0
```

## 4. upper left corner
All that is left to search rectangle is to search upper left corners.

How to serach? At a glance, you might find out following three rectangles.
```
| 1 111 1 | 1 0
| 1 101 1 | 0 1
| 1 110 1 | 1 0
| 0 111 1 |[0]1
|---------|----
|[1]111 1 | 1 0
| 1 111 1 | 1 1
|---------|----
| 0 010[0]| 1 0
```
```
1| 1 11 1 | 1 0
1| 1 01 1 | 0 1
1| 1 10 1 | 1 0
-|--------|----
0|[1]11 1 |[0]1
1| 1 11 1 | 1 0
1| 1 11[1]| 1 1
-|--------|----
0| 0 10[0]| 1 0
```
```
----|---|----
1111|[1]| 1 0
1101| 1 | 0 1
1110| 1 | 1 0
0111| 1 |[0]1
1111| 1 | 1 0
1111|[1]| 1 1
----|---|----
0010|[0]| 1 0
```

## 5.
Sadly, howerver first one is not rectangle,<br>
the rectangle is contained by another.

Because you can move right wall to right side.

```
	      V you can move right side wall
| 1 111 1 * 1 |0
| 1 101 1 * 0 |1
| 1 110 1 * 1 |0
| 0 111 1 *[0]|1
|---------*---|- < upper wall
|[1]111 1 * 1 |0
| 1 111 1 * 1 |1
|---------*---|-
| 0 010[0]* 1 |0

```

<br>
This thing implies that<br>
upper wall's lower bound is higher than right wall's upper wall.


## 6. Summry
In summry, we are looking for the card whose upper left corner was chipped.
```
     |--|
1 111|1 | 1 0
1 101|1 | 0 1
1 110|1 | 1 0
 |---|  |
0|111 1 |[0]1
1|111 1 | 1 0
1|111 1 | 1 1
 |------|
0 010[0]  1 0
```

# Detail Proceadure.
Sorry, for detail, read the source code.<br>

1. How to search left bottom corner.<br>
2. How to search right bottom corner.<br>
