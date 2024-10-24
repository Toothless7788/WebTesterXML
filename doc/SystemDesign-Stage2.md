# This file is created for selenium test of a website
# Created on 1/2/2024
# Last-edit: 5/2/2024

Files to be created: 
1. web_tester.py
2. web-testing-loginpage.xml
3. web-testing-registerpage.xml
4. web-testing-settingpage.xml
5. web-testing-homepage.xml
6. web-testing-wishlistpage.xml
7. field.py
8. step.py
9. test.py
10. expectation.py
11. main.py
12. 


Note: 
1. web-tester.py should be OOP, e.g. have a class
2. The python file takes the data from XML files and then input them on the website, i.e. no data should be stored in web-tester.py
3. 

------------------------------------------------------------------------------------------

Main (filename: main.py)

The main programme that instantiate WebTester and then call the run() function. 


Codes required: 
1. Instantiate the class WebTester
2. Call run()
3. Print out the loaded xml content
4. 


-login_file_path: String; The file path of the xml file for login page
-register_file_path: String; The file path of the xml file for register page
-setting_file_path: String; The file path of the xml file for setting page
-home_file_path: String; The file path of the xml file for home page
-wish_list_file_path: String; The file path of the xml file for wish_list page

------------------------------------------------------------------------------------------

Web Tester (filename: web_tester.py)

A universal web test software. With the file path of an XML file, input the corresponding data to the website. Then, check whether there are expected results, e.g. update Database, return error messages


Codes required: 
1. 

-file_path: String; the file path of the xml file to be read
-web_driver: WebDriver; Chrome, Safari, FireFox, Edge
-timeout: int; The maximum time to run the whole programme. If exceeds, exit the programme. Default: 60s
-submission_timeout: int; The maximum time to wait for the response from the submission of a form. Default: 20s
-fields: Dictionary(String, Field); We use dictionary (key = field's id; element = field) rather than array as it is faster, i.e. no need to loop through the array every time
-tests: list(Test); We use array/list as unlike fields, we will run through all tests eventually so there's no need using dictionary


+init(file_path: String, web_driver: String, timeout=60: int, submission_timeout=20: int): void; Store the file_path and web_driver (need to use if statement). Instantiate Selenium
+run(): void; invoke read_xml_config() and fill_web()
-read_xml_config(): void; using class variable file_path, read the corresponding file. Then, convert and store the xml contents to the corresponding dictionary/array
-fill_web(): void; With the filled tests, use a loop to fill in the webpage using selenium
-isDatabaseUpdated(id: String, value: String): boolean; Check whether the database is updated and contains the corresponding data (can do later)

------------------------------------------------------------------------------------------

Field (filename: field.py)

A class that represents a field, containing certain data/values of the field


-accessed_by: String; id, name
-key: String; id/name of the HTML element
-type: String; text, text-area, password, radio, select-one, select-multiple, check-box, button, submit, div, hidden
-action: String; type, click, select
-value: String; value of the HMTL element


+init(accessed_by: String, key: String, type: String, action: String, value: String): void; Set the values of the variables
Getter and setter functions for all variables


Codes required: 
1. 

------------------------------------------------------------------------------------------

Step (filename: step.py)

A class that represents a step in testing, e.g. clicking a button, filling in a text box


-access_by: String; id, name
-key: String; id/name of the HTML elements to be handled
-action: String; type, click, select
-value: String; The value to be filled in the desinated HTML element


+init(access_by: String, key: String, action: String, value: String): void; 
Getter and setter functions for all variables

------------------------------------------------------------------------------------------

Test (filename: test.py)

A class that represents a testing. It contains step(s) which will be executed. 


-id: int; id of the testing
-description: String; compulsory, general, submission; They are not used in testing but in report
-run: boolean: whether this test is to be run or to be skipped. Default: true
-language: String; en (English)
-steps: list(Step); The array/list containing all the steps required to be performed for this test
-expectations: list(Expectation); The array/list containing all the expected responses after performing this test


+init(id: int, description: String, run: boolean, language: String): void; 
Getter and setter functions for all variables

------------------------------------------------------------------------------------------

Expectation (filename: expectation.py)

After you made an HTTP request, e.g. form submission, there will be a response/expectation. It could be in the form of an error message or an additional field. 


-form-submission: boolean; Whether the response is reiggered by a form submission
-access_by: String; id, name
-key: String; id/name of the HTML elements to be checked
-value: String; The expected value of the returned HTML element


+init(form-submission: boolean, access_by: String, key: String, value: String): void; 
Getter and setter functions for all variables


