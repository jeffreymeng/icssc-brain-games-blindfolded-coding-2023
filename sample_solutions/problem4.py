

def find_lock_solutions(next_combination_digit: list[int | str]) -> list[str]:
    def find_lock_solutions_ending_in_digit(end_digit: int | str, partial_solution: str):
        new_partial_solutions = []
        for digit in range(10):
            if next_combination_digit[digit] == end_digit:
                new_partial_solutions.append(str(digit) + partial_solution)

        if len(new_partial_solutions) == 0: # there are no solutions
            return []
        elif len(new_partial_solutions[0]) == 4: # we've found all the solutions
            return new_partial_solutions
        else:
            all_new_solutions = []
            for new_ps in new_partial_solutions:
                all_new_solutions.extend(find_lock_solutions_ending_in_digit(int(new_ps[0]), new_ps))
            return all_new_solutions

    return find_lock_solutions_ending_in_digit("END", "")

# brute force is ok too
def find_lock_solutions2(next_combination_digit: list[int | str]) -> list[str]:
    solutions = []
    for i in range(10000):
        num = str(i)
        num = "0" * (4 - len(num)) + num

        if next_combination_digit[int(num[0])] == int(num[1]) and \
           next_combination_digit[int(num[1])] == int(num[2]) and \
           next_combination_digit[int(num[2])] == int(num[3]) and \
           next_combination_digit[int(num[3])] == "END":
            solutions.append(num)

    return solutions


if __name__ == "__main__":
    # sample cases

    print("Testing sample case 1...", end="")
    input1 = [0, 2, 3, 4, "END", 5, 6, 7, 8, 9]
    output1 = ["1234"]
    try:
        assert find_lock_solutions(input1) == output1
    except AssertionError:
        print("\nCase 1 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(find_lock_solutions(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")

    print("Testing sample case 2...", end="")
    input2 = [2, "END", 3, 1, 4, 3, 8, 2, 9, "END"]
    output2 = ["0231", "7231"]
    try:
        assert find_lock_solutions(input2) == output2
    except AssertionError:
        print("\nCase 2 was not correct")
        print("Expected: ", repr(output2))
        print("Your answer: ", repr(find_lock_solutions(input2)))
    except Exception as e:
        raise e
    else:
        print("Passed!")
