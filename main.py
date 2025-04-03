from flask import Flask, request, jsonify
from src.send_email import Send_email

app = Flask(__name__)

invoices = {
    "12345": {"share_id": "12345", "amount": 50000, "status": "pending", "due_date": "2025-04-10"},
    "67890": {"share_id": "67890", "amount": 75000, "status": "paid", "due_date": "2025-03-15"}
}

@app.route('/send_email', methods=['POST'])
def send_mail():
    
    info_request = request.get_json()
    tt = Send_email(info_request['message'], info_request['recipient'])
    if tt.send_the_email():
        respuesta = {
            "mensaje": "the message has been sent"
        }
    else:
        respuesta = {
            "mensaje": "the message could not be sent"
        }
    return jsonify(respuesta)


@app.route('/send_reset_link', methods=['POST'])
def send_reset_link():
    info_request = request.get_json()
    tt = Send_email(info_request['message'], info_request['recipient'])
    if tt.send_the_reset_link():
        respuesta = {
            "mensaje": "the message has been sent"
        }
    else:
        respuesta = {
            "mensaje": "the message could not be sent"
        }
    return jsonify(respuesta)

@app.route('/send_payment_info', methods=['POST'])
def send_payment_info():
    info_request = request.get_json()
    tt = Send_email(info_request['message'], info_request['recipient'], info_request['subject'])
    if tt.send_the_payment_info():
        respuesta = {
            "mensaje": "the message has been sent"
        }
    else:
        respuesta = {
            "mensaje": "the message could not be sent"
        }
    return jsonify(respuesta)

@app.route('/shares/<share_id>', methods=['GET'])
def get_invoice(share_id):
    invoice = invoices.get(share_id)
    if invoice:
        return jsonify(invoice), 200
    else:
        return jsonify({"error": "Factura no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)