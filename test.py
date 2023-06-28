from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager

# Proxy設定
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "127.0.0.1:9150"  # Torのデフォルトポートは9050ですが、Tor Browserでは9150を使います
proxy.ssl_proxy = "127.0.0.1:9150"

# WebDriverの設定
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# WebDriverのインスタンスを生成
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=capabilities)

# 指定したURLに遷移
driver.get("http://www.google.com")

# ブラウザを閉じる
driver.quit()
