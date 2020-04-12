# -*- coding: utf-8 -*-
"""
Created on April 12, 2020

@author: Mate Ajdukovic
"""

from nose.tools import assert_true

from base_test import BaseTest
from page_objects.allow_gps_page import AllowGPSPage
from page_objects.header import HeaderPage
from page_objects.login_page import LoginPage
from page_objects.recording_page import RecordingPage


class TestTourNotSaved(BaseTest):
    """
    Test suite deals with tours that are not saved
    """

    def test_01_stop_recording_tour_before_moving(self):
        """
        Login with existing user and verify user's tour is not recorded as user did not move during tour.
        """
        login_page = LoginPage(self.driver)
        allow_gps_page = AllowGPSPage(self.driver)
        header_page = HeaderPage(self.driver)
        recording_page = RecordingPage(self.driver)

        "Continue with saved email"
        login_page.click_continue_with_email_button()
        login_page.click_on_saved_email_button()

        "Allow access to GPS/user's location"
        allow_gps_page.click_allow_gps_access_button()
        allow_gps_page.click_allow_location_access_button()

        "Open recording page and start recording"
        header_page.click_record_button()
        recording_page.click_start_recording_button()

        current_speed, average_speed, in_motion, travelled_distance = recording_page.get_all_recording_data()
        """ Verify default data is correct """
        assert_true(current_speed == '0', "Current speed is not 0")
        assert_true(average_speed == '0', "Average speed is not 0")
        assert_true(in_motion == '0:00', "In Motion is not 0:00")
        assert_true(travelled_distance == '0', "Travelled distance is not 0")
        print("All default recording data is correct.")

        "Stop recording user's session"
        recording_page.long_press_stop_recording_button()
        start_recording_button_displayed = recording_page.is_start_recording_element_displayed()

        "Verify user's tour is not recorded by finding 'Start recording' button, as user did not move"
        assert_true(start_recording_button_displayed, "Start recording button is not displayed")
        print("Start recording button is displayed, user's tour is not saved.")
