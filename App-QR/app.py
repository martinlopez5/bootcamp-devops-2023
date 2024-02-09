from flask import Flask, render_template, request, send_file, make_response, url_for
from flask_sqlalchemy import SQLAlchemy
import qrcode
from io import BytesIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Float, nullable=False)
    num_people = db.Column(db.Integer, nullable=False)

# Lista global para almacenar los códigos QR
qr_codes = []

def generate_qr_codes(num_people, amount_per_person):
    global qr_codes
    qr_codes = []
    for i in range(1, num_people + 1):
        qr = qrcode.make(f"Pagar {amount_per_person:.2f} - Usuario {i}")
        qr_codes.append(qr)

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
    generate_qr_codes(num_people, amount_per_person)

    return render_template('result.html', num_people=num_people)

@app.route('/qrcode/<int:index>')
def qrcode_image(index):
    if index >= 1 and index <= len(qr_codes):
        img = BytesIO()
        qr_codes[index-1].save(img, format='PNG')
        img.seek(0)
        response = make_response(send_file(img, mimetype='image/png'))
        response.headers['Content-Disposition'] = f'inline; filename=qrcode_{index}.png'
        return response
    else:
        return "QR Code not found", 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')





