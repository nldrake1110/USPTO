#Import ElementTree
from xml.etree import ElementTree as ET

#Create parsable XML tree that won't take up a lot of RAM Space
registrations = ET.iterparse('apc180410.xml')

#Make sure that user has the most recent data file
print("""Please make sure that you have downloaded the most recent registration data
from the USPTO's Bulk Data Website.  This information is available at: https://bulkdata.uspto.gov/.
""")
#Determine whether user is seraching using Registration Date

search = input('Are you searching for a trademark by registration date? (Y/N) ')

proper_responses = ['y', 'Y', 'Yes', 'yes']
if search in proper_responses:


    #Ask user to enter in the registration number they are searching for if they answered 'Y'
    reg_date = input('Please enter the registration date of the Trademarks you are searching for (YYYYMMDD): ')

    #Loop if registration Date is too short / long to permit a correction.
    while len(reg_date) < 8 or len(reg_date) > 8:
        print('Registration date invalid. Please re-enter the registration Date.')
        reg_date = input('Please enter the registration date of the Trademarks you are searching for (YYYYMMDD): ')
    #Begin search of XML document
    if len(reg_date) == 8:

        for event, element in registrations: #I don't know why the event, element is necessary but it seems to relate to tuples

           if element.tag == 'mark-dentification':

               if element.text == reg_date:
                   print(element.text)
                   quit()

else:
    print('Sorry we were unable to assist you. Have a wonderful day!')

#Search XML to JSON - there is. Install it
