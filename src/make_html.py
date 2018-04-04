#!/usr/bin/env python3.6
import os

from pelican import Pelican
from pelican.settings import read_settings


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

settings_filepath = os.path.expanduser(dname+"/pelicanconf.py")
settings = read_settings(settings_filepath)
pelican = Pelican(settings)
pelican.run()
