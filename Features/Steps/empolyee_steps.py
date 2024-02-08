from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from employee_locators import *

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
    EC.visibility_of_element_located((By.XPATH, submit_button)))

    name_textbox = context.driver.find_element(By.XPATH, textbox_name)
    name_textbox.send_keys("promotion dedo")
    sleep(2)
    msg_textarea = context.driver.find_element(By.XPATH, textarea_msg)
    msg_textarea.send_keys("Bhagwan ka diya sab kuch he bas ek promotion ki jarurat he")
    sleep(2)
    submit_btn = context.driver.find_element(By.XPATH, submit_button)
    submit_btn.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, msg_thanks)))
    Thanks_message_element = context.driver.find_element(By.XPATH, "//p[text()='Thanks for contacting us']")
    Thanks_message = Thanks_message_element.text
    assert "Thanks for contacting us" in Thanks_message, f"Assertion Error: Thanks for contacting us not found in {Thanks_message}"



@then('uske bad agar aaj tu fir wapas aaya to aur ek kam dunga')
def wapas_aaja(context):
    context.driver.quit()

#### scenario 2 ###

@when('Koi b 5 cheej automate kar')
def abhi_thi_kar_k_deta_hu(context):
    #### TASK 1 ####
    # handling dynamic element- user want to grab 2 paragraph 1 before click on 'click here' another after click
    dynamic_content = context.driver.find_element(By.XPATH, dyna_content)
    dynamic_content.click()
    wait = WebDriverWait(context.driver, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH, first_paragraph)))
    first_para = context.driver.find_element(By.XPATH, first_paragraph)
    para1 = first_para.text
    context.driver.find_element(By.XPATH, click_here).click()

    #for second para
    wait.until(EC.visibility_of_element_located((By.XPATH, first_paragraph)))
    second_para = context.driver.find_element(By.XPATH, first_paragraph)
    para2 = second_para.text

    #verify both text are not match
    assert para1 != para2

    #### TASK 2 ####




@then('laptop band kar k tu ghar ja tera promotion letter mail karta hu')
def ja_simran_jeele_apni_jindagi(context):
    context.driver.quit()