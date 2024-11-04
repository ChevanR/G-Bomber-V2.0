# G-Bomber
G-Bomber is a tool designed for use by security researchers to test email systems' resilience to bulk email sending. It is intended for educational and research purposes only.

## Legal Disclaimer
This software is provided "as is", without warranty of any kind, express or implied. The author expressly disclaims all liability for any misuse of this software. It is provided under the stipulation that it will be used responsibly and ethically, without intent to harm or harass others. Misuse for spamming or any unauthorized activity is strictly prohibited.

### Prerequisites
Before you begin, make sure you have the following:
- Python 3.x: Installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
- Internet Connection: Required to send emails via SMTP.
- Valid SMTP Server Credentials: You will need access to an SMTP server and valid credentials (username and password) that will allow you to send emails.

### Installing the Script
1. Clone the Repository: Download the script to your local machine by cloning the repository or directly downloading the source code.

git clone https://github.com/chevanr/g-bomber.git cd g-bomber


2. Configure SMTP Accounts:
- Create a text file named `accounts.txt` in the same directory as the script.
- Format the file with your SMTP credentials as follows:

  your-email@example.com:password
  
  second-email@example.com:secondpassword

- Each line represents one SMTP account. Make sure there are no extra spaces or lines.

### Running the Script
To run the script, open the command prompt, cd to the script's directory, and execute:

python G-Bomber.py

Follow the on-screen prompts to specify the recipient's email address, subject, message, number of emails, batch size, and the delay between batches.

## Configuration Tips
- SMTP Settings: Depending on your email provider, you might need to configure additional SMTP settings such as the server address and port. This script assumes defaults that are common for many services but check your provider's documentation.
- Security Settings: If using Gmail, you may need to set up an "App Password" if you have two-factor authentication enabled.

## Troubleshooting
- SMTP Connection Issues: If you encounter errors related to SMTP connections, ensure your credentials are correct and that your email provider hasn’t blocked your IP or requires additional security measures.
- Python Errors: Make sure you are using Python 3.x. Some older or incompatible versions might lead to unexpected issues.
- Email Not Sending: Check your spam folder and ensure that the emails aren’t being filtered out. Also, verify that you haven’t hit sending limits imposed by your email provider.

## Contributing
Contributions to this project are welcome. Please ensure that any enhancements or bug fixes are in line with ethical use and legal compliance.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

