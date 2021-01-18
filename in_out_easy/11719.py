while True:
    try:
        string = input()
        print(string)
    except EOFError:
        break