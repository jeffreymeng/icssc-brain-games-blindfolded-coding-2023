

def lab_location(readings: list[int]) -> int:
    # your code here

    return 0 # change this!

if __name__ == "__main__":
    # sample cases

    print("Testing sample case 1...", end="")
    assert lab_location([100, 90, 85] + [85] * 355 + [90, 98]) == 0
    print("Passed!")

    print("Testing sample case 2...", end="")
    assert lab_location([70] * 4 + [70, 80, 90, 89, 70, 20, 70] + [70] * 349) == 7
    print("Passed!")
