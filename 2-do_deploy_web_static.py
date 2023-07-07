#!/usr/bin/python5
"""Automated deployment"""


from fabric.api import *
from os import path

env.hosts = ['52.91.127.148', '34.207.58.138']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Function for web deployment"""
    if path.exists(archive_path):
        tim = archive_path[20:-4]
        put(archive_path, '/tmp/')

        pad = "/data/web_static/releases/web_static"

        a = "mkdir -p {}{}".format(pad, tim)
        b = "tar -xzf /tmp/web_static_{}.tgz -C {}{}".format(tim, pad, tim)
        c = "rm /tmp/web_static_{}.tgz".format(tim)
        d = "mv {}{}/web_static/* {}{}".format(pad, tim, pad, tim)
        e = "rm -rf {}{}/web_static".format(pad, tim)
        f = "rm -rf /data/web_static/current"
        g = "ln -s {}{}/data/web_static/current".format(pad, tim)
        
        commands = [a, b, c, d, e, f, g]
        for command in commands:
            run(command)

    else:
        return False

# Coded by EnGentech
