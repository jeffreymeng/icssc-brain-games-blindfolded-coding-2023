
def warm_up() -> None:
    print("l3tz dooo this")
    print(23 ** 5)
    print("there they're their it's ok")
    print('"')
    print("a double quote")
    print("bob then the words a quote then an actual quote")
    print("hi wait you typed it wrong go back two characters ok this time you really did type it wrong press delete stop")
    print(max(248 ** 30, 4 ** 200, 45 ** 45))


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

