# Task-Tracker-DICT-AKLAN-webinar

A local Python **Task Tracker** application available in both a **Modern iOS-Inspired Desktop GUI** (`PyQt6`) and a **Beginner-Readable Terminal CLI** (`basic.py` / `tracker.py --cli`), built for the DICT Aklan Python Webinar.

---

## Features

- **Add, Edit, Complete, Delete, and List Tasks:** Track task descriptions, completion status (`Pending` / `Completed`), priority (`Low`, `Medium`, `High`), and scheduled **Date & Time**.
- **Modern iOS-Inspired Desktop UI (`tracker.py`):**
  - **Poppins Typography** with a clean, solid-color Apple-inspired Light & Dark color system (no gradients, no emojis).
  - **Phosphor Icons Only:** Crisp vector icons rendered via `QSvgRenderer`.
  - **Circular Blur Theme Transition:** Top-right icon-only theme switcher (`Sun` / `Moon`) with an expanding circular-blur reveal animation (`700ms`, `cubic-bezier(0.4, 0, 0.2, 1)`).
  - **In-Table Filter Tabs & Pagination:** Filter by **All Tasks**, **Pending**, or **Completed** directly inside the data table header and navigate pages (`6` entries per page) in the table footer.
  - **1st-Column Radio Toggle & Row Actions:** Quick completion toggle in the first column and **Edit** (`PencilSimple`) + **Delete** (`Trash`) action buttons in the last column.
  - **Modern Create / Edit Modal:** `20px`-rounded modal dialog with a custom iOS-inspired Date picker and AM/PM Time picker.
- **Local JSON Persistence (`tasks.json`):** Automatically saves and loads tasks locally while handling missing or malformed JSON files gracefully.
- **Robust Input Validation:** Rejects blank descriptions after trimming whitespace and validates numeric task IDs and valid index ranges.

---

## Project Structure

| File | Description |
|---|---|
| `tracker.py` | Modern iOS-inspired `PyQt6` desktop application (also supports `--cli` mode) |
| `basic.py` | Standalone, beginner-readable terminal CLI task tracker (standard library only) |
| `unittesting.py` | Unit tests verifying task formatting, input validation, editing, and JSON error handling |
| `instructions.md` | Core project user needs, features, data model, and constraints |
| `criteria.md` | Acceptance criteria for menu flow, validation, and JSON persistence |
| `architecture.md` | Overview of core functions (`main`, `load_tasks`, `save_tasks`, `add_task`, `list_tasks`, `complete_task`, `delete_task`) |
| `code_review.md` | Checklist for reviewing AI-generated code (Correctness, Readability, Robustness, Security, Maintainability, Verification) |
| `practice1.md` | Prediction & explanation exercises on Python conditionals, loops, `return` vs. `print`, and invalid input |
| `post_test.md` | Post-test assessment questions and answer key |
| `extensions.md` | Beginner, Intermediate, Advanced, API, and Deployment extension roadmap |
| `skill.md` | Python Modern iOS-Inspired UI/UX design system specification |
| `Orbiting Package Tracker Icon.png` | Application window and header brand logo |

---

## Getting Started

### 1. Run the Modern Desktop GUI (`tracker.py`)

Make sure `PyQt6` is installed in your Python environment:

```powershell
pip install PyQt6
python tracker.py
```

### 2. Run the Terminal CLI Version

You can run the zero-dependency terminal version directly with `basic.py` or via the `--cli` flag on `tracker.py`:

```powershell
python basic.py
# or
python tracker.py --cli
```

### 3. Run the Unit Tests

```powershell
python -m unittest unittesting.py
```

---

## Security & Demo Note

Data is stored locally in `tasks.json`. Do not store sensitive personal information or credentials in this local demo.
