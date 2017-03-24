# import smtplib

# from email.mime.text import MIMEText

# msg = MIMEText('Testing some Mailgun awesomness')
# msg['Subject'] = "Hello"
# msg['From']    = "foosmtp@mg.zhayitong.com"
# msg['To']      = "yitong@youngand.co"

# s = smtplib.SMTP('smtp.mailgun.org', 587)

# s.login('postmaster@mg.zhayitong.com', '1672577ea1fa321c3cbd1ab701a4b87c')
# s.sendmail(msg['From'], msg['To'], msg.as_string())
# s.quit()

import requests 
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/mg.zhayitong.com/messages",
        auth=("api", "key-cb5f815bb6358968c4fa5ec13e76cdda"),
        data={"from": "fooapi <fooapi@mg.zhayitong.com>",
              "to": ["yitong@youngand.co"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

send_simple_message()