from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Portfolio
from . import db
from .data import currentPrice  

import json

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
def add_asset():


    if request.method == 'POST':

        asset = request.form.get('asset')
        asset_type = request.form.get('assetType')
        if(asset_type == 'on'):
            asset_type = 'Crypto'
        else:
            asset_type = 'Stock'
        bought = request.form.get('bought')
        quantity = request.form.get('quantity')
        date_bought = request.form.get('date_bought')


        if len(asset) < 1:
                flash('Asset is too short!', category='error')
        else:
                newass = Portfolio(asset=asset, asset_type=asset_type, bought=bought, quantity=quantity, date_bought=date_bought, user_id=current_user.id)
                db.session.add(newass)
                db.session.commit()

    return render_template("home.html", user=current_user)            


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
    
@views.route('/delete-asset', methods=['POST'])
def delete_asset():
    portfolio = json.loads(request.data)
    portfolioId = portfolio['portfolioId']
    portfolio = Portfolio.query.get(portfolioId)

    if portfolio:
        if portfolio.user_id == current_user.id:
            db.session.delete(portfolio)
            db.session.commit()

    return jsonify({})