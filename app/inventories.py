from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import datetime

from .models.inventory import Inventory

from flask import Blueprint

bp = Blueprint('inventories', __name__)

class InventorySearch(FlaskForm):
    inventory_id = IntegerField('Inventory id')
    search = SubmitField('Search')

@bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
    available = True
    form = InventorySearch()
    seller_id = form.inventory_id.data
    if not seller_id:
        seller_id = 0
    inv = Inventory.get(seller_id)
    if len(inv) == 0:
        available = False
    return render_template('inventory.html',
                            sid = seller_id,
                           inventory_products=inv, form = form, available = available)
    


