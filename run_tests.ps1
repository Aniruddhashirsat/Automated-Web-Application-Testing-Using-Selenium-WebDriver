# =====================================================================
# STAQA Automation Mini-Project: Automated Test Runner Script
# Executes the full Selenium pytest test suite and opens the HTML report
# =====================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " STAQA: Automated Web Testing Suite (Selenium WebDriver)" -ForegroundColor Cyan
Write-Host " Savitribai Phule Pune University (SPPU) Mini-Project" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# Ensure reports directory exists
if (-Not (Test-Path "reports")) {
    New-Item -ItemType Directory -Path "reports" -Force | Out-Null
}

if (-Not (Test-Path "screenshots")) {
    New-Item -ItemType Directory -Path "screenshots" -Force | Out-Null
}

Write-Host "[1/3] Executing Selenium WebDriver test suite in headless mode..." -ForegroundColor Yellow
$ReportPath = "reports\report.html"

# Run pytest with HTML report generation
pytest tests/ -v --html=$ReportPath --self-contained-html

$TestExitCode = $LASTEXITCODE

Write-Host "`n[2/3] Test execution completed with exit code: $TestExitCode" -ForegroundColor Yellow

if (Test-Path $ReportPath) {
    Write-Host "[3/3] Opening HTML Test Report in default browser..." -ForegroundColor Green
    Start-Process $ReportPath
} else {
    Write-Host "[!] HTML report was not generated." -ForegroundColor Red
}

Write-Host "`nExecution complete. Check reports/ and screenshots/ for output." -ForegroundColor Cyan
