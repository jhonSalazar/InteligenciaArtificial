#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 21:13:43 2019

@author: jhon
"""

import gym 

environment = gym.make("MountainCar-v0") 
MAX_NUM_EPISODES =1000


for episode in range(MAX_NUM_EPISODES):
    done = False
    obs = environment.reset()
    total_reward = 0.0 #variable para guardar la recompensan total de cada episodio
    step = 0
    
    while not done:
        environment.render()
        action = environment.action_space.sample()
        next_state, reward, done,info = environment.step(action)
        total_reward +=reward
        step+=1
        obs= next_state
    
    print("\n Episodio numero {} finalizada con {} iteraciones. Recompensa Final {}".format(episode,step+1,total_reward))
   


    
        
environment.close() # Cerramos la sesión de Open AI Gym
