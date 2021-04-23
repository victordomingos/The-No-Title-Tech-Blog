Title: NPK-Backup
Slug: npk-backup
Lang: en
Status: hidden
Cover: images/2018/npk-backup.png

![NPK-Backup]({filename}/images/2018/npk-backup.png)

A set of two Python scripts made to automate a simple off-site backup operation in a headless Mac mini server using Dropbox. One script zips any new files/folders in a specified folder and then uploads the archive to Dropbox. The other (running in another machine with Dropbox sync enabled) removes the older archives, after a specified number of days.  

Why all tis work? Well, the regular Dropbox app didn't run anymore on such an old operating system (Snow Leopard), but Python and the Dropbox API did. Just added the main script to *launchd* and it worked like a charm!  

Want to know more about this project? Check out its [full story]({filename}/articles/2018/2018-04-12_python_to_the_rescue.md) in the blog.  

___

**Current Status: <span style="color:chocolate">not maintained anymore</span>**  
**Main toolset: ** [Python 3.5+](https://www.python.org){target=:_blank}, [Dropbox API](https://www.dropbox.com/developers/documentation/http/documentation){target=:_blank}, [Requests](https://requests.readthedocs.io/en/master/){target=:_blank}  
**Source code: ** [**Fork it on GitHub**](https://github.com/victordomingos/NPK-Backup){target=:_blank}


