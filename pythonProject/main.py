from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutomationTestSelenium:
    def __init__(self):
        """
        Initialize
        """
        self.driver = webdriver.Chrome()

    def set_window_size(self, width, height):
        """
        Set the size of web browser window
        :param width: the width of window
        :param height: the height of window
        """
        self.driver.set_window_size(width, height)

    def set_home_page(self):
        """
        Set the default url of testing page
        """

        url = "https://www.packform.com"

        # navigate to home page if not
        if self.driver.current_url != url:
            self.driver.get(url)
            sleep(2)

    def check_display(self):
        """
        check display of logo, sign up button and sign in button
        """

        self.set_home_page()

        print("# Check display of logo, sign up button and sign in button")

        self.check_display_logo(True)
        self.check_display_sign_up(True)
        self.check_display_sign_in(True)

    def check_display_logo(self, printed):
        """
        Check the display of logo
        :param printed: boolean value to set the output message
        :return: True - if logo is visible, False - if logo is not visible
        """

        # check display of logo
        header_logo_item = self.driver.find_element(By.CLASS_NAME, 'components-Header__logo--2GmiX')
        header_logo_displayed = header_logo_item.is_displayed()

        footer_logo_item = self.driver.find_element(By.CLASS_NAME, 'components-Footer__footerLogo--1ZOb5')
        footer_logo_displayed = footer_logo_item.is_displayed()

        if printed is True:
            if header_logo_displayed:
                print("Header logo is visible")
            else:
                print("Footer logo is not visible")

            if footer_logo_displayed:
                print("Footer logo is visible")
            else:
                print("Footer logo is not visible")

        return header_logo_displayed and footer_logo_displayed

    def check_display_sign_up(self, printed):
        """
        Check the display of sign up button
        :param printed: boolean value to set the output message
        :return: Object element - if visible, False - if not visible
        """

        # check display of Sign up button
        sign_up_item = self.driver.find_element(By.LINK_TEXT, 'Sign Up')

        if sign_up_item.is_displayed():
            if printed is True:
                print("Sign up button is visible")
            return sign_up_item
        else:
            if printed is True:
                print("Sign up button is not visible")
            return False

    def check_display_sign_in(self, printed):
        """
        Check the display of sign in menu item
        :param printed: boolean value to set the output message
        :return: Object element - if visible, False - if not visible
        """

        # check display of Sign in button
        sign_in_item = self.driver.find_element(By.CLASS_NAME, 'components-Menu__signinItem--ECeXB')

        if sign_in_item.is_displayed():
            if printed is True:
                print("Sign in button is visible")
            return sign_in_item
        else:
            if printed is True:
                print("Sign in button is not visible")
            return False

    def check_sign_up_page(self):
        """
        Check url and title of sign up page
        """

        self.set_home_page()

        print("# Check sign up page")

        # Find sign up button and click on it
        sign_up_item = self.check_display_sign_up(False)

        if sign_up_item is not False:
            sign_up_item.click()
            sleep(2)

            # check redirected url
            if self.driver.current_url == "https://app.packform.com/sign_up/customer":
                print("Click on Sign up : Redirected url is corrected.", self.driver.current_url)
            else:
                print("Click on Sign up : Redirected url is uncorrected. It was : ", self.driver.current_url)

            # check display of title header
            sign_up_now_header_item = self.driver.find_element(By.CLASS_NAME, 'SignUp_header_vvza5')
            if sign_up_now_header_item.is_displayed():
                print("\"Sign up now\" header is visible")
            else:
                print("\"Sign up now\" header is not visible")

        else:
            print("Sign up button is not visible, So can not check Sign up page!")

    def check_sign_in_page(self):
        """
        Check url and title of sign in page
        """

        self.set_home_page()

        print("# Check sign in page")

        # Find sign in menu item and click on it
        sign_in_item = self.check_display_sign_in(False)

        if sign_in_item is not False:
            # On large width window, it can be clicked on top bar
            sign_in_item.click()
        else:
            # On small width window, It is hide on Side Toggle Menu
            self.driver.find_element(By.CSS_SELECTOR, ".fa-bars").click()
            self.driver.find_element(By.LINK_TEXT, "SIGN IN").click()

        sleep(2)

        # check redirected url
        if self.driver.current_url == "https://app.packform.com/sign_in":
            print("Redirected Sign in url is corrected.", self.driver.current_url)
        else:
            print("Redirected Sign in url is uncorrected. It was : ", self.driver.current_url)

        # check display of title header
        welcome_back_header_item = self.driver.find_element(By.CLASS_NAME, 'SignIn_header_uub0M')

        if welcome_back_header_item.is_displayed():
            print("\"Welcome back\" header is visible")
        else:
            print("\"Welcome back\" header is not visible")

    def check_catalog_page(self):
        """
        After click on catalog menu item. Recheck display of logo and sign up element.
        Check display of "Film and Wrap" catalog item
        """

        self.set_home_page()

        print("# Check catalog page")

        # Find catalog menu item and click on it
        catalog_menu_item = self.driver.find_element(By.XPATH, '//a[@href="/catalog/"]')

        if catalog_menu_item.is_displayed():
            # On large width window, it can be clicked on top bar
            catalog_menu_item.click()
        else:
            # On small width window, It is hide on Side Toggle Menu
            self.driver.find_element(By.CSS_SELECTOR, ".fa-bars").click()
            self.driver.find_element(By.LINK_TEXT, "Catalog").click()

        print("After clicking on Catalog menu item")

        # Recheck the display of logo and sign up button
        self.check_display_logo(True)
        self.check_display_sign_up(True)

        # Scroll to end of the browser to wait finishing lazy load
        self.scroll_to_end()

        cat_text_item = self.driver.find_element(By.XPATH, '//span[text()="Film and Wrap"]')
        cat_img_item = self.driver.find_element(By.XPATH, '//img[@src="/_nuxt/img/e49c4e9.png"]')

        if cat_text_item.is_displayed() and cat_img_item.is_displayed():
            print('"Film and Wrap" item and corresponding picture are visible')

            print('# Check pop up')
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Film and Wrap"]/parent::div'))).click()

            dialog_item = self.driver.find_element(By.CLASS_NAME,
                                                   "components-catalog-SignupDialog__dialogContent--SCxIf")

            if dialog_item.is_displayed():

                print('Pop up dialog is visible')

                # Check button of popup
                dialog_sign_up_item = self.driver.find_element(By.XPATH,
                                                               "//div[@class='components-catalog-SignupDialog__actions--sk1Mj']"
                                                               "//*[contains(text(),'Sign Up')]")
                dialog_cancel_item = self.driver.find_element(By.XPATH,
                                                              "//div[@class='components-catalog-SignupDialog__actions--sk1Mj']"
                                                              "//*[contains(text(),'Cancel')]")

                if dialog_sign_up_item.is_displayed() and dialog_cancel_item.is_displayed():
                    print('Sign in button and Cancel button of Pop up dialog is visible')
                else:
                    print('Sign in button and Cancel button of Pop up dialog is not visible')

            else:
                print('Pop up dialog did not appear')

        else:
            print('"Film and Wrap" item and corresponding picture are not visible')

    def scroll_to_end(self):
        """
        Scroll to end of the browser to wait finishing lazy load
        """

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(0.5)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


if __name__ == '__main__':
    test = AutomationTestSelenium()
    test.set_window_size(1920, 1080)

    test.check_display()
    test.check_sign_up_page()
    test.check_sign_in_page()
    test.check_catalog_page()

    # Close driver
    test.driver.close()
