## 2. Taking Measurements
You’re now in the basement, and you just need to find the lab! Fortunately, you 
brought your brain wave detector with you to detect brain waves emitted by the
brain cell lab. You rotate around in a circle, quickly taking measurements
for every degree. Unfortunately, it turns out that there are many sources 
of brain waves in the environment, which creates background interference, so
the lab isn't in the direction with the highest number of brain waves, but rather
the direction with the number of brain waves that stands out the most against the background
waves around it. To determine how much the background waves are for a particular degree, 
look at two readings to the left and two readings to the right of the measurement, 
and average these four readings. 
Can you write a program to find the degree with the highest readings relative to the background
wave measurements?

For example, suppose you get the following readings
```
...
5 deg: 70 units
6 deg: 80 units
7 deg: 90 units
8 deg: 89 units
9 deg: 70 units
10 deg: 20 units
11 deg: 70 units
...
```
The relative reading at 7 deg is 90 - (70 + 80 + 89 + 90)/4 = 7.75 units.
The relative reading at 8 deg is 89 - (80 + 90 + 70 + 20)/4 = 24.0 units.
The relative reading at 9 deg is 70 - (90 + 89 + 20 + 70)/4 = 2.75 units.
Out of these three degrees, degree 8 is the direction with the most brain waves.

### The task
Write a function `lab_location(readings: list[int]) -> int` that takes in a list of
exactly 360 integers, with the nth integer representing the reading at n degrees.

Return the integer degree with the highest reading relative to the background, since
that's where the lab must be! If there are multiple equal highest readings, you may return
the location of any one of them.

**Sample Input**
```python
lab_location([100, 90, 85] + [85] * 355 + [90, 98])
# e.g. [100, 90, 85, (85 repeated 355 more times), 90, 98]
```
Return: `0`. The background radiation for this angle is 
(90 + 85 + 90 + 98)/4, which is 90.75. The measurement at degree 0 is 100, 9.75 higher than the background! 

**Sample Input 2**
```python
lab_location([70] * 4 + [70, 80, 90, 89, 70, 20, 70] + [70] * 349)
```
Return: `7`. (value = 89) See above example for details.
