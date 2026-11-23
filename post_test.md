# Post-test | check what you learned

- **1. Which operator compares equality in Python?**
- **2. Why use functions in an application?**
- **3. Name two invalid-input tests for the Task Tracker.**
- **4. What should you do before trusting AI-generated code?**
- **5. Give one safe practice for protecting credentials or personal data.**

---

## Answer Key (Bullet Summary)

- **1. Equality operator in Python:** The `==` operator compares whether two values are equal (whereas a single `=` is used for variable assignment).
- **2. Why use functions in an application:** Functions organize code into reusable, named blocks with a single responsibility (`add_task`, `load_tasks`, `save_tasks`), making the program easier to read, test, debug, and maintain without duplicating logic.
- **3. Two invalid-input tests for the Task Tracker:**
  - Entering a blank or whitespace-only task description (`"   "`) to verify it is rejected after trimming.
  - Entering a non-numeric task ID (`"abc"`) or an out-of-range task number (`"9"` or `"0"`) when completing/deleting a task (or an invalid menu choice like `"9"`), verifying the app shows a helpful message instead of crashing.
- **4. What to do before trusting AI-generated code:** Review and verify the code against every acceptance criterion—check its **correctness**, **readability** (make sure you can explain each function), **robustness** on unexpected inputs, **security**, and **run the program and unit tests** in a safe environment.
- **5. One safe practice for protecting credentials or personal data:** Never hardcode secrets, API keys, or sensitive personal data in source code or commit them to plain local files/repositories (use environment variables, secret managers, `.gitignore`, and keep demo data non-sensitive).
