#!/usr/bin/python3
"""Automated deployment"""


from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['52.91.127.148', '34.207.58.138']
env.user = 'ubuntu'

current_time = datetime.now()
tim = current_time.strftime('%Y%m%d%H%M%S')


def do_deploy(archive_path):
    """Function for web deployment"""
    if path.exists(archive_path):
        put(archive_path, '/tmp/')
        
        commands = ["mkdir -p /data/web_static/releases/\
        web_static_{}".format(tim), "tar -xzf /data/web_static/\
        releases/web_static_{}".format(tim), "rm /tmp/\
        web_static_{}".format(tim), "mv /data/web_static/release/\
        web_static_{}/web_static/* /data/web_static/releases/\
        web_static_{}".format(tim, tim), "rm -rf /data/\
        web_static/releases/web_static_{}/\
        web_static".format(tim), "rm -rf /data/web_static/\
        current", "ln -s /data/web_static/releases/\
        web_static_{}/data/web_static/current".format(tim)]

        for x in commands:
            run(x)

    else:
        return False

# Coded by EnGentech
