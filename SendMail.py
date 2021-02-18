from email.message import EmailMessage
import smtplib, ssl

message  = EmailMessage()

message["from"] = "satishkr639@gmail.com"
message["to"] = "satishkr639@gmail.com"
message["subject"] = "Hi there, email from python"
body = "This is the body of automated mail"
message.set_content(body)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.send_message("satishkr639@gmail.com", "satishkr639@gmail.com", "Hi hello")
print(message)