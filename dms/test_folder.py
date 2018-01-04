#!/usr/bin/env python
# coding: utf-8

import time
import random


def get_name(self):
        """Returns name of view."""
        raise NotImplementedError

    def get_page_index(self):
        """Returns index of page within the drawer."""
        raise NotImplementedError

    def navigate_to_page(self):
        """Navigate to the drawer and swipe until it gets to desired page."""
        BaseTest.navigate_to_page(self)
        tab_view = TabViewPage(self.driver)
        sleep(self.ANIMATION_DELAY)

        for __ in range(self.get_page_index()):
            tab_view.go_to_next_page()
            sleep(self.ANIMATION_DELAY)