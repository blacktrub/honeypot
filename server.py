#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if login == 'admin' and password == 'admin':
            return render_template('success.html')
        else:
            return redirect(url_for('admin_page'))
    return render_template('admin.html')

