class ElementLocator(object):
    # header panel
    headerLogo = '/html/body/header/h1/a'

    # home page
    home_page_title = '//*[@id="main"]/h1'
    home_page_txt_search = '//*[@id="searchbox"]'
    home_page_btn_filter = '//*[@id="searchsubmit"]'
    home_page_btn_add = '//*[@id="add"]'

    # Add computer page
    add_computer_txt_name = '//*[@id="name"]'
    add_computer_txt_intro = '//*[@id="introduced"]'
    add_computer_txt_discon = '//*[@id="discontinued"]'
    add_computer_select_company = '//*[@id="company"]'
    add_computer_btn_create = '//*[@id="main"]/form/div/input'
    add_computer_btn_cancel = '//*[@id="main"]/form/div/a'
