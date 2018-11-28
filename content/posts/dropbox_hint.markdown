title: Skip local Dropbox directory and directly upload to Dropbox
slug: skip-local-dropbox-directory-directly-upload-to-dropbox
lang: en
category: dropbox
date: 2018-08-04
modified: 2018-08-04
<br />
To directly upload files to your Dropbox account without copying them to the local Dropbox folder use symbolic links ([steps 1-7](#ss)). This is an alternative to using the Dropbox web interface, which can be impractical in case you have to upload many files.

<a name="ss">Step by step</a>

1. Connect an external drive with the files you want to upload directly. An external drive is handy, because you can physically remove it in step 5

2. Open Windows command prompt (cmd.exe) under administrator priviliges and change to your local Dropbox directory (<a href="static/2018-dbgf/001.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

3. Create a symbolic link connecting files on the external drive E:\newfiles to somewhere inside your local Dropbox directory (<a href="static/2018-dbgf/002.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>) <img src="static/2018-dbgf/002.gif" alt="drawing" style="margin-top:20px; width:600px;"/>

4. Wait until Dropbox finishes indexing and uploading all the files to cloud

5. Physically disconnect your external drive containing files from your computer to prevent Dropbox deleting them in the next step (<a href="static/2018-dbgf/003.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)

6. Use selective sync option in the Dropbox settings to prevent downloading the new files back to your local Dropbox direcory (<a href="static/2018-dbgf/004.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>) - remember to first disconnect the external drive

7. Use rmdir command to remove the symbolic link (<a href="static/2018-dbgf/005.gif" alt="drawing" style="width:400px;" target="_blank" >screenshot</a>)


That's all!

~                                                        