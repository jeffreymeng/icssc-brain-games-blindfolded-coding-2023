def largest_color(colors: list[list[int]]) -> int:
    pass # code here!



if __name__ == "__main__":
    # sample cases

    print("Testing sample case 1...", end="")
    input1 = [[1, 1, 2, 2, 2],
                      [3, 1, 1, 1, 2],
                      [3, 3, 1, 4, 4]
                      ]
    output1 = 6
    try:
        assert largest_color(input1) == output1
    except AssertionError:
        print("\nCase 1 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(largest_color(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")

    print("Testing sample case 2...", end="")
    input2 = [[1, 1, 2, 2, 2],
              [3, 1, 1, 1, 2],
              [3, 3, 1, 4, 2],
              [3, 3, 4, 4, 2],
              [1, 1, 1, 2, 2]
              ]
    output2 = 8
    try:
        assert sorted(largest_color(input2)) == output2
    except AssertionError:
        print("\nCase 2 was not correct")
        print("Expected: ", repr(output2))
        print("Your answer: ", repr(largest_color(input2)))
    except Exception as e:
        raise e
    else:
        print("Passed!")
