![LOG-YY-Nuker Banner2](https://user-images.githubusercontent.com/109160786/182344001-a5220958-21db-4b88-a004-1a09b8f5b297.png)



☆ **  !! DON'T WORRY IF THE INSTALLATION IS LONGER IT'S NORMAL !!  ** ☆ 


### > ☆ Requirements ☆

> [1] **Windows 10 / 11**
> [2] **Download Python (Only v3,9+) :** [v3.10](https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe) **or** [v3.9](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)

### > ☆   O+   ☆
> [3] **200% Safe!**
> [4] **Having FUN EVERY MINUTES**
> [5] **If you have question, bugs, report, My Discord : #waltta#6182**

> !?!?!? **DO NOT** Installing LOG-YY-Nuker From Anyother Place Than This Page, Expect it be **Hacked/Scammed.** !?!?!?
> Download HERE ONLY (or my website) : https://github.com/waltta/LOG-YY-Nuker-Discord


#### > ☆  Installation  ☆

> [1] Extract LOG-YY-Nuker.rar
> [2] Launch "setup.bat" and wait, it will be install all modules required for LOG-YY Nuker work !
> [3] Once all modules have been installed LOG-YY will Auto-Launch !
> [4] Have FUN !

## Main Theme
> ![log-yy main_menu](https://user-images.githubusercontent.com/109160786/182341685-12cf7f94-79ac-444e-9cd7-8a200a521c39.jpg) 


## **☆    PROXY LIST     ☆**


### <a id="code-example"></a>-- ✘ Proxy List ✘

```py
    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    proxysources = [
        ["http://spys.me/proxy.txt","%ip%:%port% "],
        ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
        ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
        ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
        ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
        ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
    ]
    threads = [] 
    for url in proxysources:
        t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp, "w") as f:
        for proxy in proxies:
            for i in range(random.randint(7, 10)):
                f.write(f"{proxy}\n")
    execution_time = (time.time() - startTime)
```
### <a id="code-example"></a>✘ Auto Downloading Modules ✘

```py
import os 
import threading

try:
    import EXAMPLE v1
except:
    os.system("pip install EXAMPLE v1")
    import EXAMPLE v1

try:
    import EXAMPLE v2
except:
    os.system("pip install EXAMPLE v2")
    import EXAMPLE v2
```

<h1 align="center">
  <a id="top"></a>👁 LOG-YY-Nuker IS HERE ! 👁
</h1>

☆ @waltta#6821 ☆
</h2>
