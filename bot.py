from selenium import webdriver
import pandas as pd
import time
web = webdriver.Chrome()
web.get('https://codeforces.com/lists/new')
username = web.find_element_by_xpath('//*[@id="handleOrEmail"]')
password = web.find_element_by_xpath('//*[@id="password"]')
username.send_keys("<HANDLE NAME OR EMAIL ADDRESS>")
password.send_keys("<PASSWORD>")

web.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input').click()
time.sleep(5)
web.find_element_by_xpath('//*[@id="englishName"]').send_keys('IITG CSE 2024')
web.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[5]/td/input').click()
web.find_element_by_xpath('//*[@id="pageContent"]/div[4]/div/div/a[2]').click()
names=''
df = pd.read_csv('<NAME OF CSV FILE>')
for name in df['<Column name>']:
	names =names+ name+', '
time.sleep(2)
print(names)
#web.find_element_by_xpath('//*[@id="handlesToAdd"]').click()
#web.find_element_by_xpath('//*[@id="handlesToAdd"]').send_keys(names)
#command =("document.querySelector('#handlesToAdd').value = ('%$s')",names)
#command=''.join(command)
#web.execute_script(command)
#web.find_element_by_xpath('//*[@id="facebox"]/div/div/div/form/table/tbody/tr[7]/td/input').click()
