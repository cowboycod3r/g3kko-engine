from g3kko import db
from datetime import date


# Buchung;Valuta;Auftraggeber/Empfänger;Buchungstext;Verwendungszweck;Betrag;Währung;Saldo;Währung

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False, default=date.today)
    value_date = db.Column(db.Date, nullable=False, default=date.today)
    principal = db.Column(db.Text, nullable=True)
    order_text = db.Column(db.Text, nullable=True)
    purpose = db.Column(db.Text, nullable=True)
    value = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False, default='USD')
    shares = db.Column(db.Float, nullable=True)
    isin = db.Column(db.String(12), nullable=True)

    def __repr__(self):
        return '<Transaction %i %s %f>' % (self.id, self.value_date, self.value)
