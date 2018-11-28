title: Skip local Dropbox directory and directly upload files
slug: skip-local-dropbox-directory-directly-upload-files
lang: en
category: dropbox
date: 2018-08-04
modified: 2018-08-04
<br />
To directly upload files to Dropbox account without copying them to the local Dropbox folder use symbolic links ([steps 1-6](#ss)). Connect an external drive with the files you want to upload and create a symbolic link to from this external drive to your local Dropbox folder. The files will start uploading to your Dropbox account without being physically copied to the local Dropbox folder. After the files have uploaded, disconnect and physically remove the external drive with the files and use Selective sync to prevent copying files back to your local drive. The last step is to remove the symbolic link. 

(PS The safe solution is to use the Dropbox web interface and hopefully they will some day fix the limit on the number of files simultaneously uploaded, because this makes it impractical in case you have to upload many files)

<a name="ss">Step by step</a>

Step 1 - Open Windows command prompt (cmd.exe) under administrator priviliges and change to your local Dropbox directory (<a href="static/2018-dbgf/001.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

Step 2 - Create a symbolic link connecting files on the external drive E:\newfiles to somewhere inside your local Dropbox directory (<a href="static/2018-dbgf/002.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

<img src="static/2018-dbgf/002.gif" alt="drawing" style="width:600px;"/>

Step 3 - Wait until Dropbox finishes indexing and uploading all the files to cloud

Step 4 - Physically disconnect your external drive containing files from your computer to prevent Dropbox deleting them in the next step (<a href="static/2018-dbgf/003.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

Step 5 - Use selective sync option in the Dropbox settings to prevent downloading the new files back to your local Dropbox direcory (<a href="static/2018-dbgf/004.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>) - remember to first disconnect the external drive

Step 6 - Use rmdir command to remove the symbolic link (<a href="static/2018-dbgf/005.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)


That's all!

~                                                        