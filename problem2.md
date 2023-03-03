## 2. Getting In 
You're now ready to infiltrate the lab! After consulting some blueprints of the 
building, you decide the easiest way in to the basement lab is through the elevator. You don’t 
have the key card required to press the `-1` button (for the basement), but luckily, you notice 
the elevator control panel is loose! You can reorder the wires to make any 
button go to any floor, as long as you make sure the elevator’s safety checks 
still pass. It turns out the elevator only makes sure that the sum of all 
target floors is correct, and that there are no duplicate floors. Interestingly, 
the elevator doesn't even check that all buttons go to valid floors! You decide 
to rewire the elevator such that the button for floor `2` takes you to floor `-1` 
instead.

### The task
Write a function `rewire_elevator(floors: list[int]) -> list[int]` that takes in a list of
integers, with the nth integer representing the floor that the nth button 
takes you to. The input will always have at least **four** items in it, and will 
always be in the format `[-1, 1, 2, 3, ...]`. e.g. The input will always start with
`-1, 1, 2, 3` and continue with sequential integers until the end of the list.

Return a list of integers representing the floors that each
button takes you to after you rewire it, with the third button in the list
(the button at index 2) taking you to floor -1 instead, following the 
elevator’s checks above.

[Check out the template: problem2.py](problem2.py)

**Sample input:**
```python
rewire_elevator([-1, 1, 2, 3, 4, 5])
```
**Sample output:** (_One of many possible outputs_)
```python
[-3,-2,-1, 2, 4, 14]
```
**Explanation**: The button that used to take us to 2 now takes us to floor -1, the sum hasn't changed,
and there are no duplicate numbers, which is all we want.

**Sample input 2:**
```python
rewire_elevator([-1, 1, 2, 3])
```
**Sample output 2:**  (_One of many possible outputs_)
```python
[-5,-3,-1, 9]
```
Same thing: The button that used to take us to 2 now takes us to floor -1, the sum hasn't changed,
and there are no duplicate numbers, which is all we want.
