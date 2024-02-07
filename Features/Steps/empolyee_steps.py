from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@given('Tu pehle chrome browser open kar')
def browser_open_kar_be(context):
    context.driver = webdriver.Chrome()

@when(u'ye wali website open kar "{website}"')
def site_open_kar_na_yaar(context, website):
    context.website = website
    context.driver.get(context.website)


@when('usme apna naam aur aaj tak tune kya kya kam kiya wo fill kar')
def form_bhar(context):
    # Set up an explicit wait with a timeout of 10 seconds
    wait = WebDriverWait(context.driver, 10)
    # Wait until the element is visible
    element = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//button[@name='et_builder_submit_button'])[1]")))

    name_textbox = context.driver.find_element(By.XPATH, "//input[@id='et_pb_contact_name_0']")
    name_textbox.send_keys("promotion dedo")
    sleep(2)
    msg_textarea = context.driver.find_element(By.XPATH, "//textarea[@id='et_pb_contact_message_0']")
    msg_textarea.send_keys("Bhagwan ka diya sab kuch he bas ek promotion ki jarurat he")
    sleep(2)
    submit_btn = context.driver.find_element(By.XPATH, "(//button[@name='et_builder_submit_button'])[1]")
    submit_btn.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Thanks for contacting us']")))
    Thanks_message_locator = context.driver.find_element(By.XPATH, "//p[text()='Thanks for contacting us']")
    Thanks_message = Thanks_message_locator.text
    assert "Thanks for contacting us" in Thanks_message, f"Assertion Error: Thanks for contacting us not found in {Thanks_message}"

@then('uske bad agar aaj tu fir wapas aaya to aur ek kam dunga')
def wapas_aaja(context):
    context.driver.quit()