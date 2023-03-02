

def find_lock_solutions(next_combination_digit: list[int | "END"]) -> list[str]:
    # your code here

    return 0 # change this!

if __name__ == "__main__":
    # sample cases

    print("Testing sample case 1...", end="")
    assert find_lock_solutions([0, 2, 3, 4, "END", 5, 6, 7, 8, 9]) == ["1234"]
    print("Passed!")

    print("Testing sample case 2...", end="")
    assert find_lock_solutions([2, "END", 3, 1, 4, 3, 8, 2, 9, "END"]) == ["0231", "7231"]
    print("Passed!")
