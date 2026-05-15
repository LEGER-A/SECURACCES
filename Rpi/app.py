from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__)

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

# accès autorisé seulement si admin connecté
@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect('id_utilisateurs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT uid, resultat, date FROM journaux_acces")
    access = cursor.fetchall()
    print(access)
    conn.close()

    return render_template("dashboard.html", journaux=access)

@app.route("/add_card", methods=["POST"])
def add_card():
    uid = request.form.get("uid")
    conn = sqlite3.connect("id_utilisateurs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cartes_rfid(uid) VALUES (?)",(uid,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")
    
def check_uid(uid):

    ## Connection a la base sqlite3
    conn = sqlite3.connect('id_utilisateurs.db')

    ## Creation d'un curseur
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM cartes_rfid WHERE uid=?",
        (uid,)
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
