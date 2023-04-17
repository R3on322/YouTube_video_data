import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def get_data_from_youtube(url: str) -> dict:
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument('--headless=new')
    service = Service(
        # executable_path='YOUR PATH TO yandexdriver.exe',
        executable_path='C:\\Users\\Vikoffka\\PycharmProjects\\YouTube_video_data\\services\\yandexdriver.exe'
    )
    driver = webdriver.Chrome(service=service,
                              options=options)
    driver.get(url)
    time.sleep(3)
    print('Загружаем страницу YouTube')
    driver.find_element(By.XPATH, '//*[@id="expand"]').click()
    data = driver.page_source
    print('Парсим страницу')
    soup = BeautifulSoup(data, 'lxml')
    name = soup.title.text
    count_views = soup.find('div', {'class': 'style-scope ytd-watch-metadata', 'id': 'description-inner'})\
        .find('span', {'class': 'style-scope yt-formatted-string bold', 'style-target': 'bold'})
    publication_date = count_views.find_next().find_next().text
    count_likes = soup.find('button', {'class': "yt-spec-button-shape-next yt-spec-button-shape-next--tonal "
                                                "yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m "
                                                "yt-spec-button-shape-next--icon-leading "
                                                "yt-spec-button-shape-next--segmented-start"}).text

    return {'video_name': name,
            'views': count_views.text,
            'publication_date': publication_date,
            'likes': count_likes
            }


#print(get_data_from_youtube('https://youtu.be/am8H2iaxQ8E'))
#print(get_data_from_youtube('https://www.youtube.com/watch?v=7hn1_t2ZtJQ&list=PLqGS6O1-DZLprgEaEeKn9BWKZBvzVi_la&index=7'))
#print(get_data_from_youtube('https://www.youtube.com/watch?v=XJCYxIbsXmk&list=PLRU2Gs7fnCuiwcEDU0AWGkSTawEQpLFPb&index=8'))
#print(get_data_from_youtube('https://www.youtube.com/watch?v=pMZsat9uc1E'))
#print(get_data_from_youtube('https://www.youtube.com/watch?v=ZuPlCM6sFyo'))
# print(get_data_from_youtube('https://www.youtube.com/watch?v=GENhF_2Azbo&list=PLRU2Gs7fnCuiwcEDU0AWGkSTawEQpLFPb&index=3'))
# print(get_data_from_youtube('https://' + 'www.youtube.com/watch?v=GENhF_2Azbo&list=PLRU2Gs7fnCuiwcEDU0AWGkSTawEQpLFPb&index=3'))
# print(get_data_from_youtube('https://www.youtube.com/live/PrnuBXe1tmg?feature=share'))