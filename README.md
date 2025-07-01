# 🗂 Automatic File Organizer

A simple Python tool to keep your Downloads folder clean and organized in real time.  
It watches for new files and automatically moves them into categorized subfolders (Images, Documents, Videos, Archives, Others) based on file type.

## ✨ Features

✅ Monitors your Downloads folder in real time  
✅ Automatically organizes files into subfolders  
✅ Written in clean Python, easy to understand and customize  
✅ Uses `watchdog` for efficient file system monitoring  
✅ Small, lightweight, and actually useful for daily productivity

## 🚀 How to run

1. **Clone or download** this repository.
2. Install required Python library:
   ```bash
   pip install watchdog
   ```
3. Open `file_organizer.py` and update these lines to your actual paths:
   ```python
   SOURCE_DIR = r"C:\Users\<YourUsername>\Downloads"
   DEST_DIRS = {
       "images": r"C:\Users\<YourUsername>\Downloads\Images",
       "documents": r"C:\Users\<YourUsername>\Downloads\Documents",
       "videos": r"C:\Users\<YourUsername>\Downloads\Videos",
       "others": r"C:\Users\<YourUsername>\Downloads\Others"
   }
   ```
4. Run the script:
   ```bash
   python file_organizer.py
   ```
5. Download something (like a PDF or image) into your Downloads folder, and see it get moved automatically!

## 📂 Folder structure

Your Downloads folder will now look like this:

```
Downloads/
├─ Images/
├─ Documents/
├─ Videos/
└─ Others/
```

---

## ⚙ How it works

* Uses `watchdog` to watch for new or renamed files.
* Matches file extensions like `.pdf`, `.jpg`, `.mp4` to decide the folder.
* Ignores temporary files (e.g., `.tmp`, `.crdownload`) created while downloading.
* Moves completed files automatically to keep your Downloads folder tidy.

---

## 🛠 Built with

* Python 🐍
* `watchdog` for file system monitoring
* `shutil` and `os` for moving files
* `logging` for clear console logs

---

## ✅ Why this project?

Built as a quick but useful automation tool — and to demonstrate:

* Real-world use of Python scripting
* File system automation
* Clean code and logging practices

---

## ✏ Author

Made by Aniruddh Reddy for learning and productivity.
