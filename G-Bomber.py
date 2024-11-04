import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ANSI Escape Sequences for colors
RED = '\033[91m'
GREEN = '\033[32m'
YELLOW = '\33[93m'
BLUE = '\33[94m'
END = '\033[0m'


def display_banner():
    os.system("clear || cls")
    print(RED + """  
          ▄████        ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
         ██▒ ▀█▒      ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
        ▒██░▄▄▄░ ████ ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
        ░▓█  ██▓ ▒ ▒▒ ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
        ░▒▓███▀▒ ░  ░ ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
         ░▒   ▒       ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
          ░   ░       ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
        ░ ░   ░        ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
             ░        ░          ░ ░         ░    ░         ░  ░   ░     
                    ░                           ░                 
    """ + END)
    print(RED + 'Supreme G-Bomber'.center(85))
    print(RED + 'Made By: Chev'.center(85))
    print(RED + 'Version: 2.0\n'.center(85) + END)


def load_accounts(filename):
    accounts = []
    with open(filename, 'r') as file:
        for line in file:
            if ':' in line:
                email, password = line.strip().split(':')
                accounts.append((email, password))
            else:
                print("Skipping malformed line:", line.strip())
    return accounts


def send_batch_emails(server, account_email, recipient, subject, message,
                      batch_size):
    msg = MIMEMultipart()
    msg['From'] = account_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    for _ in range(batch_size):
        try:
            server.send_message(msg)
            print(f'Email sent from {account_email}')
            time.sleep(
                2
            )  # Short delay between emails to avoid triggering spam filters
        except smtplib.SMTPServerDisconnected:
            print("Lost server connection. Reconnecting...")
            server.connect("smtp.gmail.com", 587)
            server.starttls()
            server.login(account_email,
                         password)  # Re-login after reconnection
            server.send_message(msg)
            print(f'Email re-sent from {account_email}')


def send_emails(account_list,
                recipient,
                subject,
                message,
                total_emails,
                batch_size=10,
                delay=300):
    emails_sent = 0
    while emails_sent < total_emails:
        for email, password in account_list:
            server = None
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)

                # Calculate the number of emails to send in this batch
                remaining_emails = total_emails - emails_sent
                emails_to_send = min(batch_size, remaining_emails)

                send_batch_emails(server, email, recipient, subject, message,
                                  emails_to_send)
                emails_sent += emails_to_send

                if emails_sent >= total_emails:
                    print("All emails have been sent.")
                    return

                print(f'Waiting {delay} seconds before the next batch...')
                time.sleep(delay)
            except Exception as e:
                print(f"An error occurred while sending from {email}: {e}")
            finally:
                if server:
                    server.quit()


def main():
    display_banner()
    accounts = load_accounts('accounts.txt')
    recipient = input('Enter the recipient email address: ')
    subject = input('Enter the email subject: ')
    message = input('Enter your message: ')
    count = int(input('How many times do you want to send the email? '))
    batch_size = int(input('Enter the number of emails per batch: '))
    delay = int(
        input('Enter delay between batches in seconds (default 60): '))
    send_emails(accounts, recipient, subject, message, count, batch_size, delay)


if __name__ == "__main__":
    main()
