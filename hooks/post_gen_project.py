#!/usr/bin/env python

"""
Cookie Cutter post generation hook

"""
from __future__ import print_function

import os, sys, shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def apply_git():
    """Apply the relevant files to git, and create github as required"""

    # Initialise and add files to the git repository
    print("\n--------------------------------------")
    print("Initialising git & github remote repo - {{cookiecutter.project_repo}}")
    os.system( "git init .")
    os.system( "git add examples/*.py" )
    os.system( "git add docs/*.rst" )
    os.system( "git add README.rst" )
    os.system( "git add CONTRIBUTING.rst" )
    os.system( "git add .gitignore")

    # Perform initial commit project files
    print("\n--------------")
    print("Initial commit")
    os.system( "git commit -m 'Initial commit with cookiecutter create' >/dev/null")

    print("\n---------------------------")
    print( "Creating remote repository")
    os.system( "git remote add origin {{cookiecutter.project_ghurl}} >/dev/null")
    os.system( "curl -u '{{cookiecutter.author_username}}' https://api.github.com/user/repos -d '{\"name\":\"{{cookiecutter.project_repo}}\",\"description\":\"{{cookiecutter.project_desc}}\"}' >/dev/null")
    os.system( "git push -u origin master" )



def add_bug_reporting():
    """Add the Bug reporting section to the README.rst"""
    section = """
Every care is taken to try to ensure that this documentation comes to you error free.
If you do find an error - please report the problem on :
`GitHub <{{cookiecutter.project_gh}}>`_
or
by email to : `{{cookiecutter.author}} <mailto:{{cookiecutter.author_email}}?Subject={{cookiecutter.project_repo}}%20Error>`_
""".split("\n")

    max_len = max(map(len,section))
    max_len = max_len + (max_len % 2)

    with open(os.path.join(PROJECT_DIRECTORY,"README.rst"), "a") as readme:
        readme.write("+" + "-"*max_len + "+\n")
        readme.write("|" + " "*(max_len/2-2) + "Bugs" + " "*(max_len/2-2) + "+\n")
        readme.write("+" + "="*max_len + "+\n")
        for l in section:
            readme.write("|" + l + " "*(max_len-len(l)) + "|\n")
        readme.write("+" + "-"*max_len + "+\n")


add_bug_reporting()

apply_git()



