

def lab_location(readings: list[int]) -> int:
    # your code here

    return -1 # change this!

if __name__ == "__main__":
    # sample cases

    print("Testing sample case 1...", end="")
    input1 = [100, 90, 85] + [85] * 355 + [90, 98]
    output1 = 0
    try:
        assert lab_location(input1) == output1
    except AssertionError:
        print("\nCase 1 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(lab_location(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")

    print("Testing sample case 2...", end="")
    input2 = [70] * 4 + [70, 80, 90, 89, 70, 20, 70] + [70] * 349
    output2 = 7
    try:
        assert lab_location(input2) == output2
    except AssertionError:
        print("\nCase 2 was not correct")
        print("Expected: ", repr(output2))
        print("Your answer: ", repr(lab_location(input2)))
    except Exception as e:
        raise e
    else:
        print("Passed!")
