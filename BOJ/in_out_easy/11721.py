def slice_string(string, d):
    for i in range(0, len(string), d):
        print(string[i : i + d])


string = input()
slice_string(string, 10)
