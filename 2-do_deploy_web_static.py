#!/usr/bin/python3
"""Automated deployment for the Airbnb project"""


from fabric.api import *
from os import path

env.hosts = ['52.91.127.148', '34.207.58.138']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Function for web deployment"""
    try:
        if path.exists(archive_path):
            arc_tgz = archive_path.split("/")
            arg_save = arc_tgz[1]
            arc_tgz = arc_tgz[1].split('.')
            arc_tgz = arc_tgz[0]

            """Upload archive to the server"""
            put(archive_path, '/tmp')

            """Save folder paths in variables"""
            uncomp_fold = '/data/web_static/releases/{}'.format(arc_tgz)
            tmp_location = '/tmp/{}'.format(arg_save)

            """Run remote commands on the server"""
            run('mkdir -p {}'.format(uncomp_fold))
            run('tar -xvzf {} -C {}'.format(tmp_location, uncomp_fold))
            run('rm {}'.format(tmp_location))
            run('mv {}/web_static/* {}'.format(uncomp_fold, uncomp_fold))
            run('rm -rf {}/web_static'.format(uncomp_fold))
            run('rm -rf /data/web_static/current')
            run('ln -sf {} /data/web_static/current'.format(uncomp_fold))
            run('sudo service nginx restart')
            return True
        else:
            return False
    except Exception:
        return False

# Coded by EnGentech
