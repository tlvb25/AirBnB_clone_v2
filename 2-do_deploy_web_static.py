#!/usr/bin/python3
# Fabric script that distibutes archive to servers
from fabric.api import run, env, put, local
import os

env.host = ['35.237.156.23', '35.185.70.190']

def do_deploy(archive_path):
    '''Distributes archive to servers'''

    if not os.path.exists(archive_path):
        return False
    path = archive_path.split('/')[-1]
    file = path.split('.')[0]
    step = put(archive_path, '/tmp/{}.tgz'.format(file))
    if step.failed:
        return False
    step = run('mkdir -p /data/web_static/releases/{}/'.format(file))
    if step.failed:
        return False
    step = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(file, file))
    if step.failed:
        return False
    step = run('rm /tmp/{}'.format(file))
    if step.failed:
        return False
    step = run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(file, file))
    if step.failed:
        return False
    step = run('rm -rf /data/web_static/releases/{}/web_static'.
            format(file))
    if step.failed:
        return False
    step = run('rm -rf /data/web_static/current')
    if step.failed:
        return False
    step = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(file))
    if step.failed:
        return False
    print('New version deployed!')
    return True
    