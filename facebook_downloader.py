import requests
from selenium import webdriver


def download(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    elem = driver.find_elements_by_class_name("sec")
    image_link = elem[1].get_attribute("href")
    driver.close()

    res = requests.get(image_link)
    res.raise_for_status()
    title = image_link.split("?")[0].split("/")[-1]
    print(title)
    imageFile = open(title, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    return title


def main():
    url = input("Enter image url: ")
    url = "m".join(url.split("www"))
    download(url)



