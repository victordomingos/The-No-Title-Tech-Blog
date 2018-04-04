#!/usr/bin/env python3.6
from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FtpTarget
from ftpsync.synchronizers import UploadSynchronizer

from ftpsetupfile import *


local = FsTarget(LOCAL_DIR)
remote = FtpTarget(REMOTE_DIR, REMOTE_HOST, username=FTP_USERNAME, password=FTP_PASSWD)
opts = {"force": True, "delete_unmatched": True, "verbose": 3}

s = UploadSynchronizer(local, remote, opts)
s.run()

