import os
import pyglet

sd = r"D:\Users\VG\proj\p_Python\dinnn"
sf = r"VG company.wav"
sp = os.path.join(sd, sf)
print(sp)

sound = pyglet.media.load(sp)
sound.play()
pyglet.app.run()
