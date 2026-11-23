def format_task(description, done=False):

    marker = "x" if done else " "

    return f"[{marker}] {description}"

 

print(format_task("Study Python"))

print(format_task("Review code", True))