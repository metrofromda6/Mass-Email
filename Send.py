import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass  # For securely entering passwords

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Prompt for email
your_email = input("Enter your email: ")

# Prompt for app password (if using two-step verification)
your_password = getpass.getpass("Enter your app password (or account password if not using 2FA): ")

# Email content
subject = 'H1 NEW RELEASE'
body = '''Hope this email finds you well!

Just wanted to send you an email to let you know about an up-and-coming artist we represent who goes by the name of H1, who has a new single called REDRUM featuring DIBZ, set for release on the 27th of September. Would love to get any feedback from you to further develop his project and brand within the industry.

https://soundcloud.com/h1frmda6/redrum-ft-dibz/s-nAoVDJmlfeD?si=5e8627c4e58f4d46acea3c45e84779b5&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing 

https://drive.google.com/file/d/1UOehFuN73vfl2rzKPibRywNLucXtmA3V/view?usp=sharing 

H1, Perth’s newest drill rapper, a rising star in the West, is back for his second release in 2024. REDRUM is set for release on Friday, September 27th. A single that reflects his life and the lives of people around him. H1’s raw lyrics, unique storytelling mixed with his clever wordplay is guaranteed to have listeners on the edge of their seat.

EPK attached below: 

https://drive.google.com/file/d/1SfZDlGrGJ2zIH3FKiyYoA6ROUi5H5esE/view?usp=share_link 

H1 - REDRUM will be available worldwide on Friday, 27th September 2024. 

Thank you so much for taking the time, and I hope you have a great rest of your week.

Regards,
Lindsay Hendley 
FPS Management Team.'''

# List of recipients
recipients = [
    'nfo_rn@your.abc.net.au',
    'radio.news@abc.net.au',
    'radio.news@sbs.com.au',
    'jjj.news@abc.net.au',
    'syd.news@sca.com.au',
    'newsroom@2gb.com',
    'breakfast@2ser.com',
    'nsw.news@abc.net.au',
    'sydnews@arn.com.au',
    'news@2sm.com.au',
    'news@nova969.com.au',
    'news@canberrafm.com.au',
    'ccnews@capitalradio.net.au',
    '666@your.abc.net.au',
    'bne.news@sca.com.au',
    'bnenews@arn.com.au',
    'radio.612@abc.net.au',
    'news.qld@abc.net.au',
    'news@4bc.com.au',
    'news@nova1069.com.au',
    'sanews@abc.net.au',
    'adelaidenews@arn.com.au',
    'news@fiveaa.com.au',
    'newsroom5rm.com',
    'news@nova919.com.au',
    'news@mytriplem.com.au',
    'ade_news@sca.com.au',
    'melnews@arn.com.au',
    'mel.news@sca.com.au',
    'news@fox.com.au',
    'news@nova100.com.au',
    'news@3aw.com.au',
    '774@your.abc.net.au',
    'abcradiomelbourne@abc.net.au',
    'abcnewswa@your.abc.net.au',
    'news@mix.com.au',
    'perth.newsroom@sca.com.au',
    'news@nova937.com.au',
    'news@6pr.com.au',
    'sxnews@sca.com.au',
    'huonfm@huonfm.com',
    'newsroom@ultra106five.com',
    'tasmania.news@abc.net.au',
    'news@mix1049.com.au',
    'abcdarwin@your.abc.net.au'
]

# Create a function to send the email
def send_email(recipients, subject, body):
    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(your_email, your_password)

        # Loop through all recipients
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = your_email
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body of the email to the message
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.sendmail(your_email, recipient, msg.as_string())
            print(f'Email sent to {recipient}')

        # Close the server connection
        server.quit()

    except smtplib.SMTPAuthenticationError:
        print("Error: Unable to authenticate. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to send the emails
send_email(recipients, subject, body)