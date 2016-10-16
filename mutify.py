import dbus
import time
import subprocess


def toggleMute():
	toggle = 'amixer set Master toggle'
	subprocess.Popen(toggle.split())
		
session_bus = dbus.SessionBus()

tryAgain = True

flag = True

while(True):
	if(tryAgain):
		try:
			spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
			spotify_properties = dbus.Interface(spotify_bus,"org.freedesktop.DBus.Properties")
			tryAgain = False
		except:
			continue
	try:
		metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
	except:
		tryAgain = True
		continue
	#print(metadata['xesam:title'])
	if('spotify' in metadata['xesam:title'].lower()):
		if(flag):
			print('Muted')
			flag = False
			toggleMute()
	else:
		if(not flag):
			print('Unmuted')
			flag = True
			toggleMute()

	time.sleep(1)

