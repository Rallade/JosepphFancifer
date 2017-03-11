from flask import Flask, request
from twilio import twiml
from nlp import fancify
app = Flask(__name__)




@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    fancy = fancify(message_body)
    resp = twiml.Response()
    #resp.message('Hello {}, you said: {}'.format(number, message_body))
    resp.message('This is now fancy:\n' + fancy)
    return str(resp)



if __name__ == '__main__':
    app.run()
