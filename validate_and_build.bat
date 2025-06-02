
@echo off
echo Installing required dependencies...
npm install rehype-highlight remark-gfm

echo.
echo Running local build to catch errors before deploy...
npm run build

echo.
pause
