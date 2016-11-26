import tkinter
import pygame.mixer

app = tkinter.Tk()
app.title('DJ Mix')

filename = 'music.wav'

pygame.mixer.init()

track = pygame.mixer.Sound(filename)
channel = pygame.mixer.find_channel()

def start():
    channel.play(track)

def stop():
    channel.stop()

start_btn = tkinter.Button(app, command=start, text='Start')
start_btn.pack(side=tkinter.LEFT)
stop_btn = tkinter.Button(app, command=stop, text='Stop')
stop_btn.pack(side=tkinter.RIGHT)
app.mainloop()
