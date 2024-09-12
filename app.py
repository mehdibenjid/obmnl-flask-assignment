# Import libraries
from flask import Flask, request, url_for, redirect, render_template
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation
app.route('/', methods=['GET'])
def get_transactions():
    return render_template('transactions.html', transactions=transactions)
# Create operation
app.route('/add', methods=['GET','POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        data = request.form
# Update operation

# Delete operation

# Run the Flask app
    