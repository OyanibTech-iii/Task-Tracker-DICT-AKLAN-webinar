# Python Practice 1: Predictions & Explanations

Before checking the answers for each question below, write down your **Prediction** and **Explanation** first.

---

## Question 1: Conditionals (`>=`)

**Prompt:** What is printed when `score = 75` and the condition is `score >= 75`?

```python
score = 75
if score >= 75:
    print("Passed")
else:
    print("Try again")
```

### Your Turn
- **Prediction:** *(What do you think will be printed?)*
- **Explanation:** *(Why does the condition evaluate that way?)*

<details>
<summary><strong>Reveal Answer</strong></summary>

- **Answer:** `"Passed"` (the code inside the `if` block is printed).
- **Explanation:** The `>=` operator means **"greater than or equal to"**. Since `score` is `75`, and `75` is equal to `75`, the condition `75 >= 75` evaluates to `True`, executing the `if` branch.

</details>

---

## Question 2: Looping Over an Empty List

**Prompt:** What happens when a loop receives an empty list?

```python
tasks = []
for task in tasks:
    print(f"- {task}")
print("Done")
```

### Your Turn
- **Prediction:** *(How many times will the loop run, and what will happen?)*
- **Explanation:** *(Why does Python handle an empty list this way?)*

<details>
<summary><strong>Reveal Answer</strong></summary>

- **Answer:** The loop body does not run at all (zero iterations). No error is raised, and Python immediately moves on to the code after the loop (printing `"Done"`).
- **Explanation:** A `for` loop runs once for each item in the collection. Because an empty list `[]` contains `0` items, there is nothing to iterate over, so the loop finishes immediately and safely. In a task tracker app, it is common to check `if not tasks:` first so you can display a friendly message like `"No tasks yet."`

</details>

---

## Question 3: `return` vs. `print`

**Prompt:** How is `return` different from `print`?

```python
def format_with_print(task):
    print(f"[ ] {task}")

def format_with_return(task):
    return f"[ ] {task}"
```

### Your Turn
- **Prediction:** *(What happens if you assign the result of each function to a variable, e.g., `result = ...`?)*
- **Explanation:** *(What is the difference between showing text on screen and sending data back to the caller?)*

<details>
<summary><strong>Reveal Answer</strong></summary>

- **Answer:**
  - `print()` displays text on the terminal screen for a human to read, but it does **not** hand a value back to the code (a function that only uses `print` returns `None`).
  - `return` exits the function and sends a value back to the caller so the rest of the program can store it in a variable, pass it to another function, test it, or print it later.
- **Explanation:** If you run `result = format_with_print("Study")`, `" [ ] Study"` appears on screen immediately, but `result` is `None`. If you run `result = format_with_return("Study")`, nothing is printed automatically, and `result` stores the string `"[ ] Study"` for later use.

</details>

---

## Question 4: Handling Invalid Menu Input

**Prompt:** What should the app do if the user enters menu choice `9` (when valid choices are, for example, `1`–`5`)?

### Your Turn
- **Prediction:** *(What should the user see, and what should the program do next?)*
- **Explanation:** *(Why is this important according to our project constraints?)*

<details>
<summary><strong>Reveal Answer</strong></summary>

- **Answer:** The app should **not crash**. It should print a clear, friendly message (such as `"Invalid choice. Please enter a valid option."`) and keep the main menu loop running so the user can try again.
- **Explanation:** One of our core constraints in `instructions.md` is **"handle invalid input."** Using an `else:` branch in the menu's `if / elif / else` structure catches any unrecognized input (like `9`, `abc`, or an empty press of Enter) gracefully without losing the user's unsaved tasks.

</details>

---

## Answer Key (Bullet Summary)

- **When `score = 75` and condition is `score >= 75`:** The condition evaluates to `True` because `>=` includes equality (`75` is equal to `75`), so the `if` branch runs and prints its output (e.g., `"Passed"`).
- **When a loop receives an empty list:** The loop body executes `0` times (it is skipped entirely without raising an error), and the program continues directly to the next line after the loop.
- **How `return` is different from `print`:** `print` only displays text on the terminal screen (and returns `None`), whereas `return` exits the function and sends a value back to the caller so it can be stored in a variable or reused in code.
- **When the user enters menu choice `9`:** The app should catch the unrecognized option with an `else` branch, print a friendly `"Invalid choice"` message without crashing, and return to the menu prompt so the user can try again.

