# **AutoFinanceMailer**

AutoFinanceMailer is a lightweight automation tool designedfor professionals in financial servies who are required to submit monthly investment statements to their employer or institution. Many financial institutions, especially in regualted environments, require employees to upload or submit these reoprts manually as part of their **compliance obligations**.

However, this manual processs is repetitive, time-consuming, and error-prone.

AutoFinanceMailer helps solve this by: 
- Automatically detecting when a new investment statemet is donwloaded
- Instantly sends that file to your work email (or compliance team) as a PDF attachment - with zero manual effot.
This tool saves time, reduces friction, and minimises the risk of missed reports, which could otherwise lead to compliance breaches.

## Features 
- Watches your Downloads folder recursively for new monthly statement PDFs
- Detects files with the pattern MonthlyStatement-YYYY-MM.pdf
- Automatically sends the detected file as an email attachment
- Configurable email settings via a separate config file
- CLI interface with a simple quit command 
- Mac and Windows compatible 9cross-platform via watchdog)

## Installation 
1. Clone the repo: 
```
git clone hteps:github.com/yourusername/AutoFinanceMailer.git
cd InvestMailAutomation
```

2. Install dependencies:
```
pip install watchdog
```

3. Set up your email configuration 
- Rename email_config.sample.py to email_config.py
- Fill in your email and SMTP credentials 

## Configuration 
**email_config.sample.py**

##Gmail SMTP Authentication Setup
To use Gmail's SMTP server emails securely, you need to authenticate using a special App Password (if you have 2-step Verification enabled on your Google account).

## What is a Gmail App Password? 
- A 16 character password displayed as 4 groups of 4 lowercase letters (e.g, abcd efgh ijkl mnop)
- Replaces your normal Gmail password specifically for apps that don't support OAuth2
- Used in email_config.py as gmail_pass

## How to generate a Gmail App Password: 
1. Go to Google Account security settings: 
https://myaccount.google.com/security
2. Enable 2-step Verification if not already on 
3. Generate an App password: 
   - Click App passwords
   - Choose "Mail" as the app
   - Select device (or use "Other" and name it "AutoFinanceMailer")
   - Click **Generate**
4. Copy the password shown (format: abcd efgh ijkl mnop) and paste it into your email_config.py


# Rename this file to email_config.py and fill in your credentials
```gmail_pass = "your_gmail_app_password_here"\
user = "your_email@gmail.com"
host = "smtp.gmail.com"
port = 465
receiver = "receiver_email@example.com"
subject = "Automated Trading Report"`
message = "This is an automated email of your Monthly Statement"
```


## Usage
Run monitor script:
```
python monitor.py
```
The app will recursively watch your home/Downloads folder for the target files.
To stop it, type q and press Enter.

## Planned Features
- **Persistent app execution:**
  - Package as an executable (e.g .exe or background service) that runs continuously 
  - Use pyintaller for creating platform-specific binaries
- **AI-powered email summaries:**
  - Use a local or cloud-based AI model to extract and summarise the key content of each monthly report
  - Summary included in the email body to provide context at a glance 
- **Reminder notifications:** 
  - A monthly reminder (e.g on the 1st) shown as a system notification on macOS and Windows
  - Useful when you forget to download the report - before compliance deadlines 
  - Cross-platform using player or win10toast + osascript
- **Company API integration:** 
  - Automate the final upload step by interacting directly with your employer's complaince software or internal API (if available)
  - Bypass the need to manually upload PDFs
- **Dynamic file matching support:**
  - Allow pattern customisation for different brokerages/platforms

## Lessons Learned 
- Regex for file detection must be precise to avoid missing or false-positive matches
- Some files may be detected before they're fully downloaded - adding a short delay can improve reliability 
- Packaging into executables for different platforms requires platform-specific testing and attention to dependencies 

