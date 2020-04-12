"""
Created on April 12, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class HeaderPage(Page):
    """ Class contains elements from Header page """

    def __init__(self, driver):
        super(HeaderPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    record_button_android = (
        MobileBy.ACCESSIBILITY_ID, 'MAP')

    # iOS
    record_button_ios = (
        MobileBy.ACCESSIBILITY_ID, 'MAP')

    def click_record_button(self):
        """
        Click on Record element
        :return: None
        """
        el = self.wait_for_element_present(
            *getattr(self, 'record_button_' + self.os))
        el.click()
