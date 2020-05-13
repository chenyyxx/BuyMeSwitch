import smtplib

def sentmail(link):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text+link)
    server.close()

    print('Email sent!')


gmail_user = 'chenyx.eric2013@gmail.com'
gmail_password = 'Arkcyx23'

sent_from = gmail_user
to = ['chenyx.eric2013@gmail.com', 'sding@macalester.edu']
subject = 'Switch IS AVAILABLE!!'
body = 'GO GET IT NOW!!!'
# body = test.body
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

# if __name__ == "__main__":
#     sentmail("aaa")
