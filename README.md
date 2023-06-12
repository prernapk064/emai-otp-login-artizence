login by email otp verification

here I have created endpoint register/ for registering by entering the email and password. for this, I have created registerAPI views.

after registration mail will be sent to your email which will contain otp.

the developer has to add their own email and password in the settings file, then he can send a mail to other Gmail using that.

to verify the OTP I have created an endpoint verify/ for verifying I have created verifyOTP views.
Users can sign in by verifying their email.


Installation guide:

pip install python
pip install Django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
