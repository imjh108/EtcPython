# -*- coding: cp949 -*-
#
# AVmerge.py
#     �밳�� ��� re-encoding ���� �ܼ� merge �� �� ����
#     ffmpeg.exe -i %1 -i %2 -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 output.mp4
#
# designed by Julius JH Im

import os
import sys
from   moviepy.editor import *

def AVmerge():
    videoFName = input('���� ������? ')
    audioFName = input('����� ������? ')
    if not os.path.exists(videoFName) or not os.path.exists(audioFName) or\
       not os.path.isfile(videoFName) or not os.path.isfile(audioFName):
        print('Error, �߸��� ���ϸ�:', videoFName, audioFName)
        return

    video       = VideoFileClip(videoFName)
    audio       = AudioFileClip(audioFName)
    video.audio = audio
    video.write_videofile(os.path.join('AVmerge.mp4'))

if __name__ == '__main__':
    AVmerge()
