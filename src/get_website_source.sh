#!/usr/bin/env bash
echo " "
echo "Obtaining current source from Git repository..."
git clone https://github.com/victordomingos/The-No-Title-Tech-Blog.git
cd The-No-Title-Tech-Blog
cd src
pelican content
ls -lhosa
MY_SRC_PATH=$(pwd)
echo "The downloaded source code is at:"
echo $MY_SRC_PATH
