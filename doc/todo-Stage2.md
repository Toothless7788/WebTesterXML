# This file contains the amendments required for stage-2 webtester created by w45242hy
# Created on 19/2/2024 by w45242hy
# Last-edit: 19/2/2024 by w45242hy


Note: 
1. The section "Goals" contain the required amendments for stage 2 
2. The section "To-do items" contains the details of how to amend the programmes
3. <fieldset> will contain information of all the HTML elements that will be tested. It is to make a record of the default values/attributes/texts of the HTML elements to be tested
4. In Python programmes, <field> will be stored in a dictionary with format [field_id: instance of field], which will be retrieved for resetting webform by default values
5. 

Goals: 
1. Allow default value + default_value_type in field.py so that reset_form() set value to default rather than null (done)
2. (Maybe: if we just reset every field in that webform without checking whether they been tested, we do not need the dictionary, a list will do) Use dictionary to store fields in fieldset instead of list (key=internal_id: value=instance of field) (done)
3. Allow user to find_element(By.XPATH) to find element if accessby = "xpath" (done)
4. Consider using text instead of attribute in e.g. <message> or <field>, store data (done)
5. Create better format of printing of test results (copy JUnit or PyUnit)
6. 


To-do items: 
1. Change <field> format: <field id="field_id" name="field_name" class="field_class" type="" value="" defaultindex="" defaultvalue="">Default value</field> (done)
2. Remove attribute "value" in <message> and change the format of <message>: <message accessby="" key="" language="" type="">Expected value/message</message> (done)
3. Change all setter and getter functions to proerties and property-setters (Write code in Python way) (done)
4. Create 3 dictionaries in web_tester.py, which store <field>s based on their accessed_by
    - dictionary1: store by id
    - dictionary2: store by name
    - dictionary3: store by xpath
    - Some dictionaries might have overlapped content while there is also a chance that this is not the case (e.g. when id/name/class="". Then, we do not need to pass the instance of field to the corresponding dictionary) (kind of done -> I did not use this approach)
5. 



Tag Notes: 
1. <field>: 
- id: ID of the HTML element; Default ""
- name: name of the HTML element; Default ""
- class: class of the HTML element; Default ""
- type: text/number/select-multiple/select-one/check-box/radio/text-area/password/hidden/button/html-div/submit
- value: default attribute "value" of the HTML element; Default ""
- defaultindex: default index(s) separated by comma; Only for select-box and check-box
- defaultvalue: default value(s) separated by comma; Only for select-box and check-box
- text: default text of the element
- 

2. <step>: 
- accessby: id/name/xpath; xpath stands for the path of the HTML element in the XML file
- key: id/name/xpath of the HTML element, depending on accessby
- action: type/click/select; click is also for check-box
- value: value to be inputted to the HTML element
- 

3. <message>: 
- accessby: id/name/xpath; xpath stands for the path of the HTML element in the XML 
- key: id/name/xpath of the HTML element to be compared, depending on accessby
- language: en/zh-HK
- type: attribute/text; value means the expected attribute "value" (sometimes, it might change after an action, e.g. userSession); text means the expected display text of the HTML element
- text: The expected value of attribute "value"/display text, depending on type
- 