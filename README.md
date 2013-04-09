Stok3r v0.01 April 2013 by Mark Benson - https://github.com/MarkJB
======

Stok3r is a batch processing script that feeds stls to slic3r-console.exe 

It scans the current directory or the path supplied for STL files, calls slic3r-console.exe with slic3r defaults or settings specified in a config.ini files and slices any stl files found.

Stok3r can be told to automatically scan for new stls every n seconds (default is 10).
WARNING! When run with the -a|--auto flag stls will be deleted after slic3r does its thing.

Useage: 

stok3r.py -h|--help

 -c|--config file     Slic3r generated config file to specify slic3r settings

 -p|--path path       Path to scan for stl files. Default is to scan current directory

 -a|--auto n          Automatically scan for and slice stl files every n seconds. Default is 10 seconds. WARNING: When run with -a or --auto, stls are deleted from the specified directory once they have been sliced.

 -h|--help            Show this basic help file

Example:

stok3r.py -p|--path c:\path\to\stls -c|--config c:\path\to\slic3r\config.ini -a|--auto n


CCNC licence. Copyright 2013 n stuff. All other rights reserved blah blah blah...

This thing is free. No support is offered or implied. Unless I feel like it. No liability accepted if this thing goes mental and eats your cat (or files).

TODO: Clean up and remove duplicated code.

