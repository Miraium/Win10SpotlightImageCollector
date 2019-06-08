mkdir %~dp0\output
cd %HOMEPATH%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
copy * %~dp0\output\*
cd %~dp0\output
ren * *.jpg
pause