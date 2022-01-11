from flask import Flask, render_template, request, redirect
from monitor import actu_wallet

app = Flask(__name__, template_folder='html')


@app.route("/add_crypto", methods=["GET", "POST"])
def add_crypto():
    if request.method == "POST":
        req = request.form

        rep = f"{req.get('crypto')}" + " " + f"{req.get('amount')}" + " " + f"{req.get('price')}" + " " + f"{req.get('levarage')}"
        print(rep)
        actu = []
        actu.append(rep)
        print(actu)
        return f"{actu_wallet(actu)}"

    return render_template('dashboard.html')
