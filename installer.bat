@echo off
title Scamma Tool Installer
color 0B

echo [*] Initialisation de l'installation de Scamma Tool...
timeout /t 1 >nul

:: Verifie si Python est installe
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [!] Python n'est pas installe. Veuillez l'installer depuis https://www.python.org/downloads/
    pause
    exit /b
)

:: Verifie si pip est installe
python -m pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [*] Installation de pip...
    python -m ensurepip
)

:: Cree un environnement virtuel (optionnel)
echo [*] Creation d'un environnement virtuel (env)
python -m venv env

:: Active l'environnement virtuel
call env\Scripts\activate

:: Installe les dependances
echo [*] Installation des dependances via pip...
pip install -r requirements.txt

IF %ERRORLEVEL% EQU 0 (
    echo [✓] Installation terminee avec succès.
) ELSE (
    echo [X] Une erreur s'est produite lors de l'installation.
)

echo.
pause
