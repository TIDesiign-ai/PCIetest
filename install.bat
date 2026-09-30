```bat
@echo off
setlocal

cd /d "%~dp0"

echo ========================================
echo FastAPI Duplex Packet Test
echo ========================================
echo.

python --version
if errorlevel 1 (
    echo [ERROR] Pythonが見つかりません。
    echo Python 3.10以降をインストールしてください。
    pause
    exit /b 1
)

echo.
echo [1/2] 必要なパッケージをインストールしています...
python -m pip install --user fastapi "uvicorn[standard]" requests

if errorlevel 1 (
    echo.
    echo [ERROR] パッケージのインストールに失敗しました。
    pause
    exit /b 1
)

echo.
echo [2/2] FastAPIを起動します...
echo.
echo 終了するには Ctrl+C を押してください。
echo.

python main.py

echo.
echo FastAPIが終了しました。
pause
```
