# komoot-app-qa
This repository contains test "Login with existing user and verify user's tour is not recorded as user did not move during tour" for Komoot app using Appium tool and Android emulator.

Steps to execute test with Android and Appium:

1. Setup Appium
2. Install PyCharm
3. Install Python 3.6.8
4. Create and activate virtualenv
5. Install required packages (run: pip install -r requirements.txt)
6. Create Android emulator as per "desired_caps" from BaseTest class or set "desired_caps" for real device
7. Install Komoot app from Play store
8. Login to the Komoot app manually for first time with your email and save it with "Google Smart Lock" (this email will be used in automated test to login)
9. In the "LoginPage" class of this repo adjust locator "saved_email_button_android" to fit your email. 
   For me it is: 
   ```
   (MobileBy.XPATH, '//android.widget.LinearLayout[@contentdesc="mate.ajdukovic@gmail.com"]/android.widget.LinearLayout')
   ```
9. Run tests from project root directory with command: nosetests -s --tc-format=python tests.test_tour_not_saved

Example of test run: https://www.youtube.com/watch?v=FU6Z75Ba4LM
