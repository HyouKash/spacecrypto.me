from app import app
from flask import Flask, render_template, request, redirect
from monitor import actu_wallet

@app.route("/add_crypto", methods=["GET", "POST"])
def add_crypto():
    if request.method == "POST":

        req = request.form
        
        rep = f"{req.get('crypto')}" + " " + f"{req.get('amount')}" + " " + f"{req.get('levarage')}" + " " + f"{req.get('price')}"
        actu = []
        actu.append(rep)
        return f"{actu_wallet(actu)}"

    return render_template('dashboard.html')
