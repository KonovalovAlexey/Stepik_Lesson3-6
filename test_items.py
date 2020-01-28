import time


def test_button_add_to_busket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    #button.klick()
    time.sleep(10)
    
def test_button_text(browser):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        button = browser.find_element_by_xpath("//button[text()='Add to basket']")
        
        
    except:
        button = browser.find_element_by_css_selector("#add_to_basket_form > button")
        
        if True:
            assert button == True, "Кнопка есть, проверьте название на английском"
        

    