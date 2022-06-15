from selene.support.shared import browser
from selene import be, have
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

browser.config.driver = webdriver.Chrome(
    service=Service(executable_path='.\\chromedriver.exe')
)
browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
browser.element('[id="search"]').should(have.text(' User-oriented Web UI browser tests in Python'))
