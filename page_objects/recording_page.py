"""
Created on April 12, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from page_objects.page import Page


class RecordingPage(Page):
    """ Class contains elements from Allow GPS page """

    def __init__(self, driver):
        super(RecordingPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    start_recording_button_android = (MobileBy.ID, 'de.komoot.android:id/button_tracking_start')
    stop_recording_button_android = (MobileBy.ID, 'de.komoot.android:id/msb_stop_button_tb')
    current_speed_field_android = (MobileBy.ID, 'de.komoot.android:id/tpl_current_speed_small_ttv')
    average_speed_field_android = (MobileBy.ID, 'de.komoot.android:id/tpl_average_speed_small_ttv')
    in_motion_field_android = (MobileBy.ID, 'de.komoot.android:id/tpl_elapsed_time_small_ttv')
    travelled_distance_field_android = (MobileBy.ID, 'de.komoot.android:id/tpl_passed_distance_small_ttv')

    # iOS
    start_recording_button_ios = (MobileBy.ID, 'de.komoot.android:id/button_tracking_start')
    stop_recording_button_ios = (MobileBy.ID, 'de.komoot.android:id/msb_stop_button_tb')
    current_speed_field_ios = (MobileBy.ID, 'de.komoot.android:id/tpl_current_speed_small_ttv')
    average_speed_field_ios = (MobileBy.ID, 'de.komoot.android:id/tpl_average_speed_small_ttv')
    in_motion_field_ios = (MobileBy.ID, 'de.komoot.android:id/tpl_elapsed_time_small_ttv')
    travelled_distance_field_ios = (MobileBy.ID, 'de.komoot.android:id/tpl_passed_distance_small_ttv')
    
    def click_start_recording_button(self):
        """
        Click on Start recording element
        :return: None
        """
        el = self.wait_for_element_present(
            *getattr(self, 'start_recording_button_' + self.os))
        el.click()

    def long_press_stop_recording_button(self):
        """
        Long press Stop recording element
        :return: None
        """
        el = self.wait_for_element_present(
            *getattr(self, 'stop_recording_button_' + self.os))
        actions = TouchAction(self.driver)
        actions.long_press(el)
        actions.perform()

    def is_start_recording_element_displayed(self):
        """
        Check if Start recording element is present
        :return: True if Start recording button is displayed, else False
        :rtype: boolean
        """
        return self.is_element_visible(*getattr(self, 'start_recording_button_' + self.os))

    def get_all_recording_data(self):
        """
        Get Current speed, Average speed, In Motion and Travelled data
        :return: Current speed, Average speed, In Motion, Travelled
        :rtype: string
        """
        current_speed = self.get_element_text(*getattr(self, 'current_speed_field_' + self.os))
        average_speed = self.get_element_text(*getattr(self, 'average_speed_field_' + self.os))
        in_motion = self.get_element_text(*getattr(self, 'in_motion_field_' + self.os))
        travelled_distance = self.get_element_text(*getattr(self, 'travelled_distance_field_' + self.os))

        return current_speed, average_speed, in_motion, travelled_distance
