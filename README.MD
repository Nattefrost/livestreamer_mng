#INSTALLING

# ON WINDOWS 

- Make sure you have VLC media player installed
- Double click "install.bat"
- Follow instructions, during the python install dont forget to check "Add python to PATH"
If you already have python3 installed on your computer, just exit the installer when it starts. 
If you have python 2 and it's in the PATH, alias your .exes and use pip to download livestreamer.
- After that you should have a shortcut on your desktop, double-click it and you should be done.


# ON GNU/LINUX 

- sh install.sh
- sh start.sh

If this doesnt work, you can separately install : 
- vlc
- python3
- tkinter for python3
- pip for python3 (python packet manager)
- livestreamer as a python package (pip install livestreamer)

# ON HOW TO USE


Open file 'streams.txt', copy-paste urls from your favourite streamers. This file should not contain ANYTHING ELSE than urls.
So a line in this file should look like this (dont forget 'http://'): http://streamingWebsite.com/channelName
If a stream can't be read, refer to the Livestreamer doc about supported platforms : 
						http://docs.livestreamer.io/plugin_matrix.html

When you have made up your list of favourite streams, execute start.bat (start.sh on GNU/Linux or the desktop shortcut on Microsoft Windows)
You should see a window with a list of urls you entered in 'streams.txt' only those which are online should be there.
Select the one you want to watch, double-click or press RETURN and enjoy your stream. =)


For any problem(this soft is in a very early stage) or request, send a mail to
escande dot d at gmail dot com
