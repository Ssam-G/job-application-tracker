from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = 'jobs.db'

allowed_statuses = ["Applied", "Interviewing", "Offered", "Accepted", "Rejected"]

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            title TEXT NOT NULL,
            date_applied TEXT NOT NULL,
            link TEXT,
            status TEXT NOT NULL DEFAULT "Applied"
        )
        """
    )
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    jobs = conn.execute("SELECT * FROM jobs ORDER BY date_applied DESC").fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

@app.route("/add", methods=["POST"])
def add_job():
    company = request.form.get("company", "").strip()
    if company == "":
        return redirect(url_for("index"))
    title = request.form.get("title", "").strip()
    if title == "":
        return redirect(url_for("index"))
    date_applied = request.form.get("date_applied", "").strip()
    if date_applied == "":
        return redirect(url_for("index"))
    link = request.form.get("link", "").strip()
    if link == "":
        link = None

    conn = get_db_connection()
    conn.execute("INSERT INTO jobs (company, title, date_applied, link) VALUES (?, ?, ?, ?)", (company, title, date_applied, link, ))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

@app.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit_job(job_id: int):
    conn = get_db_connection()
    job = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
    
    if job is None:
        conn.close()
        return redirect(url_for("index"))

    if request.method == "POST":
        company = request.form.get("company", "").strip()
        if company == "":
            conn.close()
            return redirect(url_for("index"))
        title = request.form.get("title", "").strip()
        if title == "":
            conn.close()
            return redirect(url_for("index"))
        date_applied = request.form.get("date_applied", "").strip()
        if date_applied == "":
            conn.close()
            return redirect(url_for("index"))
        link = request.form.get("link", "").strip()
        if link == "":
            link = None
        status = request.form.get("status", "").strip()
        if status not in allowed_statuses:
            conn.close()
            return redirect(url_for("index"))

        conn.execute(
            "UPDATE jobs SET company = ?, title = ?, date_applied = ?, link = ?, status = ? WHERE id = ?",
            (company, title, date_applied, link, status, job_id)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    conn.close()
    return render_template("edit.html", job=job, allowed_statuses=allowed_statuses, index=url_for("index"))

@app.route("/delete/<int:job_id>", methods=["POST"])
def delete_job(job_id: int):
    conn = get_db_connection()
    conn.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=5000, debug=True)