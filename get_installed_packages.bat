@echo off

chcp 65001 >nul

echo 掃描系統已安裝的 Appx 套件...

powershell -NoProfile -Command "Get-AppxPackage | Select-Object -ExpandProperty Name | Sort-Object" > "%~dp0installed_packages.txt"

echo 完成, 儲存至 %~dp0installed_packages.txt