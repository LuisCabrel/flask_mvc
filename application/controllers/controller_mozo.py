from application import app

from flask import Flask, jsonify  # importamos los modulos necesarios
from flask import render_template, request, redirect, url_for, flash, session
from application.models.model_user import User
from application.config.routes import urls

model = User()


@app.route(urls['mozo.pedido'], methods=['GET'])
def pedido():
    return render_template('mozo/pedido.html')