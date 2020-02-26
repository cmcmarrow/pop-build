#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pop.hub


def start():
    hub = pop.hub.Hub()
    hub.pop.sub.add("popbuild.popbuild")
    hub.popbuild.init.cli()


start()
