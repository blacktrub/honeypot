#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging.config import dictConfig
from logging import getLogger

from flask import Flask, render_template, request, redirect, url_for

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.FileHandler',
        'filename': '/var/log/honeypot/app.log',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    },
    '': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
logger = getLogger(__name__)


@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        logger.info('try with %s %s', dict(request.form), dict(request.headers))
        if login == 'admin' and password == 'admin':
            return render_template('success.html')
        else:
            return redirect(url_for('admin_page'))
    logger.info('open with %s %s', dict(request.args), dict(request.headers))
    return render_template('admin.html')

