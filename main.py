#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from dom_monitor import DomMonitor


def main():
    mon = DomMonitor()
    mon.exec(*sys.argv)


if __name__ == '__main__':
    main()
