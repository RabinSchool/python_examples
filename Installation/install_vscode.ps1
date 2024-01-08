$url = "https://vscode.download.prss.microsoft.com/dbazure/download/stable/0ee08df0cf4527e40edc9aa28f4b5bd38bbff2b2/VSCodeSetup-x64-1.85.1.exe"
$vscode_dest = "C:\temp\VSCodeSetup-x64-1.85.1.exe"
Invoke-RestMethod -Uri $url -OutFile $vscode_dest


Start-Process -FilePath $vscode_dest -Argument "/VERYSILENT /NORESTART /MERGETASKS=!runcode,desktopicon,addcontextmenufiles,addcontextmenufolders"

code --install-extenstion "GitHub.vscode-pull-request-github"
code --install-extenstion "ms-python.python"
code --install-extenstion "emeraldwalk.RunOnSave"
code --install-extenstion "donjayamanne.githistory"
code --install-extenstion "Dart-Code.flutter"
code --install-extenstion "Dart-Code.dart-code"


$url = "https://raw.githubusercontent.com/RabinSchool/python_examples/main/settings.json"
$dest = "$Env:USERPROFILE\appdata\Roaming\code\user\settings.json"
Invoke-RestMethod -Uri $url -OutFile $dest
