#!/usr/bin/env bash
pkill uwsgi;
uwsgi -x qaschool.xml;