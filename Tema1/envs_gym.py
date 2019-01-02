#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:02:59 2018

@author: jhon
"""

from gym import envs


env_name=[ env.id for env in envs.registry.all()]

for name in sorted(env_name):
    print(name)
