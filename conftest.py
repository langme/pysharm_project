#!/usr/bin/env python
# coding: utf-8

import os
import glob
import time
import subprocess
import pytest
from pathlib import Path
from appium import webdriver

from appium_util import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

adb_getprop = lambda prop: subprocess.check_output(['adb', 'shell', 'getprop', prop]).rstrip().decode('utf-8')

@pytest.fixture(scope="session", autouse=True)
def appium(request):
  """
  Create an Appium client from command line options.
  """

  desired_caps = {}

  desired_caps['platformName'] = 'Android'
  desired_caps['platformVersion'] = platform_version
  desired_caps['deviceName'] = device_name
  desired_caps['udid'] = device_name
  desired_caps['app'] = app
  desired_caps['appPackage'] = app_package
  desired_caps['appActivity'] = 'com.test.domo'
  desired_caps['unicodeKeyboard'] = True
  desired_caps['resetKeyboard'] = True

  appium_driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' %(appium_server_port), desired_caps)

  appium_driver.activate_ime_engine('io.appium.android.ime/.UnicodeIME')

  def teardown():
    appium_driver.deactivate_ime_engine()
    appium_driver.quit

  request.addfinalizer(teardown)

  return appium_driver