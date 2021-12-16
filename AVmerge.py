# -*- coding: cp949 -*-
#
# AVmerge.py
#     대개의 경우 re-encoding 보다 단순 merge 가 더 나음
#     ffmpeg.exe -i %1 -i %2 -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 output.mp4
#
# designed by Julius JH Im

import os
import sys
from   moviepy.editor import *

def AVmerge():
    videoFName = input('비디오 파일은? ')
    audioFName = input('오디오 파일은? ')
    if not os.path.exists(videoFName) or not os.path.exists(audioFName) or\
       not os.path.isfile(videoFName) or not os.path.isfile(audioFName):
        print('Error, 잘못된 파일명:', videoFName, audioFName)
        return

    video       = VideoFileClip(videoFName)
    audio       = AudioFileClip(audioFName)
    video.audio = audio
    video.write_videofile(os.path.join('AVmerge.mp4'))

if __name__ == '__main__':
    AVmerge()
