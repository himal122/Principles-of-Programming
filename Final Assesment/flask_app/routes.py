from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from forms import LoginForm
from models import User, StockItem, NavSys
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
import traceback
import logging

# Set up logging for errors
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    try:
        # Get filter values from URL (like price and stock type)
        min_price = request.args.get('min_price', default=None, type=float)
        max_price = request.args.get('max_price', default=None, type=float)
        stock_type = request.args.get('stock_type', default='', type=str)

        # basic query for stock items
        query = StockItem.query

        # filter by min price
        if min_price is not None:
            query = query.filter(StockItem.price >= min_price)
        # filter by max price
        if max_price is not None:
            query = query.filter(StockItem.price <= max_price)
        
        # filter by stock type
        if stock_type:
            if stock_type == 'NavSys':
                query = query.filter(StockItem.type == 'navsys')
            elif stock_type == 'StockItem':
                query = query.filter(StockItem.type == 'stock_item')

        # if no value is given in search input, return all items
        search_query = request.args.get('query', '').strip()

        if search_query:
            # search stock items by stock code
            query = query.filter(StockItem.stock_code.ilike(f'%{search_query}%'))

        # Pagination for the page
        page = request.args.get('page', 1, type=int)
        stock_items = query.paginate(page=page, per_page=10)

        # Render the page with results
        return render_template('index.html', 
                               stock_items=stock_items, 
                               query=search_query, 
                               min_price=min_price, 
                               max_price=max_price, 
                               stock_type=stock_type)
    except Exception as e:
        # error logger
        logger.error(f"Error in home page: {str(e)}")
        logger.error(traceback.format_exc())
        flash("Error while loading the page.", "error")
        return redirect(url_for('error_page'))


@app.route('/api/search_suggestions', methods=['GET'])
def search_suggestions():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify({"suggestions": []})

    # Get stock items matching the search query as a suggesstion
    suggestions = StockItem.query.filter(StockItem.stock_code.ilike(f'%{query}%')).limit(5).all()
    
    # Return the list of suggestions
    suggestion_list = [item.stock_code for item in suggestions]
    return jsonify({"suggestions": suggestion_list})


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()

        # Check if there are any users in the database
        user_exists = User.query.first() is not None
        if not user_exists:
            flash('No users found. Please contact the administrator.', 'warning')
            return render_template('login.html', title='Sign In', form=form)

        # If the form is submitted, check the credentials
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password', 'error')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('index'))
        
        return render_template('login.html', title='Sign In', form=form)
    
    except Exception as e:
        # erro logger
        logger.error(f"Error in login page: {str(e)}")
        logger.error(traceback.format_exc())
        flash("Error during login.", "error")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/add_stock_item', methods=['GET', 'POST'])
@login_required
def add_stock_item():
    try:
        if request.method == 'POST':
            # Get stock item details from the form
            item_type = request.form['item_type']
            stock_code = request.form['stock_code']
            quantity = int(request.form['quantity'])
            price = float(request.form['price'])
            vat_rate = float(request.form['vat_rate'])
            max_quantity = int(request.form['max_quantity'])
            brand = request.form.get('brand')

            # Check if brand is required but missing
            if item_type == 'NavSys' and not brand:
                flash('Brand is required for Navigation Systems.', 'error')
                return redirect(url_for('add_stock_item'))

            # Check if stock item already exists
            existing_item = StockItem.query.filter_by(stock_code=stock_code).first()
            if existing_item:
                flash(f'Stock code "{stock_code}" already exists. Please use a unique stock code.', 'warning')
                return redirect(url_for('add_stock_item'))

            # Create stock based on type
            if item_type == 'NavSys' and brand:
                stock_item = NavSys(
                    stock_code=stock_code, 
                    quantity=quantity, 
                    price=price, 
                    vat_rate=vat_rate, 
                    max_quantity=max_quantity, 
                    brand=brand
                )
            else:
                stock_item = StockItem(
                    stock_code=stock_code, 
                    quantity=quantity, 
                    price=price, 
                    vat_rate=vat_rate, 
                    max_quantity=max_quantity
                )

            # Save new stock item
            db.session.add(stock_item)
            db.session.commit()
            flash('Stock item added successfully!')
            return redirect(url_for('index'))

        return render_template('add_stock_item.html', title='Add Stock Item')
    
    except Exception as e:
        # error logger
        logger.error(f"Error in add_stock_item page: {str(e)}")
        logger.error(traceback.format_exc())
        flash("Error occurred while adding the stock item.", "error")
        return redirect(url_for('add_stock_item'))


@app.route('/delete_stock_item/<int:id>', methods=['POST'])
@login_required
def delete_stock_item(id):
    try:
        # delete stock item by ID
        stock_item = StockItem.query.get_or_404(id)
        db.session.delete(stock_item)
        db.session.commit()
        flash('Stock item deleted successfully!', 'success')
        return redirect(url_for('index'))
    
    except Exception as e:
        # error logger
        logger.error(f"Error in delete_stock_item: {str(e)}")
        logger.error(traceback.format_exc())
        flash("Error occurred while deleting the stock item.", "error")
        return redirect(url_for('index'))


@app.route('/update_stock_item/<int:id>', methods=['GET', 'POST'])
@login_required
def update_stock_item(id):
    try:
        # Get stock item by ID
        stock_item = StockItem.query.get_or_404(id)
        if request.method == 'POST':
            try:
                # Get updated details from form
                quantity = int(request.form['quantity'])
                price = float(request.form['price'])
                max_quantity = int(request.form['max_quantity'])
                vat_rate = float(request.form['vat_rate'])
            except ValueError:
                flash('Invalid input. Please fill all the fields.', 'error')
                return redirect(url_for('update_stock_item', id=id))

            if isinstance(stock_item, NavSys):
                stock_item.brand = request.form['brand']

            # validations
            if quantity < 0:
                flash('Quantity cannot be negative.', 'error')
                return redirect(url_for('update_stock_item', id=id))

            if price < 0:
                flash('Price cannot be negative.', 'error')
                return redirect(url_for('update_stock_item', id=id))

            if quantity > max_quantity:
                flash('Quantity cannot exceed max quantity.', 'error')
                return redirect(url_for('update_stock_item', id=id))

            # Update stock item in database
            stock_item.quantity = quantity
            stock_item.price = price
            stock_item.vat_rate = vat_rate
            stock_item.max_quantity = max_quantity
            stock_item.last_updated = datetime.now()

            # save changes
            db.session.commit()
            flash('Stock item updated successfully!', 'success')
            return redirect(url_for('index'))

        return render_template('update_stock_item.html', title='Update Stock Item', stock_item=stock_item)

    except Exception as e:
        # error logger
        logger.error(f"Error updating stock item with ID {id}: {e}")
        logger.error(traceback.format_exc())
        flash('Error occurred while updating the stock item.', 'error')
        return redirect(url_for('error_page'))


# Handle 404 errors (Page not found error)
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', title="Page Not Found", message="Page does not exist."), 404

# Handle 500 errors (Internal server error)
@app.errorhandler(500)
def internal_error(error):
    # error logger
    logger.error("Internal server error: %s", str(error))
    logger.error(traceback.format_exc())
    return render_template('error.html', title="Internal Server Error", message="Unexpected error occurred. Please try again later."), 500

# Generic error handler
@app.route('/error')
def error_page():
    return render_template('error.html', title="Error", message="An error occurred. Please try again later.")
