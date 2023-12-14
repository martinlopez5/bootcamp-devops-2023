from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import qrcode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Float, nullable=False)
    num_people = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    total_amount = float(request.form['total_amount'])
    num_people = int(request.form['num_people'])

    amount_per_person = total_amount / num_people

    # Guardar la transacción en la base de datos
    transaction = Transaction(total_amount=total_amount, num_people=num_people)
    db.session.add(transaction)
    db.session.commit()

    # Generar códigos QR
    qr_codes = []
    for i in range(1, num_people + 1):
        qr = qrcode.make(f"Pagar {amount_per_person:.2f} - Usuario {i}")
        qr_codes.append(qr)

    return render_template('result.html', qr_codes=qr_codes)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')

