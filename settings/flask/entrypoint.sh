#!/bin/sh
[ ! -d "../../migrations" ] && flask db init
flask db migrate
flask db upgrade
uwsgi wsgi.ini