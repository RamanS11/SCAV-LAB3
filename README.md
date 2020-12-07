# SCAV-LAB3

The main objective of this lab is to create a class able to create a video container from different files we'll be creating extracted from a bigger video (in our case BBB (Big Buck Bunny, that is not included in the project!)). 

To create this new container we first extracted 4 different files from the original video; a short version of the original video, a mono audio file and low bitrate audio file (both extracted from this short version), and finally we created a .srt file where we allocated the subtitles we want to show. 

All these files are created in the function 'export', that recieves the names of the output variabels we want to add to those files. Once all these files are created we must execute 'create_new_container', that creates this new container with the information previously extracted from the original video. 

Finally we created a fuinction called 'compatibility' that checks out which are the Broadcasting Standars compatible with the video evaluated. 
