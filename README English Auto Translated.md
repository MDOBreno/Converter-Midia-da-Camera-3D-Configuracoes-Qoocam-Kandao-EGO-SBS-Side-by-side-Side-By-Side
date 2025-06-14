---------------------- Instructions for Converting Photos and Videos ---------------------

[Introduction]
	- The aim is to convert photos and videos from the 3D camera "Kandao QooCam EGO", 
	in which each frame is two side-by-side images (left and right),
	merged into a single frame in FullHD resolution and proportions for each side. 
	In practice:
	 	[Photo]:  8000×3000 pixels
	 	[Video]:  3840×1080 pixels

	- So we want to generate 4 types of files and delete the 
	originals mentioned above. The files we want to produce are:
		[Photo - Spatial Photo (.heic)]: 4000×3000 pixels
		[Video - Spatial Video (.mov)]: 1920x1080 pixels
		[Photo - SBS 16x9 (.jpg)]: 8000x4500 pixels
		[Video - SBS 16x9 (.m4v)]: 4K (3840x2160 pixels)

	- All these conversions, for both photo and video,
	should be made directly from the respective photo/video original
	- The instructions are semantically divided into 3 parts:
		- Convert [Photo/Video to Spatial Photo/Video]: Requires Mac (Apple)
		- Convert [Photo to SBS]: Requires Mac (Apple or Intel)
		- Convert [Video to SBS]: Requires Mac (Apple or Intel)
		- Adjust Date/Time automatically: Mac (Apple or Intel) or Windows
		- Fill in photo location: Requires Mac (Apple or Intel)
	the first 3 "Convert" operations can be done independently of each other,
	but any of them require the last 2 ("Adjust Date/Time" and "Fill in Location").
	- The results are the most efficient form, in all aspects:
		--> Minimum redundancy of pixels while obtaining 
		the 16x9 market standard proportions
		--> Conversion to more efficient formats (reading and storage) 
		for SBS and Spatial (Apple) files, in the 16x9 market standard
	- For each of the 4 destination files, follow the instructions below.
	- Tip: If you have a NAS server, do all the processing directly there,
    because in many cases these files (that are already large) are duplicated,
    consuming internal storage and causing swapping if the machine runs low on RAM. 
    Furthermore, hard drives (typically in NASs, at about 100MB/s) 
    can be faster than the video's encoding process itself, making internal storage
    less relevant.

_______________________________________________________________________________________

[Photo - Spatial Photo (.heic)] and [Video - Spatial Video (.mov)]
	- Go into the folder:
		"SpatialConverter-vX.X.X"
	- Open the file/website "WebPage Download Releases"
	- If there’s a newer version on the site, download/replace (with) it
	- Inside the "SpatialConverter-vX.X.X" folder, execute README.txt
    - To adjust photo and video datetime, follow this procedure first:
    	[Adjust Date/Time automatically (Required)]
	- Then drag these files into your "Photos" (iCloud) App, 
	and it will start syncing this media with iCloud.
	- Once syncing is finished, for each set of photos/videos taken at the same place, 
	select all of them, then "Command+i", click on the location's name,
	search or enter the place's name or address, and press enter.

_______________________________________________________________________________________

[Photo - SBS 16x9 (.jpg)]
	- The idea here is to amplify (pixel redundancy) the photos to match the 
	16x9 TV/Monitor proportions, according to the "Proportions and Pixels.png" file.
	- Duplicate the folder of the original photos {[Photo]: 8000×3000 pixels},
	since this procedure modifies files (instead of creating/exporting new ones),
	this prevents:
		- Doing other conversions afterwards
		- Having a backup in case something goes awry.
	- Select all, and [Command+o] to view them all in a single MacOS Preview window.
	- Select a photo in the side panel, then [Command+A] to select all photos.
	- Go to Tools -> Adjust Size
	- Unlock the padlock, then set Height to 4500 pixels, and click OK
	- Select a photo again, [Command+A] to select all, then [Command+S] to save all
    - To adjust photo and video datetime, follow this procedure first:
    	[Adjust Date/Time automatically (Required)]
	- Then drag these files into your "Photos" (iCloud) App, 
	and it will start syncing this media with iCloud.
	- Once syncing is finished, for each set of photos/videos taken at the same 
	place, select all of them, then "Command+i", click on the location's name, 
	search or enter the place's name or address, and press enter.

_______________________________________________________________________________________

[Video - SBS 16x9 (.m4v)]
	- The idea here is to amplify (pixel redundancy) the video to match the 
	16x9 TV/Monitor proportions, according to the "Proportions and Pixels.png" file.
	- Generate the files following the instructions in:
	"/Video/Instructions FinalCutPro English Auto Translated.pdf"
	- Opening the video afterwards generates duplicated copies, I don't know 
	why this happens, in the following directory (so it's good to delete afterwards 
	to free up space, e.g.: 50GB):
		'/Users/YourMacUsername/Movies/TV/Media.localized/Home Videos'
    - To adjust photo and video datetime, follow this procedure first:
    	[Adjust Date/Time automatically (Required)]
	- Then drag these files into your "Photos" (iCloud) App, 
	and it will start syncing this media with iCloud.
	- Once syncing is finished, for each set of photos/videos taken at the same 
	place, select all of them, then "Command+i", 
	click on the location's name, search or enter the place's name or address, 
	and press enter.

_______________________________________________________________________________________

[Adjust Date/Time automatically (Required)]
	- If you don't have exiftool installed on your computer, install it first:
		- On MacOS (assuming you already have HomeBrew):
			brew install exiftool
		- On Windows (assuming you already have Chocolatey):
			choco install exiftool
	- Now go to your camera, open: Settings -> "Date & Time" -> "Time Zone"
	and note which time zone is configured there. (For me it was -3:00)
	- To correct dates and times in the ExecutableForScriptCorrectionOfDates folder,
	there is a file called gerar_scripts.py, and on line 19 it contains:
		[ if add_timezone:					]
	    [ 	dt -= timedelta(hours=-3)   	]
	Change the value “-3” to whatever your camera's "Time Zone" was
	at the moment you captured your photos and video. In my example, I'll keep “-3”
	- Next, make a copy of gerar_scripts.py into the folder where these files are and 
	execute in terminal:
    	python3 gerar_scripts.py
    That will create the files corrigir_datas.sh (Mac) and corrigir_datas.bat (Windows)
    Then do the following for your operating system:
    	--> Windows: (double-click corrigir_datas.bat)
		--> Mac (in terminal): 	./corrigir_datas.sh
	This will adjust dates automatically.
	- Note that for [Spatial Photo/Video], because it's a modern/versatile format, 
	I use it to match the exact moment it was taken, but for [Photo/Video - SBS] 
	I set the datetime exactly 100 years earlier. That way it's in the same album 
	(but separate in time), allowing me to view it sequentially on a 3D TV, 
	while easily distinguishing which moment it was.

