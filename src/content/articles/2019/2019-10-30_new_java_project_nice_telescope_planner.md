Title: New project: Nice Telescope Planner
Date: 2019-10-30 00:30
Lang: en
Tags: java, python, gui, swing, swingx, jparsec, space, telescope, astronomy, desktop, astropy, skyfield, PyONGC, OpenNGC
Category: Programming
Slug: new_java_project_nice_telescope_planner
Author: Victor Domingos
Cover: images/projects/nice_telescope_planner.png
Summary: And now, for something different, I have just dived into Java. I am sharing with you the first (pre-)release of Nice Telescope Planner, a simple cross-platform desktop utility for amateur astronomy hobbyists, written in Java. The aim is to provide an easy to use tool to help planning sky observation sessions, suggesting some of the interesting objects you may be able to watch at naked eye, or using amateur equipment (binoculars or small to medium size telescopes) in a given date/time and place.

When I first played around with this idea, after a coffee table conversation with a friend who 
happens to have a telescope at home, I sketched out on paper what could be a basic user 
interface for an application like this and looked around to see if there were some Python 
packages that could make this task possible. And I actually found a few 
([Astropy](https://www.astropy.org/), [astroplan](https://astroplan.readthedocs.io/en/latest/), 
[Skyfield](https://rhodesmill.org/skyfield/), [PyOngc](https://github.com/mattiaverga/PyOngc)) 
that allowed a reasonable abstraction level of abstraction for someone who does not have an 
academic astronomy background. I even started to do some code experiments with those, but then 
I had other priorities (I have been attending a training course on programming and software 
development), so I decided to let the project in the fridge for a while.

Then, while learning Java, me and the other students were invited to come up with a personal 
project for evaluation, and I took the challenge. This reincarnation of the telescope session 
planning application is the result of about a month of work, while learning the basics of Java
and Swing, as well as the intrinsecacies of the MySQL connector and [JPARSEC](http://conga.oan.es/~alonso/jparsec/doc/index.html) libraries.

#### Features included in this version:

- **Location manager:**
     * Full observatory location CRUD (using external MySQL database).
     * Manual GPS coordinates introduction.
     * Automatic coordinates generation based on manual country and city selection.
     * Automatic coordinates generation based on manual country and observatory selection.
     * Automatic coordinates based on IP address.
- **Session setup:**
     * Location selection.
     * Session date selection.
     * Session start and end times.
- **Filtering:**
     * by limiting magnitude (slider and spin text box).
     * by limiting magnitude presets.
     * by object kind.
     * by constellation.
- **Space Objects supported:**
     * All Solar System planets, including Pluto.
     * The Moon.
     * Several other natural satellites.
- **Basic object data: **
     * Magnitude.
     * Angular diameter.
     * Elongation.
     * Phase.
     * Phase angle.
     * Equatorial coordinates - right ascension (RA) and declination (Dec).
     * Current distance to Earth, in several units.
     * Constellation (i.e. the approximate area of the sky where you can find each target).
- **Photos of planets and natural satellites (public domain images from NASA/Wikimedia Commons).**
- **Rise/Set/Transit times.**
- **Table of hourly positions (Altitude/Azimuth).**


Please take into consideration that there are still lots of features missing, like session saving and management, session notes, deep space targets listing, bookmarking favorite targets, filtering bookmarked and seen objects, and others. At this time, you can expect the application to display all the Solar System planets, the Moon and some of the natural satellites that can be seen from Earth.

At this time, this application is still under development and requires a MySQL database server. The database must be manually created, for instance by "forward engineering" the provided file (docs/EER_diagram.mwb) using MySQL Workbench. In the future, it will probably progress into a more nicely integrated solution, like a built-in SQLite database.

You can expect the application to display all the Solar System planets, the Moon and some of the natural satellites that can be seen from Earth. Please take into consideration that there are still some bugs and lots of features missing, like session saving and management, session notes, deep space targets listing, bookmarking favorite targets, filtering bookmarked and seen objects, and others. 



You can check out the development repository on GitHub:

* **GitHub Repository: **  [Nice Telescope Planner](https://github.com/victordomingos/NiceTelescopePlanner){:target=“_blank”}

If you have some nice tip and want to contribute, I will certainly appreciate very much! :)
