# Use PixAI for SillyTavern Image Generation
Using scripts from https://github.com/Recentaly/PixAI-Wrapper

# 1. Requirements
- Google Chrome
- Python

# 2. How to use
## 2.1 Run init.bat
This will create python virtual environment and download essentials.
## 2.2 Fill account.txt file
First line for mail, second line for password.
```bash
example@mail.com
password1234
```
## 2.3 Run run.bat
It will open Google Chrome to login into your PixAI account and get token. Then the server on http://localhost:5000 will be started.
## 2.4 Configure Image Generation in SillyTavern
