# -*- coding: utf-8 -*-

import gtk
from sugar.activity import activity
from openshot import openshot
import sys
sys.path.append(activity.get_bundle_path() + "/openshot")


class OpenShot(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle, False)
        data = openshot.main()
        canvas_ = data[1]
        self.set_canvas(canvas_)
        self.show_all()
        data[0].refresh()
        data[0].run()
