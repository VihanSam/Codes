from ursina import *
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()

Sky()
player=FirstPersonController(y=2, orgin_y=-.5)
ground=Entity(model='plane', scale=(100, 1, 100), color=color.lime, texture="white_cube",
    texture_scale=(100, 100), collider='box')
wall_1=Entity(model="cube", collider="box", position=(-8, 0, 0), scale=(8,5,1), rotation=(0, 0, 0),
    texture="brick", texture_scale=(5,5), color=color.rgb(255, 128, 0))
wall_2 = duplicate(wall_1, z=5)
wall_3=duplicate(wall_1, z=10)
wall_4=Entity(model="cube", collider="box", position=(-15, 0, 10), scale=(1,5,20), rotation=(0, 0, 0),
    texture="brick", texture_scale=(5,5), color=color.rgb(255, 128, 0))
wall_5 = duplicate(wall_1, z=5)
wall_6 = duplicate(wall_1, z=10)
wall_7 = duplicate(wall_1, z=15)
wall_8 = duplicate(wall_1, z=20)
wall_2 = duplicate(wall_1, z=10)

gun=Entity(model="assets/gun.obj", parent=camera.ui, scale=.08, color=color.gold, position=(.3, -.2),
    rotation=(-5, -10, ))

app.run()