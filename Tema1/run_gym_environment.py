#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:14:07 2018

@author: jhon
"""

import gym
import sys

def run_gym_environment(argv):
    ##el primero parametro de arg  será el nmombre del entorno a ejecutar
    environment = gym.make(argv[1])
    environment.reset()
    
    for _  in range(int(argv[2])):
        environment.render()
        environment.step(environment.action_space.sample())
    environment.close()
    
if __name__== "__main__":
    run_gym_environment(sys.argv)