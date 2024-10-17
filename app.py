import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # Get the message the user sent
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    # Define responses based on incoming messages
    if 'hello' in incoming_msg:
        msg.body('Hi there! How can I assist you today?')
    elif 'bye' in incoming_msg:
        msg.body('Goodbye! Have a great day!')
    else:
        msg.body('I am sorry, I did not understand that. Can you please rephrase?')

    return str(response)

if __name__ == '__main__':
    # Use the environment variable for the port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
