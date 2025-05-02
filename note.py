import os
import json



# ----------------- Singleton Pattern -----------------
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.save_directory = "./notes"
            os.makedirs(cls._instance.save_directory, exist_ok=True)
        return cls._instance



# ----------------- Note Types (Factory Pattern) -----------------
class Note:
    def save(self, content: str, filename: str):
        raise NotImplementedError()

class PlainTextNote(Note):
    def save(self, content, filename):
        with open(f"{Config().save_directory}/{filename}.txt", "w") as f:
            f.write(content)

class MarkdownNote(Note):
    def save(self, content, filename):
        with open(f"{Config().save_directory}/{filename}.md", "w") as f:
            f.write(f"# {content}")

class NoteFactory:
    @staticmethod
    def create_note(format_type: str) -> Note:
        if format_type == "text":
            return PlainTextNote()
        elif format_type == "markdown":
            return MarkdownNote()
        else:
            raise ValueError("Unsupported format")



# ----------------- Export Strategies (Strategy Pattern) -----------------
class ExportStrategy:
    def export(self, content: str, filename: str):
        raise NotImplementedError()

class JSONExportStrategy(ExportStrategy):
    def export(self, content, filename):
        with open(f"{Config().save_directory}/{filename}.json", "w") as f:
            json.dump({"note": content}, f)

class HTMLExportStrategy(ExportStrategy):
    def export(self, content, filename):
        with open(f"{Config().save_directory}/{filename}.html", "w") as f:
            f.write(f"<html><body><p>{content}</p></body></html>")



# ----------------- Repository Pattern -----------------
class NoteRepository:
    def __init__(self):
        self.directory = Config().save_directory

    def save(self, filename, content):
        with open(f"{self.directory}/{filename}.txt", "w") as f:
            f.write(content)

    def load(self, filename):
        path = f"{self.directory}/{filename}.txt"
        if not os.path.exists(path):
            raise FileNotFoundError(f"{filename}.txt not found.")
        with open(path, "r") as f:
            return f.read()



# ----------------- Application Logic -----------------
def main():
    print("📝 Welcome to Note Manager")
    note_type = input("Choose format (text/markdown): ").strip().lower()
    filename = input("Enter note filename: ").strip()
    content = input("Enter note content: ").strip()

    # Create and save note using Factory
    note = NoteFactory.create_note(note_type)
    note.save(content, filename)
    print(f"✅ Note saved as {filename}.{note_type}")

    # Export using Strategy
    export_type = input("Export to (json/html/none)? ").strip().lower()
    if export_type == "json":
        exporter = JSONExportStrategy()
        exporter.export(content, filename)
        print(f"📤 Exported to {filename}.json")
    elif export_type == "html":
        exporter = HTMLExportStrategy()
        exporter.export(content, filename)
        print(f"📤 Exported to {filename}.html")

    # Load note using Repository
    repo = NoteRepository()
    try:
        loaded = repo.load(filename)
        print(f"📄 Loaded from file:\n{loaded}")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
