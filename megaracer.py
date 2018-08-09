from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://play.typeracer.com")

private_play_selector = '#gwt-uid-17 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div'
public_play_selector = '#gwt-uid-15 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div'
practice_play_selector = '#gwt-uid-15 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div'

raceType = raw_input('Choose race type:\n'
                     '0: public\n'
                     '1: practice\n'
                     '2: private\n'
                     '->')
try:
    raceType = int(raceType)
    if raceType < 0 or raceType > 2:
        raise Exception('Out of range.')
except:
    print 'Invalid input. quitting.'
    driver.close()
    exit()

selected = raceType + 3
driver.find_elements_by_class_name('gwt-Anchor')[selected].click()
if selected == 3:
    selected = public_play_selector
elif selected == 4:
    selected = practice_play_selector
elif selected == 5:
    selected == private_play_selector

textFound = False
sout = ''

raw_input('Press enter when ready in lobby>>')

print 'Waiting for text to appear...'
while not textFound:
    try:
        div = driver.find_element_by_css_selector(selected)
        print 'Found_a'
        sdiv = div.find_elements_by_xpath('.//*')
        print 'Found_b'
        subs = sdiv[0].find_elements_by_xpath('.//*')
        print 'Found_c'

        for s in subs:
            sout += s.get_attribute('innerHTML')

        print 'Text:\n================================================'
        print sout
        textFound = True;
    except:
        pass

inputFound = False
while not inputFound:
    try:
        el = driver.find_element_by_class_name("txtInput")
        if el.is_enabled():

            print 'Typing...'
            inputFound = True
    except:
        pass

print
for l in sout:
    driver.find_element_by_class_name("txtInput").send_keys(l)
    # print l,

print
raw_input("Press Enter to quit.")
try:
    driver.close()
except:
    pass


