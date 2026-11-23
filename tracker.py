"""
Task Tracker Desktop Application
Built according to the Python Modern iOS-Inspired UI/UX Design System (skill.md)
and fulfilling all functional & acceptance criteria (instructions.md, criteria.md, architecture.md).
"""

import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from PyQt6.QtCore import (
    QByteArray,
    QDate,
    QEasingCurve,
    QEvent,
    QPoint,
    QPointF,
    QRectF,
    QSize,
    QTime,
    Qt,
    QTimer,
    QVariantAnimation,
)
from PyQt6.QtGui import (
    QColor,
    QFont,
    QIcon,
    QPainter,
    QPainterPath,
    QPixmap,
)
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QDialog,
    QFrame,
    QGraphicsBlurEffect,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

# ============================================================================
# 1. CENTRALIZED DESIGN TOKENS (from skill.md Sections 3, 4, 5, 6)
# ============================================================================

LIGHT_THEME: Dict[str, str] = {
    "primary": "#007AFF",
    "primary_hover": "#0062CC",
    "primary_pressed": "#004C9E",
    "background": "#F5F5F7",
    "surface": "#FFFFFF",
    "surface_hover": "#F0F0F5",
    "surface_pressed": "#E4E4EB",
    "text": "#1D1D1F",
    "secondary_text": "#86868B",
    "border": "#E5E5EA",
    "border_hover": "#C7C7CC",
    "success": "#34C759",
    "success_bg": "#EAF9EE",
    "warning": "#FF9F0A",
    "warning_bg": "#FFF5E5",
    "danger": "#FF3B30",
    "danger_hover": "#E03025",
    "danger_pressed": "#C2251B",
    "danger_bg": "#FFECEB",
    "danger_bg_hover": "#FFDAD7",
    "nav_active_bg": "#E8F2FF",
    "nav_active_hover": "#D4E7FF",
}

DARK_THEME: Dict[str, str] = {
    "primary": "#0A84FF",
    "primary_hover": "#3399FF",
    "primary_pressed": "#0069D9",
    "background": "#000000",
    "surface": "#1C1C1E",
    "surface_hover": "#2C2C2E",
    "surface_pressed": "#3A3A3C",
    "text": "#FFFFFF",
    "secondary_text": "#98989D",
    "border": "#38383A",
    "border_hover": "#545458",
    "success": "#30D158",
    "success_bg": "#12321B",
    "warning": "#FFD60A",
    "warning_bg": "#332B05",
    "danger": "#FF453A",
    "danger_hover": "#FF6259",
    "danger_pressed": "#D9342B",
    "danger_bg": "#361514",
    "danger_bg_hover": "#4D1E1C",
    "nav_active_bg": "#132A42",
    "nav_active_hover": "#1A3A5C",
}

RADIUS: Dict[str, int] = {
    "small_button": 8,
    "button": 10,
    "input": 10,
    "card": 14,
    "floating": 16,
    "panel": 18,
    "modal": 20,
    "pill": 999,
}

SPACING: Dict[str, int] = {
    "xs": 4,
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 24,
    "xxl": 32,
    "xxxl": 48,
}

FONT_FAMILIES = "Poppins, SF Pro Display, SF Pro Text, Inter, Segoe UI, Arial"

# ============================================================================
# 2. PHOSPHOR ICONS (Official 256x256 SVG paths — skill.md Section 10)
#    Strictly NO emojis, NO gradients, Phosphor Icons ONLY.
# ============================================================================

PHOSPHOR_SVGS: Dict[str, str] = {
    "SquaresFour": (
        '<path d="M104,40H56A16,16,0,0,0,40,56v48a16,16,0,0,0,16,16h48a16,16,0,0,0,16-16V56A16,16,0,0,0,104,40Zm0,64H56V56h48v48Zm96-64H152a16,16,0,0,0-16,16v48a16,16,0,0,0,16,16h48a16,16,0,0,0,16-16V56A16,16,0,0,0,200,40Zm0,64H152V56h48v48Zm-96,32H56a16,16,0,0,0-16,16v48a16,16,0,0,0,16,16h48a16,16,0,0,0,16-16V152A16,16,0,0,0,104,136Zm0,64H56V152h48v48Zm96-64H152a16,16,0,0,0-16,16v48a16,16,0,0,0,16,16h48a16,16,0,0,0,16-16V152A16,16,0,0,0,200,136Zm0,64H152V152h48v48Z"/>'
    ),
    "Plus": (
        '<path d="M224,128a8,8,0,0,1-8,8H136v80a8,8,0,0,1-16,0V136H40a8,8,0,0,1,0-16h80V40a8,8,0,0,1,16,0v80h80A8,8,0,0,1,224,128Z"/>'
    ),
    "PencilSimple": (
        '<path d="M227.31,73.37,182.63,28.68a16,16,0,0,0-22.63,0L36.69,152A15.86,15.86,0,0,0,32,163.31V208a16,16,0,0,0,16,16H92.69A15.86,15.86,0,0,0,104,219.31L227.31,96a16,16,0,0,0,0-22.63ZM92.69,208H48V163.31l88-88L180.69,120ZM192,108.68,147.31,64l24-24L216,84.68Z"/>'
    ),
    "Trash": (
        '<path d="M216,48H176V40a24,24,0,0,0-24-24H104A24,24,0,0,0,80,40v8H40a8,8,0,0,0,0,16h8V208a16,16,0,0,0,16,16H192a16,16,0,0,0,16-16V64h8a8,8,0,0,0,0-16ZM96,40a8,8,0,0,1,8-8h48a8,8,0,0,1,8,8v8H96Zm96,168H64V64H192ZM112,104v64a8,8,0,0,1-16,0V104a8,8,0,0,1,16,0Zm48,0v64a8,8,0,0,1-16,0V104a8,8,0,0,1,16,0Z"/>'
    ),
    "CheckCircleFill": (
        '<path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm45.66,85.66-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35a8,8,0,0,1,11.32,11.32Z"/>'
    ),
    "CheckCircle": (
        '<path d="M173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34ZM232,128A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88,88,0,1,0-88,88A88.1,88.1,0,0,0,216,128Z"/>'
    ),
    "Circle": (
        '<path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Z"/>'
    ),
    "MagnifyingGlass": (
        '<path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"/>'
    ),
    "Database": (
        '<path d="M128,24C74.17,24,32,48.6,32,80v96c0,31.4,42.17,56,96,56s96-24.6,96-56V80C224,48.6,181.83,24,128,24Zm80,104c0,19.85-34.09,40-80,40s-80-20.15-80-40V101.29c17.06,13.38,46.29,26.71,80,26.71s62.94-13.33,80-26.71ZM128,40c45.91,0,80,20.15,80,40s-34.09,40-80,40S48,99.85,48,80,82.09,40,128,40Zm0,176c-45.91,0-80-20.15-80-40V149.29c17.06,13.38,46.29,26.71,80,26.71s62.94-13.33,80-26.71V176C208,195.85,173.91,216,128,216Z"/>'
    ),
    "CalendarBlank": (
        '<path d="M208,32H184V24a8,8,0,0,0-16,0v8H88V24a8,8,0,0,0-16,0v8H48A16,16,0,0,0,32,48V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V48A16,16,0,0,0,208,32ZM72,48v8a8,8,0,0,0,16,0V48h80v8a8,8,0,0,0,16,0V48h24V80H48V48ZM208,208H48V96H208V208Z"/>'
    ),
    "Clock": (
        '<path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm64-88a8,8,0,0,1-8,8H128a8,8,0,0,1-8-8V72a8,8,0,0,1,16,0v48h48A8,8,0,0,1,192,128Z"/>'
    ),
    "Gear": (
        '<path d="M128,80a48,48,0,1,0,48,48A48.05,48.05,0,0,0,128,80Zm0,80a32,32,0,1,1,32-32A32,32,0,0,1,128,160ZM232.92,140.84l-14.6-25.29a104.58,104.58,0,0,0,0-23.1l14.6-25.29a8,8,0,0,0-2.93-10.93l-26.35-15.2a8,8,0,0,0-10.92,2.93L178.13,69.25a99.2,99.2,0,0,0-20-11.55V28.52a8,8,0,0,0-8-8H119.88a8,8,0,0,0-8,8V57.7a99.2,99.2,0,0,0-20,11.55L77.28,43.96a8,8,0,0,0-10.92-2.93L40,56.23a8,8,0,0,0-2.93,10.93l14.6,25.29a104.58,104.58,0,0,0,0,23.1L37.08,140.84A8,8,0,0,0,40,151.77l26.35,15.2a8,8,0,0,0,10.92-2.93l14.61-25.29a99.2,99.2,0,0,0,20,11.55v29.18a8,8,0,0,0,8,8h30.24a8,8,0,0,0,8-8V150.3a99.2,99.2,0,0,0,20-11.55l14.61,25.29a8,8,0,0,0,10.92,2.93l26.35-15.2A8,8,0,0,0,232.92,140.84Z"/>'
    ),
    "SignOut": (
        '<path d="M112,216a8,8,0,0,1-8,8H48a16,16,0,0,1-16-16V48A16,16,0,0,1,48,32h56a8,8,0,0,1,0,16H48V208h56A8,8,0,0,1,112,216Zm109.66-93.66-40-40a8,8,0,0,0-11.32,11.32L196.69,120H104a8,8,0,0,0,0,16h92.69l-26.35,26.34a8,8,0,0,0,11.32,11.32l40-40A8,8,0,0,0,221.66,122.34Z"/>'
    ),
    "WarningCircle": (
        '<path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm-8-80V80a8,8,0,0,1,16,0v56a8,8,0,0,1-16,0Zm20,36a12,12,0,1,1-12-12A12,12,0,0,1,140,172Z"/>'
    ),
    "Folder": (
        '<path d="M216,72H131.31L104,44.69A15.86,15.86,0,0,0,92.69,40H40A16,16,0,0,0,24,56V200.62A15.4,15.4,0,0,0,39.38,216H216.89A15.13,15.13,0,0,0,232,200.89V88A16,16,0,0,0,216,72ZM40,56H92.69l16,16H40ZM216,200H40V88H216Z"/>'
    ),
    "Sun": (
        '<path d="M120,40V16a8,8,0,0,1,16,0V40a8,8,0,0,1-16,0Zm72,88a64,64,0,1,1-64-64A64.07,64.07,0,0,1,192,128Zm-16,0a48,48,0,1,0-48,48A48.05,48.05,0,0,0,176,128ZM58.34,69.66A8,8,0,0,0,69.66,58.34l-16-16A8,8,0,0,0,42.34,53.66Zm0,116.68-16,16a8,8,0,0,0,11.32,11.32l16-16a8,8,0,0,0-11.32-11.32ZM192,72a8,8,0,0,0,5.66-2.34l16-16a8,8,0,0,0-11.32-11.32l-16,16A8,8,0,0,0,192,72Zm5.66,114.34a8,8,0,0,0-11.32,11.32l16,16a8,8,0,0,0,11.32-11.32ZM48,128a8,8,0,0,0-8-8H16a8,8,0,0,0,0,16H40A8,8,0,0,0,48,128Zm80,80a8,8,0,0,0-8,8v24a8,8,0,0,0,16,0V216A8,8,0,0,0,128,208Zm112-88H216a8,8,0,0,0,0,16h24a8,8,0,0,0,0-16Z"/>'
    ),
    "Moon": (
        '<path d="M233.54,142.23a8,8,0,0,0-8-2,88.08,88.08,0,0,1-109.8-109.8,8,8,0,0,0-10-10,104.84,104.84,0,0,0-52.91,37A104,104,0,0,0,136,224a103.09,103.09,0,0,0,62.52-20.88,104.84,104.84,0,0,0,37-52.91A8,8,0,0,0,233.54,142.23ZM188.9,190.34A88,88,0,0,1,65.66,67.11a89,89,0,0,1,31.4-26A106,106,0,0,0,96,56,104.11,104.11,0,0,0,200,160a106,106,0,0,0,14.92-1.06A89,89,0,0,1,188.9,190.34Z"/>'
    ),
    "CaretLeft": (
        '<path d="M165.66,202.34a8,8,0,0,1-11.32,11.32l-80-80a8,8,0,0,1,0-11.32l80-80a8,8,0,0,1,11.32,11.32L91.31,128Z"/>'
    ),
    "CaretRight": (
        '<path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"/>'
    ),
    "CaretUp": (
        '<path d="M213.66,165.66a8,8,0,0,1-11.32,0L128,91.31,53.66,165.66a8,8,0,0,1-11.32-11.32l80-80a8,8,0,0,1,11.32,0l80,80A8,8,0,0,1,213.66,165.66Z"/>'
    ),
    "CaretDown": (
        '<path d="M213.66,101.66l-80,80a8,8,0,0,1-11.32,0l-80-80A8,8,0,0,1,53.66,90.34L128,164.69l74.34-74.35a8,8,0,0,1,11.32,11.32Z"/>'
    ),
}


def render_phosphor_pixmap(name: str, color: str, size: int = 20) -> QPixmap:
    """Render a Phosphor SVG icon to a crisp high-DPI QPixmap."""
    inner = PHOSPHOR_SVGS.get(name, PHOSPHOR_SVGS["Circle"])
    svg_xml = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" '
        f'fill="{color}">{inner}</svg>'
    )
    renderer = QSvgRenderer(QByteArray(svg_xml.encode("utf-8")))
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    renderer.render(painter, QRectF(0, 0, size, size))
    painter.end()
    return pixmap


def render_phosphor_icon(name: str, color: str, size: int = 20) -> QIcon:
    """Wrap a rendered Phosphor pixmap in a QIcon."""
    return QIcon(render_phosphor_pixmap(name, color, size))


def blur_pixmap(source: QPixmap, blur_radius: float) -> QPixmap:
    """Apply a fast downscale-upscale Gaussian approximation to a QPixmap (High-DPI safe)."""
    if blur_radius <= 0.5 or source.isNull():
        return source
    dpr = source.devicePixelRatio()
    logical_w = max(1, int(source.width() / dpr))
    logical_h = max(1, int(source.height() / dpr))
    scale_factor = max(2, int(blur_radius * 0.9))
    small_w = max(1, logical_w // scale_factor)
    small_h = max(1, logical_h // scale_factor)

    small = source.scaled(
        small_w,
        small_h,
        Qt.AspectRatioMode.IgnoreAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )
    blurred = small.scaled(
        source.width(),
        source.height(),
        Qt.AspectRatioMode.IgnoreAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )
    blurred.setDevicePixelRatio(dpr)
    return blurred


# ============================================================================
# 3. CORE BUSINESS LOGIC & PERSISTENCE (architecture.md & criteria.md)
#    Kept cleanly separated from UI components so functions can be tested
#    directly and reused by both CLI and GUI modes.
# ============================================================================

DATA_FILE = Path("tasks.json")
LOGO_FILE = Path(__file__).resolve().parent / "Orbiting Package Tracker Icon.png"
VALID_PRIORITIES = ("low", "medium", "high")


def load_tasks(file_path: Path = DATA_FILE) -> List[Dict[str, object]]:
    """Read tasks from local JSON file; handle missing or malformed files gracefully."""
    if not file_path.exists():
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                print("Warning: tasks.json root is not a list. Starting empty.")
                return []
            valid_tasks: List[Dict[str, object]] = []
            for item in data:
                if isinstance(item, dict) and str(item.get("description", "")).strip():
                    priority = str(item.get("priority", "medium")).strip().lower()
                    if priority not in VALID_PRIORITIES:
                        priority = "medium"
                    task_entry: Dict[str, object] = {
                        "description": str(item["description"]).strip(),
                        "done": bool(item.get("done", False)),
                        "priority": priority,
                    }
                    if "date" in item and str(item["date"]).strip():
                        task_entry["date"] = str(item["date"]).strip()
                    if "time" in item and str(item["time"]).strip():
                        task_entry["time"] = str(item["time"]).strip()
                    valid_tasks.append(task_entry)
            return valid_tasks
    except (json.JSONDecodeError, OSError):
        print("Warning: Malformed or unreadable tasks.json. Starting with an empty list.")
        return []


def save_tasks(tasks: List[Dict[str, object]], file_path: Path = DATA_FILE) -> bool:
    """Write tasks to local JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=2)
        return True
    except OSError as error:
        print(f"Error saving tasks: {error}")
        return False


def validate_and_create_task(
    description: str,
    priority: str = "medium",
    date_str: Optional[str] = None,
    time_str: Optional[str] = None,
) -> Tuple[bool, str, Optional[Dict[str, object]]]:
    """Validate description (reject blank after trimming), priority, and optional date/time."""
    cleaned = description.strip()
    if not cleaned:
        return False, "Description cannot be blank.", None

    cleaned_priority = priority.strip().lower() if priority else "medium"
    if cleaned_priority not in VALID_PRIORITIES:
        return False, "Priority must be low, medium, or high.", None

    task: Dict[str, object] = {
        "description": cleaned,
        "done": False,
        "priority": cleaned_priority,
    }
    if date_str is not None and str(date_str).strip():
        task["date"] = str(date_str).strip()
    if time_str is not None and str(time_str).strip():
        task["time"] = str(time_str).strip()

    return True, f"Added task: '{cleaned}'.", task


def validate_task_number(tasks: List[Dict[str, object]], raw_number: str):
    """Validate that raw_number is a whole number within 1..len(tasks)."""
    cleaned = str(raw_number).strip()
    if not cleaned.isdigit():
        return False, "Enter a whole-number task number.", None

    number = int(cleaned)
    if not 1 <= number <= len(tasks):
        return False, "That task number does not exist.", None

    return True, "", number


def edit_task(
    tasks: List[Dict[str, object]],
    raw_number: str,
    description: str,
    priority: str = "medium",
    date_str: Optional[str] = None,
    time_str: Optional[str] = None,
) -> Tuple[bool, str]:
    """Validate task ID and update description, priority, date, and time."""
    ok_num, msg_num, number = validate_task_number(tasks, raw_number)
    if not ok_num or number is None:
        return False, msg_num

    ok_val, msg_val, validated = validate_and_create_task(
        description, priority, date_str, time_str
    )
    if not ok_val or validated is None:
        return False, msg_val

    target = tasks[number - 1]
    target["description"] = validated["description"]
    target["priority"] = validated["priority"]
    if "date" in validated:
        target["date"] = validated["date"]
    if "time" in validated:
        target["time"] = validated["time"]

    return True, f"Updated task #{number}: '{validated['description']}'."


def add_task(
    tasks: List[Dict[str, object]],
    description: Optional[str] = None,
    priority: Optional[str] = None,
) -> bool:
    """Add a task after trimming and validating description and priority."""
    if description is None:
        description = input("Task description: ")
    if priority is None:
        raw_p = input("Priority (low/medium/high) [medium]: ").strip().lower()
        priority = raw_p if raw_p else "medium"

    now = datetime.now()
    ok, msg, task = validate_and_create_task(
        description,
        priority,
        date_str=now.strftime("%Y-%m-%d"),
        time_str=now.strftime("%I:%M %p"),
    )
    if not ok or task is None:
        print(msg)
        return False

    tasks.append(task)
    print(msg)
    return True


def list_tasks(tasks: List[Dict[str, object]]) -> List[str]:
    """Format and display all tasks with task number, status, priority, and date/time."""
    if not tasks:
        print("No tasks yet.")
        return []

    lines: List[str] = []
    for index, task in enumerate(tasks, start=1):
        marker = "x" if task.get("done") else " "
        priority = str(task.get("priority", "medium")).lower()
        description = str(task.get("description", ""))
        dt_part = ""
        if task.get("date") or task.get("time"):
            dt_part = f" [{task.get('date', '')} {task.get('time', '')}]".rstrip()
        line = f"{index}. [{marker}] ({priority}) {description}{dt_part}"
        lines.append(line)
        print(line)
    return lines


def complete_task(
    tasks: List[Dict[str, object]], raw_number: Optional[str] = None
) -> bool:
    """Validate task ID and mark the task as completed."""
    if raw_number is None:
        raw_number = input("Task number: ")

    ok, msg, number = validate_task_number(tasks, raw_number)
    if not ok or number is None:
        print(msg)
        return False

    tasks[number - 1]["done"] = True
    print(f"Completed task #{number}: '{tasks[number - 1]['description']}'.")
    return True


def delete_task(
    tasks: List[Dict[str, object]], raw_number: Optional[str] = None
) -> bool:
    """Validate task ID and remove the task from the list."""
    if raw_number is None:
        raw_number = input("Task number: ")

    ok, msg, number = validate_task_number(tasks, raw_number)
    if not ok or number is None:
        print(msg)
        return False

    removed = tasks.pop(number - 1)
    print(f"Deleted task #{number}: '{removed['description']}'.")
    return True


# ============================================================================
# 4. CIRCULAR BLUR THEME TRANSITION OVERLAY (Ported from React beui-circle-blur)
# ============================================================================


class CircleBlurTransitionOverlay(QWidget):
    """
    Animates the new theme expanding from the top-right theme toggle button
    with a circular clip-path and a decaying blur filter (8px -> 0px) over 700ms
    with cubic-bezier(0.4, 0, 0.2, 1), matching the React `circle-blur` View Transition.
    """

    def __init__(
        self,
        parent: QWidget,
        old_pixmap: QPixmap,
        new_pixmap: QPixmap,
        origin: QPoint,
    ):
        super().__init__(parent)
        self.setGeometry(parent.rect())
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

        self.old_pixmap = old_pixmap
        self.new_pixmap = new_pixmap
        # Pre-compute blurred stages for smooth 60fps painting as blur decays 8px -> 0px
        self.blurred_heavy = blur_pixmap(new_pixmap, 10.0)
        self.blurred_mid = blur_pixmap(new_pixmap, 5.0)
        self.origin = QPointF(origin)

        # Maximum radius needed to cover the farthest corner from origin (150% reveal)
        w, h = float(self.width()), float(self.height())
        corners = [QPointF(0, 0), QPointF(w, 0), QPointF(0, h), QPointF(w, h)]
        self.max_radius = max(
            math.hypot(self.origin.x() - c.x(), self.origin.y() - c.y()) for c in corners
        ) * 1.05
        self.progress = 0.0

        # cubic-bezier(0.4, 0, 0.2, 1) over 700ms
        self.anim = QVariantAnimation(self)
        self.anim.setDuration(700)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        curve = QEasingCurve(QEasingCurve.Type.BezierSpline)
        curve.addCubicBezierSegment(
            QPointF(0.4, 0.0), QPointF(0.2, 1.0), QPointF(1.0, 1.0)
        )
        self.anim.setEasingCurve(curve)
        self.anim.valueChanged.connect(self._on_tick)
        self.anim.finished.connect(self._on_finished)
        self.on_finished_callback = None

    def start(self, on_finished=None) -> None:
        self.on_finished_callback = on_finished
        self.show()
        self.raise_()
        self.anim.start()

    def _on_finished(self) -> None:
        if callable(self.on_finished_callback):
            self.on_finished_callback()
        self.hide()
        self.deleteLater()

    def _on_tick(self, value) -> None:
        self.progress = float(value)
        self.update()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

        # 1. Draw old theme snapshot as base layer (::view-transition-old(root))
        painter.drawPixmap(0, 0, self.old_pixmap)

        # 2. Clip to expanding circle centered at origin (::view-transition-new(root))
        radius = max(1.0, self.progress * self.max_radius)
        clip_path = QPainterPath()
        clip_path.addEllipse(self.origin, radius, radius)
        painter.setClipPath(clip_path)

        # 3. Draw opaque new snapshot base, then overlay decaying blur (blur(8px) -> blur(0px))
        #    so the expanding circle is 100% solid (never semi-transparent).
        painter.setOpacity(1.0)
        painter.drawPixmap(0, 0, self.new_pixmap)
        if self.progress < 0.45:
            t_local = self.progress / 0.45
            painter.setOpacity(1.0 - t_local * 0.5)
            painter.drawPixmap(0, 0, self.blurred_heavy)
        elif self.progress < 0.85:
            t_local = (self.progress - 0.45) / 0.40
            painter.setOpacity(1.0 - t_local)
            painter.drawPixmap(0, 0, self.blurred_mid)

        # 4. Subtle soft rim along the expanding circle edge for a feathered blur reveal
        painter.setOpacity(1.0)
        painter.setClipping(False)
        rim_alpha = int(95 * (1.0 - self.progress))
        if rim_alpha > 4:
            pen_color = QColor(128, 128, 135, rim_alpha)
            painter.setPen(pen_color)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawEllipse(self.origin, radius, radius)

        painter.end()


# ============================================================================
# 5. MODERN iOS-INSPIRED UI COMPONENTS (skill.md Sections 7–14)
# ============================================================================


class ModernDatePicker(QFrame):
    """
    Modern iOS-inspired Date Input with a Phosphor CalendarBlank icon button
    and clean popup calendar (no old Windows 3D spinbox arrows).
    """

    def __init__(self, theme: Dict[str, str], parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.theme = theme
        self.setObjectName("ModernDateFrame")
        self.setFixedHeight(42)
        self._build_ui()

    def _build_ui(self) -> None:
        t = self.theme
        self.setStyleSheet(
            f"""
            QFrame#ModernDateFrame {{
                background-color: {t['surface']};
                border: 1px solid {t['border']};
                border-radius: {RADIUS['input']}px;
            }}
            QFrame#ModernDateFrame:hover {{
                background-color: {t['surface_hover']};
                border: 1px solid {t['border_hover']};
            }}
            """
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 8, 0)
        layout.setSpacing(6)

        cal_icon = QLabel()
        cal_icon.setFixedSize(18, 18)
        cal_icon.setPixmap(render_phosphor_pixmap("CalendarBlank", t["primary"], 18))
        cal_icon.setStyleSheet("background: transparent; border: none;")
        layout.addWidget(cal_icon)

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setStyleSheet(
            f"""
            QDateEdit {{
                background: transparent;
                color: {t['text']};
                border: none;
                font-size: 13px;
                font-weight: 600;
                padding: 0px;
            }}
            QDateEdit::drop-down {{
                border: none;
                background: transparent;
                width: 22px;
            }}
            QDateEdit::down-arrow {{
                image: none;
                width: 0px;
                height: 0px;
            }}
            """
        )
        layout.addWidget(self.date_edit, stretch=1)

        drop_lbl = QLabel()
        drop_lbl.setFixedSize(16, 16)
        drop_lbl.setPixmap(render_phosphor_pixmap("CaretDown", t["secondary_text"], 14))
        drop_lbl.setStyleSheet("background: transparent; border: none;")
        layout.addWidget(drop_lbl)

    def date(self) -> QDate:
        return self.date_edit.date()

    def setDate(self, d: QDate) -> None:
        self.date_edit.setDate(d)


class ModernTimePicker(QFrame):
    """
    Modern iOS-inspired Time Picker replacing old Windows 3D spin arrows.
    Features a Phosphor Clock icon, clean Hour & Minute selectors with wheel/click
    stepping, and a pill-style AM/PM toggle button.
    """

    def __init__(self, theme: Dict[str, str], parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.theme = theme
        now = QTime.currentTime()
        self._hour24 = now.hour()
        self._minute = now.minute()

        self.setObjectName("ModernTimeFrame")
        self.setFixedHeight(42)
        self._build_ui()
        self._sync_display()

    def _build_ui(self) -> None:
        t = self.theme
        self.setStyleSheet(
            f"""
            QFrame#ModernTimeFrame {{
                background-color: {t['surface']};
                border: 1px solid {t['border']};
                border-radius: {RADIUS['input']}px;
            }}
            QFrame#ModernTimeFrame:hover {{
                background-color: {t['surface_hover']};
                border: 1px solid {t['border_hover']};
            }}
            """
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 4, 6, 4)
        layout.setSpacing(4)

        # Phosphor Clock icon
        clock_icon = QLabel()
        clock_icon.setFixedSize(18, 18)
        clock_icon.setPixmap(render_phosphor_pixmap("Clock", t["primary"], 18))
        clock_icon.setStyleSheet("background: transparent; border: none;")
        layout.addWidget(clock_icon)

        # Hour dropdown (01..12)
        self.hour_combo = QComboBox()
        self.hour_combo.addItems([f"{h:02d}" for h in range(1, 13)])
        self.hour_combo.setCursor(Qt.CursorShape.PointingHandCursor)
        self.hour_combo.setFixedWidth(44)
        self.hour_combo.setFixedHeight(30)
        self.hour_combo.currentTextChanged.connect(self._on_parts_changed)

        # Colon separator
        colon_lbl = QLabel(":")
        colon_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        colon_lbl.setFixedWidth(8)
        colon_lbl.setStyleSheet(
            f"color: {t['text']}; font-size: 14px; font-weight: 700; background: transparent; border: none;"
        )

        # Minute dropdown (00..59)
        self.min_combo = QComboBox()
        self.min_combo.addItems([f"{m:02d}" for m in range(0, 60)])
        self.min_combo.setCursor(Qt.CursorShape.PointingHandCursor)
        self.min_combo.setFixedWidth(44)
        self.min_combo.setFixedHeight(30)
        self.min_combo.currentTextChanged.connect(self._on_parts_changed)

        combo_qss = f"""
            QComboBox {{
                background-color: {t['background']};
                color: {t['text']};
                border: none;
                border-radius: 6px;
                padding: 0 6px;
                font-size: 13px;
                font-weight: 600;
            }}
            QComboBox:hover {{
                background-color: {t['surface_pressed']};
            }}
            QComboBox::drop-down {{
                width: 0px;
                border: none;
            }}
            QComboBox::down-arrow {{
                image: none;
                width: 0px;
                height: 0px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {t['surface']};
                color: {t['text']};
                border: 1px solid {t['border']};
                border-radius: 8px;
                selection-background-color: {t['nav_active_bg']};
                selection-color: {t['primary']};
                outline: none;
            }}
        """
        self.hour_combo.setStyleSheet(combo_qss)
        self.min_combo.setStyleSheet(combo_qss)

        layout.addWidget(self.hour_combo)
        layout.addWidget(colon_lbl)
        layout.addWidget(self.min_combo)
        layout.addStretch()

        # Modern iOS AM/PM Pill Segmented Toggle Button
        self.ampm_btn = QPushButton("AM")
        self.ampm_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ampm_btn.setFixedSize(44, 28)
        self.ampm_btn.setToolTip("Toggle AM / PM")
        self.ampm_btn.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {t['nav_active_bg']};
                color: {t['primary']};
                border: none;
                border-radius: 7px;
                font-size: 12px;
                font-weight: 700;
                padding: 0px;
            }}
            QPushButton:hover {{
                background-color: {t['nav_active_hover']};
            }}
            QPushButton:pressed {{
                background-color: {t['primary']};
                color: #FFFFFF;
            }}
            """
        )
        self.ampm_btn.clicked.connect(self._toggle_ampm)
        layout.addWidget(self.ampm_btn)

    def _toggle_ampm(self) -> None:
        self._hour24 = (self._hour24 + 12) % 24
        self._sync_display()

    def _on_parts_changed(self) -> None:
        h_text = self.hour_combo.currentText()
        m_text = self.min_combo.currentText()
        if not h_text.isdigit() or not m_text.isdigit():
            return
        h12 = int(h_text)
        m = int(m_text)
        is_pm = self.ampm_btn.text() == "PM"
        if is_pm:
            self._hour24 = 12 if h12 == 12 else h12 + 12
        else:
            self._hour24 = 0 if h12 == 12 else h12
        self._minute = m

    def _sync_display(self) -> None:
        is_pm = self._hour24 >= 12
        h12 = self._hour24 % 12
        if h12 == 0:
            h12 = 12
        self.hour_combo.blockSignals(True)
        self.min_combo.blockSignals(True)
        self.hour_combo.setCurrentText(f"{h12:02d}")
        self.min_combo.setCurrentText(f"{self._minute:02d}")
        self.ampm_btn.setText("PM" if is_pm else "AM")
        self.hour_combo.blockSignals(False)
        self.min_combo.blockSignals(False)

    def time(self) -> QTime:
        return QTime(self._hour24, self._minute)

    def setTime(self, qtime: QTime) -> None:
        if qtime.isValid():
            self._hour24 = qtime.hour()
            self._minute = qtime.minute()
            self._sync_display()


class TaskModal(QDialog):
    """
    Modal dialog for both creating a new task and editing an existing task.
    Includes Description, Priority, Date, and Time fields (skill.md Section 13: 20px radius).
    """

    def __init__(
        self,
        theme: Dict[str, str],
        on_submit,
        initial_task: Optional[Dict[str, object]] = None,
        task_number: Optional[int] = None,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.theme = theme
        self.on_submit = on_submit
        self.initial_task = initial_task
        self.task_number = task_number
        self.is_edit = initial_task is not None

        self.setWindowTitle(
            f"Edit Task #{task_number}" if self.is_edit else "New Task"
        )
        self.setModal(True)
        self.setFixedWidth(460)
        self._build_ui()

    def _build_ui(self) -> None:
        t = self.theme
        self.setStyleSheet(
            f"""
            QDialog {{
                background-color: {t['surface']};
                border: 1px solid {t['border']};
                border-radius: {RADIUS['modal']}px;
                font-family: {FONT_FAMILIES};
            }}
            QLabel {{
                background: transparent;
                border: none;
            }}
            QLineEdit, QComboBox, QDateEdit, QTimeEdit {{
                background-color: {t['surface']};
                color: {t['text']};
                border: 1px solid {t['border']};
                border-radius: {RADIUS['input']}px;
                padding: 0 12px;
                font-size: 14px;
            }}
            QLineEdit:hover, QComboBox:hover, QDateEdit:hover, QTimeEdit:hover {{
                border: 1px solid {t['border_hover']};
                background-color: {t['surface_hover']};
            }}
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTimeEdit:focus {{
                border: 1px solid {t['primary']};
                background-color: {t['surface']};
            }}
            QComboBox::drop-down, QDateEdit::drop-down, QTimeEdit::drop-down {{
                border: none;
                width: 24px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {t['surface']};
                color: {t['text']};
                border: 1px solid {t['border']};
                selection-background-color: {t['nav_active_bg']};
                selection-color: {t['primary']};
            }}
            """
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            SPACING["xl"], SPACING["xl"], SPACING["xl"], SPACING["xl"]
        )
        layout.setSpacing(SPACING["lg"])

        # Modal Header
        title_col = QVBoxLayout()
        title_col.setSpacing(SPACING["xs"])
        heading_text = (
            f"Edit Task #{self.task_number}" if self.is_edit else "Create New Task"
        )
        sub_text = (
            "Update the task description, priority, date, or time below."
            if self.is_edit
            else "Enter a task description, priority level, date, and time."
        )
        title_lbl = QLabel(heading_text)
        title_lbl.setStyleSheet(
            f"color: {t['text']}; font-size: 20px; font-weight: 600;"
        )
        sub_lbl = QLabel(sub_text)
        sub_lbl.setStyleSheet(f"color: {t['secondary_text']}; font-size: 13px;")
        title_col.addWidget(title_lbl)
        title_col.addWidget(sub_lbl)
        layout.addLayout(title_col)

        # Description Field
        desc_group = QVBoxLayout()
        desc_group.setSpacing(SPACING["xs"])
        desc_lbl = QLabel("Task Description")
        desc_lbl.setStyleSheet(
            f"color: {t['text']}; font-size: 13px; font-weight: 500;"
        )
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("e.g. Review pull request...")
        self.desc_input.setFixedHeight(42)
        if self.initial_task:
            self.desc_input.setText(str(self.initial_task.get("description", "")))
        self.desc_input.returnPressed.connect(self._handle_submit)
        desc_group.addWidget(desc_lbl)
        desc_group.addWidget(self.desc_input)
        layout.addLayout(desc_group)

        # Priority Field
        prio_group = QVBoxLayout()
        prio_group.setSpacing(SPACING["xs"])
        prio_lbl = QLabel("Priority")
        prio_lbl.setStyleSheet(
            f"color: {t['text']}; font-size: 13px; font-weight: 500;"
        )
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Medium", "High", "Low"])
        self.priority_combo.setFixedHeight(42)
        if self.initial_task:
            init_p = str(self.initial_task.get("priority", "medium")).capitalize()
            idx = self.priority_combo.findText(init_p)
            if idx >= 0:
                self.priority_combo.setCurrentIndex(idx)
        prio_group.addWidget(prio_lbl)
        prio_group.addWidget(self.priority_combo)
        layout.addLayout(prio_group)

        # Date & Time Row (Side-by-Side Modern Pickers — no legacy Windows 3D spin arrows)
        dt_row = QHBoxLayout()
        dt_row.setSpacing(SPACING["md"])

        # Modern Date Picker
        date_group = QVBoxLayout()
        date_group.setSpacing(SPACING["xs"])
        date_lbl = QLabel("Date")
        date_lbl.setStyleSheet(
            f"color: {t['text']}; font-size: 13px; font-weight: 500;"
        )
        self.date_edit = ModernDatePicker(t)
        default_date = QDate.currentDate()
        if self.initial_task and self.initial_task.get("date"):
            parsed_d = QDate.fromString(
                str(self.initial_task.get("date")), "yyyy-MM-dd"
            )
            if parsed_d.isValid():
                default_date = parsed_d
        self.date_edit.setDate(default_date)
        date_group.addWidget(date_lbl)
        date_group.addWidget(self.date_edit)
        dt_row.addLayout(date_group, stretch=1)

        # Modern Time Picker
        time_group = QVBoxLayout()
        time_group.setSpacing(SPACING["xs"])
        time_lbl = QLabel("Time")
        time_lbl.setStyleSheet(
            f"color: {t['text']}; font-size: 13px; font-weight: 500;"
        )
        self.time_edit = ModernTimePicker(t)
        default_time = QTime.currentTime()
        if self.initial_task and self.initial_task.get("time"):
            parsed_t = QTime.fromString(
                str(self.initial_task.get("time")), "hh:mm AP"
            )
            if not parsed_t.isValid():
                parsed_t = QTime.fromString(
                    str(self.initial_task.get("time")), "h:mm AP"
                )
            if parsed_t.isValid():
                default_time = parsed_t
        self.time_edit.setTime(default_time)
        time_group.addWidget(time_lbl)
        time_group.addWidget(self.time_edit)
        dt_row.addLayout(time_group, stretch=1)

        layout.addLayout(dt_row)

        # Inline validation error label (preserves entered values — skill.md Section 8)
        self.error_lbl = QLabel("")
        self.error_lbl.setStyleSheet(
            f"color: {t['danger']}; font-size: 12px; font-weight: 500;"
        )
        self.error_lbl.setVisible(False)
        layout.addWidget(self.error_lbl)

        # Action Buttons Row
        btn_row = QHBoxLayout()
        btn_row.setSpacing(SPACING["md"])
        btn_row.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        cancel_btn.setFixedHeight(42)
        cancel_btn.setFixedWidth(105)
        cancel_btn.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {t['surface']};
                color: {t['text']};
                font-size: 14px;
                font-weight: 600;
                border: 1px solid {t['border']};
                border-radius: {RADIUS['button']}px;
            }}
            QPushButton:hover {{
                background-color: {t['surface_hover']};
                border: 1px solid {t['border_hover']};
            }}
            QPushButton:pressed {{
                background-color: {t['surface_pressed']};
            }}
            """
        )
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(cancel_btn)

        submit_label = "  Save Changes" if self.is_edit else "  Create Task"
        submit_icon = "PencilSimple" if self.is_edit else "Plus"
        submit_btn = QPushButton(submit_label)
        submit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        submit_btn.setFixedHeight(42)
        submit_btn.setFixedWidth(155)
        submit_btn.setIcon(render_phosphor_icon(submit_icon, "#FFFFFF", 18))
        submit_btn.setIconSize(QSize(18, 18))
        submit_btn.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {t['primary']};
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 600;
                border-radius: {RADIUS['button']}px;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {t['primary_hover']};
            }}
            QPushButton:pressed {{
                background-color: {t['primary_pressed']};
            }}
            """
        )
        submit_btn.clicked.connect(self._handle_submit)
        btn_row.addWidget(submit_btn)

        layout.addLayout(btn_row)

    def _handle_submit(self) -> None:
        desc = self.desc_input.text()
        prio = self.priority_combo.currentText().lower()
        date_str = self.date_edit.date().toString("yyyy-MM-dd")
        time_str = self.time_edit.time().toString("hh:mm AP")

        ok, msg = self.on_submit(desc, prio, date_str, time_str)
        if not ok:
            self.error_lbl.setText(msg)
            self.error_lbl.setVisible(True)
            return
        self.accept()

    # Keep backwards-compatible alias for unit test calls
    def _handle_create(self) -> None:
        self._handle_submit()


# Backwards-compatible class alias
NewTaskModal = TaskModal


class TaskRowWidget(QFrame):
    """
    A 52px row inside the task data table:
    1st col: Radio toggle | 2nd col: ID | 3rd col: Description | 4th col: Date & Time
    5th col: Status | 6th col: Priority | 7th col: Actions (Edit + Delete)
    """

    def __init__(
        self,
        task_number: int,
        task: Dict[str, object],
        theme: Dict[str, str],
        on_toggle,
        on_edit,
        on_delete,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.task_number = task_number
        self.task = task
        self.theme = theme
        self.on_toggle = on_toggle
        self.on_edit = on_edit
        self.on_delete = on_delete

        self.setFixedHeight(52)
        self.setObjectName("TaskRow")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self._build_ui()

    def _build_ui(self) -> None:
        t = self.theme
        done = bool(self.task.get("done", False))
        priority = str(self.task.get("priority", "medium")).lower()
        description = str(self.task.get("description", ""))
        date_val = str(self.task.get("date", "")).strip()
        time_val = str(self.task.get("time", "")).strip()
        schedule_text = (
            f"{date_val} • {time_val}"
            if (date_val and time_val)
            else (date_val or time_val or "—")
        )

        self.setStyleSheet(
            f"""
            QFrame#TaskRow {{
                background-color: {t['surface']};
                border: 1px solid {t['border']};
                border-radius: {RADIUS['button']}px;
            }}
            QFrame#TaskRow:hover {{
                background-color: {t['surface_hover']};
                border: 1px solid {t['border_hover']};
            }}
            """
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(
            SPACING["lg"], SPACING["sm"], SPACING["lg"], SPACING["sm"]
        )
        layout.setSpacing(SPACING["md"])

        # 1st Column: Radio / Status Toggle Button
        status_container = QWidget()
        status_container.setFixedWidth(56)
        status_container.setStyleSheet("background: transparent; border: none;")
        status_col = QHBoxLayout(status_container)
        status_col.setContentsMargins(0, 0, 0, 0)
        status_col.setAlignment(Qt.AlignmentFlag.AlignCenter)

        status_btn = QPushButton()
        status_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        status_btn.setFixedSize(28, 28)
        icon_name = "CheckCircleFill" if done else "Circle"
        icon_color = t["success"] if done else t["secondary_text"]
        status_btn.setIcon(render_phosphor_icon(icon_name, icon_color, 20))
        status_btn.setIconSize(QSize(20, 20))
        status_btn.setToolTip("Toggle task completion")
        status_btn.setStyleSheet(
            f"""
            QPushButton {{
                background: transparent;
                border: none;
                border-radius: 14px;
            }}
            QPushButton:hover {{
                background-color: {t['surface_pressed']};
            }}
            """
        )
        status_btn.clicked.connect(lambda: self.on_toggle(str(self.task_number)))
        status_col.addWidget(status_btn)
        layout.addWidget(status_container)

        # 2nd Column: Task ID badge (#1, #2, ...)
        id_label = QLabel(f"#{self.task_number}")
        id_label.setFixedWidth(44)
        id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        id_label.setStyleSheet(
            f"color: {t['secondary_text']}; font-size: 13px; font-weight: 600; background: transparent; border: none;"
        )
        layout.addWidget(id_label)

        # 3rd Column: Task Description
        desc_label = QLabel(description)
        desc_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        text_color = t["secondary_text"] if done else t["text"]
        strike = "text-decoration: line-through;" if done else ""
        desc_label.setStyleSheet(
            f"color: {text_color}; font-size: 14px; font-weight: 500; {strike} background: transparent; border: none;"
        )
        layout.addWidget(desc_label)

        # 4th Column: Date & Time Schedule
        dt_label = QLabel(schedule_text)
        dt_label.setFixedWidth(160)
        dt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dt_label.setStyleSheet(
            f"color: {t['secondary_text']}; font-size: 12px; font-weight: 500; background: transparent; border: none;"
        )
        layout.addWidget(dt_label)

        # 5th Column: Status Pill (Completed / Pending)
        status_text = "Completed" if done else "Pending"
        status_pill = QLabel(status_text)
        status_fg = t["success"] if done else t["secondary_text"]
        status_bg = t["success_bg"] if done else t["background"]
        status_pill.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status_pill.setFixedHeight(24)
        status_pill.setFixedWidth(96)
        status_pill.setStyleSheet(
            f"""
            background-color: {status_bg};
            color: {status_fg};
            font-size: 12px;
            font-weight: 600;
            border-radius: 12px;
            border: none;
            """
        )
        layout.addWidget(status_pill)

        # 6th Column: Priority Pill
        priority_colors = {
            "high": (t["danger"], t["danger_bg"]),
            "medium": (t["warning"], t["warning_bg"]),
            "low": (t["primary"], t["nav_active_bg"]),
        }
        p_fg, p_bg = priority_colors.get(
            priority, (t["secondary_text"], t["background"])
        )
        priority_pill = QLabel(priority.capitalize())
        priority_pill.setAlignment(Qt.AlignmentFlag.AlignCenter)
        priority_pill.setFixedHeight(24)
        priority_pill.setFixedWidth(96)
        priority_pill.setStyleSheet(
            f"""
            background-color: {p_bg};
            color: {p_fg};
            font-size: 12px;
            font-weight: 600;
            border-radius: 12px;
            border: none;
            """
        )
        layout.addWidget(priority_pill)

        # 7th Column: Actions (Edit Button + Delete Button)
        act_container = QWidget()
        act_container.setFixedWidth(84)
        act_container.setStyleSheet("background: transparent; border: none;")
        act_col = QHBoxLayout(act_container)
        act_col.setContentsMargins(0, 0, 0, 0)
        act_col.setSpacing(SPACING["xs"])
        act_col.setAlignment(Qt.AlignmentFlag.AlignCenter)

        edit_btn = QPushButton()
        edit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        edit_btn.setFixedSize(32, 32)
        edit_btn.setIcon(render_phosphor_icon("PencilSimple", t["primary"], 16))
        edit_btn.setIconSize(QSize(16, 16))
        edit_btn.setToolTip(f"Edit task #{self.task_number}")
        edit_btn.setStyleSheet(
            f"""
            QPushButton {{
                background: transparent;
                border: none;
                border-radius: {RADIUS['small_button']}px;
            }}
            QPushButton:hover {{
                background-color: {t['nav_active_bg']};
            }}
            QPushButton:pressed {{
                background-color: {t['nav_active_hover']};
            }}
            """
        )
        edit_btn.clicked.connect(lambda: self.on_edit(str(self.task_number)))
        act_col.addWidget(edit_btn)

        del_btn = QPushButton()
        del_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        del_btn.setFixedSize(32, 32)
        del_btn.setIcon(render_phosphor_icon("Trash", t["danger"], 16))
        del_btn.setIconSize(QSize(16, 16))
        del_btn.setToolTip(f"Delete task #{self.task_number}")
        del_btn.setStyleSheet(
            f"""
            QPushButton {{
                background: transparent;
                border: none;
                border-radius: {RADIUS['small_button']}px;
            }}
            QPushButton:hover {{
                background-color: {t['danger_bg_hover']};
            }}
            QPushButton:pressed {{
                background-color: {t['danger_bg']};
            }}
            """
        )
        del_btn.clicked.connect(lambda: self.on_delete(str(self.task_number)))
        act_col.addWidget(del_btn)
        layout.addWidget(act_container)


class TaskTrackerWindow(QMainWindow):
    """Main Desktop Application Window adhering to skill.md iOS-inspired design system."""

    PAGE_SIZE = 6

    def __init__(self, data_file: Path = DATA_FILE):
        super().__init__()
        self.data_file = data_file
        self.is_dark_mode = False
        self.theme = LIGHT_THEME
        self.active_filter = "all"  # "all", "pending", "completed"
        self.current_page = 1
        self.tasks: List[Dict[str, object]] = load_tasks(self.data_file)
        self._active_transition: Optional[CircleBlurTransitionOverlay] = None

        self.setWindowTitle("Task Tracker")
        if LOGO_FILE.exists():
            self.setWindowIcon(QIcon(str(LOGO_FILE)))
        self.setMinimumSize(940, 620)
        self.resize(1040, 680)

        self._toast_timer = QTimer(self)
        self._toast_timer.setSingleShot(True)
        self._toast_timer.timeout.connect(self._hide_toast)

        self._init_ui()
        self._apply_theme()
        self._refresh_task_list()

    def _init_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # --------------------------------------------------------------------
        # A. MAIN CONTENT AREA
        # --------------------------------------------------------------------
        self.main_area = QWidget()
        self.main_area.setObjectName("MainArea")
        main_layout = QVBoxLayout(self.main_area)
        main_layout.setContentsMargins(
            SPACING["xxl"], SPACING["xl"], SPACING["xxl"], SPACING["xl"]
        )
        main_layout.setSpacing(SPACING["lg"])

        # Top Bar: Brand Logo + Title on Left | Action Buttons + Icon-Only Theme Switcher on Right
        header_row = QHBoxLayout()
        header_row.setSpacing(SPACING["md"])

        self.brand_icon = QLabel()
        self.brand_icon.setFixedSize(36, 36)
        header_row.addWidget(self.brand_icon)

        title_col = QVBoxLayout()
        title_col.setSpacing(2)
        self.page_title = QLabel("Task Tracker")
        self.page_subtitle = QLabel("Manage and track your local tasks")
        title_col.addWidget(self.page_title)
        title_col.addWidget(self.page_subtitle)
        header_row.addLayout(title_col)

        header_row.addStretch()

        # Primary "+ New Task" Button (opens Modal Dialog)
        self.add_btn = QPushButton("  New Task")
        self.add_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.add_btn.setFixedHeight(42)
        self.add_btn.setFixedWidth(135)
        self.add_btn.clicked.connect(self.open_new_task_modal)
        header_row.addWidget(self.add_btn)

        # Save Tasks Button
        self.save_now_btn = QPushButton("  Save")
        self.save_now_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.save_now_btn.setFixedHeight(42)
        self.save_now_btn.clicked.connect(self.handle_save_now)
        header_row.addWidget(self.save_now_btn)

        # Icon-only Theme Toggle Button at Top Right (triggers circular blur transition)
        self.theme_toggle_btn = QPushButton()
        self.theme_toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.theme_toggle_btn.setFixedSize(42, 42)
        self.theme_toggle_btn.setToolTip("Switch to dark mode")
        self.theme_toggle_btn.clicked.connect(self.toggle_theme)
        header_row.addWidget(self.theme_toggle_btn)

        main_layout.addLayout(header_row)

        # Toast / Feedback Banner (skill.md Section 13: Phosphor icon + short text)
        self.toast_frame = QFrame()
        self.toast_frame.setObjectName("ToastFrame")
        self.toast_frame.setFixedHeight(44)
        toast_layout = QHBoxLayout(self.toast_frame)
        toast_layout.setContentsMargins(SPACING["lg"], 0, SPACING["lg"], 0)
        toast_layout.setSpacing(SPACING["sm"])
        self.toast_icon = QLabel()
        self.toast_icon.setFixedSize(18, 18)
        self.toast_label = QLabel("")
        toast_layout.addWidget(self.toast_icon)
        toast_layout.addWidget(self.toast_label)
        toast_layout.addStretch()
        self.toast_frame.setVisible(False)
        main_layout.addWidget(self.toast_frame)

        # --------------------------------------------------------------------
        # B. DATA TABLE CARD (Contains Filter Tabs, Table Headers, Rows, & Pagination)
        # --------------------------------------------------------------------
        self.list_card = QFrame()
        self.list_card.setObjectName("ListCard")
        list_card_layout = QVBoxLayout(self.list_card)
        list_card_layout.setContentsMargins(
            SPACING["xl"], SPACING["lg"], SPACING["xl"], SPACING["lg"]
        )
        list_card_layout.setSpacing(SPACING["md"])

        # Top Bar inside Data Table: Filter Tabs (Left) + Task Count Badge (Right)
        table_top_bar = QHBoxLayout()
        table_top_bar.setSpacing(SPACING["sm"])

        self.nav_all_btn = self._create_filter_tab("All Tasks", "SquaresFour", "all")
        self.nav_pending_btn = self._create_filter_tab("Pending", "Folder", "pending")
        self.nav_done_btn = self._create_filter_tab(
            "Completed", "CheckCircle", "completed"
        )

        table_top_bar.addWidget(self.nav_all_btn)
        table_top_bar.addWidget(self.nav_pending_btn)
        table_top_bar.addWidget(self.nav_done_btn)
        table_top_bar.addStretch()

        self.stats_label = QLabel("0 of 0 completed")
        table_top_bar.addWidget(self.stats_label)

        list_card_layout.addLayout(table_top_bar)

        # Subtle Divider inside Data Table
        self.table_top_divider = QFrame()
        self.table_top_divider.setFixedHeight(1)
        list_card_layout.addWidget(self.table_top_divider)

        # Table Column Headers
        col_header = QHBoxLayout()
        col_header.setContentsMargins(SPACING["lg"], 0, SPACING["lg"], 0)
        col_header.setSpacing(SPACING["md"])

        self.col_status = QLabel("DONE")
        self.col_status.setFixedWidth(56)
        self.col_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.col_id = QLabel("ID")
        self.col_id.setFixedWidth(44)
        self.col_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.col_desc = QLabel("DESCRIPTION")
        self.col_dt = QLabel("DATE & TIME")
        self.col_dt.setFixedWidth(160)
        self.col_dt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.col_state = QLabel("STATUS")
        self.col_state.setFixedWidth(96)
        self.col_state.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.col_prio = QLabel("PRIORITY")
        self.col_prio.setFixedWidth(96)
        self.col_prio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.col_act = QLabel("ACTIONS")
        self.col_act.setFixedWidth(84)
        self.col_act.setAlignment(Qt.AlignmentFlag.AlignCenter)

        col_header.addWidget(self.col_status)
        col_header.addWidget(self.col_id)
        col_header.addWidget(self.col_desc, stretch=1)
        col_header.addWidget(self.col_dt)
        col_header.addWidget(self.col_state)
        col_header.addWidget(self.col_prio)
        col_header.addWidget(self.col_act)
        list_card_layout.addLayout(col_header)

        # Scrollable Task Rows Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.rows_container = QWidget()
        self.rows_layout = QVBoxLayout(self.rows_container)
        self.rows_layout.setContentsMargins(0, 0, 0, 0)
        self.rows_layout.setSpacing(SPACING["sm"])
        self.rows_layout.addStretch()

        self.scroll_area.setWidget(self.rows_container)
        list_card_layout.addWidget(self.scroll_area, stretch=1)

        # Subtle Bottom Divider before Pagination
        self.table_bottom_divider = QFrame()
        self.table_bottom_divider.setFixedHeight(1)
        list_card_layout.addWidget(self.table_bottom_divider)

        # Pagination Bar inside Data Table Footer
        pagination_row = QHBoxLayout()
        pagination_row.setSpacing(SPACING["sm"])

        self.page_info_label = QLabel("Showing 0–0 of 0")
        pagination_row.addWidget(self.page_info_label)
        pagination_row.addStretch()

        self.prev_page_btn = QPushButton("  Previous")
        self.prev_page_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.prev_page_btn.setFixedHeight(36)
        self.prev_page_btn.clicked.connect(self.prev_page)
        pagination_row.addWidget(self.prev_page_btn)

        self.page_number_label = QLabel("Page 1 of 1")
        self.page_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_number_label.setFixedWidth(96)
        pagination_row.addWidget(self.page_number_label)

        self.next_page_btn = QPushButton("Next  ")
        self.next_page_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.next_page_btn.setFixedHeight(36)
        self.next_page_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.next_page_btn.clicked.connect(self.next_page)
        pagination_row.addWidget(self.next_page_btn)

        list_card_layout.addLayout(pagination_row)

        main_layout.addWidget(self.list_card, stretch=1)
        root_layout.addWidget(self.main_area, stretch=1)

        # Hidden compatibility inputs for headless programmatic tests
        self.desc_input = QLineEdit(self)
        self.desc_input.setVisible(False)
        self.priority_combo = QComboBox(self)
        self.priority_combo.addItems(["Medium", "High", "Low"])
        self.priority_combo.setVisible(False)
        self.task_id_input = QLineEdit(self)
        self.task_id_input.setVisible(False)
        self.search_input = QLineEdit(self)
        self.search_input.setVisible(False)

    def _create_filter_tab(
        self, label: str, icon_name: str, filter_key: str
    ) -> QPushButton:
        btn = QPushButton(f"  {label}")
        btn.setProperty("icon_name", icon_name)
        btn.setProperty("filter_key", filter_key)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedHeight(38)
        btn.clicked.connect(lambda: self._set_filter(filter_key))
        return btn

    def _set_filter(self, filter_key: str) -> None:
        self.active_filter = filter_key
        self.current_page = 1
        self._apply_theme()
        self._refresh_task_list()

    def prev_page(self) -> None:
        if self.current_page > 1:
            self.current_page -= 1
            self._refresh_task_list()

    def next_page(self) -> None:
        filtered = self._get_filtered_tasks()
        total_pages = max(1, math.ceil(len(filtered) / self.PAGE_SIZE))
        if self.current_page < total_pages:
            self.current_page += 1
            self._refresh_task_list()

    def open_new_task_modal(self) -> None:
        """Open the modal dialog to create a new task entry with date and time."""
        modal = TaskModal(
            theme=self.theme,
            on_submit=self._create_task_from_modal,
            parent=self,
        )
        modal.exec()

    def open_edit_task_modal(self, raw_number: str) -> None:
        """Open the modal dialog pre-populated with an existing task's details."""
        ok, msg, number = validate_task_number(self.tasks, raw_number)
        if not ok or number is None:
            self.show_toast(msg, "error")
            return

        task = self.tasks[number - 1]
        modal = TaskModal(
            theme=self.theme,
            on_submit=lambda desc, prio, d_str, t_str: self._edit_task_from_modal(
                str(number), desc, prio, d_str, t_str
            ),
            initial_task=task,
            task_number=number,
            parent=self,
        )
        modal.exec()

    def _create_task_from_modal(
        self,
        description: str,
        priority: str,
        date_str: Optional[str] = None,
        time_str: Optional[str] = None,
    ) -> Tuple[bool, str]:
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")
        if time_str is None:
            time_str = datetime.now().strftime("%I:%M %p")

        ok, msg, task = validate_and_create_task(
            description, priority, date_str=date_str, time_str=time_str
        )
        if not ok or task is None:
            self.show_toast(msg, "error")
            return False, msg

        self.tasks.append(task)
        save_tasks(self.tasks, self.data_file)
        filtered = self._get_filtered_tasks()
        self.current_page = max(1, math.ceil(len(filtered) / self.PAGE_SIZE))
        self._refresh_task_list()
        self.show_toast(msg, "success")
        return True, msg

    def _edit_task_from_modal(
        self,
        raw_number: str,
        description: str,
        priority: str,
        date_str: Optional[str] = None,
        time_str: Optional[str] = None,
    ) -> Tuple[bool, str]:
        ok, msg = edit_task(
            self.tasks,
            raw_number,
            description,
            priority,
            date_str=date_str,
            time_str=time_str,
        )
        if not ok:
            self.show_toast(msg, "error")
            return False, msg

        save_tasks(self.tasks, self.data_file)
        self._refresh_task_list()
        self.show_toast(msg, "success")
        return True, msg

    # ------------------------------------------------------------------------
    # THEME STYLING & CIRCULAR BLUR REVEAL TRANSITION
    # ------------------------------------------------------------------------

    def toggle_theme(self) -> None:
        """
        Switch theme using the circular-blur View Transition animation (`circle-blur`)
        expanding from the center of the top-right theme toggle button.
        """
        # If an animation is currently running, finish/hide it before capturing the snapshot
        if self._active_transition is not None:
            try:
                self._active_transition.anim.stop()
                self._active_transition.hide()
                self._active_transition.deleteLater()
            except RuntimeError:
                pass
            self._active_transition = None

        central = self.centralWidget()
        can_animate = (
            central is not None
            and self.isVisible()
            and central.width() > 0
            and central.height() > 0
        )

        old_snapshot = central.grab() if can_animate else QPixmap()

        self.is_dark_mode = not self.is_dark_mode
        self.theme = DARK_THEME if self.is_dark_mode else LIGHT_THEME
        self.theme_toggle_btn.setToolTip(
            "Switch to light mode" if self.is_dark_mode else "Switch to dark mode"
        )
        self._apply_theme()
        self._refresh_task_list()

        if can_animate and not old_snapshot.isNull():
            # Force layout activation so new task rows are sized before grabbing new_snapshot
            if central.layout() is not None:
                central.layout().activate()
            if self.rows_container.layout() is not None:
                self.rows_container.layout().activate()

            new_snapshot = central.grab()
            btn_center = self.theme_toggle_btn.mapTo(
                central,
                QPoint(
                    self.theme_toggle_btn.width() // 2,
                    self.theme_toggle_btn.height() // 2,
                ),
            )
            overlay = CircleBlurTransitionOverlay(
                parent=central,
                old_pixmap=old_snapshot,
                new_pixmap=new_snapshot,
                origin=btn_center,
            )
            self._active_transition = overlay
            overlay.start(on_finished=lambda: self._clear_transition(overlay))

    def _clear_transition(self, overlay: CircleBlurTransitionOverlay) -> None:
        if self._active_transition is overlay:
            self._active_transition = None

    def _apply_theme(self) -> None:
        t = self.theme

        self.setStyleSheet(
            f"""
            QMainWindow, QWidget#MainArea {{
                background-color: {t['background']};
                font-family: {FONT_FAMILIES};
            }}
            QFrame#ListCard {{
                background-color: {t['surface']};
                border: 1px solid {t['border']};
                border-radius: {RADIUS['card']}px;
            }}
            QScrollArea {{
                background: transparent;
                border: none;
            }}
            """
        )

        self.rows_container.setStyleSheet(f"background-color: {t['surface']};")
        self.table_top_divider.setStyleSheet(
            f"background-color: {t['border']}; border: none;"
        )
        self.table_bottom_divider.setStyleSheet(
            f"background-color: {t['border']}; border: none;"
        )

        # Typography scale (skill.md Section 4) & Logo
        if LOGO_FILE.exists():
            logo_pix = QPixmap(str(LOGO_FILE)).scaled(
                36,
                36,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.brand_icon.setPixmap(logo_pix)
        else:
            self.brand_icon.setPixmap(
                render_phosphor_pixmap("SquaresFour", t["primary"], 28)
            )

        self.page_title.setStyleSheet(
            f"color: {t['text']}; font-size: 24px; font-weight: 700; border: none;"
        )
        self.page_subtitle.setStyleSheet(
            f"color: {t['secondary_text']}; font-size: 13px; border: none;"
        )
        self.stats_label.setStyleSheet(
            f"color: {t['secondary_text']}; font-size: 13px; font-weight: 600; border: none;"
        )
        self.page_info_label.setStyleSheet(
            f"color: {t['secondary_text']}; font-size: 13px; font-weight: 500; border: none;"
        )
        self.page_number_label.setStyleSheet(
            f"color: {t['text']}; font-size: 13px; font-weight: 600; border: none;"
        )

        for hdr in (
            self.col_status,
            self.col_id,
            self.col_desc,
            self.col_dt,
            self.col_state,
            self.col_prio,
            self.col_act,
        ):
            hdr.setStyleSheet(
                f"color: {t['secondary_text']}; font-size: 12px; font-weight: 600; border: none;"
            )

        # In-table Filter Tab Buttons
        for btn in (self.nav_all_btn, self.nav_pending_btn, self.nav_done_btn):
            icon_name = btn.property("icon_name")
            filter_key = btn.property("filter_key")
            is_active = filter_key == self.active_filter
            fg = t["primary"] if is_active else t["text"]
            bg = t["nav_active_bg"] if is_active else t["background"]
            hover_bg = t["nav_active_hover"] if is_active else t["surface_hover"]
            pressed_bg = t["nav_active_hover"] if is_active else t["surface_pressed"]
            border_col = t["primary"] if is_active else t["border"]
            weight = "600" if is_active else "500"
            btn.setIcon(render_phosphor_icon(icon_name, fg, 18))
            btn.setIconSize(QSize(18, 18))
            btn.setStyleSheet(
                f"""
                QPushButton {{
                    background-color: {bg};
                    color: {fg};
                    font-size: 13px;
                    font-weight: {weight};
                    padding: 0 14px;
                    border-radius: {RADIUS['small_button']}px;
                    border: 1px solid {border_col};
                }}
                QPushButton:hover {{
                    background-color: {hover_bg};
                }}
                QPushButton:pressed {{
                    background-color: {pressed_bg};
                }}
                """
            )

        # Primary Button: + New Task (skill.md Section 7)
        self.add_btn.setIcon(render_phosphor_icon("Plus", "#FFFFFF", 18))
        self.add_btn.setIconSize(QSize(18, 18))
        self.add_btn.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {t['primary']};
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 600;
                border-radius: {RADIUS['button']}px;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {t['primary_hover']};
            }}
            QPushButton:pressed {{
                background-color: {t['primary_pressed']};
            }}
            """
        )

        # Secondary Buttons: Save & Pagination Prev/Next
        secondary_qss = f"""
            QPushButton {{
                background-color: {t['surface']};
                color: {t['text']};
                font-size: 13px;
                font-weight: 600;
                border: 1px solid {t['border']};
                border-radius: {RADIUS['button']}px;
                padding: 0 14px;
            }}
            QPushButton:hover:enabled {{
                background-color: {t['surface_hover']};
                border: 1px solid {t['border_hover']};
            }}
            QPushButton:pressed:enabled {{
                background-color: {t['surface_pressed']};
            }}
            QPushButton:disabled {{
                color: {t['secondary_text']};
                background-color: {t['background']};
                border: 1px solid {t['border']};
            }}
        """
        self.save_now_btn.setIcon(render_phosphor_icon("Database", t["primary"], 18))
        self.save_now_btn.setIconSize(QSize(18, 18))
        self.save_now_btn.setStyleSheet(secondary_qss)

        self.prev_page_btn.setIcon(render_phosphor_icon("CaretLeft", t["text"], 16))
        self.prev_page_btn.setIconSize(QSize(16, 16))
        self.prev_page_btn.setStyleSheet(secondary_qss)

        self.next_page_btn.setIcon(render_phosphor_icon("CaretRight", t["text"], 16))
        self.next_page_btn.setIconSize(QSize(16, 16))
        self.next_page_btn.setStyleSheet(secondary_qss)

        # Top-right icon-only Theme Toggle (Phosphor Sun in dark mode, Moon in light mode)
        theme_icon = "Sun" if self.is_dark_mode else "Moon"
        self.theme_toggle_btn.setIcon(render_phosphor_icon(theme_icon, t["text"], 20))
        self.theme_toggle_btn.setIconSize(QSize(20, 20))
        self.theme_toggle_btn.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {t['surface']};
                border: 1px solid {t['border']};
                border-radius: {RADIUS['button']}px;
                padding: 0px;
            }}
            QPushButton:hover {{
                background-color: {t['surface_hover']};
                border: 1px solid {t['border_hover']};
            }}
            QPushButton:pressed {{
                background-color: {t['surface_pressed']};
            }}
            """
        )

    # ------------------------------------------------------------------------
    # USER ACTIONS & VALIDATION (criteria.md)
    # ------------------------------------------------------------------------

    def show_toast(self, message: str, status: str = "success") -> None:
        """Display a minimal Phosphor-icon toast banner without emojis."""
        t = self.theme
        if status == "error":
            fg, bg, icon_name = t["danger"], t["danger_bg"], "WarningCircle"
        elif status == "warning":
            fg, bg, icon_name = t["warning"], t["warning_bg"], "WarningCircle"
        else:
            fg, bg, icon_name = t["success"], t["success_bg"], "CheckCircleFill"

        self.toast_frame.setStyleSheet(
            f"""
            QFrame#ToastFrame {{
                background-color: {bg};
                border: 1px solid {fg};
                border-radius: {RADIUS['button']}px;
            }}
            """
        )
        self.toast_icon.setPixmap(render_phosphor_pixmap(icon_name, fg, 18))
        self.toast_label.setText(message)
        self.toast_label.setStyleSheet(
            f"color: {fg}; font-size: 13px; font-weight: 600; border: none; background: transparent;"
        )
        self.toast_frame.setVisible(True)
        self._toast_timer.start(3500)

    def _hide_toast(self) -> None:
        self.toast_frame.setVisible(False)

    def handle_add_task(self) -> None:
        raw_desc = self.desc_input.text()
        raw_prio = self.priority_combo.currentText().lower()
        ok, _ = self._create_task_from_modal(raw_desc, raw_prio)
        if ok:
            self.desc_input.clear()

    def handle_toggle_task(self, raw_number: str) -> None:
        ok, msg, number = validate_task_number(self.tasks, raw_number)
        if not ok or number is None:
            self.show_toast(msg, "error")
            return

        current = bool(self.tasks[number - 1].get("done", False))
        self.tasks[number - 1]["done"] = not current
        save_tasks(self.tasks, self.data_file)
        self._refresh_task_list()
        state_word = "completed" if not current else "reopened"
        self.show_toast(f"Task #{number} marked as {state_word}.", "success")

    def handle_complete_by_id(self) -> None:
        raw_number = self.task_id_input.text()
        ok, msg, number = validate_task_number(self.tasks, raw_number)
        if not ok or number is None:
            self.show_toast(msg, "error")
            return

        self.tasks[number - 1]["done"] = True
        save_tasks(self.tasks, self.data_file)
        self.task_id_input.clear()
        self._refresh_task_list()
        self.show_toast(
            f"Completed task #{number}: '{self.tasks[number - 1]['description']}'.",
            "success",
        )

    def handle_delete_by_id(self) -> None:
        raw_number = self.task_id_input.text()
        self.handle_delete_task(raw_number, clear_input=True)

    def handle_delete_task(self, raw_number: str, clear_input: bool = False) -> None:
        ok, msg, number = validate_task_number(self.tasks, raw_number)
        if not ok or number is None:
            self.show_toast(msg, "error")
            return

        removed = self.tasks.pop(number - 1)
        save_tasks(self.tasks, self.data_file)
        if clear_input:
            self.task_id_input.clear()
        self._refresh_task_list()
        self.show_toast(
            f"Deleted task #{number}: '{removed['description']}'.", "success"
        )

    def handle_save_now(self) -> None:
        if save_tasks(self.tasks, self.data_file):
            self.show_toast("All tasks saved to tasks.json.", "success")
        else:
            self.show_toast("Could not save tasks.json.", "error")

    def handle_exit(self) -> None:
        save_tasks(self.tasks, self.data_file)
        self.close()

    def _get_filtered_tasks(self) -> List[Tuple[int, Dict[str, object]]]:
        query = self.search_input.text().strip().lower()
        results: List[Tuple[int, Dict[str, object]]] = []
        for index, task in enumerate(self.tasks, start=1):
            done = bool(task.get("done", False))
            if self.active_filter == "pending" and done:
                continue
            if self.active_filter == "completed" and not done:
                continue
            desc = str(task.get("description", ""))
            prio = str(task.get("priority", "medium"))
            if query and query not in desc.lower() and query not in prio.lower():
                continue
            results.append((index, task))
        return results

    def _refresh_task_list(self) -> None:
        # Clear existing row widgets immediately (setParent(None) detaches right away
        # so synchronous central.grab() snapshots never see stacked old+new rows).
        while self.rows_layout.count() > 0:
            item = self.rows_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.hide()
                widget.setParent(None)
                widget.deleteLater()

        total = len(self.tasks)
        completed_count = sum(1 for task in self.tasks if task.get("done"))
        self.stats_label.setText(f"{completed_count} of {total} completed")

        filtered = self._get_filtered_tasks()
        total_filtered = len(filtered)
        total_pages = max(1, math.ceil(total_filtered / self.PAGE_SIZE))
        if self.current_page > total_pages:
            self.current_page = total_pages
        if self.current_page < 1:
            self.current_page = 1

        start_idx = (self.current_page - 1) * self.PAGE_SIZE
        end_idx = min(start_idx + self.PAGE_SIZE, total_filtered)
        page_items = filtered[start_idx:end_idx]

        for index, task in page_items:
            row_widget = TaskRowWidget(
                task_number=index,
                task=task,
                theme=self.theme,
                on_toggle=self.handle_toggle_task,
                on_edit=self.open_edit_task_modal,
                on_delete=self.handle_delete_task,
            )
            self.rows_layout.addWidget(row_widget)

        if not page_items:
            empty_label = QLabel(
                "No tasks in this view. Click 'New Task' above to create an entry."
            )
            empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            empty_label.setFixedHeight(140)
            empty_label.setStyleSheet(
                f"color: {self.theme['secondary_text']}; font-size: 14px; border: none;"
            )
            self.rows_layout.addWidget(empty_label)

        self.rows_layout.addStretch()

        # Update pagination footer controls
        if total_filtered == 0:
            self.page_info_label.setText("Showing 0 of 0 entries")
        else:
            self.page_info_label.setText(
                f"Showing {start_idx + 1}–{end_idx} of {total_filtered} entries"
            )
        self.page_number_label.setText(f"Page {self.current_page} of {total_pages}")
        self.prev_page_btn.setEnabled(self.current_page > 1)
        self.next_page_btn.setEnabled(self.current_page < total_pages)


# ============================================================================
# 6. CLI & GUI ENTRY POINT (architecture.md: main() controls flow)
# ============================================================================


def run_cli() -> None:
    """Terminal menu loop satisfying all CLI acceptance criteria."""
    tasks = load_tasks(DATA_FILE)
    while True:
        print("\n=== TASK TRACKER ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Save now")
        print("6. Exit")
        choice = input("Choose 1-6: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            if save_tasks(tasks, DATA_FILE):
                print("Tasks saved successfully.")
        elif choice == "6":
            save_tasks(tasks, DATA_FILE)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please choose a number from 1 to 6.")


def main() -> None:
    """Launch the Modern iOS-inspired Desktop UI (or CLI mode when --cli is passed)."""
    if "--cli" in sys.argv:
        run_cli()
        return

    app = QApplication(sys.argv)
    app.setFont(QFont("Poppins", 10))
    window = TaskTrackerWindow(DATA_FILE)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
