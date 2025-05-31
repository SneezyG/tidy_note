# File-Based Note Management System

A CLI-based note management system that demonstrates the implementation of common software design patterns using Python. Notes are stored and managed via a local file system (no database), making this a lightweight and self-contained application.

## 🎯 Project Goals

- Showcase practical use of classic design patterns
- Provide a modular, extensible architecture
- Implement file-based persistence for offline use

## 🧱 Key Features

- Create, read, update, and delete (CRUD) notes
- Categorize notes by tags or topics
- Save notes to and load from local files
- Simple command-line interface (CLI)
- Clean, object-oriented architecture using design patterns

## 🧠 Design Patterns Used

| Pattern        | Purpose                                                         |
|----------------|-----------------------------------------------------------------|
| **Singleton**  | Manage a single instance of the file manager                    |
| **Factory**    | Create different types of note objects dynamically              |
| **Strategy**   | Apply different saving/loading strategies (e.g., JSON, TXT)     |
| **Observer**   | Track and notify listeners on note creation or deletion events  |
| **Command**    | Handle undo/redo operations for note actions (optional/bonus)   |

## 🛠️ Tech Stack

- Python 3.x
- `os`, `json`, and `datetime` standard libraries
- Optional: `argparse` for CLI argument handling

