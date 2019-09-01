#%%
import time
from pathlib import Path
import requests
from requests_html import HTMLSession

#%%
session = HTMLSession()
url = "https://store.line.me/stickershop/product/12652/ja"
r = session.get(url)

#%%
is_apng = bool(r.html.find(".MdIcoPlay_b"))
if is_apng:
    import subprocess
is_apng

#%%
title = r.html.find(".mdCMN38Item01Ttl", first=True).text
title

#%%
span_list = r.html.find(".FnCustomBase")
get_imgurl = lambda span: span.attrs["style"].split("(")[1].split(";")[0]
apngurl = lambda imgurl: imgurl.replace("android", "iphone").replace(
    "sticker.png", "sticker_animation@2x.png")
imgurl_list = [get_imgurl(span) for span in span_list]
if is_apng:
    imgurl_list = [apngurl(imgurl) for imgurl in imgurl_list]
imgurl_list

#%%
dirpath = Path(f"./imgs/{title}")
dirpath.mkdir(parents=True, exist_ok=True)

#%%
for i, imgurl in enumerate(imgurl_list):
    req = requests.get(imgurl)
    print(imgurl)

    time.sleep(5)
    with open(dirpath / f"{i+1:02}.png", "wb") as f:
        f.write(req.content)

#%%
if is_apng:
    cmd = f"bash scripts/convert.sh {dirpath}"
    proc = subprocess.run(cmd.split(),
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    print(proc.stdout.decode("utf8"))
