# Use PixAI for SillyTavern Image Generation
Using scripts from https://github.com/Recentaly/PixAI-Wrapper

![alt text](https://github.com/godisdeadLOL/PixAI-SillyTavern-ImageGenerator/blob/main/images/2.png)

## My honest opinion
https://pixai.art/generator/realtime/drawing is used.

Images are generated pretty fast but they often lack quality. Can be very abstract or blurry. If you remove "masterpiece", "best quality" and similar from prompt you can even generate not anime pictures. Overall, I think it's a good free option.

# 1. Requirements
- Google Chrome
- Python

# 2. How to use
## 2.1 Download and unpack somewhere
## 2.2 Run init.bat
This will create python virtual environment and download essentials. Wait until cmd closes.
## 2.3 Fill account.txt file with your PixAI account
First line for mail, second line for password.
```bash
example@mail.com
password1234
```
## 2.4 Run run.bat
It will open Google Chrome to login into your PixAI account and get token. **Do not fear.** Then the server on http://localhost:5000 will be started.
## 2.5 Configure Image Generation in SillyTavern
Set source to AUTOMATIC1111 and url to http://localhost:5000
<br><br>
![alt text](https://github.com/godisdeadLOL/PixAI-SillyTavern-ImageGenerator/blob/main/images/1.png)
## 2.6 Test it
Write `/sd (your prompts)` in any chat to test if it works.
