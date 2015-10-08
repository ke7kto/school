###################################################################
#
#    Citrix Receiver for Linux, Version 11.x
#
#    Copyright 1996-2009 Citrix Systems, Inc. All rights reserved.
#
###################################################################

This file contains the latest information relating to the 
Citrix Receiver for Linux.

For information regarding new features and system requirements, refer
to the Citrix Receiver for Linux, Version 11.x Administrator's Guide.

Please read this file fully before installing and using the Citrix Receiver for Linux. 
It contains important information that may be more up to date 
than other documentation you have available.

For the latest information on this, and other Citrix Systems, Inc.
products, please visit our Web site at:

http://www.citrix.com/

1.  Contents
============

Section 2 - Documentation
Section 3 - Getting Support
Section 4 - Known Issues
Section 5 - Contact Information

2.  Documentation
=================

This document contains important late-breaking information and
known issues for the Citrix Receiver for Linux, Version 11.x. 

For information about installing and configuring the Citrix Receiver for Linux, 
Version 11.x, see the Citrix Receiver for Linux, Version 11.x Administrator's Guide,
available from the Citrix Web site at http://support.citrix.com/pages/docs/.

3.  Getting Support
===================

Citrix provides technical support primarily through the 
Citrix Solutions Network (CSN) channel partners. Please contact
your supplier for first-line support, or use Citrix Online
Technical Support to find the nearest CSN partner.

Citrix offers online technical support services on the
Citrix Web site. The Support page includes links to downloads,
the Citrix Knowledge Center, Citrix Consulting Services, and
other useful support pages.

4.  Known Issues
================

4.1  Maximizing then restoring seamless windows can cause display corruption 
----------------------------------------------------------------------------
If you maximize a seamless window from the taskbar and then restore the window 
using the title bar, the display may appear corrupted. To avoid this issue, 
if you maximize a seamless window from the taskbar, ensure you restore the 
window from the taskbar rather than from the title bar.
[#143377]

4.2  Some keys do not work in the simplified Chinese locale on some distributions 
---------------------------------------------------------------------------------
The arrow, Home, End, Page Up, and Page Down keys do not work in the simplified
Chinese locale on some Linux distributions. You can fix this problem by removing 
the following line from the client's module.ini file:
UseLocalM=True
[#150369]

4.3  The Firewall dialog box does not accept non-ASCII characters
-----------------------------------------------------------------
For some old Linux distributions, the Firewall dialog box does not accept 
non-ASCII characters. If you want to enable non-ASCII characters on this 
dialog box, either comment out or remove the following lines from the Wfica 
resource file in the client's installation directory:

Wfica*ProxyAuthDialog.ProxyUsername*international: False
Wfica*ProxyAuthDialog.ProxyPassword*international: False

Note that due to a third party issue, this workaround may cause 
the client to shut down unexpectedly on some old Linux distributions 
if a user double-clicks on the dialog box.
[#150143]

4.4  The Connection Status dialog box does not display the Euro character correctly
-----------------------------------------------------------------------------------
If you log on to a connection and your user name contains a Euro character, this 
character does not display correctly on the Connection Status dialog box in the 
Connection Center. There is no workaround for this issue.
[#151152]

4.5  The client may not start correctly when using en_GB.UTF-8 on SuSE 10.x
---------------------------------------------------------------------------
Using en_GB.UTF-8 on SuSE 10.x, the client may not start correctly when it 
uses the fallback font specification in the fontList. You can modify the 
Wfcmgr resource file in the $ICAROOT/nls/{language}/UTF-8 directory to 
fix this issue. Update the final two lines in the Wfcmgr*fontList section 
as follows:

-*-*-medium-r-*-*-*-120-75-75-c-*-*-*;\
-*-*-medium-r-*-*-*-120-*-*-c-*-*-*:

This specifies the use of character-cell (fixed cell size) fonts and so 
avoids using the fallback font specification.
[#151365]

4.6  PowerPoint files on mapped client drives may allow concurrent access
-------------------------------------------------------------------------
The Citrix Receiver for Linux supports file locking on mapped client drives. This prevents 
concurrent write access to Microsoft Word documents, Microsoft Excel documents, 
and other files on mapped drives. However, some applications restrict multiple 
access by opening files using Windows sharing modes, which are not supported on
UNIX platforms. As a result, concurrent write access to Microsoft PowerPoint files
is permitted in some circumstances when it should not be possible. If you need 
concurrent access to PowerPoint files, Citrix recommends putting these files on a 
file system that is accessible from the server, rather than on a mapped client drive. 
[#151466]

4.7  Selective Trust causes some proxy settings to be ignored
-------------------------------------------------------------
Selective trust only allows proxy types that do not specify a server 
(namely Auto, None, and Wpad). Secure and Socks proxy settings are ignored. 
You can change this by editing Trusted_Region.ini, using the instructions 
included as comments in that file.
[#199319]

4.8 Unable to reconnect to virtual desktops using the Citrix XenApp menu
------------------------------------------------------------------------
You cannot reconnect to a virtual desktop using the Reconnect Citrix XenApp 
option on the Citrix XenApp menu. As a workaround, click the desktop icon 
for the virtual desktop you want to reconnect to in the Citrix XenApp view 
on the main client window.
[#205538]

4.9 Large files shared in client drive mapping have a zero file size and cannot be moved
----------------------------------------------------------------------------------------
If you attempt to move a large file from a local mapped drive to a shared server folder, 
the action fails and you receive an error saying the file cannot be found. If you attempt 
to open the file you receive the same error. In both cases, the file appears to have a 
file size of zero. Note that this error occurs only for files originally larger than 2Gb 
in size.
[#199215]

4.10 Multimedia files may not work correctly with SpeedScreen Multimedia Acceleration enabled
---------------------------------------------------------------------------------------------
If SpeedScreen Multimedia Acceleration is enabled, multimedia files  may not work correctly 
on the client device. For example, media files may not play at all, the media player window 
may turn black after seeking, or audio may not synchronize or play at the correct speed. 
As a workaround, you can disable SpeedScreen Multimedia Acceleration on the client device. 

To disable SpeedScreen Multimedia Acceleration for all client devices, modify module.ini, 
setting the Multimedia parameter to "Off".

To disable SpeedScreen Multimedia Acceleration for a single client device, modify wfclient.ini, 
setting the SpeedScreenMMAVideoEnabled and SpeedScreenMMAAudioEnabled parameters to "Off".
[#198305, 198337, 198369, 198370, 205952, 206253, 206304, 203605, 203607]

4.11 SpeedScreen Multimedia Acceleration does not work on 64-bit operating systems
----------------------------------------------------------------------------------
The Citrix Receiver for Linux requires 32-bit GStreamer codecs for SpeedScreen Multimedia 
Acceleration to work correctly. To use SpeedScreen Multimedia Acceleration on 64-bit 
operating systems, you must install the appropriate 32-bit GStreamer codecs for your 
operating system before installing the Citrix Receiver for Linux .
[#201589] 

4.12 Applications display only on a single monitor after reconnection
---------------------------------------------------------------------
If you have applications displayed on different monitors in a multimonitor 
setup, all applications may appear on a single monitor after reconnection. 
This issue is only seen with the Compiz window manager.
[#201028]

4.13 Blank spaces appear when maximizing applications in multimonitor environments
----------------------------------------------------------------------------------
When maximising applications in multimonitor environments, blank spaces appear on 
screen where the operating system taskbar would normally appear.
[#200474]

4.14 The Citrix Receiver for Linux may not install correctly on 64-bit operating systems
----------------------------------------------------------------------------------------
By default, the Citrix Receiver for Linux may not install correctly on 64-bit 
operating systems. To prevent this problem, you must install 32-bit sound and 
X server libraries before installing the Citrix Receiver for Linux .
[#200461]

4.15 Known Issues with USB Devices
----------------------------------
For a list of known issues seen when using USB devices with virtual desktops, 
see http://support.citrix.com/article/CTX120090
[#205817, 205818, 205819]

4.16 Including spaces in the client install path
------------------------------------------------
You may experience issues if you attempt to install the client in a location 
where the install path includes spaces. You must not include spaces in the 
client install path.
[#206306] 

5.  Contact Information
=======================

Citrix Systems, Inc.
851 West Cypress Creek Road
Fort Lauderdale, Florida 33309 USA
954-267-3000
http://www.citrix.com/

##################################################################

