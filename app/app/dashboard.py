from app import app
from flask import Flask, render_template, request, redirect, make_response
from monitor import actu_wallet
import sqlite3
import random
import hashlib
import string
import base64

lower = string.ascii_letters + string.digits

@app.route("/add_crypto", methods=["GET", "POST"])
def add_crypto():
    user_id = request.cookies.get('user')
    if user_id:
        con = sqlite3.connect('/home/web/spacecrypto/app/app/dashboardV1.db')
        cur = con.cursor()
        cur.execute(f'''SELECT * from Cryptos where ID = "{user_id}"''')
        data = cur.fetchall()[0]
        con.close()
        if request.method == "POST":

            req = request.form
            
            rep = f"{req.get('crypto')}" + "|" + f"{req.get('amount')}" + "|" + f"{req.get('levarage')}" + "|" + f"{req.get('price')}"
            crypto = rep.split("|")[0]
            con = sqlite3.connect('app/dashboardV1.db')
            cur = con.cursor()
            cur.execute(f'''UPDATE Cryptos SET {crypto} = "{rep}" WHERE ID = "{user_id}"''')
            con.commit()
            con.close()
        return render_template("dashboard.html")
    else:
        m = hashlib.sha3_512()
        cookie = "".join([random.choice(lower) for _ in  range(50)])
        m.update(cookie.encode("UTF-8"))
        cookie = base64.b64encode(m.hexdigest().encode())
        data = (cookie.decode(), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        con = sqlite3.connect('app/dashboardV1.db')
        cur = con.cursor()
        cur.execute('''INSERT INTO Cryptos VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',data)
        con.commit()
        con.close()
        resp = make_response(render_template('dashboard.html'))
        resp.set_cookie('user', f'{cookie.decode()}')

        return resp
