import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comemts):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'fc60eef28582a0'
    password = '4853c91af178a1'
    message = f"<h3>New feedback Submission</h3><ul><li>Customer:{customer}</li>" \
              f"<li>Dealer:{dealer}</li>" \
              f"<li>Rating:{rating}</li>" \
              f"<li>Comments:{comemts}</li></ul>"
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus - Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
