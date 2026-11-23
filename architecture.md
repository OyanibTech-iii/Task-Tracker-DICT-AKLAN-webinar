# Project architecture

- **`main()`:** controls the menu and connects the actions.
- **`load_tasks()` / `save_tasks()`:** read and write local JSON.
- **`add_task()`:** collects and validates a description and priority.
- **`list_tasks()`:** displays records consistently.
- **`complete_task()` / `delete_task()`:** validate task numbers before modifying data.
- Data stays local; do not store sensitive personal information in this demo.
