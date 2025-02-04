# Unclosed File Resource Leak in Python
This repository demonstrates a common, yet easily missed error in Python: not properly closing files after use.

The `bug.py` file shows a function that opens a file but fails to close it. This can lead to resource exhaustion, especially in applications that open many files.

The `bugSolution.py` file shows how to fix the issue using a `with` statement which automatically handles file closing, even if exceptions are raised.