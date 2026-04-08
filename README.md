# ⚙️ File Organizer CLI Tool

> Turn chaos into order — automatically organize your files with a single command.

---

## 🚀 Overview

This is a **Python-based CLI automation tool** that scans a directory and organizes files into structured folders based on their type.

Instead of manually sorting files, this tool does it instantly and efficiently.

---

## ✨ Features

✔ Automatically detects file types
✔ Creates folders dynamically (Images, Documents, etc.)
✔ Moves files into appropriate directories
✔ Skips system files and folders safely
✔ Clean and scalable logic using Python

---

## 🧠 How It Works

The script:

1. Scans all files in the current directory
2. Identifies file extensions
3. Matches them with predefined categories
4. Creates folders if they don’t exist
5. Moves files into their respective folders

---

## 📂 Supported Categories

| Category     | File Types        |
| ------------ | ----------------- |
| 📸 Images    | .jpg, .png, .jpeg |
| 📄 Documents | .pdf, .txt, .md   |
| 🎬 Videos    | .mp4              |
| 🎧 Audio     | .mp3              |
| 📦 Others    | Everything else   |

---

## 🛠️ Tech Stack

* 🐍 Python
* 📁 os module (file handling & automation)

---

## 🖥️ Example

Before:

```id="ex1"
main.py
file.pdf
photo.jpg
song.mp3
notes.txt
```

After running the script:

```id="ex2"
Images/
  photo.jpg

Documents/
  file.pdf
  notes.txt

Audio/
  song.mp3

main.py
```

---

## ⚡ How to Run

```id="run1"
python main.py
```

Make sure your files are in the same directory as the script.

---

## 🧪 What I Learned

* Working with the **os module**
* Handling file systems in Python
* Writing clean and scalable logic
* Building real-world automation tools
* Managing projects using Git & GitHub

---

## 🔮 Future Improvements

* Accept custom directory paths (user input)
* Add logging system for file movements
* Build interactive CLI interface
* Develop GUI version (Tkinter / Web UI)


---

## 👨‍💻 Author

Built by **Mehfooz**
Aspiring backend developer focused on real-world problem solving and automation.

---

## ⭐ Final Note

This project reflects a shift from **learning syntax → building solutions**.

If you found this useful or interesting, consider giving it a ⭐


