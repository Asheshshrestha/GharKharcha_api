from django.core.mail import send_mail
import gharkharcha.settings as stng

def send_single_mail(subject,message,mail_address,fail_silently):
    '''
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
    '''
    sub = subject
    msg = message
    mail_from = ''
    mail_to = mail_address
    try:
        send_mail(
            subject = sub,
            message = msg,
            from_email= stng.EMAIL_HOST_USER ,
            recipient_list=[mail_to],
            fail_silently = fail_silently
        )
    except Exception as e:
        print("excepiton",str(e))
        return e

def send_mass_mail(subject,message,reciepent_list,fail_silently):
    '''
    (subject, message, from_email, recipient_list)
    '''

    sub = subject
    msg = message
    mail_from = ''
    mail_to = reciepent_list
    try:
        send_mail(
            sub,
            msg,
            mail_from,
            mail_to,
            fail_silently = fail_silently
        )
    except Exception as e:
        pass
    