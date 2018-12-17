#!/usr/bin/env python

import cgi
#import cgitb; cgitb.enable() # troubleshooting

import sys
import os
import re
import urllib2
import xml.etree.ElementTree as ET

bucket_url = ''
xmlns = '{http://s3.amazonaws.com/doc/2006-03-01/}'
site_readable = 'crawl.kelbi.org'

filename_pattern = re.compile("[^\da-zA-Z\-\.:]")

base_path = '/var/www/crawl/'
cache_base_path = '/tmp/crawl-web-cache/'

args = cgi.FieldStorage()

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def http_code(code):
    print "Status: " + str(code)
    print

def draw_directory(html_body, title):
    if title == None: title = "player files"
    print "Content-type: text/html"
    print
    print "<!DOCTYPE HTML><html><head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><title>%s - %s</title><style>body{font-size:larger}</style></head>" % (title, site_readable)
    print "<body>" + html_body + "</body>"
    print "</html>"

def do_work():
    # get desired path
    mode = None
    if 'm' not in args:
        return http_code(400)
    else:
        mode_select = args['m'].value
        if mode_select == '1': mode = 'ttyrec/'
        elif mode_select == '2': mode = 'morgue/'
        else: return http_code(400)
    
    cache_path = cache_base_path + mode
    local_path = base_path + mode

    # list all user folders
    if 'u' not in args:
        user_list = set() # build this list from local and remote storage

        # first retrieve remote items
        remote = None
        try:
            remote = urllib2.urlopen(bucket_url + '?prefix=%s&delimiter=/&max-keys=1000000' % mode)
        except:
            remote = None

        # parse remote response
        if remote and remote.getcode() == 200:
            response = remote.read()
            root = ET.fromstring(response)
            for contents in root.findall(xmlns+'CommonPrefixes'):
                item = contents.find(xmlns+'Prefix').text[len(mode):-1]
                user_list.add(item)

        # read local directories
        local_files = None
        try:
            local_files = os.listdir(local_path)
        except:
            local_files = []

        for item in local_files:
            if item not in user_list:
                user_list.add(item)

        # build directory html
        html_body = "<table><tr><td><a href='../'>&#8592;</a></td><td>User</td></tr>"
        for item in sorted(user_list, key=str.lower):
            html_body += "<tr><td /><td><a href='%s'>%s</a></td>" % (item,item)
        html_body += "</table>"
        return draw_directory(html_body, mode)

    # list all files for user
    elif 'f' not in args:
        user = args['u'].value # has no trailing slash
        if not user.isalnum(): return http_code(404)
        if len(user) > 50: return http_code(400)
        user += '/'

        file_dict = {} # build this list from local and remote storage

        # first retrieve remote items
        remote = None
        try:
            remote = urllib2.urlopen(bucket_url + '?prefix=%s&delimiter=/&max-keys=1000000' % (mode + user))
        except:
            remote = None

        # parse remote response
        if remote and remote.getcode() == 200:
            response = remote.read()
            root = ET.fromstring(response)
            for contents in root.findall(xmlns + 'Contents'):
                file_key = contents.find(xmlns + 'Key')
                if file_key.text == mode+user: continue # skip the folder itself
                size = contents.find(xmlns + 'Size')
                file_dict[file_key.text[len(mode+user):]] = size.text

        # read local directories
        local_files = None
        try:
            local_files = os.listdir(local_path + user)
        except:
            local_files = []

        for item in local_files:
            if item not in file_dict.keys():
                item_size = os.path.getsize(local_path + user + item)
                file_dict[item] = item_size

        # build directory html
        html_body = "<table><tr><td><a href='../'>&#8592;</a></td><td>Name</td><td>Size</td></tr>"
        for key in sorted(file_dict.keys()): #, key=lambda date: datetime.strptime(date, "%d-%b-%")):
            filename = cgi.escape(key)
            html_body += "<tr><td /><td><a href='./%s'>%s</a></td>" % (filename, filename)
            html_body += "<td>%s</td>" % sizeof_fmt(int(file_dict[key]))
            html_body += "</tr>"
        html_body += "</table>"
        return draw_directory(html_body, mode)

    # retrieve specified file
    else:
        user = args['u'].value
        filename = args['f'].value
        if not user.isalnum(): return http_code(404)
        if len(user) > 50: return http_code(400)
        if filename_pattern.match(filename): return http_code(404)
        if len(filename) > 100: return http_code(400)
        user += '/'

        try:
            file = urllib2.urlopen(bucket_url + mode + user + filename)

            httpcode = file.getcode()

            if httpcode == 200:
                print "Content-type: application/octet-stream"
                print
                sys.stdout.write(file.read())
                sys.stdout.flush()
                #print file.read()
            else:
                return http_code(httpcode)
        except:
            return http_code(404)

do_work()
