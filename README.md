# Air Alarm

Video overview:  <https://youtu.be/M5bPgH7Z2i0>
This repository is my final project for the СS50X course. In which I implemented a site that displays information about air alarms in the regions of Ukraine.


## Overview of the Course
CS50x was a transformative experience, immersing me in the fascinating realm of computer science and programming. This comprehensive course explored a wide range of topics, from fundamental concepts like algorithms and data structures to advanced subjects such as web development and software engineering. Throughout the program, I gained essential programming skills and honed my problem-solving abilities, deepening my understanding of computer science principles.

The pinnacle of the CS50x journey was the final project, where I creatively applied my newfound knowledge to solve real-world problems. This project not only showcased my ability to tackle complex challenges but also underscored the practical applications of computer science. In the end, CS50x equipped me with a strong foundation in computer science and a newfound appreciation for its versatility and relevance in various domains, opening doors to exciting opportunities in our ever-evolving technological landscape.


## Contents of the Repository
The following files are included in this repository:

- [app.py](app.py): The file for configuring the Flask web application, creating routes and APIs

- [requirements.txt](requirements.txt): This file has all the requirements to run the program

- [index.html](templates/index.html): This file contains the HTML code of the web page

- [layout.html](templates/layout.html): This file stores the layout for all HTML files

- [config.ini](static/config/config.ini): The settings for the parser is kept in this file, namely the telegram api id and api hash.
  
- [main.css](static/css/main.css): This file contains all of the CSS styles used by the site.
  
- [main.js](static/js/main.js): This file contains all of the JS scripts that the site uses.
  
- [parser_telegram.py](static/python/parser_telegram.py): This file contains the telegram parser for the channel where air alarm information is broadcast.


## Libraries used in the project
- [Telethon](https://docs.telethon.dev/en/stable/): to parse information from channel telegrams;

- [Configparser](https://docs.python.org/3/library/configparser.html): to retrieve the configuration from a configuration file;

- [Flask](https://flask.palletsprojects.com/en/3.0.x/): to create and host a web application;


## Project Description
On this website, you'll discover an interactive map of Ukraine with all of its regions, created with path components. The website uses a color-coding system to notify visitors about air quality problems in certain areas. When an air alert is issued in a certain location, the site highlights it in red. Furthermore, the information tab provides extra information, such as the alert's start time and length.

### Additional Site Functions

Aside from the interactive map and air quality alerts, the site has a number of other features:

- **Theme Selection**: Users may customize their surfing experience by switching between dark and bright themes.
  
- **In-Depth Air Quality Alert Information**: The site gives access to in-depth information on the gathered air quality warnings. Users may examine a list of air quality alarms and obtain detailed information.

- **Manual Air Alarm Status Update**: Users can manually update an alarm's air quality status.

### Information Source

The site uses an API that connects to a bespoke Telegram parser script to receive air quality alarm information. The Telegram parser pulls data from specified channels providing current-day air quality notifications. It determines the start and end timings of each air quality warning and utilizes this information to construct a message that includes information such as the area name, alert status, start time, and length of the alert.


## Warning

After you have installed all of the files on your computer, you must modify the configuration file [config.ini](static/config/config.ini) and add your telegram account info there. Otherwise, nothing will function.


## Course URL

To learn about CS50 Python course, go to the official course website on the edX platform: [CS50's Introduction to Computer Science](https://www.edx.org/learn/computer-science/harvard-university-cs50-s-introduction-to-computer-science).


## License

This repository is provided for educational and reference purposes under the MIT License.
