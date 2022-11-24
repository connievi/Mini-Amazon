from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.user import User


from flask import Blueprint
bp = Blueprint('products', __name__)

from .models.product import Product
from .models.purchase import Purchase


class ProductsKInput(FlaskForm):
    value = IntegerField('Get top k expensive products') or 0
    search = SubmitField('Search')

class ProductsKInput(FlaskForm):
    value = IntegerField('Get top k expensive products') or 0
    search = SubmitField('Search')

class FilterProductCategory(FlaskForm):
    category = StringField('Enter Name')
    search = SubmitField('Enter Name')


@bp.route('/products', methods = ['GET', 'POST'])
def index():    

    # form corresponds with top K
    form1 = ProductsKInput()
    form2 = FilterProductCategory()
    # k = form1.value.data
    
    # if k is None:
    #     products = []
    # else:
    #     products = Product.get_top_K_expensive(True, k)

    products = Product.get_all(True)    
    return render_template('products.html',
                           avail_products=products, form1 = form1, form2 = form2)

@bp.route('/product-detail/<product_id>', methods=['GET', 'POST'])
def detail_product(product_id):
    form1 = ProductsKInput()
    form2 = FilterProductCategory()
    
    # Feedback.update_review(review_id,
    #                      form.review.data)
    # if request.method == "POST":
    #     return redirect(url_for('feedback.feedback'))
    return render_template('product-detail.html',
                             form1 = form1, form2 = form2)
