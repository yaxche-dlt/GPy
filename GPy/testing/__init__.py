"""

MaxZ

"""
import unittest
import sys

def deepTest(reason):
    if 'deep' in reason:
        return lambda x:x
    return unittest.skip("Not deep scanning, enable deepscan by adding 'deep' argument")
