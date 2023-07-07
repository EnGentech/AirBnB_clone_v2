#!/usr/bin/python3
"""Automated deployment for the Airbnb project"""


from fabric.api import *
from os import path

env.hosts = ['52.91.127.148', '34.207.58.138']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Function for web deployment"""
    if path.exists(archive_path):
        tim = archive_path[20:-4]
        put(archive_path, '/tmp/')

        pad = "/data/web_static/releases/web_static_"

        a = "sudo mkdir -p {}{}".format(pad, tim)
        b = "sudo tar -xzf /tmp/web_static_\
        {}.tgz -C {}{}".format(tim, pad, tim)
        c = "sudo rm /tmp/web_static_{}.tgz".format(tim)
        d = "sudo mv {}{}/web_static/* {}{}".format(pad, tim, pad, tim)
        e = "sudo rm -rf {}{}/web_static".format(pad, tim)
        f = "sudo rm -rf /data/web_static/current"
        g = "sudo ln -s {}{}/data/web_static/current".format(pad, tim)

        commands = [a, b, c, d, e, f, g]
        for command in commands:
            run(command)

    else:
        return False

# Coded by EnGentech
