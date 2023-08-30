# Software Installation on Windows 11
## Git
```
winget install --id Git.Git -e --source winget
```
## Python
```
winget install -e --id Anaconda.Miniconda3
```
![Screenshot 2023-08-19 142037](https://github.com/Geochemical-Modeling/PHREEQC_automation/assets/6643873/cef4add3-b4a6-4654-8fa6-9151b7657523)

Use **Anaconda Powershell Prompt**

## PHREEQC
[Batch Versions of PHREEQC](https://www.usgs.gov/software/phreeqc-version-3)

In powershell, use "where.exe phreeqc" to find the installation location  
> C:\Program Files\USGS\phreeqc-3.7.3-15968-x64\bin\phreeqc.bat  
> C:\Program Files\USGS\phreeqc-3.7.3-15968-x64\bin\ClrRelease\phreeqc.exe

### PHREEQC Automation
```
git clone https://github.com/Geochemical-Modeling/PHREEQC_automation.git
```
### Test PHREEQC

### CPU
Intel Xeon Silver 4208 CPU @ 2.10GHz Cores: 8 Threads: 16
 
