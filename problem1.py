

def warm_up() -> None:
    pass # your code here!


if __name__ == "__main__":
    # sample cases -- you can modify, remove, or leave these statements in

    print("Testing first print statement...\n")
    # we use __import__ to prevent issues if the import statement at the top is deleted
    with __import__("contextlib").redirect_stdout(__import__("io").StringIO()) as f:
        warm_up()
    s = f.getvalue()
    print(s)

    assert s.split("\n")[0] == "l3tz dooo this"
    print("Passed!")

