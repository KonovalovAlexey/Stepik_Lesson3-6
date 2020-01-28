import time


def test_button_add_to_busket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    #button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    #button.klick()
    
    try:
        button = browser.find_element_by_xpath("//button[text()='Add to basket']")
        
        
    except:
        button = browser.find_element_by_css_selector("#add_to_basket_form > button")
        time.sleep(10)
        if True:
            assert button == True, "Кнопка есть, проверьте название на английском"
        

    