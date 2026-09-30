@echo off
setlocal

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
echo [1/2] pipを更新しています...
python -m pip install --upgrade pip

echo.
echo [2/2] 必要なパッケージをインストールしています...
python -m pip install fastapi "uvicorn[standard]" requests

if errorlevel 1 (
    echo.
    echo [ERROR] インストールに失敗しました。
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed!
echo ========================================
echo.
echo 起動する場合は main.py を実行してください。
echo.

pause
