Title: Projects
Slug: projects

Here you can find a few of my programming projects. Most of them started as a learning experience and then evolved into a daily use tool. I like to learn through real world examples, so I always try to solve some kind of problem while learning how to use a new Python feature or some API. So, I would probably write each of these applications in a very different way if I was starting it as a new project.

These are all open source projects, that are available on GitHub. Please feel free to check the license, clone them, use them, or even contribute back.  

### RepService

![RepService - Database application for in-store registering of warranty and service/repair processes]({filename}/images/projects/repservice.jpg)
Database application for in-store registering of warranty and service/repair processes in general. It enables store staff to keep an organized log of the products left for repair by costumers, their route during the process and the communications made. Processes that require special attention, for instance because of a delay in delivery or while waiting for an answer from the costumer, are highlighted in the main list, in order to allow proper intervention by the staff team.

**Current Status: <span style="color:chocolate">under development</span>**  
**Main toolset:** Python 3.6+, SQLalchemy, SQLite, tkinter, ttk   

### PT-Tracking

![PT-Tracking - Parcel tracking application for CTT and CTT Expresso]({filename}/images/projects/pt-tracking.png)
Simple database application allows to keep a register and automatically track online the shipments and registered mail sent through the portuguese mail companies CTT and CTT Expresso. It also helps in making sure that all checks for orders with payment on delivery are correctly received and deposited on the bank on the correct dates.

**Current Status: <span style="color:green">stable</span>**    
**Main toolset:** Python 3.6+, SQLite, tkinter, ttk, BeautifulSoup, Requests  

### ContarDinheiro.py
![ContarDinheiro.py - A single-window utility to help you count money]({filename}/images/projects/contar-dinheiro.png)
Every programmer makes one of these at some point, like while learning a language or a new GUI toolkit. Just a single-window utility to help you count all those bills and coins.

**Current Status: <span style="color:green">stable</span>**  
**Main toolset:** Python 3.6+, tkinter, ttk   

### NPK Backup
A set of two Python scripts made to automate a simple off-site backup operation in a headless Mac mini server using Dropbox. One script zips any new files/folders in a specified folder and then uploads the archive to Dropbox. The other (running in another machine with Dropbox sync enabled) removes the older archives, after a specified number of days. Why all tis work? Well, the regular Dropbox app didn't run anymore on such an old operating system (Snow Leopard), but Python and the Dropbox API did. Just added the main script to *launchd* and it worked like a charm!

**Current Status: <span style="color:green">stable</span>**  
**Main toolset:** Python 3.5+, Dropbox API, Requests  

### OpenWeather

![OpenWeather - Check the weather in your iPhone using a Python app]({filename}/images/projects/openweather.png)
A little fun project made in an iPhone using Pythonista. It's a nicely formatted console app that checks the weather forecast for the next few days. This version is custom made for iPhone, so it uses Pythonista 3. It makes use of the web API provided by openweathermap.org. It shows the current weather and the forecast for the next 5 days. It can use the device's barometer and location services, if available. If they are not available, the app falls back, respectively, to the data provided by the web API and a default location.


**Current Status: <span style="color:green">stable</span>**  
**Main toolset:** Python 3.6+, Pythonista for iOS, Requests, OpenWeatherMap.org API, JSON  
