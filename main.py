#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from dom_monitor import DomMonitor


def main(*arg):
    mon = DomMonitor()
    mon.exec(*arg)


if __name__ == '__main__':
    args = sys.argv
    main(*args)
