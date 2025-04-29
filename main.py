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
        
        # Validar campos requeridos
        required_fields = ['recipient', 'message', 'subject']
        if not all(field in info_request for field in required_fields):
            return jsonify({
                "status": "error",
                "message": "Missing required fields",
                "required": required_fields
            }), 400

        # Enviar el correo usando la clase Send_email
        email_sender = Send_email(
            message=info_request['message'],
            recipient=info_request['recipient'],
            subject_line=info_request['subject']
        )

        if email_sender.send_the_payment_info():
            return jsonify({
                "status": "success",
                "message": "Payment notification sent successfully"
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "Failed to send payment notification"
            }), 500

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
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