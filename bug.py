def function_with_unclosed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    # Missing f.close() or with statement to close the file properly
    # ... more code ...

function_with_unclosed_file("my_file.txt")