#%%
from typing import List
import time
from pathlib import Path
import requests
from requests_html import HTMLSession

#%%
session = HTMLSession()
url = "https://store.line.me/stickershop/product/8460/ja?from=sticker"
r = session.get(url)

#%%
is_animetaion = bool(r.html.find(".MdIcoPlay_b"))
is_sound = bool(r.html.find(".MdIcoSound_b"))

#%%
title = r.html.find(".mdCMN38Item01Ttl", first=True).text
dirpath = Path(f"./imgs/{title}")
dirpath.mkdir(parents=True, exist_ok=True)


#%%
def get_imgurl_list():
    span_list = r.html.find(".FnCustomBase")
    get_imgurl = lambda span: span.attrs["style"].split("(")[1].split(";")[0]
    url_list = [get_imgurl(span) for span in span_list]
    return url_list


#%%
def save_data(url_list: List[str], ext: str):
    for i, url in enumerate(url_list):
        req = requests.get(url)
        print(url)

        time.sleep(5)
        with open(dirpath / f"{i+1:02}.{ext}", "wb") as f:
            f.write(req.content)


#%%
def excute(cmd: List[str]):
    import subprocess
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(proc.stdout.decode("utf8"))


if is_animetaion:
    animation = lambda imgurl: imgurl\
        .replace("android", "iphone")\
        .replace("sticker.png", "sticker_animation@2x.png")

    imgurl_list = get_imgurl_list()
    imgurl_list = [animation(imgurl) for imgurl in imgurl_list]
    save_data(imgurl_list, "png")

    cmd = ["bash", "scripts/convert-animation.sh", f"{dirpath}"]
    excute(cmd)

elif is_sound:
    sound = lambda imgurl: imgurl.replace("sticker.png", "sticker_sound.m4a")

    imgurl_list = get_imgurl_list()
    sound_list = [sound(imgurl) for imgurl in imgurl_list]
    save_data(imgurl_list, "png")
    save_data(sound_list, "m4a")

    cmd = ["bash", "scripts/convert-sound.sh", f"{dirpath}"]
    excute(cmd)

else:
    imgurl_list = get_imgurl_list()
    save_data(imgurl_list, "png")
