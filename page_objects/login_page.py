"""
Created on April 12, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class LoginPage(Page):
    """ Class contains elements from Login page """

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    continue_with_email_button_android = (
        MobileBy.ID, 'de.komoot.android:id/jka_v2_proceed_with_email_fragment')
    saved_email_button_android = (
        MobileBy.XPATH,
        '//android.widget.LinearLayout[@content-desc="mate.ajdukovic@gmail.com"]/android.widget.LinearLayout')

    # iOS
    continue_with_email_button_ios = (
        MobileBy.ID, 'de.komoot.android:id/jka_v2_proceed_with_email_fragment')
    saved_email_button_ios = (
        MobileBy.XPATH,
        '//android.widget.LinearLayout[@content-desc="mate.ajdukovic@gmail.com"]/android.widget.LinearLayout')

    def click_continue_with_email_button(self):
        """
        Click on Continue with email element
        :return: None
        """
        el = self.wait_for_element_present(
            *getattr(self, 'continue_with_email_button_' + self.os))
        el.click()

    def click_on_saved_email_button(self):
        """
        Click on Saved email element
        :return: None
        """
        el = self.wait_for_element_present(
            *getattr(self, 'saved_email_button_' + self.os))
        el.click()
