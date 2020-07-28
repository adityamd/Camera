<h1>Camera</h1>

This project is a simple camera application built using OpenCV,PyAudio,FFMPEG and Tkinter that can click images, record videos with audio and save them. The application looks like:<br>
<p align='center'>
<img src="https://github.com/adityamd/Camera/blob/Images_Add/static/Screenshot%20(61).png" height=400px width=400px>
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
    <li>You must not have any file named "Image_1.jpg" or "Video0.mp4" in order to save the images or recordings correctly</li>
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
 The final step to run the project is to install OpenCV. You can install OpenCV using the command: <br><br><code>pip install opencv-python</code></br><br>Fire command <code>pip list</code>
 on your cmd/powershell/terminal and look for 'opencv-python' to check if opencv is installed correctly on your system.
 
 <br><br>
 
