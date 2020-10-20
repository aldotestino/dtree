@echo off
SET current_directory="%cd%"
cd /d *Path to wls.py* 
py wls.py %current_directory% %1