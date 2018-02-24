from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'g3kko engine is running'


@app.route('/transaction', methods=['GET', 'POST'])
def transaction_api():
    if request.method == 'POST':
        return 'transaction/id'
    else:
        return 'returns the api definition of transaction (CRUD operations) or stores a new tansaction with new id'


@app.route('/transaction/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def transaction(id):
    return 'returns a transaction with id %d' % id


@app.route('/transactions')
def transactions():
    return 'returns the api definition of transactions (listing, search and filer operation of more than one element)'


@app.route('/fund')
def fund():
    return 'returns the api definition of fund (CRUD operations)'
