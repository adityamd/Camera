<h1>Camera</h1>

This project is a simple camera application built using OpenCV,PyAudio,FFMPEG and Tkinter that can click images, record videos with audio and save them. The application looks like:<br>
<p align='center'>
<img src="https://github.com/adityamd/Camera/blob/Images_Add/static/Screenshot%20(61).png" height=400px width=400px>
</p>
<br>
<h3>Sample Image:</h3>
  <p align='center'>
    <img src="https://github.com/adityamd/Camera/blob/master/static/Image_1.jpg" height=400px width=400px>
  </p> 
<br>
<br>
<b> Few Points to note here are:
  <ul>
    <li>The button <em>"Click"</em> clicks a picture and saves it in the current working folder as "Image_1.jpg".</li>
    <li>The button <em>"Record"</em> starts recording the audio and video until you press it again that stops the recoring. The video is saved as "Video0.mp4".</li>
    <li>Use <em>"Exit"</em> button to exit the application.</li>
      <kbd><b>
        Note: Using the Close application button on top right corner will not release the web-cam.
        </b></kbd>
    </li>
    <li>You must not have any file named "Image_1.jpg" or "Video0.mp4" in order to save the images or recordings correctly.</li>
  </ul>
</b>
<br>
<h2>Installation Procedure</h2>
<h3>Installing Python:</h3>
 You can install python(3.8.5) directly <a href="https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe">here</a> or go to the page <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a> 
 and click "Download Python 3.8.5". Don't forget to check the box "Add To Path", once you launch the installation wizard. 
 <br>
 To check if python is installed correctly and is added to your path, go to the command prompt/powershell/terminal on your system and type 'python'.
 
 <br><br>
 
 <h3>Installing Pip:</h3>
 Pip is a very convinient and efficient packet manager used to download different python modules. It will be useful in installing OpenCV. 
 To install pip, download get-pip.py file and execute it using the following comands: <br><br><code> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py </code><br>
 <code>python get-pip.py</code></br><br>Fire command <code>pip list</code> on your cmd/powershell/terminal to check if pip is installed correctly on your system.
 
 <br><br>
 
 <h3>Installing OpenCV:</h3>
 The next step to run the project is to install OpenCV. You can install OpenCV using the command: <br><br><code>pip install opencv-python</code></br><br>Fire command <code>pip list</code>
 on your cmd/powershell/terminal and look for 'opencv-python' to check if opencv is installed correctly on your system.
 
 <br><br>
 
 <h3>Installing PyAudio:</h3>
  PyAudio is a python module that helps playing with the audio. You can play,record,save or analyze any sound or audio stream using this library. To install it, simply fire the command <code>pip install pyaudio</code> on your system cmd/powershell/terminal. To confirm pyaudio download, head to the terminal and type <code>pip list</code>. Look for pyaudio module in the output.
  
  <br><br>
  
  <h3>Installing FFMPEG:</h3>
   The last and final step to run the project is installing FFMPEG on your system. FFMPEG is a command line utility that helps you muxing the audio with the video.To install FFMPEG:
   <ol>
    <li>Head on over thhe link below</li>
    <a href="http://ffmpeg.zeranoe.com/builds/ ">http://ffmpeg.zeranoe.com/builds/ </a>
    </li>
    <li>Choose the file you want to download based on your system requirements (static version is recommended).</li>
    <li>After downloading, unzip the file on your local system</li>
    <li>Lastly, in order to use this utility anywhere, you will need to add FFMPEG to the path. For this, head over to the directory where you have extracted the file. Go to bin folder and copy the path. Now, search for <em>"Edit the system environment variables"</em> in Windows search bar, click on "Environment Variables", look for the option "Path"in System Variables section,click on it, click "New" and paste the path to "bin" folder.</li>
  </ol>
In order to check, if FFMPEG is installed correctly and added to path, open your system cmd/powershell/terminal and type <code>ffmpeg</code>.
<br>
<h2>Run The Application</h2>
To run the application:
<ol>
  <li>Open cmd/powershell/terminal on your system and head over to the directory where you have cloned this repository.</li>
  <li>Type <code>python camera.py</code></li>
  You should see the application window opening.
</ol>
