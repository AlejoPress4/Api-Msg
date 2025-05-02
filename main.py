from flask import Flask, request, jsonify
from src.send_email import Send_email
app = Flask(__name__)


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

@app.route('/payment_notification', methods=['POST'])
def payment_notification():
    try:
        info_request = request.get_json()
        
        # Validar campos requeridos (solo recipient y message como los otros endpoints)
        required_fields = ['recipient', 'message']
        if not all(field in info_request for field in required_fields):
            return jsonify({
                "mensaje": "the message could not be sent",
                "details": f"Missing required fields: {required_fields}"
            }), 400

        # Enviar el correo usando la clase Send_email (mismo formato que send_mail)
        email_sender = Send_email(
            message=info_request['message'],
            recipient=info_request['recipient']
        )

        if email_sender.send_the_payment_info():
            return jsonify({
                "mensaje": "the message has been sent"
            }), 200
        else:
            return jsonify({
                "mensaje": "the message could not be sent"
            }), 500

    except Exception as e:
        print(f"Error en payment_notification: {str(e)}")
        return jsonify({
            "mensaje": "the message could not be sent",
            "error": str(e)
        }), 500

# @app.route('/shares/<share_id>', methods=['GET'])
# def get_invoice(share_id):
#     invoice = invoices.get(share_id)
#     if invoice:
#         return jsonify(invoice), 200
#     else:
#         return jsonify({"error": "Factura no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)