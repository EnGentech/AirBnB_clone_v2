#!/usr/bin/python3
"""this scrip is written with shutil to compress files"""

from fabric.api import local
from datetime import datetime

current_time = datetime.now()
new_time = current_time.strftime('%Y%m%d%H%M%S')


def do_pack():
    """define a function to pack all the files into an archive"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz \
        web_static".format(new_time))

        return ("versions/web_static_{}".format(new_time))
    except Exception:
        return None

# Coded by EnGentech
