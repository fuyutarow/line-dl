from setuptools import setup

setup(
    name="line-dl",
    version="2019.9.08",
    description='get LINE stickers',
    license='MIT',
    author='FUKUDA Yutaro',
    url='https://gitlab.sairilab.com/sairilab/line-dl',
    entry_points={
        "console_scripts": [
            "line-dl = src.__main__:main",
        ],
    },
    install_requires=[
        'requests',
        'requests-html',
    ],
    scripts=[
        'bin/convert-sound',
        'bin/convert-anime',
        'bin/convert-soundanime',
    ],
)
