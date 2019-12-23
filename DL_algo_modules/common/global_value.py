#！/usr/bin/python
# -*- coding: utf-8 -*-

class GlobalValue():
    def __init__(self):
        self._global_dict
        self._global_dict = {}
    
    def set_value(self, key, value):
        self._global_dict[key] = value
    
    def get_value(self, key, def_val=None):
        return self._global_dict.get(key, default=def_val)

GLOBAL_VALUE = GlobalValue()