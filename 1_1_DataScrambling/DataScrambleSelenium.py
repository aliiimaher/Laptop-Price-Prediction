from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

# Path to the ChromeDriver executable
from selenium.webdriver.support.wait import WebDriverWait

import re

import re

import re

def convert_to_english_number(persian_number):
    # Dictionary to map Persian/Arabic digits to English digits
    persian_to_english_digits = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9'
    }

    # Remove commas
    persian_number = persian_number.replace(",", "")

    # Convert Persian digits to English digits
    english_number = ''.join(persian_to_english_digits.get(char, char) for char in persian_number)

    return english_number


def replace_persian_arabic_numbers(input_string):
    # Mapping of Persian and Arabic numerals to English numerals
    persian_arabic_to_english = {
        '۰': '0', '١': '1', '۱': '1', '٢': '2', '۲': '2', '٣': '3', '۳': '3',
        '٤': '4', '۴': '4', '٥': '5', '۵': '5', '٦': '6', '۶': '6', '٧': '7',
        '۷': '7', '٨': '8', '۸': '8', '٩': '9', '۹': '9'
    }

    # Replace each Persian/Arabic numeral with the corresponding English numeral
    for persian_arabic_digit, english_digit in persian_arabic_to_english.items():
        input_string = input_string.replace(persian_arabic_digit, english_digit)

    return input_string


def extract_all_numbers_from_persian(text):
    # Define Persian digits and their corresponding Latin digits
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    latin_digits = '0123456789'
    trans = str.maketrans(persian_digits, latin_digits)

    # Translate Persian digits to Latin digits
    translated_text = text.translate(trans)

    # Regular expression to find all numbers, including floating-point numbers
    matches = re.findall(r'\d+\.\d+|\d+', translated_text)

    # Convert matched strings to floats or ints
    numbers = [float(match) if '.' in match else int(match) for match in matches]

    return numbers

chromedriver_path = 'chromedriver.exe'  # Replace with your actual path

# List of phpMyAdmin URLs and their credentials

# Initialize the WebDriver with Service


service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def findurls(url):
    try:
        driver.get(url)

        wait = WebDriverWait(driver, 15)
        loading_screen = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "styles_Loading__circle3__otcH4")))
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
        items = []
        for i in range(1, 21):
            css_selector = f'div.product-list_ProductList__item__LiiNI[data-product-index="{i}"] a'
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
            href_value = element.get_attribute('href')
            items.append(href_value)
            print(i, "- ", href_value)
        return items
    except Exception as e:
        print("execption first e = ", e)
        findurls(url)

def adddata(url):
    try:

        driver.get(url)
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "styles_Loading__circle3__otcH4")))
        loading_screen = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "styles_Loading__circle3__otcH4")))
        loading_screen = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

        # Check for iframes and switch if necessary
        html_content = driver.page_source

        file_path = "page_content.html"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)



        # laptop title
        h1_title_element = driver.find_element(By.TAG_NAME, "h1")
        data = {
            'title': h1_title_element.text,
            'url': url
        }


        # weight
        element = driver.find_element(By.XPATH,
                                      "//div[contains(@class, 'w-full flex last styles_SpecificationAttribute__valuesBox__gvZeQ')]//p[contains(text(), 'کیلوگرم')]")
        if(extract_all_numbers_from_persian(element.text)):
            data['weight'] = str(extract_all_numbers_from_persian(element.text)[0])
        else:
            data['weight'] = element.text
        print('weight' , str(data['weight']))


        #Processor manufacturer

        parent_div = driver.find_element(By.XPATH, "//p[contains(text(), 'سازنده پردازنده')]/following-sibling::div")

        # Now find the p element within this div
        Processor_manufacturer = parent_div.find_element(By.TAG_NAME, "p")
        data['Processor manufacturer'] = Processor_manufacturer.text
        print('Processor manufacturer' , Processor_manufacturer.text)

        # Print the extracted text


        #Processor model
        parent_div = driver.find_element(By.XPATH, "//p[contains(text(), 'مدل پردازنده')]/following-sibling::div")

        # Now find the p element within this div
        Processor_model = parent_div.find_element(By.TAG_NAME, "p")
        # data['Processor model'] = Processor_model.text
        # Print the extracted text
        data['Processor model'] = str(replace_persian_arabic_numbers(Processor_model.text))
        print('Processor model' , str(replace_persian_arabic_numbers(Processor_model.text)))


        #Processor series
        parent_div = driver.find_element(By.XPATH, "//p[contains(text(), 'سری پردازنده')]/following-sibling::div")

        # Now find the p element within this div
        Processor_series = parent_div.find_element(By.TAG_NAME, "p")
        # data['Processor model'] = Processor_model.text
        # Print the extracted text
        data['Processor series'] = str(replace_persian_arabic_numbers(Processor_series.text))
        print('max hertz' , str(replace_persian_arabic_numbers(Processor_series.text)))


        #Processor min and max frequence
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "فرکانس پردازنده")]/following-sibling::div/p')
        if(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))):
            minmaxfq = extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))
            if len(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))) >= 2:
                data['min hertz'] = str(minmaxfq[0])
                data['max hertz'] = str(minmaxfq[1])
            else:
                data['min hertz'] = str(minmaxfq[0])
                data['max hertz'] = str(minmaxfq[0])
        else:
            minmaxfq = parent_div.get_attribute('textContent')
            data['min hertz'] = minmaxfq
            data['max hertz'] = minmaxfq

        print('min hertz' , data['min hertz'])
        print('max hertz' , data['max hertz'])


        #cach memory
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "حافظه Cache")]/following-sibling::div/p')
        if extract_all_numbers_from_persian(parent_div.get_attribute('textContent')):
            cachemem = str(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))[0])
        else:
            cachemem = parent_div.get_attribute('textContent')
        print('cach mem' , cachemem)

        data['cach mem'] = cachemem

        #RAM
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "ظرفیت حافظه RAM")]/following-sibling::div/p')
        if(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))):
            RAM = str(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))[0])
        else:
            RAM = parent_div.get_attribute('textContent')
        print('RAM' , RAM)
        data['RAM'] = RAM

        #RAM type
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "نوع حافظه RAM")]/following-sibling::div/p')
        RAMtype = str(replace_persian_arabic_numbers(parent_div.get_attribute('textContent')))
        print('RAM' , RAMtype)

        data['RAM'] = RAMtype


        #internal storage
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "ظرفیت حافظه داخلی")]/following-sibling::div/p')
        strg = str((parent_div.get_attribute('textContent')))
        print('internal storage' , strg)

        data['internal storage'] = strg

        #internal storage
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "ظرفیت حافظه داخلی")]/following-sibling::div/p')
        strgtype = str((parent_div.get_attribute('textContent')))
        print('internal storage type' , strgtype)

        data['internal storage type'] = strgtype


        #storage type
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "نوع حافظه داخلی")]/following-sibling::div/p')
        strgtype = (parent_div.get_attribute('textContent'))
        print('internal storage type' , strgtype)

        data['internal storage type'] = strgtype

        # GPU manufacturer
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "سازنده پردازنده گرافیکی")]/following-sibling::div/p')
        GPUman = (parent_div.get_attribute('textContent'))
        print("GPU manufacturer" , GPUman)

        data['GPU manufacturer'] = GPUman


        # GPU model
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "مدل پردازنده گرافیکی")]/following-sibling::div/p')
        GPUmodel = replace_persian_arabic_numbers(parent_div.get_attribute('textContent'))
        print("GPU model" , GPUmodel)

        data['GPU model'] = GPUmodel


        # GPU memory
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "حافظه اختصاصی پردازنده گرافیکی")]/following-sibling::div/p')
        if(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))):
            GPUsize = str(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))[0])
        else:
            GPUsize = parent_div.get_attribute('textContent')
        print("GPU memory" , GPUsize)

        data['GPU memory'] = GPUsize


        # screen size
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "اندازه صفحه نمایش")]/following-sibling::div/p')
        if extract_all_numbers_from_persian(parent_div.get_attribute('textContent')):
            screenize = str(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))[0])
        else:
            screenize = parent_div.get_attribute('textContent')
        print("screen size" , screenize)
        data['screen size'] = screenize

        # screen refresh rate
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "توضیحات صفحه نمایش")]/following-sibling::div/p')
        if extract_all_numbers_from_persian(parent_div.get_attribute('textContent')):
            screenrate = str(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))[0])
        else:
            screenrate = parent_div.get_attribute('textContent')
        print("screen refresh rate " , screenrate)

        data['screen refresh rate'] = screenrate

        # battery
        parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "توضیحات باتری")]/following-sibling::div/p')
        if(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))):
            battery = str(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))[0])
        else:
            battery = (parent_div.get_attribute('textContent'))
        print("battery " , battery)

        data['battery'] = battery


        # # webcam
        # parent_div = driver.find_element(By.XPATH, '//p[contains(text(), "توضیحات وبکم")]/following-sibling::div/p')
        # if(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))):
        #     webcam = str(extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))[0])
        # else:
        #     webcam = extract_all_numbers_from_persian(parent_div.get_attribute('textContent'))
        # print("webcam " , webcam)
        # data['webcam'] = webcam

        #price
        price_elements = driver.find_elements(By.XPATH, "//*[@data-testid='price-no-discount']")
        print("price " , convert_to_english_number(price_elements[0].text))
        data['price'] = convert_to_english_number(price_elements[0].text)


        outy = 'dataout.csv'
        with open(outy, 'a', encoding='utf-8') as ff:
            jont = ','.join(data.values())
            print("jont = ", jont)
            ff.write(jont + '\n', )



    except Exception as e:
        # Print the exception
        print(f"An error occurred: {e}")

for i in range(1, 62):
    url = f"https://www.digikala.com/search/notebook-netbook-ultrabook/product-list/?has_selling_stock=1&page={i}&sort=7"
    items = findurls(url)
    print("item= ", items)
    for j in items:
        adddata(j)