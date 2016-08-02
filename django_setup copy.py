#!/usr/bin/python
# Script to set up basic Django structure

import subprocess
import os
import django
import re
import time
import pdb


def update_file(pathStr, index, inputStr, flags=0):

    print ('updating file: ' + pathStr + ':' + index)

    with open(pathStr, 'r+') as f:
        fileContents = f.read()
        textPattern = re.compile(re.escape(index), flags)
        fileContents = textPattern.sub(inputStr, fileContents)
        f.seek(0)
        f.truncate()
        f.write(fileContents)


def get_Secret_Key(pathStr):

    print ('getting secret key....')

    secret_key = ''

    f_handle = open(pathStr)

    for line in f_handle:

            line = line.rstrip()

            if re.search('^SECRET_KEY ', line):

                secret_key = re.findall('\'.+', line)

    f_handle.close()

    return str(secret_key[0])


def get_subprocess(cmd):

    print ('getting subprocess: ' + str(cmd))

    ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)

    return ps.communicate()[0]

    psid = ps.pid

    os.kill(psid, 9)


def get_venv(case):

    print ('returning venv....')

    return {
        0: 'development',
        1: 'testing',
        2: 'production',
        3: 'staging',
    }.get(case, 0)


def setup_venv(tempStr):

    print ('setting up virtual envs....')

    pathStr = get_subprocess(['which', 'virtualenvwrapper.sh'])

    pathStr = pathStr.decode('ascii').strip()

    prefixStr = 'source ' + pathStr

    pyStr = get_subprocess(['which', 'python3'])

    pyStr = pyStr.decode('ascii').strip()

    for venv in range(4):

        venvStr = get_venv(venv)

        projectStr = 've_' + venvStr[:3]

        print ('venv: ' + projectStr)

        cmdStr = prefixStr + ' && mkvirtualenv --python=' + pyStr + \
                             ' %s --no-site-packages' % (projectStr)

        subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

        time.sleep(8)

        cmdStr = ('source ~/.virtualenvs/' + projectStr + '/bin/activate && '
                  'pip install -r ./requirements/' + venvStr + '.txt')

        print ('cmdStr: ' + cmdStr)

        ps = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)

        print (ps.communicate()[0])

        ps.wait()


def setup_structure(rootStr, tempStr):

    print ('setting up structure....')

    get_subprocess(['mkdir', rootStr])

    os.chdir(rootStr)

    get_subprocess(['mkdir', 'functional_tests'])

    pathStr = '../django_templates/test_all_users.py'

    get_subprocess(['cp', pathStr, 'functional_tests/test_all_users.py'])

    get_subprocess(['touch', 'functional_tests/__init__.py'])

    get_subprocess(['django-admin.py', 'startproject', tempStr, '.'])

    time.sleep(8)

    get_subprocess(['touch', tempStr + '/views.py'])

    write_file(tempStr + '/views.py', '# -*- coding: utf-8 -*-\n'
               'from django.shortcuts import render\n'
               'from django.utils.timezone import now\n\n\n'
               'def home(request):\n    return render'
               '(request, "' + tempStr + '/index.html",\n'
               '{\'today\': today, \'now\': now()})\n\n\n'
               'def home_files(request, filename):\n    return render(request, '
               'filename, {}, content_type="text/plain")\n\n\n')

    get_subprocess(['mv', tempStr + '/manage.py', 'manage.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/settings.py',
                    './' + tempStr + '/settings.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/urls.py',
                    './' + tempStr + '/urls.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/wsgi.py',
                    './' + tempStr + '/wsgi.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/__init__.py',
                    './' + tempStr + '/__init__.py'])

    get_subprocess(['rm', '-r', tempStr + '/' + tempStr])

    indexStr = 'urlpatterns = ['

    inputStr = 'urlpatterns += i18n_patterns('

    update_file(tempStr + '/urls.py', indexStr, inputStr)

    indexStr = ']'

    inputStr = ')'

    update_file(tempStr + '/urls.py', indexStr, inputStr)

    inputStr = 'from django.contrib import admin\n\nurlpatterns = [\n\n    url(r\'^'\
               '(?P<filename>(robots.txt)|' \
               '(humans.txt))$\',\n     home_files, name=\'home_files\'),\n\n]\n'

    indexStr = 'from django.contrib import admin'

    update_file(tempStr + '/urls.py', indexStr, inputStr)

    indexStr = 'from django.contrib import admin'

    inputStr = 'from django.contrib import admin\n' \
               'from django.conf.urls.i18n import i18n_patterns\n' \
               'from .views import home, home_files\n'

    update_file(tempStr + '/urls.py', indexStr, inputStr)

    indexStr = 'site.urls)),'

    inputStr = ('site.urls)),\n    url(r\'^$\', home, name=\'home\'),\n')

    update_file(tempStr + '/urls.py', indexStr, inputStr)

    get_subprocess(['mkdir', 'requirements'])

    get_subprocess(['touch', 'requirements/base.txt'])

    get_subprocess(['mkdir', tempStr + '/settings'])

    get_subprocess(['mkdir', tempStr + '/static'])

    get_subprocess(['mkdir', tempStr + '/locale'])

    get_subprocess(['mkdir', '-p', tempStr + '/static/js'])

    get_subprocess(['mkdir', '-p', tempStr + '/static/js/vendor'])

    get_subprocess(['mkdir', '-p', tempStr + '/static/css'])

    get_subprocess(['mkdir', tempStr + '/templates'])

    get_subprocess(['mkdir', tempStr + '/media'])

    get_subprocess(['mkdir', tempStr + '/templates/' + tempStr])

    get_subprocess(['cp', '../django_templates/html5bs/robots.txt',
                    tempStr + '/templates/robots.txt'])

    get_subprocess(['cp', '../django_templates/html5bs/humans.txt',
                    tempStr + '/templates/humans.txt'])

    get_subprocess(['cp', '../django_templates/html5bs/404.html',
                    tempStr + '/templates/404.html'])

    get_subprocess(['cp', '../django_templates/html5bs/base.html', tempStr +
                    '/templates/base.html'])

    get_subprocess(['touch', tempStr + '/templates/' + tempStr + '/index.html'])

    write_file(tempStr + '/templates/' + tempStr + '/index.html',
               '{% extends "base.html" '
               '%}\n{% block head_title %}TaskBuster Django Tutorial'
               '{% endblock %}\n{% block content %}{% endblock %}\n')

    get_subprocess(['cp', '../django_templates/html5bs/css/main.css',
                    tempStr + '/static/css/main.css'])

    get_subprocess(['cp', '../django_templates/html5bs/favicon.ico',
                    tempStr + '/static/favicon.ico'])

    get_subprocess(['cp', '../django_templates/html5bs/css/normalize.css',
                    tempStr + '/static/css/normalize.css'])

    get_subprocess(['cp', '../django_templates/html5bs/css/normalize.min.css',
                    tempStr + '/static/css/normalize.min.css'])

    get_subprocess(['cp', '../django_templates/html5bs/js/main.js',
                    tempStr + '/static/js/main.js'])

    get_subprocess(['cp', '../django_templates/html5bs/js/plugins.js',
                    tempStr + '/static/js/plugins.js'])

    get_subprocess(['cp', '../django_templates/html5bs/js/vendor/'
                    'modernizr-2.8.3.min.js', tempStr + '/static/js/vendor'
                    'modernizr-2.8.3.min.js'])

    os.chdir(tempStr + '/settings')

    get_subprocess(['touch', '__init__.py', 'base.py'])

    os.chdir('../..')


def write_file(pathStr, inputStr):

    print ('writing to file: ' + pathStr + inputStr)

    f_handle = open(pathStr, 'a')

    f_handle.write(inputStr)

    f_handle.flush()

    f_handle.close()


def setup_requirements():

    print ('setting up requirements....')

    pathStr = 'requirements/base.txt'

    inputStr = 'Django==' + django.get_version() + '\npytz\n'

    write_file(pathStr, inputStr)

    for venv in range(4):

        pathStr = 'requirements/' + get_venv(venv) + '.txt'

        get_subprocess(['touch', pathStr])

        ps = subprocess.Popen(['echo', '-r base.txt'], shell=False,
                              stdout=subprocess.PIPE)

        subprocess.Popen(['tee', '-a', pathStr], shell=False,
                         stdin=ps.stdout)

        if venv == 1:

            write_file(pathStr, 'selenium==2.48.0\ncoverage\n')


def setup_settings(tempStr):

    print ('setting up settings....')

    os.chdir(tempStr + '/settings')

    for venv in range(4):

        pathStr = get_venv(venv) + '.py'

        inputStr = '# -*- coding: utf-8 -*-\nfrom .base import *\n'

        if pathStr[:-3] == 'production':

            inputStr = inputStr + 'DEBUG = False\n'

        else:

            inputStr = inputStr + 'DEBUG = True\n'

        write_file(pathStr, inputStr)

    get_subprocess(['mv', '../settings.py', 'base.py'])

    time.sleep(3)

    for venv in range(2):

        if venv == 0:

            venvStr = 'development'

        else:

            venvStr = 'testing'

        pathStr = ('/Users/GSW/.virtualenvs/ve_' + venvStr[:3] +
                   '/bin/postactivate')

        inputStr = 'export DJANGO_SETTINGS_MODULE=' + tempStr + \
                   '.settings.' + venvStr + '\nexport SECRET_KEY=' + \
                   get_Secret_Key('base.py') + '\n'

        get_subprocess(['touch', pathStr])

        write_file(pathStr, inputStr)

        pathStr = ('/Users/GSW/.virtualenvs/ve_' + venvStr[:3] +
                   '/bin/predeactivate')

        get_subprocess(['touch', pathStr])

        inputStr = ('unset DJANGO_ SETTINGS_MODULE\nunset SECRET_KEY\n')

        write_file(pathStr, inputStr)

    inputStr = ('STATICFILES_DIRS = (\n  os.path.join(BASE_DIR, "static"),'
                '\n)\n\n')

    pathStr = os.getcwd() + '/base.py'

    write_file(pathStr, inputStr)

    update_file(pathStr, '[]', '[os.path.join(BASE_DIR, "templates")]')

    update_file(pathStr, "TIME_ZONE = 'UTC'", "TIME_ZONE = 'Europe/Madrid'")

    indexStr = 'context_processors\': ['

    inputStr = 'context_processors\': [\n           \'django.template.' \
               'context_processors.i18n\',\n'

    update_file(pathStr, indexStr, inputStr)

    indexStr = 'MIDDLEWARE_CLASSES = ('

    inputStr = 'MIDDLEWARE_CLASSES = (\n    \'django.contrib.sessions.' \
               'middleware.SessionMiddleware\',\n    \'django.middleware.' \
               'locale.LocaleMiddleware\',\n    \'django.middleware.common.' \
               'CommonMiddleware\',\n'

    update_file(pathStr, indexStr, inputStr)

    indexStr = 'import os'

    inputStr = 'import os\nfrom django.utils.translation import ugettext_lazy as _\n'

    update_file(pathStr, indexStr, inputStr)

    indexStr = 'USE_TZ = True'

    inputStr = 'USE_TZ = True\nLANGUAGES = (\n    (\'en\', _(\'English\')),\n    ' \
               '(\'es\', _(\'Castellano\')),\n)\n\nLOCALE_PATHS = (\n    ' \
               'os.path.join(BASE_DIR, \'locale\'),\n)'

    update_file(pathStr, indexStr, inputStr)

    with open(os.getcwd() + '/base.py', 'a') as f:
        with open('/Users/GSW/Documents/Sites/django_templates/'
                  'base_sk_template.py') as f2:
            lines = f2.readlines()
            for line in lines:
                f.write(line)

    os.chdir('../..')


def setup_git():

    print ('setting up git....')

    get_subprocess(['git', 'init'])

    get_subprocess(['touch', '.gitignore'])

    inputStr = 'db.sqlite3\n__pycache__\n.coverage\nhtmlconv'

    write_file(os.getcwd() + '/.gitignore', inputStr)

    get_subprocess(['git', 'add', '-A'])

    get_subprocess(['git', 'commit', '-m', 'Project created'])


def setup_translation(rootStr):

    os.chdir('/Users/GSW/Documents/Sites/' + rootStr)

    get_subprocess(['python', 'manage.py', 'makemessages', '-l', 'es'])


def main():

    os.chdir('/Users/GSW/Documents/Sites/')

    tempStr = 'gsw'

    rootStr = tempStr + '_project'

    setup_structure(rootStr, tempStr)

    setup_requirements()

    setup_venv(tempStr)

    setup_settings(tempStr)

    setup_git()

    setup_translation(rootStr)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
