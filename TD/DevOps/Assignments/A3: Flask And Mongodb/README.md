# A3: Flask and MongoDB — Assignment

This folder contains a Flask application with:

1. **`/api` route** — Returns a JSON list. The data is stored in a backend file (`data.json`), read by the server, and sent as the response.
2. **Frontend form** — Submits data to **MongoDB Atlas**. On success, the user is redirected to a page that shows **"Data submitted successfully"**. On error, the error message is shown on the same page (no redirect).

---

## Setup

### 1. Create a virtual environment (recommended)

If this folder name contains a colon (`:`), create the venv in the **parent** folder instead (see **Run (full sequence)** below).

```bash
cd "A3: Flask And Mongodb"
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MongoDB Atlas

1. Create a cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Get your connection string: **Cluster → Connect → Connect your application**.
3. Copy `.env.example` to `.env` and set your URI:

```bash
cp .env.example .env
# Edit .env and set MONGODB_URI to your Atlas connection string.
```

Example `.env`:

```
MONGODB_URI=mongodb+srv://USER:PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
MONGODB_DB=flask_a3
```

### 4. Run the app

The app loads variables from `.env` automatically. From the project folder:

```bash
python app.py
```

Or set the variable inline:

```bash
MONGODB_URI="your-connection-string" python app.py
```

The app runs at **http://127.0.0.1:5000**.

---

## Usage

| Action | Command or URL |
|--------|----------------|
| **Get JSON list from backend file** | Open or `curl http://127.0.0.1:5000/api` |
| **Open form** | http://127.0.0.1:5000/ |
| **After successful submit** | Redirect to `/success` → "Data submitted successfully" |
| **On submit error** | Error shown on the same form page |

### Example: Call `/api`

```bash
curl http://127.0.0.1:5000/api
```

Response: JSON array read from `data.json` (e.g. list of items with `id`, `name`, `description`).

---

## Project structure

```
A3: Flask And Mongodb/
├── app.py              # Flask app: /api, /, /submit, /success
├── data.json           # Backend file used by /api
├── requirements.txt
├── .env.example
├── README.md
└── templates/
    ├── index.html      # Form page (and error display)
    └── success.html    # "Data submitted successfully" page
```

---

### Suggested doc content

1. **`/api` route**
   - Screenshot or command: e.g. `curl http://127.0.0.1:5000/api` (or browser screenshot).
   - Short note: "The API reads the list from the backend file `data.json` and returns it as JSON."

2. **Form and MongoDB**
   - Screenshot of the form and of the success page ("Data submitted successfully").
   - Short note: "The form submits data to MongoDB Atlas. On success, the user is redirected to the success page; on error, the error is shown on the same page."

