from flask import Flask, request, jsonify, render_template, redirect, session
import sqlite3
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "SECURACCES_SECRET"

API_TOKEN = "SECURACCES_CIEL_E6"

@app.route('/api/access', methods=['POST'])
def api_access():

    auth_header = request.headers.get("Authorization")

    if auth_header != f"Bearer {API_TOKEN}":
        return jsonify({"access": "deny"}), 401

    data = request.get_json()

    uid = data.get("uid")

    print("UID reçu :", uid)
    result = check_uid(uid)

    return jsonify({"access": result})

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect("id_utilisateurs.db")
        cursor = conn.cursor()
        bcrypt = Bcrypt()
        cursor.execute("SELECT * FROM admins WHERE username=?",(username,))
        admin = cursor.fetchone()

        conn.close()

        if admin:
            hash_password = admin[2]
            if bcrypt.check_password_hash(hash_password, password):
                session["admin"] = username
                return redirect("/dashboard")

    return render_template("login.html")


# accès autorisé seulement si admin connecté
@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/login")

    conn = sqlite3.connect('id_utilisateurs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT uid, resultat, date FROM journaux_acces")
    access = cursor.fetchall()
    cursor.execute("SELECT uid FROM cartes_rfid")
    cartes_rfid = cursor.fetchall()
    conn.close()

    return render_template("dashboard.html", journaux=access, cartes=cartes_rfid)

@app.route("/add_card", methods=["POST"])
def add_card():
    uid = request.form.get("uid")
    conn = sqlite3.connect("id_utilisateurs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cartes_rfid(uid) VALUES (?)",(uid,))

    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/delete_card", methods=["POST"])
def delete_card():
    uid = request.form.get("uid")
    conn = sqlite3.connect("id_utilisateurs.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cartes_rfid WHERE uid=?",(uid,))

    conn.commit()
    conn.close()

    return redirect("/dashboard")

def check_uid(uid):

    ## Connection a la base sqlite3
    conn = sqlite3.connect('id_utilisateurs.db')

    ## Creation d'un curseur
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM cartes_rfid WHERE uid=?",(uid,)
    )

    card = cursor.fetchone()

    if card:
        result = "allow"
    else:
        result = "deny"

    cursor.execute(
        "INSERT INTO journaux_acces(uid, resultat) VALUES (?,?)",
        (uid, result)
    )

    conn.commit()
    conn.close()

    return result
    


app.run(host='0.0.0.0', port=5000)
