#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk, os

from sugar.activity import activity


class OpenShotActivity(activity.Activity):
    
    def __init__(self, handle):
        
        activity.Activity.__init__(self, handle, False)
        
        builder = gtk.Builder()

        builder.add_from_file(os.path.join(os.path.realpath(__file__).replace(__file__, ''), 'openshot/windows/ui/Main.ui'))
        vbox = builder.get_object('vboxMenu')
        
        self.set_canvas(vbox)
        self.show_all()
