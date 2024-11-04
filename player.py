import RPi.GPIO as GPIO
import os
import time
import subprocess
import random
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)

relay_open = False
playing = False
music_paths = ["./music", "/mnt/data/applebackups/tomv-new单曲"]
postfixes = (".wav", ".mp3", ".flac", ".ape")

def get_music(music_path):
    music = []
    for p,f,i in os.walk(music_path):
        for i_ in i:
            if i_.endswith(postfixes):
                music.append("\"" + os.path.join(p, i_) + "\"")
    return music

def get_musics(path_list):
    musics = []
    for pl in path_list:
        musics.extend(get_music(pl))
    return musics


if __name__ == "__main__":
    musics = get_musics(music_paths)
    while 1:
        relay_open = GPIO.input(22) == 0
        if relay_open and not playing:
            random.shuffle(musics)
            print("starting to play ... ")
            cmd = ["/usr/bin/cvlc", "--play-and-exit", *musics]
            cmd = " ".join(cmd)
            print(cmd)
            subp = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
            playing = True
        if not relay_open and playing:
            print("stopping playing ... ")
            os.killpg(os.getpgid(subp.pid), signal.SIGTERM)
            playing = False

        time.sleep(0.3)
