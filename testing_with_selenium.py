name: CI Pipeline

on: 
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: windows-latest  # Running on Windows

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.0"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install selenium chromedriver-autoinstaller

      - name: Install Chrome and Chromedriver
        shell: powershell
        run: |
          choco install googlechrome -y
          choco install chromedriver -y

      - name: Verify Chrome installation
        shell: powershell
        run: |
          $chromePath = (Get-Command chrome).Source
          if ($chromePath) {
              Write-Host "✅ Chrome found at $chromePath"
          } else {
              Write-Host "❌ Chrome not found"
              exit 1
          }

      - name: Start FastAPI Server
        run: |
          uvicorn backend:app --host 0.0.0.0 --port 8000 &
        shell: bash  # Ensures proper background execution

      - name: Wait for FastAPI Server
        shell: powershell
        run: |
          $retries = 10
          $delay = 3
          for ($i = 0; $i -lt $retries; $i++) {
              try {
                  Invoke-WebRequest -Uri "http://127.0.0.1:8000/docs" -UseBasicParsing
                  Write-Host "✅ FastAPI server is up!"
                  exit 0
              } catch {
                  Write-Host "⏳ FastAPI server not available yet. Retrying in $delay seconds..."
                  Start-Sleep -Seconds $delay
              }
          }
          Write-Host "❌ FastAPI server failed to start."
          exit 1

      - name: Run pytest tests
        run: pytest -v testing_with_pytest.py
      
      - name: Run unittest tests
        run: python testing_with_unittest.py

      - name: Run Selenium tests
        run: python testing_with_selenium.py
        env:
          PATH: ${{ runner.tool_cache }}/chromedriver:$PATH
