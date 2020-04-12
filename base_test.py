# -*- coding: utf-8 -*-
"""
Created on April 12, 2020

@author: Mate Ajdukovic
"""
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from nose.tools import assert_true


class BaseTest:
    """
    This class deals with starting Appium session and setting Komoot app to the initial state
    All test classes extend this class
    """
    desired_caps = {
          "platformName": "Android",
          "platformVersion": "9.0",
          "automationName": "uiautomator2",
          "deviceName": "Android Emulator",
          "avd": "Pixel_2_API_28",
          "appPackage": "de.komoot.android",
          "appActivity": "de.komoot.android.app.InspirationActivity"
    }

    def setup(self):
        """
        Create driver instance with desired capabilities which will be used through tests suite
        """
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=self.desired_caps)

    # def bla(self):
    #     self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
    #                                    desired_capabilities=self.desired_caps)
    #     continue_with_email = self.driver.find_element_by_id('de.komoot.android:id/jka_v2_proceed_with_email_fragment')
    #     continue_with_email.click()
    #
    #     time.sleep(3)
    #
    #     saved_email = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="mate.ajdukovic@gmail.com"]/android.widget.LinearLayout')
    #     saved_email.click()
    #
    #     time.sleep(7)
    #
    #     allow_gps_access = self.driver.find_element_by_id('de.komoot.android:id/button_request_permission')
    #     allow_gps_access.click()
    #
    #     time.sleep(2)
    #
    #     allow_location_access = self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
    #     allow_location_access.click()
    #
    #     time.sleep(2)
    #
    #     record_header = self.driver.find_element_by_accessibility_id('MAP')
    #     record_header.click()
    #
    #     time.sleep(2)
    #
    #     start_recording_button = self.driver.find_element_by_id('de.komoot.android:id/button_tracking_start')
    #     start_recording_button.click()
    #
    #     time.sleep(2)
    #
    #     stop_button = self.driver.find_element_by_id('de.komoot.android:id/msb_stop_button_tb')
    #
    #     actions = TouchAction(self.driver)
    #     actions.long_press(stop_button)
    #     actions.perform()
    #
    #     time.sleep(2)
    #
    #     start_recording_button = self.driver.find_element_by_id('de.komoot.android:id/button_tracking_start')
    #
    #     assert_true(start_recording_button.is_displayed(), "Start recording button is not displayed")
    #     print("Start recording button is displayed, user's tour is not saved.")
    #
    #     time.sleep(10)
    #
    #     self.driver.quit()

    def teardown(self):
        """
        Quit driver session and close app
        """
        self.driver.quit()
