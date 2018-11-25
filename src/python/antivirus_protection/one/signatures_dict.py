# -*- coding: utf8 -*-
# @Author: Alexander Sharov

import os
import json


def get_signatures_dict(signatures_json):
    abspath = os.path.abspath(os.path.dirname(__file__))
    return json.loads(open(os.path.join(abspath, signatures_json), "r", encoding="utf-8").read())["data"]
