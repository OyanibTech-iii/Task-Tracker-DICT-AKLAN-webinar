import unittest
from pathlib import Path

import tracker


def format_task(description, done=False):
    marker = "x" if done else " "
    return f"[{marker}] {description}"


class TestFormatTask(unittest.TestCase):
    def test_open_task(self):
        self.assertEqual(format_task("Study Python"), "[ ] Study Python")

    def test_completed_task(self):
        self.assertEqual(format_task("Study Python", True), "[x] Study Python")


class TestTaskTrackerLogic(unittest.TestCase):
    def test_reject_blank_description_after_trimming(self):
        ok, msg, task = tracker.validate_and_create_task("    ", "medium")
        self.assertFalse(ok)
        self.assertIsNone(task)
        self.assertEqual(msg, "Description cannot be blank.")

    def test_valid_task_creation(self):
        ok, msg, task = tracker.validate_and_create_task("  Review code  ", "HIGH")
        self.assertTrue(ok)
        self.assertEqual(
            task,
            {"description": "Review code", "done": False, "priority": "high"},
        )

    def test_validate_task_number_ranges(self):
        tasks = [{"description": "Task 1", "done": False, "priority": "low"}]
        ok_alpha, _, _ = tracker.validate_task_number(tasks, "abc")
        ok_zero, _, _ = tracker.validate_task_number(tasks, "0")
        ok_oob, _, _ = tracker.validate_task_number(tasks, "9")
        ok_valid, _, num = tracker.validate_task_number(tasks, "1")

        self.assertFalse(ok_alpha)
        self.assertFalse(ok_zero)
        self.assertFalse(ok_oob)
        self.assertTrue(ok_valid)
        self.assertEqual(num, 1)

    def test_malformed_json_handled_gracefully(self):
        temp_file = Path("temp_malformed_test.json")
        try:
            temp_file.write_text("{not valid json", encoding="utf-8")
            loaded = tracker.load_tasks(temp_file)
            self.assertEqual(loaded, [])
        finally:
            temp_file.unlink(missing_ok=True)

    def test_create_with_date_time_and_edit_task(self):
        ok, _, task = tracker.validate_and_create_task(
            "Ship release", "high", date_str="2026-11-23", time_str="04:30 PM"
        )
        self.assertTrue(ok)
        self.assertEqual(task["date"], "2026-11-23")
        self.assertEqual(task["time"], "04:30 PM")

        tasks = [task]
        ok_edit, _ = tracker.edit_task(
            tasks, "1", "Ship release v2", "low", "2026-11-24", "09:00 AM"
        )
        self.assertTrue(ok_edit)
        self.assertEqual(tasks[0]["description"], "Ship release v2")
        self.assertEqual(tasks[0]["priority"], "low")
        self.assertEqual(tasks[0]["date"], "2026-11-24")
        self.assertEqual(tasks[0]["time"], "09:00 AM")


if __name__ == "__main__":
    unittest.main()
