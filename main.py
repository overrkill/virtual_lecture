#Author Overrkill
#script to automate login 
#instructions
#add your userid & password
#add your course id 
#copy path to your chromedriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#username n password and course id
user = "your tcs id"
pswd = "your tcs passwd"
c_id = "your tcs batch"

#subject dictionaries
sub_dict = {"bct":"17BTIT731","ds":"17BTIT701","dsl":"17BTIT712","ml":"17BTIT703","mll":"17BTIT711","pcd":"17BTIT702","wsn":"17BTIT737"}


subject = input("which subject (bct ,ds ,dsl ,ml ,mll ,pcd ,wsn) \n you got a single chance bro\n").lower()

#Replace your path to chrome driver
driver = webdriver.Chrome(r"path\to\your\chromedriver.exe")

driver.get("https://www.tcsion.com/LX/login#lx")
uname = driver.find_element_by_xpath('//*[@id="Usrname"]')
uname.send_keys(user)
psss  = driver.find_element_by_xpath('//*[@id="Passwd"]')
psss.send_keys(pswd)

#login
login_btn = driver.find_element_by_link_text("LOGIN")
print("logging in.....")
login_btn.click()
print("logged in")

#course navigation
print("finding your courses")
cs = driver.get('https://g01.tcsion.com/LX/vccourses/new_listing_courses?c_id={}&from_dsb=dashboard&current_community_id={}&from=Course&type=current'.format(c_id,c_id))

print('navigating to {}'.format(subject))

sub=driver.find_element_by_partial_link_text(sub_dict[subject])

sub.click()

#join class
join_btns =  driver.find_elements_by_link_text("Join Now")
if len(join_btns)>=1:
    
    for i in join_btns:
        print(i)
    join_btns[0].click()

    sleep(4)

    print("Current Window ",driver.title)

    sleep(2)

    print('switching to virtual classroom')

    driver.switch_to.window(driver.window_handles[1])

    print(driver.title)
    print(" Getting into the arena of ",subject)
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[5]/button[2]').click()
else:
    print('no {} lecture scheduled tell your {} teacher'.format(subject,subject))

