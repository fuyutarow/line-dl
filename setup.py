from setuptools import setup

setup(
    name="line",
    version="2019.8.30",
    description='get LINE stickers',
    license='MIT',
    author='FUKUDA Yutaro',
    url='https://github.com/fuyutarow/line-stickers',
    entry_points={
        "console_scripts": [
            "line = src.__main__:main",
        ],
    },
    scripts=[
        'scripts/convert-sound.sh',
        'scripts/convert-anime.sh',
        'scripts/convert-soundanime.sh',
        'scripts/apng2gif.js',
    ],
    install_requires=[
        'requests',
        'requests-html',
    ],
)
