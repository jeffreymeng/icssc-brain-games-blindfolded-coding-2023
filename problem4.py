

def find_lock_solutions(next_combination_digit: list[int | "END"]) -> list[str]:
    # your code here

    return 0 # change this!


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
        assert sorted(find_lock_solutions(input2)) == output2
    except AssertionError:
        print("\nCase 2 was not correct")
        print("Expected: ", repr(output2))
        print("Your answer: ", repr(find_lock_solutions(input2)))
    except Exception as e:
        raise e
    else:
        print("Passed!")
