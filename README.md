# LINE stickers 

![](https://stickershop.line-scdn.net/stickershop/v1/sticker/222551965/android/sticker.png)


## Requirements
- Python 3.5+
- ffmpeg (required for converting apng to gif)
- Node.js (required for converting png and m4a to mp4)

```sh
brew install ffmpeg ;: for converting png and m4a to mp4
npm i -g https://github.com/suchipi/node-apng2gif ;: for converting apng to gif
```

## Installation
```sh
pip install -e git+https://github.com/fuyutarow/line-stickers#egg=line
```

## Usage

target: https://store.line.me/stickershop/product/8751482/ja
```sh
line -o mystickers "https://store.line.me/stickershop/product/8751482/ja"
```

:warning: Quote url. "${url}"


## Features
- Support for only animation stickers
- Support for only sound stickers
- Support for animation and sound stickers

----

## Project setup
```sh
brew install pipenv
pipenv install --dev
```

## Run main
```sh
pipenv run get -o mystickers "https://store.line.me/stickershop/product/8751482/ja"
```

## Development workflow
```sh
pipenv shell
code .
```

## Lints and fixes files
```sh
pipenv run lint
```

----

## Recommended
```sh
alias pi=pipenv
```

## Recommended 2
Let's name local GoogleDrive directory `~/Gdrive` and
use [Backup and Sync](https://www.google.com/drive/download/backup-and-sync/).

```sh
alias line="line -o ~/Gdrive/stickers"
ln -s ~/Gdrive/stickers ~/Gdrive/スタンプ🥺
```
and add ` ~/Gdrive/スタンプ🥺` to sidebar of Finder.


Enjoy!
![](https://stickershop.line-scdn.net/stickershop/v1/sticker/105752559/iphone/sticker_animation@2x.png)
