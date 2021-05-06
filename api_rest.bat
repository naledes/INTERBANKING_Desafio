@echo off
call npm install -g json-server
echo.
call json-server --watch --ro c:\z_interbanking_desafio\internet_ult_anio.json
