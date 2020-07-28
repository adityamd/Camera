import PIL
from PIL.ImageTk import PhotoImage
import tkinter as tk
import cv2
import threading
import pyaudio
import os
import subprocess
import time
import wave
class video_record(threading.Thread):
    recording=False;
    height=480
    width=640
    cap=None
    def __init__(self,capt,height=None,width=None):
        threading.Thread.__init__(self)
        self.cap=capt
        self.name="Video_Thread"
        if height!=None:
            self.height=height
        if width!=None:
            self.width=width
    
    def run(self):
        self.recording=True
        print("Starting Recording...")
        fourcc=cv2.VideoWriter_fourcc(*"MP4V")
        fps=15
        out_stream=cv2.VideoWriter("Video1.mp4",fourcc,fps,(width,height))
        while self.recording:
            _,frame=self.cap.read()
            out_stream.write(cv2.flip(frame,1))
        out_stream.release()
        print("Recording Stopped")
        
class audio_record(threading.Thread):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    recording=False
    p=pyaudio.PyAudio()
    OUTPUT_FILE = "output.wav"
    def __init__(self):
        threading.Thread.__init__(self)
        self.name="Audio_Thread"
        
    def run(self):
        self.recording=True
        stream = self.p.open(format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK)
        frames = []

        while self.recording:
            data = stream.read(self.CHUNK)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        self.p.terminate()
        wf = wave.open(self.OUTPUT_FILE, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("Audio Terminated")
        
height=480
width=640
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
root=tk.Tk()
lb=tk.Label(root)
lb.pack(fill=tk.BOTH,expand=tk.YES)
recording=True
video=None
audio=None
count=0
def show_img():
    _,frame=cap.read()
    im=cv2.flip(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB),1)
    im=PIL.Image.fromarray(im)
    img=PhotoImage(im)
    lb.config(image=img)
    lb.tk_img=img
    lb.after(1,lambda : show_img())
    
def click_img():
    _,frame=cap.read()
    im=cv2.flip(frame,1)
    cv2.imwrite("Image_1.jpg",im)
    print("Image Saved")
    
def record_func():
    global recording,video,cap,audio,count
    if recording:
        video=video_record(cap)
        audio=audio_record()
        video.start()
        audio.start()
        recording=False
    else:
        video.recording=False
        audio.recording=False
        time.sleep(1)
        _=subprocess.run("ffmpeg -i output.wav output.mp3",shell=True)
        _=subprocess.run("ffmpeg -i output.mp3 -i Video1.mp4 -c copy Video{0}.mp4".format(count),shell=True)
        count+=1
        if os.path.exists(os.getcwd()+"\\output.wav"):
            os.remove(os.getcwd()+"\\output.wav")
        if os.path.exists(os.getcwd()+"\\output.mp3"):
            os.remove(os.getcwd()+"\\output.mp3")
        if os.path.exists(os.getcwd()+"\\Video1.mp4"):
            os.remove(os.getcwd()+"\\Video1.mp4")
        recording=True   
    
def exit_func():
    cap.release()
    try:    
        video.join()
        audio.join()
    except:
        pass
    root.destroy()
    
lb.after(1,lambda : show_img())

save=tk.Button(root,text='Click',fg='red',bg='white',command=click_img)
save.pack(fill=tk.X,expand=tk.YES)
record=tk.Button(root,text="Record!",fg='white',bg='black',command=record_func)
record.pack(fill=tk.X,expand=tk.YES)
exit=tk.Button(root,text='Exit',fg='white',bg='red',command=exit_func)
exit.pack(fill=tk.X,expand=tk.YES)
root.mainloop()
