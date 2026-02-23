# A1: Linux Basics — Submission Document

**Assignment:** Linux Basics  
**Submission:** Commands with explanations and output (attach screenshots in final doc)  
**GitHub repo link:** [Add your repository link here]

---

## 1. Creating and Renaming Files/Directories

### Commands used

```bash
mkdir test_dir
touch test_dir/example.txt
mv test_dir/example.txt test_dir/renamed_example.txt
```

### Explanation

- **`mkdir test_dir`** — Creates a new directory named `test_dir` in the current folder.
- **`touch test_dir/example.txt`** — Creates an empty file `example.txt` inside `test_dir`. `touch` updates the file’s access time or creates the file if it doesn’t exist.
- **`mv test_dir/example.txt test_dir/renamed_example.txt`** — Renames `example.txt` to `renamed_example.txt` in the same directory.

### Verification / Screenshot

Run `ls -la test_dir` to verify. You should see `renamed_example.txt`.

**Command:**
```bash
ls -la test_dir
```

**Sample output:**
```
total 0
drwxr-xr-x  2 user  staff   64 Feb 23 17:59 .
drwxr-xr-x  3 user  staff   96 Feb 23 17:59 ..
-rw-r--r--  1 user  staff    0 Feb 23 17:59 renamed_example.txt
```

---

## 2. Viewing File Contents

### 2a. Display full contents of /etc/passwd

**Command:**
```bash
cat /etc/passwd
```

**Explanation:** `cat` reads the file and prints its entire contents to the terminal. `/etc/passwd` is the system user database (user names, UIDs, home dirs, shells).

---

### 2b. First 5 lines only

**Command:**
```bash
head -5 /etc/passwd
```

**Explanation:** `head` prints the first few lines of a file. `-5` limits output to the first 5 lines.

**Sample output:**
```
##
# User Database
# 
# Note that this file is consulted directly only when the system is running
# in single-user mode.
```

---

### 2c. Last 5 lines only

**Command:**
```bash
tail -5 /etc/passwd
```

**Explanation:** `tail` prints the last few lines of a file. `-5` limits output to the last 5 lines.

**Sample output:**
```
_spinandd:*:305:305:SPINAND Daemon:/var/empty:/usr/bin/false
_corespeechd:*:306:306:CoreSpeech Services:/var/empty:/usr/bin/false
_diagnosticservicesd:*:307:307:Diagnostic Services:/var/empty:/usr/bin/false
_mds_stores:*:308:308:Spotlight File Metadata Index Daemon:/var/empty:/usr/bin/false
_oahd:*:441:441:OAH Daemon:/var/empty:/usr/bin/false
```

---

## 3. Searching for Patterns

**Command:**
```bash
grep "root" /etc/passwd
```

**Explanation:** `grep` searches for lines that contain the given pattern (here, the word `"root"`) in the specified file and prints only those lines.

**Sample output:**
```
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_cvmsroot:*:212:212:CVMS Root:/var/empty:/usr/bin/false
```

**Screenshot:** [Paste screenshot]

---

## 4. Zipping and Unzipping

### Commands used

```bash
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir
```

### Explanation

- **`zip -r test_dir.zip test_dir`** — Creates `test_dir.zip` containing `test_dir` and everything inside it. `-r` means “recursive” (include subdirectories and their files).
- **`unzip test_dir.zip -d unzipped_dir`** — Extracts the zip into a new directory `unzipped_dir`. `-d` specifies the destination directory.

### Verification

**Commands:**
```bash
ls -la test_dir.zip
ls -la unzipped_dir/
```

**Sample output (unzipped_dir):**
```
total 0
drwxr-xr-x  3 user  staff  96 Feb 23 17:59 .
drwxr-xr-x  5 user  staff 160 Feb 23 17:59 ..
drwxr-xr-x  3 user  staff  96 Feb 23 17:59 test_dir
```

---

## 5. Downloading Files

**Command:**
```bash
wget https://example.com/
```

To save with a specific name (e.g. `sample.txt`):

```bash
wget -O sample.txt https://example.com/
```

**Explanation:** `wget` downloads files from the given URL. `-O sample.txt` saves the content to the file `sample.txt`. (If `wget` is not installed, you can use `curl -o sample.txt https://example.com/` on macOS.)

---

## 6. Changing Permissions

**Commands used:**
```bash
touch secure.txt
chmod 444 secure.txt
```

**Explanation:**

- **`touch secure.txt`** — Creates an empty file `secure.txt`.
- **`chmod 444 secure.txt`** — Sets permissions to read-only for everyone. `444` means: owner = read (4), group = read (4), others = read (4). No write (2) or execute (1) bits, so the file is read-only for all.

**Verification:**
```bash
ls -la secure.txt
```

**Sample output:**
```
-r--r--r--  1 user  staff  0 Feb 23 17:59 secure.txt
```

The `r--r--r--` confirms read-only for owner, group, and others.

---

## 7. Working with Environment Variables

**Command:**
```bash
export MY_VAR="Hello, Linux!"
```

**Verification:**
```bash
echo $MY_VAR
```

**Explanation:** `export` makes the variable `MY_VAR` available to the current shell and to any programs started from it. `echo $MY_VAR` prints its value to confirm.

**Sample output:**
```
Hello, Linux!
```

**Note:** This variable lasts only in the current terminal session. To make it permanent, add the `export` line to `~/.bashrc` or `~/.zshrc`.

---

## Summary Checklist

| Task | Command(s) | Done |
|------|------------|------|
| 1. Create/rename dir & file | mkdir, touch, mv | ✓ |
| 2a. View file (full) | cat /etc/passwd | ✓ |
| 2b. First 5 lines | head -5 /etc/passwd | ✓ |
| 2c. Last 5 lines | tail -5 /etc/passwd | ✓ |
| 3. Search pattern | grep "root" /etc/passwd | ✓ |
| 4. Zip & unzip | zip -r, unzip -d | ✓ |
| 5. Download file | wget (or curl) | ✓ |
| 6. Read-only permissions | chmod 444 secure.txt | ✓ |
| 7. Environment variable | export MY_VAR="Hello, Linux!" | ✓ |

---
