#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:09:46 2019

@author: jhon
"""

import gym

env = gym.make("MountainCar-v0")

env.reset()

for _ in range(2000):
     env.render()
     env.step(env.action_space.sample())
env.close()