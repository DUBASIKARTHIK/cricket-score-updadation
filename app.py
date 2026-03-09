from flask import Flask, render_template, request, jsonify, redirect, url_for
from supabase import create_client

app = Flask(__name__)

# ─── Supabase Config ──────────────────────────────────────────────────────────
SUPABASE_URL = "https://kgmvprtxxvkaavqziwpx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtnbXZwcnR4eHZrYWF2cXppd3B4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTM0MTIyMCwiZXhwIjoyMDg2OTE3MjIwfQ.3N3nLWx7ZnfvSCdQOAbCn9TWByxCTep5Ycm3HVUigfI"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ─── Public Routes ────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("login.html")  # login page first

@app.route("/matches")
def matches():
    return render_template("matches.html")

@app.route("/match/<int:match_id>")
def match_live(match_id):
    return render_template("match_live.html", match_id=match_id)

@app.route("/ping")
def ping():
    return "Server is running"
# ─── Run ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
