import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hello"
msg['From']    = "foo@youngand.co"
msg['To']      = "zha.yitong@gmail.com"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('postmaster@youngand.co', '3kh9umujora5')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
