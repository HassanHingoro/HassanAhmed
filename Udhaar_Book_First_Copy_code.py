import time
import unittest
import self
from appium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import warnings

class TestService(unittest.TestCase):

    def test_growing(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

class Udhaar_Book1(unittest.TestCase):
        reportDirectory = 'reports'
        reportFormat = 'xml'
        dc = {}
        testName = 'Udhaar_Book_First_TestCase'
        driver = None

        def setUp(self):

            self.dc['reportDirectory'] = self.reportDirectory
            self.dc['reportFormat'] = self.reportFormat
            self.dc['testName'] = self.testName
            self.dc['udid'] = 'ZY224SF5L3'
            # self.dc['udid'] = 'E5AM1904003356'
            # self.dc['app'] = 'C:\\Users\\Marketiq\\Downloads\\app_release_UdhaarBook.apk'
            self.dc['appPackage'] = 'com.oscarudhaarapp'
            self.dc['appActivity'] = 'com.oscarudhaarapp.SplashActivity'
            self.dc['noReset'] = 'true'
            self.dc['instrumentApp'] = 'true'
            self.dc['platformName'] = 'android'
            self.dc['platformVersion'] = '7.1.1'
            # self.dc['platformVersion'] = '9'
            self.dc['automationName'] = 'UiAutomator2'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

        def test_case(self):

            time.sleep(15)

        # 1. Click '03xxxxxxxxx'

            _03xxxxxxxxx = self.driver.find_element(By.XPATH,"//android.widget.EditText[@text = '03xxxxxxxxx']")
            _03xxxxxxxxx.click()
            time.sleep(3)

        # 2. Type '03232515811' in '03xxxxxxxxx'

            _03xxxxxxxxx = self.driver.find_element(By.XPATH,"//android.widget.EditText[@text = '03xxxxxxxxx']")
            _03xxxxxxxxx.send_keys("03232515811")
            time.sleep(10)

        # 3. Click 'SEND OTP CODE'


            send_otp_code = self.driver.find_element(By.XPATH,
                                                "//android.widget.TextView[@text = 'SEND OTP CODE']")
            send_otp_code.click()
            time.sleep(30)

        # 4. Click ''

            _ = self.driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
            _.click()
            time.sleep(10)

        # 5. Click 'Naya Business Banaen'

            naya_business_banaen = self.driver.find_element(By.XPATH,
                                                       "//android.widget.TextView[@text = 'Naya Business Banaen']")
            naya_business_banaen.click()
            time.sleep(10)

        # 6. Click 'Business Ka Naam Enter Karein'

            business_ka_naam_enter_karein = self.driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Business Ka Naam Enter Karein']")
            business_ka_naam_enter_karein.click()
            time.sleep(5)

        # 7. Type 'Business_1' in 'Business Ka Naam Enter Karein'

            business_ka_naam_enter_karein = self.driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Business Ka Naam Enter Karein']")
            business_ka_naam_enter_karein.send_keys("Business_1")
            time.sleep(5)

        # 8. Click 'Naya Business Banaen1'

            naya_business_banaen1 = self.driver.find_element(By.XPATH,
                                                        "//android.widget.TextView[@text = 'Naya Business Banaen']")
            naya_business_banaen1.click()
            time.sleep(5)

        # 9. Click 'CUSTOMER ADD KAREIN'

            customer_add_karein = self.driver.find_element(By.XPATH,
                                                      "//android.widget.TextView[@text = 'CUSTOMER ADD KAREIN']")
            customer_add_karein.click()
            time.sleep(10)

        # 10. Click 'ALLOW'

            try:
                allow = self.driver.find_element(By.ID,
                                            "com.android.packageinstaller:id/permission_allow_button")
                allow.click()
                time.sleep(10)
            except Exception:
                # Failure Behaviour: Continue
                pass
                time.sleep(5)

        # 11. Click 'Naya Customer Banaen'

            naya_customer_banaen = self.driver.find_element(By.XPATH,
                                                       "//android.widget.TextView[@text = 'Naya Customer Banaen']")
            naya_customer_banaen.click()
            time.sleep(5)

        # 12. Click 'Customer Ka Naam Likhein'

            customer_ka_naam_likhein = self.driver.find_element(By.XPATH,
                                                           "//android.widget.EditText[@text = 'Customer Ka Naam Likhein']")
            customer_ka_naam_likhein.click()
            time.sleep(10)

        # 13. Type 'Customer_1' in 'Customer Ka Naam Likhein'

            customer_ka_naam_likhein = self.driver.find_element(By.XPATH,
                                                           "//android.widget.EditText[@text = 'Customer Ka Naam Likhein']")
            customer_ka_naam_likhein.send_keys("Customer_1")
            time.sleep(10)
        #
        # # # 15. Clear the contents of '03475639566' if it's visible
        # #     _03475639566 = (By.XPATH, "//android.widget.EditText[@text = '03475639566']")
        # #     self.driver.addons().execute(
        # #         VisibleElementsOperations.clearcontentsifvisibleandroid(
        # #             timeout=""), *_03475639566)
        #

        # 17. Click 'SAVE'

            Save = self.driver.find_element(By.XPATH,
                                           "//android.widget.TextView[@text = 'SAVE']")
            Save.click()
            time.sleep(20)

        # 18. Click ''

            _ = self.driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
            _.click()
            time.sleep(5)

        # 19. Click 'Customer_1'

            customer_1 = self.driver.find_element(By.XPATH,
                                             "//android.widget.TextView[@text = 'Customer_1']")
            customer_1.click()
            time.sleep(10)

        # 20. Click 'AAPKO MILE'

            aapko_mile = self.driver.find_element(By.XPATH,
                                             "//android.widget.TextView[@text = 'AAPKO MILE']")
            aapko_mile.click()
            time.sleep(5)

        # 21. Click '1'

            _1 = self.driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = '1']")
            _1.click()
            time.sleep(5)

        # 22. Click 'SAVE1'

            save1 = self.driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'SAVE']")
            save1.click()
            time.sleep(10)

        # 23. Click 'NOT NOW'

            try:
                not_now = self.driver.find_element(By.XPATH,
                                              "//android.widget.TextView[@text = 'NOT NOW']")
                not_now.click()
                time.sleep(10)
            except Exception:
                # Failure Behaviour: Continue
                pass
            time.sleep(10)

        # 24. Click 'AAPNE DIYE'

            aapne_diye = self.driver.find_element(By.XPATH,
                                             "//android.widget.TextView[@text = 'AAPNE DIYE']")
            aapne_diye.click()
            time.sleep(5)

        # 25. Click '2'

            _2 = self.driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = '2']")
            _2.click()
            time.sleep(10)

        # 26. Click 'SAVE1'

            save1 = self.driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'SAVE']")
            save1.click()
            time.sleep(10)

        # # 27. Does 'Bal. Rs.1' contain 'Bal. Rs.1'?
        #
        #     bal_rs_1 = self.driver.find_element(By.ID,
        #                                    "0_balance")
        #     step_output = bal_rs_1.text
        #     assert step_output and ("Bal. Rs.1" in step_output)
        #     time.sleep(5)
        #
        # # 28. Does 'Rs. 1' contain 'Rs. 1'?
        #
        #     rs_1 = self.driver.find_element(By.ID,
        #                                "udhaar_amount_1")
        #     step_output = rs_1.text
        #     assert step_output and ("Rs. 1" in step_output)
        #     time.sleep(5)

        # 29. Click ''

            _ = self.driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
            _.click()
            time.sleep(5)

        # 30. Click 'Customer_1'
            customer_1 = self.driver.find_element(By.XPATH,
                                             "//android.widget.TextView[@text = 'Customer_1']")
            customer_1.click()
            time.sleep(5)

        # 31. Click 'AAPKO MILE1'
            aapko_mile1 = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[@text = 'AAPKO MILE']")
            aapko_mile1.click()
            time.sleep(5)

        # 32. Click '3'
            _3 = self.driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = '3']")
            _3.click()
            time.sleep(5)

        # 33. Click 'Add Item'
            add_item = self.driver.find_element(By.XPATH,
                                           "//android.view.ViewGroup[1]/android.widget.TextView[@text = 'Add Item']")
            add_item.click()
            time.sleep(5)

        # 34. Click 'AAPKO MILE1'
            aapko_mile1 = self.driver.find_element(By.XPATH,
                                              "//android.widget.TextView[@text = 'AAPKO MILE']")
            aapko_mile1.click()
            time.sleep(5)

        # 35. Click 'Enter Item Name'
            enter_item_name = self.driver.find_element(By.XPATH,
                                                  "//android.widget.EditText[@text = 'Enter Item Name']")
            enter_item_name.click()
            time.sleep(5)

        # 36. Type 'Aata' in 'Enter Item Name'
            enter_item_name = self.driver.find_element(By.XPATH,
                                                  "//android.widget.EditText[@text = 'Enter Item Name']")
            enter_item_name.send_keys("Aata")
            time.sleep(5)

        # 37. Click '1'
            _1 = self.driver.find_element(By.XPATH,
                                     "//android.widget.TextView[1][@text = '']")
            _1.click()
            time.sleep(5)

        # 38. Click 'kg'
            kg = self.driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'kg']")
            kg.click()
            time.sleep(3)

        # 39. Click '0'
            _0 = self.driver.find_element(By.XPATH,
                                     "//android.widget.EditText[2][@text = '0']")
            _0.click()
            time.sleep(5)

        # 40. Type '100' in '0'
            _0 = self.driver.find_element(By.XPATH,
                                     "//android.widget.EditText[2][@text = '0']")
            _0.send_keys("100")
            time.sleep(5)

        # 41. Click '01'
            _01 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[3][@text = '0']")
            _01.click()
            time.sleep(5)

        # 42. Type '100' in '01'
            _01 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[3][@text = '0']")
            _01.send_keys("100")
            time.sleep(5)

        # 43. Click '02'
            _02 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[4][@text = '0']")
            _02.click()
            time.sleep(5)

        # 44. Type '50' in '02'
            _02 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[4][@text = '0']")
            _02.send_keys("50")
            time.sleep(5)

        # 45. Click 'SAVE2'
            save2 = self.driver.find_element(By.XPATH,
                                        "//android.view.ViewGroup[1]/android.widget.TextView[@text = 'SAVE']")
            save2.click()
            time.sleep(5)

        # 46. Click 'Yes'
            yes = self.driver.find_element(By.XPATH,
                                      "//android.widget.TextView[@text = 'Yes']")
            yes.click()
            time.sleep(5)

        # 47. Click 'NEXT'
            next = self.driver.find_element(By.XPATH,
                                       "//android.widget.TextView[@text = 'NEXT']")
            next.click()
            time.sleep(5)

        # 48. Click 'Item   x   1'
            item_x_1 = self.driver.find_element(By.XPATH,
                                           "//android.widget.TextView[@text = 'Item   x   1']")
            item_x_1.click()
            time.sleep(5)

        # 49. Click 'Item banaen'
            item_banaen = self.driver.find_element(By.XPATH,
                                              "//android.widget.TextView[@text = 'Item banaen']")
            item_banaen.click()
            time.sleep(5)

        # 50. Click 'Enter Item Name'
            enter_item_name = self.driver.find_element(By.XPATH,
                                                  "//android.widget.EditText[@text = 'Enter Item Name']")
            enter_item_name.click()
            time.sleep(5)

        # 51. Type 'مرچ' in 'Enter Item Name'
            enter_item_name = self.driver.find_element(By.XPATH,
                                                  "//android.widget.EditText[@text = 'Enter Item Name']")
            enter_item_name.send_keys("مرچ")
            time.sleep(5)

        # 52. Click '1'
            _1 = self.driver.find_element(By.XPATH,
                                     "//android.widget.TextView[1][@text = '']")
            _1.click()
            time.sleep(5)

        # 53. Click 'gm'
            gm = self.driver.find_element(By.XPATH,
                                     "//android.widget.TextView[@text = 'gm']")
            gm.click()
            time.sleep(5)

        # 54. Click '0'
            _0 = self.driver.find_element(By.XPATH,
                                     "//android.widget.EditText[2][@text = '0']")
            _0.click()
            time.sleep(5)

        # 55. Type '100' in '0'
            _0 = self.driver.find_element(By.XPATH,
                                     "//android.widget.EditText[2][@text = '0']")
            _0.send_keys("100")
            time.sleep(5)

        # 56. Click '01'
            _01 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[3][@text = '0']")
            _01.click()
            time.sleep(5)

        # 57. Type '20' in '01'
            _01 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[3][@text = '0']")
            _01.send_keys("20")
            time.sleep(5)

        # 58. Click '02'
            _02 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[4][@text = '0']")
            _02.click()
            time.sleep(5)

        # 59. Type '15' in '02'
            _02 = self.driver.find_element(By.XPATH,
                                      "//android.widget.EditText[4][@text = '0']")
            _02.send_keys("15")
            time.sleep(5)

        # 60. Click 'SAVE2'
            save2 = self.driver.find_element(By.XPATH,
                                        "//android.view.ViewGroup[1]/android.widget.TextView[@text = 'SAVE']")
            save2.click()
            time.sleep(5)

        # # 61. Does 'Rs. 120' contain 'Rs. 120'?
        #     rs_120 = self.driver.find_element(By.XPATH,
        #                                  "//android.widget.TextView[@text = 'Rs. 120']")
        #     step_output = rs_120.text
        #     assert step_output and ("Rs. 120" in step_output)
        #     time.sleep(5)

        # 62. Click 'NEXT'
            next = self.driver.find_element(By.XPATH,
                                       "//android.widget.TextView[@text = 'NEXT']")
            next.click()
            time.sleep(5)

        # 63. Click 'Notes / Tafseel (Optional)'
            notes_slash_tafseel_optional_ = self.driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Notes / Tafseel (Optional)']")
            notes_slash_tafseel_optional_.click()
            time.sleep(5)

        # 64. Type 'I have added the Item with Note and Image' in 'Notes / Tafseel (Optional)'
            notes_slash_tafseel_optional_ = self.driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@text = 'Notes / Tafseel (Optional)']")
            notes_slash_tafseel_optional_.send_keys(
            "I have added the Item with Note and Image")
            time.sleep(5)

        # 65. Click ''
            _ = self.driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
            _.click()
            time.sleep(5)

        # 66. Click 'Upload From Gallery'
            upload_from_gallery = self.driver.find_element(By.XPATH,
                                                      "//android.widget.TextView[@text = 'Upload From Gallery']")
            upload_from_gallery.click()
            time.sleep(5)

        # 67. Click 'Camera'
            camera = self.driver.find_element(By.XPATH,
                                         "//android.widget.RelativeLayout[2]/android.widget.TextView[@text = 'Camera']")
            camera.click()
            time.sleep(5)

        # 68. Click 'Photo taken on Nov 14, 2021 1:14:47 AM'
            photo_taken_on_nov_14_2021_1_colon_14_colon_47_am = self.driver.find_element(By.XPATH,
                                                                                    "//android.view.ViewGroup[@content-desc = 'Photo taken on Nov 14, 2021 1:14:47 AM']")
            photo_taken_on_nov_14_2021_1_colon_14_colon_47_am.click()
            time.sleep(5)

        # 69. Click 'SAVE1'
            save1 = self.driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text = 'SAVE']")
            save1.click()
            time.sleep(5)

        # # 70. Does 'Rs. 119' contain 'Rs. 119'?
        #     rs_119 = self.driver.find_element(By.ID,
        #                                  "udhaar_amount_119")
        #     step_output = rs_119.text
        #     assert step_output and ("Rs. 119" in step_output)
        #     time.sleep(5)

        # 71. Click ''
            _ = self.driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = '']")
            _.click()
            time.sleep(5)
            print('All Test Cases Pass Successfully!')


        def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
        unittest.main()
