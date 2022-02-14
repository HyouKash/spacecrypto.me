from app import app
from flask import Flask, render_template, request, redirect, make_response
from monitor import actu_wallet
import sqlite3
import random
import hashlib
import string
import base64

lower = string.ascii_letters + string.digits

@app.route("/dashboard", methods=["GET", "POST"])
def dash():
    user_id = request.cookies.get('user')
    if user_id:
        con = sqlite3.connect('app/dashboardV1.db')
        cur = con.cursor()
        cur.execute(f'''SELECT * from Cryptos where ID = "{user_id}"''')
        data = cur.fetchall()[0]
        con.close()
        if request.method == "POST":
            req = request.form

            rep = f"{req.get('webhook')}"
            con = sqlite3.connect('app/dashboardV1.db')
            cur = con.cursor()
            cur.execute(f'''UPDATE Cryptos SET webhook = "{rep}" WHERE ID = "{user_id}"''')
            con.commit()
            con.close()
        crypto_list = []
        for k in range(len(data)):
            if k == 0 or data[k] == None or data[k] == "":
                pass
            else:
                crypto_list.append(data[k])
        try:
            return render_template('temp.html', len = len(actu_wallet(crypto_list)), wallet = actu_wallet(crypto_list))
        except:
            return render_template('dashboard.html')
    else:
        m = hashlib.sha3_512()
        cookie = "".join([random.choice(lower) for _ in  range(50)])
        m.update(cookie.encode("UTF-8"))
        cookie = base64.b64encode(m.hexdigest().encode())
        data = (cookie.decode(), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        con = sqlite3.connect('app/dashboardV1.db')
        cur = con.cursor()
        cur.execute('''INSERT INTO Cryptos VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',data)
        con.commit()
        con.close()
        resp = make_response(render_template('dashboard.html'))
        resp.set_cookie('user', f'{cookie.decode()}')

        return resp