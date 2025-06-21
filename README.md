# Bulk File Renamer 🔄

**Bulk File Renamer** is a powerful yet simple Python command-line tool designed to save you time and effort by **renaming hundreds or thousands of files instantly** with just a few commands.

Whether you're a developer, photographer, content creator, or anyone managing lots of files, this tool helps you organize and rename files **efficiently, flexibly, and safely** — all from your terminal.

---

## Why Bulk File Renamer? 🚀

Manually renaming files one by one is **time-consuming, boring, and error-prone**. This tool is built with a **real-world, need-driven approach** to solve this common pain point.

- Rename hundreds of files in seconds.
- Flexible rules: search & replace, add prefixes or suffixes.
- Filter by file extensions.
- Dry-run mode to preview changes before applying.
- Lightweight, zero dependencies, easy to use.
- Open source and ready to customize for your needs.

Save time, avoid mistakes, and keep your files **organized and consistent** effortlessly.

---

## Features ⭐

- **Search & Replace:** Find specific strings in filenames and replace them.
- **Add Prefix/Suffix:** Add custom prefixes or suffixes to filenames, keeping extensions intact.
- **Extension Filtering:** Rename only files with specific extensions (e.g., `.jpg`, `.txt`).
- **Dry Run Mode:** Preview all renaming operations without actually renaming files.
- **Cross-platform:** Works on Windows, macOS, and Linux.
- **Simple CLI Interface:** No complicated GUIs or bloat—just clean and clear command-line commands.

---

## Installation

Just clone the repo or download the script:

```bash
git clone https://github.com/kemalbatuhanabut/bulk-file-renamer.git
cd bulk-file-renamer
````

You only need **Python 3.x** installed (no external packages required).

---

## Usage

```bash
python bulk_rename.py [folder] [options]
```

### Required argument:

* `folder`: Path to the folder containing files to rename.

### Optional arguments:

| Option        | Description                                            | Example            |
| ------------- | ------------------------------------------------------ | ------------------ |
| `--search`    | Text to search for in filenames                        | `--search old`     |
| `--replace`   | Text to replace the search string with                 | `--replace new`    |
| `--prefix`    | Add a prefix to each filename                          | `--prefix 2025_`   |
| `--suffix`    | Add a suffix before the file extension                 | `--suffix _backup` |
| `--extension` | Only rename files with this extension                  | `--extension .txt` |
| `--dry-run`   | Show what files would be renamed without renaming them | `--dry-run`        |

---

## Examples

* **Replace “draft” with “final” in all filenames:**

```bash
python bulk_rename.py ./my_files --search draft --replace final
```

* **Add prefix “2025\_” to all files:**

```bash
python bulk_rename.py ./my_files --prefix 2025_
```

* **Add suffix “\_backup” to all `.txt` files, without renaming yet (dry run):**

```bash
python bulk_rename.py ./my_files --suffix _backup --extension .txt --dry-run
```

---

## How It Works 🔧

The script scans the target folder, lists all files, optionally filters them by extension, then applies:

* Search & replace on the filename string
* Prefix addition
* Suffix addition (before extension)

All changes are previewed in dry-run mode or committed by renaming files using `os.rename()`.

---

## Who Is This For?

* **Photographers:** Rename photo batches by date or event name.
* **Writers & Editors:** Replace draft tags in manuscripts with final versions.
* **Developers:** Clean up messy file names or add project-specific prefixes.
* **Content Managers:** Organize files before uploading or archiving.

If you handle **lots of files** and want a **reliable and fast way** to rename them, this tool is for you.

---

## Contributing 🤝

Contributions, issues, and feature requests are welcome!

Feel free to:

* Suggest improvements
* Report bugs
* Add support for new features like regex renaming, GUI, or multi-threading

---

## License

MIT License — free and open source.

---

## Final Words

Stop wasting time renaming files manually. Try **Bulk File Renamer** and transform your file management workflow today! 💪

---

### Developed with ❤️ by \ Kemal Batuhan ABUT

---

