def largest_color(colors: list[list[int]]) -> int:
    counted = [[False for _ in row] for row in colors]
    max_count = 0
    for row in range(len(colors)):
        for col in range(len(colors[0])):
            if counted[row][col]:
                continue
            max_count = max(max_count, count_color_matches(colors, counted, row, col, colors[row][col]))
    return max_count

def count_color_matches(colors, counted, row, col, target_color):
    if row < 0 or row >= len(colors) or col < 0 or col >= len(colors[0]):
        # invalid indices
        return 0

    if counted[row][col] or colors[row][col] != target_color:
        return 0

    counted[row][col] = True

    count = 1
    count += count_color_matches(colors, counted, row - 1, col, target_color)
    count += count_color_matches(colors, counted, row + 1, col, target_color)
    count += count_color_matches(colors, counted, row, col - 1, target_color)
    count += count_color_matches(colors, counted, row, col + 1, target_color)

    return count




if __name__ == "__main__":
    # sample cases

    print("Testing sample case 1...", end="")
    input1 = [[1, 1, 2, 2, 2],
              [3, 1, 1, 1, 2],
              [3, 3, 1, 4, 4]]
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
        assert largest_color(input2)  == output2
    except AssertionError:
        print("\nCase 2 was not correct")
        print("Expected: ", repr(output2))
        print("Your answer: ", repr(largest_color(input2)))
    except Exception as e:
        raise e
    else:
        print("Passed!")
