# import os
# downloads_dir=r"C:\Users\mamil\Downloads"
# entries=os.scandir(downloads_dir)
# for i in entries:
#     print(i.name)

import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === Configuration ===
SOURCE_DIR = r"C:\Users\mamil\Downloads"
DEST_DIRS = {
    "images": r"C:\Users\mamil\OneDrive\Pictures\Downloaded images",
    "documents": r"C:\Users\mamil\OneDrive\Documents\downloaded docs",
    "videos": r"C:\Users\mamil\Videos\Downloaded video",
    "others": r"C:\Users\mamil\OneDrive\Desktop\others"
}

EXTENSIONS = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".doc", ".pptx", ".xlsx", ".txt"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
}

# === Logging setup ===
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class FileHandler(FileSystemEventHandler):
    def process(self, filepath):
        if os.path.isdir(filepath):
            return
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()

        # Ignore temp files
        if ext in [".tmp", ".crdownload", ".part"]:
            return

        moved = False
        for category, ext_list in EXTENSIONS.items():
            if ext in ext_list:
                dest_folder = DEST_DIRS[category]
                move_file(filepath, dest_folder)
                moved = True
                break

        if not moved:
            move_file(filepath, DEST_DIRS["others"])

    def on_created(self, event):
        self.process(event.src_path)

    def on_moved(self, event):
        self.process(event.dest_path)


def move_file(src_path, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        shutil.move(src_path, dest_folder)
        logging.info(f"Moved: {src_path} → {dest_folder}")
    except Exception as e:
        logging.error(f"Error moving file {src_path}: {e}")

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, SOURCE_DIR, recursive=False)
    observer.start()
    logging.info("Started monitoring Downloads folder... Press Ctrl+C to stop.")

    try:
        while True:
            pass  # Keeps the script running
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Stopped.")
    observer.join()
