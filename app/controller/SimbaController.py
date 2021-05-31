from flask import *
from flask_mail import Mail, Message

simba = Blueprint('SimbaController', __name__, url_prefix='/simba')


@simba.route('/a', methods=['GET'])
def a():    
    return {'hello':'a-simba'}



@simba.route("/email", methods=['post', 'get'])
def email_test():
    print("email send test")
    if request.method == 'POST':
        req = request.get_json()
        senders = req['email_sender']
        receiver = req['email_receiver']
        content = req['email_content']
        receiver = receiver.split(',')
       
        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()
           
        print (receiver)
        """
        msg = Message('hello',sender='sagekhw5@gmail.com',recipients=['sagekhw2@gmail.com'])
        msg.body = 'Hello Flask'
        mail.send(msg)
        """
        result = send_email(senders, receiver, content)
        print("result:",result)
       
        if not result:
            return "hello"
            #return render_template('email.html', content="Email is sent")
        else:
            return "hello"
            #return render_template('email.html', content="Email is not sent")
       
    else:
        return "hello"
        #return render_template('email.html')
   
def send_email(senders, receiver, content):
    try:
        mail = Mail(app)
        msg = Message('Title', sender = senders, recipients = receiver)
        msg.body = content
        mail.send(msg)
    except Exception:
        pass
    finally:
        pass