import tkinter
import pygame.mixer

app = tkinter.Tk()
app.title('DJ Mix')

filename = 'music.wav'

pygame.mixer.init()

track = pygame.mixer.Sound(filename)
volume = tkinter.DoubleVar()
volume.set(track.get_volume())
channel = pygame.mixer.find_channel()
pause = tkinter.BooleanVar()
pause.set(False)

def start():
    if not pause.get():
        channel.play(track)
    else:
        channel.unpause()

def stop():
    pause.set(True)
    channel.pause()

def change_volume(v):
    channel.set_volume(volume.get())

start_btn = tkinter.Button(app, command=start, text='Start')
start_btn.pack(side=tkinter.LEFT)
stop_btn = tkinter.Button(app, command=stop, text='Stop')
stop_btn.pack(side=tkinter.RIGHT)
scale = tkinter.Scale(
    variable=volume, from_=0.0, to=1.0, resolution=0.1, command=change_volume,
    label='Volume', orient=tkinter.HORIZONTAL
)
scale.pack(side=tkinter.RIGHT)
app.mainloop()
