#!/usr/bin/env python
import os, sys
import gtk, locale
from classes import info

def main():
    from classes import lock
    lock.check_pid(os.path.join(os.path.expanduser("~"), ".openshot"))
    locale.setlocale(locale.LC_ALL, '')

    gtk.gdk.threads_init()
    gtk.gdk.threads_enter()

    from classes import project
    current_project = project.project()

    from windows.MainGTK import frmMain
    app = frmMain(project=current_project, version=info.SETUP['version'])

    return [app, app.frmMain]

if __name__ == '__main__':
    main()
