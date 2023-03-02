

def lab_location(readings: list[int]) -> int:
    # your code here

    return 0 # change this!

if __name__ == "__main__":
    # sample cases
    assert lab_location([100, 90, 85] + [85] * 355 + [90, 98]) == 0
    assert lab_location([70] * 4 + [70, 80, 90, 89, 70, 20, 70] + [70] * 349) == 7
