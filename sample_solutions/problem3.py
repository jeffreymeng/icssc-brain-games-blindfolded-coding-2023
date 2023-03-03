

def lab_location(readings: list[int]):
    return max(range(360),
               key=lambda i: readings[i] - sum(readings[(di + i + 360) % 360] for di in [-2, -1, 1, 2]) / 4)

def lab_location2(readings: list[int]):
    largest_deg = -1
    largest_val = -1

    def get_reading(i):
        if i >= 360:
            i -= 360
        # if i is negative, that's fine. Python will read from the back as expected.
        return readings[i]

    for i in range(len(readings)):
        background_noise = (get_reading(i - 2) + get_reading(i - 1) + get_reading(i + 1) + get_reading(i + 2)) / 4
        val = readings[i] - background_noise
        if i == 0 or val > largest_val:
            largest_val = val
            largest_deg = i

    return largest_deg

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
