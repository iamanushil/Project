# A4: Version Control Git — Assignment Guide

Replace **YOUR_USERNAME** (e.g. `Tutedude`) with your actual username in all commands below.

---

## Prerequisites

- Git installed
- GitHub account
- SSH key added to GitHub (see Task 1)
- Python 3 with `pip install -r requirements.txt` (Flask, pymongo)
- Optional: MongoDB running locally for `/submittodoitem` (or use a cloud URI in `MONGODB_URI`)

---

## Task 1: New repo, clone via SSH, branch by username, merge to main

### 1.1 Create a new GitHub repository

- On GitHub: **New repository** (e.g. `a4-version-control-git`), **no** README, .gitignore, or license.
- Copy the SSH clone URL (e.g. `git@github.com:YOUR_USERNAME/a4-version-control-git.git`).

### 1.2 SSH key (if you don’t have one)

```bash
# Generate SSH key (use your email)
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/id_ed25519 -N ""

# Show public key and add it in GitHub: Settings → SSH and GPG keys → New SSH key
cat ~/.ssh/id_ed25519.pub
```

### 1.3 Clone and add Flask project

```bash
# Clone (use your repo’s SSH URL)
git clone git@github.com:YOUR_USERNAME/a4-version-control-git.git
cd a4-version-control-git

# Copy this assignment’s Flask project files into the repo (all files from this A4 folder)
# Then:
git add .
git status
git commit -m "Initial Flask project with /api and structure"
git push -u origin main
```

If your default branch is `master`, use `master` instead of `main`, or rename: `git branch -M main`.

### 1.4 Branch named after your username and merge into main

```bash
# Create branch named after your username (e.g. Tutedude)
git checkout -b YOUR_USERNAME

# Ensure all Flask files are added and committed
git add .
git status
git commit -m "Add Flask project files on YOUR_USERNAME branch"

# Merge into main
git checkout main
git merge YOUR_USERNAME -m "Merge YOUR_USERNAME branch into main"
git push origin main
```

**Explanation:** You created a branch with your username, added/committed the Flask project there, then merged that branch into `main` and pushed.

---

## Task 2: Branch `<your_name>_new`, update API JSON, merge, resolve conflicts

### 2.1 Create branch and update JSON for `/api`

```bash
git checkout main
git pull origin main
git checkout -b YOUR_USERNAME_new
```

Edit **`data/api_data.json`** (this file is used by the `/api` route). Example update:

```json
{
  "message": "Updated by YOUR_USERNAME_new branch",
  "version": "2.0",
  "items": ["item1", "item2"]
}
```

```bash
git add data/api_data.json
git commit -m "Update API JSON content in YOUR_USERNAME_new branch"
git push -u origin YOUR_USERNAME_new
```

### 2.2 Merge into main and resolve conflicts

```bash
git checkout main
git merge YOUR_USERNAME_new -m "Merge YOUR_USERNAME_new into main"
```

- If Git reports **conflicts**, open the conflicted file(s), keep the version from **YOUR_USERNAME_new** (the content you just added), then:

```bash
git add .
git commit -m "Resolve merge conflicts, accept YOUR_USERNAME_new changes"
```

- If no conflicts, the merge commit is already created.

```bash
git push origin main
```

**Explanation:** You updated the JSON used by `/api` on a separate branch, merged it into `main`, and if there were conflicts you resolved them by keeping the changes from `YOUR_USERNAME_new`, then staged, committed, and pushed.

---

## Task 3: master_1 (To-Do page) and master_2 (/submittodoitem), then merge both

### 3.1 Create branches from main

```bash
git checkout main
git pull origin main
git checkout -b master_1
git checkout main
git checkout -b master_2
```

### 3.2 Feature in master_1: To-Do page

The To-Do page is already in this project: **`templates/todo.html`** with form fields **Item Name** and **Item Description**. If you started from this repo, record that on `master_1`:

```bash
git checkout master_1
git add templates/todo.html templates/base.html templates/index.html
git commit -m "Add To-Do page with Item Name and Item Description form"
git push -u origin master_1
```

### 3.3 Feature in master_2: Backend /submittodoitem

The route **`/submittodoitem`** is in **`app.py`**: it accepts **itemName** and **itemDescription** via POST and stores them in MongoDB. Record it on `master_2`:

```bash
git checkout master_2
git add app.py
git commit -m "Add /submittodoitem route, POST itemName and itemDescription, store in MongoDB"
git push -u origin master_2
```

### 3.4 Merge both into main

```bash
git checkout main
git merge master_1 -m "Merge master_1: To-Do page"
git merge master_2 -m "Merge master_2: /submittodoitem backend"
git push origin main
```

**Explanation:** Two branches were created from `main`: `master_1` for the frontend To-Do form, `master_2` for the backend route. Both were merged into `main`.

---

## Task 4: Add Item ID, Item UUID, Item Hash (3 commits), reset main, re-commit, rebase

### 4.1 Add three fields in master_1 in three separate commits

```bash
git checkout master_1
git merge main -m "Sync master_1 with main before Task 4"
```

**First commit: Item ID**

In **`templates/todo.html`**, after the “Item Description” block and before the submit button, add:

```html
  <p>
    <label>Item ID <input type="text" name="itemId" /></label>
  </p>
```

Then:

```bash
git add templates/todo.html
git commit -m "Add Item ID field to To-Do form"
```

**Second commit: Item UUID**

In **`templates/todo.html`**, after the Item ID block, add:

```html
  <p>
    <label>Item UUID <input type="text" name="itemUuid" /></label>
  </p>
```

```bash
git add templates/todo.html
git commit -m "Add Item UUID field to To-Do form"
```

**Third commit: Item Hash**

After the Item UUID block, add:

```html
  <p>
    <label>Item Hash <input type="text" name="itemHash" /></label>
  </p>
```

```bash
git add templates/todo.html
git commit -m "Add Item Hash field to To-Do form"
```

### 4.2 Merge master_1 into main

```bash
git checkout main
git merge master_1 -m "Merge master_1: To-Do form with Item ID, UUID, Hash"
git push origin main
```

### 4.3 Reset main to “only Item ID” (--soft), re-commit, push

Roll back `main` to the state where only the Item ID field was added, using **git reset --soft** so you can re-commit.

```bash
git checkout main
git log --oneline -6
```

Identify **ID_COMMIT** = hash of **"Add Item ID field to To-Do form"** (first of the three Task 4 commits). Then either:

**Option A – Reset to that commit and force-push (simplest):**

```bash
git reset --hard ID_COMMIT
git push origin main --force
```

**Option B – Use --soft and re-commit (as per assignment):**

- **PARENT** = hash of the commit *before* “Add Item ID” (parent of ID_COMMIT).

```bash
git reset --soft PARENT
git reset HEAD
# Edit templates/todo.html so it has only Item Name, Item Description, and Item ID (remove UUID and Hash).
git add templates/todo.html
git commit -m "Add Item ID field to To-Do form (re-committed after reset)"
git push origin main --force
```

**Explanation:** Main is rolled back to the commit where only the Item ID field was added. Option A just moves `main` to that commit; Option B uses `--soft` and a new commit.

### 4.4 Rebase master_1 onto main (preserve individual commits, no squash)

```bash
git checkout master_1
git rebase main
```

If there are conflicts, fix them (keep the form with all fields), then:

```bash
git add .
git rebase --continue
```

**Explanation:** `master_1` is rebased onto the updated `main`, so its history is replayed on top of the “Item ID only” state. Individual commits are preserved (no squash).

---

## Submission

- **Screenshots or commands:** For each task, attach screenshots of the terminal (commands and output) or paste the commands with a short explanation.
- **Doc:** Submit in Google Doc or Microsoft Word; include the GitHub repo link.
- **Repo link:** Share the link to your GitHub repository (e.g. `https://github.com/YOUR_USERNAME/a4-version-control-git`).

---

## Run the app locally

```bash
cd "A4: Version Control Git"
pip install -r requirements.txt
# Optional: export MONGODB_URI="mongodb://localhost:27017/"
python app.py
```

- Home: http://127.0.0.1:5000/
- API (JSON): http://127.0.0.1:5000/api
- To-Do: http://127.0.0.1:5000/todo
