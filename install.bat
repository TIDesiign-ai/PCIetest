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
    pause
    exit /b 1
)

echo.
echo [1/2] パッケージをインストールしています...
python -m pip install --user fastapi "uvicorn[standard]" requests

if errorlevel 1 (
    echo.
    echo [ERROR] インストールに失敗しました。
    pause
    exit /b 1
)

echo.
echo [2/2] FastAPIを起動します...
echo.
echo Server: http://0.0.0.0:8000
echo Swagger: http://localhost:8000/docs
echo.
echo 終了するには Ctrl+C
echo.

python -m uvicorn main:app --host 0.0.0.0 --port 8000

pause

