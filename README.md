# greeting-macro
A macro that will type a greeting for you.

## Introduction
I made this small Python script because I was lazy typing greetings to people on Naver Cafe (the Korean version of Reddit).
Most Naver Cafe owner makes new member comment greeting another new member before giving them permission to read and post on the Cafe.
This could sometimes be up to 150 comments before even getting to read the post on Cafe. (I know, it's crazy) So I made this macro to type a greeting for me.

And always, This Macro can be modified and used for any other forums or websites.
## Requirments
* [Python 3.9+](https://www.python.org/downloads/)

**Python packages**

* [pynput](https://pypi.org/project/pynput/) (`pip install pynput`)

## Setup
1. Download the [main.py](https://github.com/SuhJae/greeting-macro/blob/main/main.py) file.
2. If you want to change the greeting message, open the file with any text editor and change the list `greetings`, `mainword`, `emotion` to your liking.
* By defult, the macro will combine in fillowing order: `greetings` + `emotion` + (`mainword` + `emotion`(It has 1/2 chance to be added))
3. If you don't want auto comment or using it for other websites, comment code under comment called `press COMMAND + ENTER`
4. Run the file with Python.