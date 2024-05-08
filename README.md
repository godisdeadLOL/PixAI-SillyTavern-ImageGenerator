# Use PixAI for SillyTavern Image Generation
Using scripts from https://github.com/Recentaly/PixAI-Wrapper

![alt text](https://github.com/godisdeadLOL/PixAI-SillyTavern-ImageGenerator/blob/main/images/2.png)

## My honest opinion
Images are generated pretty fast but they often lack quality. Can be very abstract or blurry. If you remove "masterpiece", "best quality" and similar from prompt you can even generate not anime pictures. Overall, I think it's a good free option for image generation in SillyTavern.

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
Set source to AUTOMATIC1111 and url to http://localhost:5000
<br><br>
![alt text](https://github.com/godisdeadLOL/PixAI-SillyTavern-ImageGenerator/blob/main/images/1.png)
