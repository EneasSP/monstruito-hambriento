# Pone la versión de VERSION en index.html y empaqueta el proyecto
# en dist\monstruito-hambriento-v<VERSION>.zip
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$version = (Get-Content -Raw -Encoding UTF8 (Join-Path $root 'VERSION')).Trim()

$indexPath = Join-Path $root 'index.html'
$html = Get-Content -Raw -Encoding UTF8 $indexPath
$html = [regex]::Replace($html, '<span class="version" id="version">v[^<]*</span>', "<span class=`"version`" id=`"version`">v$version</span>")
$utf8 = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($indexPath, $html, $utf8)

$dist = Join-Path $root 'dist'
New-Item -ItemType Directory -Force $dist | Out-Null
$zip = Join-Path $dist "monstruito-hambriento-v$version.zip"
if (Test-Path $zip) { Remove-Item $zip -Force }
$items = Get-ChildItem $root -Force | Where-Object { $_.Name -notin @('dist', '.git', '.claude', '__pycache__') }
Compress-Archive -Path $items.FullName -DestinationPath $zip
Write-Output "index.html y $zip listos (v$version)"
