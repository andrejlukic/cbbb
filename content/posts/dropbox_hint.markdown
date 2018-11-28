title: How to directly upload files to Dropbox without copying them to a your local Dropbox folder
slug: how-to-directly-upload-large-files-to-dropbox-from-external-drive
lang: en
category: dropbox
date: 2018-08-04
modified: 2018-08-04

[Directly upload files to Dropbox] To upload files directly to your Dropbox account and not copy them first to your local Dropbox folder is a bit of a hassle. The easiest way is to connect an external drive with the files you want to upload and then create a symbolic link to your local Dropbox folder. After this, the files will start uploading from your external drive to your Dropbox account without being physically copied to your local dropbox folder. After the files have uploaded disconnect and physically remove the external drive with the files and then go into Dropbox Settings -> Selective sync and uncheck the newly created folder. This way it wont sync back to your local drive. Dropbox will at this point try to delete the local files, this is why the external drive was removed in the previous step. The last step is to remove the symbolic link. 

(PS The prefered and safe solution is still to use the Dropbox web interface, hopefully they'll fix the limit on the number of files simultaneously uploaded, which makes it impractical in case you have to upload many files)

Step by step

D:\Dropbox = your local Dropbox direcory

E:\newfiles = files, that you want to add without copying them to your Dropbox directory

Step 1 - Open Windows command prompt (cmd.exe) under administrator priviliges and change to your local Dropbox directory (<a href="static/2018-dbgf/001.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

Step 2 - Create a symbolic link from your external drive E:\newfiles to your local Dropbox directory (<a href="static/2018-dbgf/002.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

<img src="static/2018-dbgf/002.gif" alt="drawing" style="width:600px;"/>

Step 3 - Wait until files are uplouded

Step 4 - Remove (and physically disconnect!) your external drive (<a href="static/2018-dbgf/003.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

Step 5 - Open Dropbox settings, selective sync and remove the sym_link directory. (<a href="static/2018-dbgf/004.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

Step 6 - Use rmdir command to remove the symbolic link (<a href="static/2018-dbgf/005.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

That's all!

~                                                        