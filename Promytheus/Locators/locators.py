class Locators():

    # locators of promytheus.net home page
    url = "http://promytheus.net/"
    link_login = "//li[@id='menu-item-963']//span[contains(@class,'menu-text')][contains(text(),'Login')]"

    # locators of login page
    textbox_email_xpath = "//input[@placeholder='Enter email']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_id = "login"

    # locators of Talents Page after signing in
    button_new_xpath = "//a[@class='btn btn-primary mr']"

    # locators for edit talents
    hyperlink_edit_xpath = "//tr[1]//td[9]//a[1]"

    # locators of Category tab in the newTalents page
    dropdown_drpdwnbtn_xpath = "//div[@class='col-lg-10']//div[@name='category']//span[@class='btn btn-default form-control ui-select-toggle']"
    dropdown_category_xpath = "//span[contains(text(),'Software Programming')]"
    button_Nextcatgry_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"


    # locators of Personal tab in the newTalents page
    textbox_fName_xpath = "//input[@placeholder='Enter First name']"
    textbox_lName_xpath = "//input[@placeholder='Enter Last name']"
    dropdown_country_xpath = "//span[contains(text(),'USA')]"
    textbox_address_xpath = "//input[@id='address']"
    textbox_city_xpath = "//input[@placeholder='Enter city']"
    textbox_state_xpath = "//input[@placeholder='Enter state']"
    textbox_postal_xpath = "//input[@placeholder='Enter postal code']"
    button_Nextpersonal_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

    # locators of Talent Traits tab in the newTalents page
    button_qtn1_xpath = "//fieldset[1]//trait-scaler[1]//button[9]"
    button_qtn2_xpath = "//fieldset[2]//trait-scaler[1]//button[9]"
    # button_qtn3_xpath = "//fieldset[3]//trait-scaler[1]//button[9]"
    button_qtn3_xpath = "//div[@class='row']//div[2]//div[1]//fieldset[3]//trait-scaler[1]//button[8]"
    button_qtn4_xpath = "//fieldset[4]//trait-scaler[1]//button[9]"
    button_qtn5_xpath = "//fieldset[5]//trait-scaler[1]//button[8]"
    button_qtn6_xpath = "//fieldset[6]//trait-scaler[1]//button[1]"
    button_qtn7_xpath = "//fieldset[7]//trait-scaler[1]//button[10]"
    button_qtn8_xpath = "//fieldset[8]//trait-scaler[1]//button[9]"
    button_qtn9_xpath = "//fieldset[9]//trait-scaler[1]//button[9]"
    button_qtn10_xpath = "//fieldset[10]//trait-scaler[1]//button[10]"
    button_qtn11_xpath = "//fieldset[11]//trait-scaler[1]//button[9]"
    button_qtn12_xpath = "//fieldset[12]//trait-scaler[1]//button[9]"
    button_qtn13_xpath = "//fieldset[13]//trait-scaler[1]//button[9]"
    button_qtn14_xpath = "//fieldset[14]//trait-scaler[1]//button[9]"
    button_qtn15_xpath = "//fieldset[15]//trait-scaler[1]//button[9]"
    button_qtn16_xpath = "//fieldset[16]//trait-scaler[1]//button[9]"
    button_qtn17_xpath = "//fieldset[17]//trait-scaler[1]//button[8]"
    button_qtn18_xpath = "//fieldset[18]//trait-scaler[1]//button[9]"
    button_qtn19_xpath = "//fieldset[19]//trait-scaler[1]//button[9]"
    button_qtn20_xpath = "//fieldset[20]//trait-scaler[1]//button[9]"
    button_qtn21_xpath = "//fieldset[21]//trait-scaler[1]//button[9]"
    button_qtn22_xpath = "//fieldset[22]//trait-scaler[1]//button[9]"
    button_NextTalent_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

    # locators for Personality Traits tab
    checkbox_qtn1_xpath = "//tr[1]//td[2]//label[1]//span[1]"
    checkbox_qtn2_xpath = "//tr[2]//td[2]//label[1]//span[1]"
    button_NextPrsnlty_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"

    # locators for all Next buttons from story to end Quick-Test tab
    stry_nextbtn_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"
    evidence_tab_next_btn = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')] "
    training_button_next_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')] "
    social_button_next_xpath = "//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Next')]"
    finish_button_xpath = "//button[contains(text(),'Finish')]"

    # locators for story page
    story_age_xpath = "//input[@placeholder='Years Old']"
    story_interest_level_xpath = "//select[@name='interestLevel']"

    # locators for evidence page
    friends_check_xpath = "//label[contains(text(), 'Friends')]/span"
    talent_work_product_xpath = "//input[@placeholder='Enter work product']"

    # locators for Training page
    professionally_coached_xpath = "//label[contains(text(),'Yes')]"
    coach_name_xpath = "//div[@class='col-lg-8']//input[@placeholder='Enter Name']"
    success_level_xpath = "//div[@class='col-lg-3']//input[@placeholder='Enter Success level']"
    skill_level_xpath = "//label[contains(text(),'Advanced')]"

    # locators for Social page
    marital_status_xpath = "//select[@name='maritalStatus']"


    def __init__(self, driver):
        driver = self.driver