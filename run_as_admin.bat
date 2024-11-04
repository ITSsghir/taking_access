@echo off
setlocal

rem Fichier de log
set log_file="%~dp0script_log.txt"

rem Vérifie si le script est exécuté avec les privilèges d'administrateur
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Demande de privilèges administratifs... >> %log_file%
    powershell -Command "Start-Process cmd -ArgumentList '/c \"%~dp0%~nx0\"' -Verb RunAs"
    exit /b
)

rem Récupère le chemin du répertoire actuel du script
set script_path="%~dp0import_os.py"
echo Chemin du script : %script_path% >> %log_file%

rem Exécute le script Python
echo Exécution du script Python... >> %log_file%
python %script_path% >> %log_file% 2>&1

if %errorLevel% NEQ 0 (
    echo Une erreur s'est produite lors de l'exécution du script Python. Code d'erreur : %errorLevel% >> %log_file%
) else (
    echo Script exécuté avec succès. >> %log_file%
)

endlocal
pause
