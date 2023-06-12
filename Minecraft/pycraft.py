from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise
app = Ursina()

window.color = color.rgb(0,200,211)
window.exit_button.visible = False
# Loading texture
grass_14 = load_texture("grass_14.png")
# How to Quit
def input(key):
    if key == 'q' or key == 'tab':
        quit()

def update():
    pass

terrain = Entity(model=None,collider=None)

terrainWidth = 10
for i in range(terrainWidth*terrainWidth):
    bud = Entity(model='cube',color=color.green,
              texture='grass_14.png')

    bud.x = i/terrainWidth
    bud.z = i%terrainWidth
    bud.y = 0
    bud.parent = terrain

terrain.combine()
terrain.collider = 'mesh'

subject = FirstPersonController()
subject.x = subject.z = 5
subject.y = 12
app.run()