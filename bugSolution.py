def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

function_with_closed_file("my_file.txt")
#The with statement ensures the file is automatically closed, even if exceptions occur.