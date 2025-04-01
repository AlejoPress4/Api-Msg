from flask import Flask, request, jsonify
from src.send_email import Send_email

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

if __name__ == '__main__':
    app.run(debug=True)