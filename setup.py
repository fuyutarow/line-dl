from setuptools import setup

setup(
    name="line-dl",
    version="2019.9.07",
    description='get LINE stickers',
    license='MIT',
    author='FUKUDA Yutaro',
    url='https://gitlab.sairilab.com/sairilab/line-dl',
    entry_points={
        "console_scripts": [
            "line-dl = src.__main__:main",
        ],
    },
    scripts=[
        'scripts/convert-sound.sh',
        'scripts/convert-anime.sh',
        'scripts/convert-soundanime.sh',
    ],
    install_requires=[
        'requests',
        'requests-html',
    ],
)
