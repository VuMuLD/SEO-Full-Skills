# SEO All-in-One — Windows installer (PowerShell 5.1+)
# Copies this folder to %USERPROFILE%\.claude\skills\seo and creates a private Python venv.
# Usage:  powershell -ExecutionPolicy Bypass -File .\install.ps1 [-Optional] [-NoVenv]

param(
    [switch]$Optional,   # also install requirements-optional.txt (Playwright, Google APIs, PDF)
    [switch]$NoVenv      # copy files only
)

$ErrorActionPreference = 'Stop'
$src = Split-Path -Parent $MyInvocation.MyCommand.Path
$dest = Join-Path $env:USERPROFILE '.claude\skills\seo'

if ((Resolve-Path $src).Path -ne $dest) {
    if (Test-Path $dest) {
        $backup = "$dest.bak-$(Get-Date -Format yyyyMMddHHmmss)"
        Write-Host "Existing skill found, backing up to $backup"
        Move-Item $dest $backup
    }
    New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null
    Copy-Item $src $dest -Recurse
    Write-Host "Skill copied to $dest"
}

if ($NoVenv) { Write-Host 'Done (no venv).'; exit 0 }

$py = $null
foreach ($cand in @('py -3', 'python', 'python3')) {
    try {
        $ver = & cmd /c "$cand -c `"import sys;print(sys.version_info>=(3,10))`"" 2>$null
        if ($ver -eq 'True') { $py = $cand; break }
    } catch {}
}
if (-not $py) { Write-Warning 'Python 3.10+ not found. Install it from python.org, then re-run.'; exit 1 }

$venv = Join-Path $dest '.venv'
& cmd /c "$py -m venv `"$venv`""
$vpy = Join-Path $venv 'Scripts\python.exe'
& $vpy -m pip install --upgrade pip --quiet
& $vpy -m pip install -r (Join-Path $dest 'requirements.txt')
if ($Optional) {
    & $vpy -m pip install -r (Join-Path $dest 'requirements-optional.txt')
    & $vpy -m playwright install chromium
}

Write-Host ''
Write-Host "Installed. Python for the scripts: $vpy"
Write-Host 'Tip: set PYTHONUTF8=1 in your environment for the cleanest Unicode output on Windows.'
Write-Host 'Restart Claude Code, then try:  /seo audit https://example.com'
