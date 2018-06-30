#!/usr/bin/env python3.6
from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FtpTarget
from ftpsync.synchronizers import UploadSynchronizer

from ftpsetupfile import *

print('\n\nOpening an FTP connection for the upload...\n')

local = FsTarget(LOCAL_DIR)
remote = FtpTarget(REMOTE_DIR, REMOTE_HOST, username=FTP_USERNAME, password=FTP_PASSWD)
opts = {"force": True, "delete_unmatched": True, "verbose": 2}

s = UploadSynchronizer(local, remote, opts)
s.run()

print('\n\nUpload complete!')