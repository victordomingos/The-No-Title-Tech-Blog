Title: NPK-Backup
Slug: npk-backup
Status: hidden
Category: Projects


A set of two Python scripts made to automate a simple off-site backup operation in a headless Mac mini server using Dropbox. One script zips any new files/folders in a specified folder and then uploads the archive to Dropbox. The other (running in another machine with Dropbox sync enabled) removes the older archives, after a specified number of days. Why all tis work? Well, the regular Dropbox app didn't run anymore on such an old operating system (Snow Leopard), but Python and the Dropbox API did. Just added the main script to *launchd* and it worked like a charm!

<small>
**Current Status: <span style="color:green">stable</span>**  
**Main toolset:** Python 3.5+, Dropbox API, Requests  
</small>

