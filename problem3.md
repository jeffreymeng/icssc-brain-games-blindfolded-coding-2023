
## 3. Crack The Lock
Congratulations! You've found the entrance to the lab. Now you just need to get through the keypad to enter
the lab. Fortunately, it turned out that due to some archaic password requirements by the keypad manufacturers,
for any digit `n` (with n between 0 and 9), the digit that comes after it must come after every instance of `n` in
the code. For example, one possibility is that every `0` in the code must be followed by a `2`, and every `2` must be
followed by a `3`, and so on. Furthermore, you were able to determine a map of digits of the code, specifying exactly
what digit must come after any specific digit in the code. It's possible that a digit cannot be followed by any digits
(meaning it must be the last digit in the code), and in fact, the code **must** end in a digit that's not followed
by any other digits. The code is four digits long, so your task is to find all the possible codes 
**of length 4** for this lock.

For example, suppose you have the following map:
```
0 -> 2
1 -> END
2 -> 3
3 -> 1
4 -> 4
5 -> 3
6 -> 8
7 -> 2
8 -> 9
9 -> END
```
This map specifies that no digit can come after 1 and 9, and these are the only possible end digits of the code. The
only possible codes of length 4 that satisfy these requirements are `"0231"` and `"7231"`. Note that it's possible for the
map to have cycles in it (for example, `4` can only be followed by `4` in this example), which of course
means it can't be part of the code.

### The task
Write a function `find_lock_solutions(map: list[int]) -> list[str]` that takes in a 10 element long list where the 