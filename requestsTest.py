import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    headers = {'User-Agent': 'Mozilla/5.0'}  # 伪装浏览器‌:ml-citation{ref="1,3" data="citationList"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        return soup.find('div').text  # 提取内容‌:ml-citation{ref="7,8" data="citationList"}
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

# 示例调用
data = fetch_data("https://example.com")
print(data)