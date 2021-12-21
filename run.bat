@echo off
title Reles
echo Test Licence
if exist licence.lic (
  echo Ok Licence
  py main.py
) else (
  echo No Licence
)
title Close
pause