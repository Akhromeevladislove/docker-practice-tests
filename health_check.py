import requests
import sys

def check_website(url):
    try:
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            print(f"✅{url} доступен (Статус: {response.status_code})")
            return True
        else:
            print(f"⚠️{url} не доступен (Статус: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌Ошибка подключения к {url}:{e}")
        return False
    
if __name__ == "__main__":
    site = sys.agrv[1] if len(sys.argv) > 1 else "https://google.com"
    check_website(site)