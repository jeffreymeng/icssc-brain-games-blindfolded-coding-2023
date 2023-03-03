
def rewire_elevator(floors: list[int]) -> list[int]:
    rewired_floors = [-3, -2, -1] + floors[3: -1]
    return rewired_floors + [sum(floors) - sum(rewired_floors)]


if __name__ == "__main__":
    # sample cases -- you can modify this code if you want to.
    # if you pass both of these test cases (without modifying them), then you will pass at least 2/10
    # of the scored test cases.

    print("Running sample case 1...", end="")

    case1_input = [-1, 1, 2, 3, 4, 5]
    case1_output = rewire_elevator(case1_input)
    assert case1_output[2] == -1, "The third element must take you to floor -1"
    assert sum(case1_output) == sum(case1_input), "The sum of the floors must not change"
    assert len(set(case1_output)) == len(case1_output), "There must not be any duplicate floors in your output"

    print("Passed!")
    print("Running sample case 2...", end="")

    case2_input = [-1, 1, 2, 3]
    case2_output = rewire_elevator(case2_input)
    assert case2_output[2] == -1, "The third element must take you to floor -1"
    assert sum(case2_output) == sum(case2_input), "The sum of the floors must not change"
    assert len(set(case2_output)) == len(case2_output), "There must not be any duplicate floors in your output"

    print("Passed!")