"""
Created on April 12, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class AllowGPSPage(Page):
    """ Class contains elements from Allow GPS page """

    def __init__(self, driver):
        super(AllowGPSPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    allow_gps_access_android = (
        MobileBy.ID, 'de.komoot.android:id/button_request_permission')
    allow_location_access_android = (
        MobileBy.ID,
        'com.android.packageinstaller:id/permission_allow_button')

    # iOS
    allow_gps_access_ios = (
        MobileBy.ID, 'de.komoot.android:id/button_request_permission')
    allow_location_access_ios = (
        MobileBy.ID,
        'com.android.packageinstaller:id/permission_allow_button')

    def click_allow_gps_access_button(self):
        """
        Click on Allow element
        :return: None
        """
        el = self.wait_for_element_present(
            *getattr(self, 'allow_gps_access_' + self.os))
        el.click()

    def click_allow_location_access_button(self):
        """
        Click on Allow access element
        :return: None
        """
        el = self.wait_for_element_present(
            *getattr(self, 'allow_location_access_' + self.os))
        el.click()
