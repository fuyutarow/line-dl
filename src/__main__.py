from typing import List
import time
import subprocess
from pathlib import Path
import requests
from requests_html import HTMLSession

RED = '\033[0;31m'
GREEN = '\033[0;32m'
NC = '\033[0m'  # No Color


def main():
    import argparse
    parser = argparse.ArgumentParser(description='count files')
    parser.add_argument(
        'target_url',
        help="LINE sticker URL. e.g. https://store.line.me/stickershop/product/*******")
    parser.add_argument("-o",
                        "--out",
                        default="stickers",
                        help="output dirctory")
    parser.add_argument("--skip-get",
                        action='store_true',
                        help="skip to get images or sounds")
    parser.add_argument("--skip-convert",
                        action='store_true',
                        help="skip to convert images or sounds")
    args = parser.parse_args()

    session = HTMLSession()
    r = session.get(args.target_url)

    title = r.html.find(".mdCMN38Item01Ttl", first=True).text
    dirpath = Path(args.out) / f"{title}"
    dirpath.mkdir(parents=True, exist_ok=True)

    def get_imgurl_list(r):
        span_list = r.html.find(".FnCustomBase")
        get_imgurl = lambda span:\
            span.attrs["style"].split("(")[1].split(";")[0]
        url_list = [get_imgurl(span) for span in span_list]
        return url_list

    def save_data(url_list: List[str], ext: str):
        if args.skip_get: return

        print(f"[INFO] save dirctory: {dirpath}")
        for i, url in enumerate(url_list):
            r = requests.get(url)

            time.sleep(5)
            fname = dirpath / f"{i+1:02}.{ext}"
            with open(fname, "wb") as f:
                f.write(r.content)
                print(f"[INFO] save {fname}")
                print(f"[INFO] get {url}")

    def excute(cmd: List[str]):
        proc = subprocess.run(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        print(proc.stdout.decode("utf8"))

    def test_command(command: str):
        if args.skip_convert: return

        cmd = ["type", command]
        proc = subprocess.run(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        if proc.returncode:
            print(f"❌ {RED}[ERROR]{NC} {proc.stderr.decode('utf8')}")
            print(f"🙏 You need to run")
            print(f"\t{GREEN}brew install {command}{NC}")
            print(f"or")
            print(f"\t{GREEN}line-dl --skip-convert <url>{NC}")
            import sys
            sys.exit()

    is_anime = bool(r.html.find(".MdIcoPlay_b"))
    is_sound = bool(r.html.find(".MdIcoSound_b"))
    if bool(r.html.find(".MdIcoAni_b")):
        is_anime = is_sound = True
    print(f"[INFO] anime: {is_anime}, sound: {is_sound}")

    imgurl_list = get_imgurl_list(r)

    if is_sound:
        test_command("ffmpeg")

        sound = lambda imgurl:\
            imgurl.replace("sticker.png", "sticker_sound.m4a")
        sound_list = [sound(imgurl) for imgurl in imgurl_list]
        save_data(sound_list, "m4a")

    if is_anime:
        test_command("apng2gif")

        anime = lambda imgurl: imgurl\
            .replace("android", "iphone")\
            .replace("sticker.png", "sticker_animation@2x.png")
        imgurl_list = [anime(imgurl) for imgurl in imgurl_list]

    save_data(imgurl_list, "png")

    if args.skip_convert:
        return
    else:
        print("[INFO] start convert.")


    # `convert-soundanime`, `convert-sound` and `convert-anime` are installed by setup.py
    if is_sound and is_anime:
        cmd = ["convert-soundanime", f"{dirpath}"]

    elif is_sound:
        cmd = ["convert-sound", f"{dirpath}"]

    elif is_anime:
        cmd = ["convert-anime", f"{dirpath}"]

    else:
        return

    excute(cmd)


if __name__ == "__main__":
    main()
