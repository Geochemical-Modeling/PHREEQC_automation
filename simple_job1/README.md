﻿# First Simple Test Job

## Modification Guide
Check file encoding "Beerling_Clean_V2.pqi" with notepad: UTF-8  

### Replace Solution 0
```
SOLUTION 0 Leachate for no-basalt planted control - simulates weathering of soil minerals and plant in no-basalt columns
temp      25
pH        8.1
pe        4
redox     pe
units     mol/l
density   1
Al	1.8347E-06
Ba	5.4686E-06
Ca	8.0346E-04
Fe	4.8291E-06
K	2.0116E-05
Li	3.3629E-07
Mg	6.1360E-05
Mn	3.3374E-08
Na	1.8010E-04
Si	5.5344E-05
Sr	9.7588E-07
Ti	1.1488E-07
Zn	2.3076E-06
F	5.8442E-05
Cl	1.6345E-04
N(3)	1.2607E-05
S(6)	5.0777E-05
N(5)	4.5146E-04
C(4)	1.1585E-03
-water    1 # kg
```
==> 

```
SOLUTION 0  Average Rain Water Northern Europe 
temp      25 
pH        5.601 
pe        13.892 
redox     pe 
units     mol/l 
density   1 
C         1.668e-05    
Ca        3.543e-05    
Cl        9.788e-05    
K         8.951e-06    
Mg        1.604e-05    
N         1.928e-05    
Na        8.917e-05    
S         2.280e-05    
-water    1 # kg 
```
### Change Parameters
* Temperatures  
Temp [5;35;5] : [5, 10, 15, 20, 25, 30, 35] 
* Leaching speed  
Shifts [100;500;50] [100, 150, 200, 250, 300, 350, 400, 450, 500]  
Time_Step * Shift =  157824904.4 (s, 5 years)

### Total Simulations
2 * 7 * 9 = 126

## More on Input
Data for the program are free format:
* Spaces or tabs may be used to delimit input fields (except SOLUTION_SPREAD, which is delimited only with tabs). 
* Blank lines are ignored. 
* Keyword data blocks within a simulation may be entered in any order. 
* Data elements entered on a single line are order specific. 
* As much as possible, the program is case insensitive. 
* Chemical formulas are case sensitive. 

[Descript of Data Input](https://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/phreeqc3-html/phreeqc3-5.htm)

## Simple Test

Test run on the Latitude 7420  
copy 'C:\Program Files\USGS\phreeqc-3.7.3-15968-x64\bin\Release\phreeqc.exe' to test folder  

```
./phreeqc.exe job001.pqi job001.pqo T_H.dat job001.log
```
| job | time (s) |  
| --    | --     |
|job001 | 283.46 |
|job063 | 910.237|
|job064 | 274.26 |
|job126 | 1161.58|
|total | 2629.537|

run the above 4 jobs with pool_size = 4:  1393.785 s 

Another run:
```
run job: job001.pqi
run job: job063.pqi
run job: job064.pqi
run job: job126.pqi
finish job: job064.pqi at 401.5542543 s
finish job: job001.pqi at 410.6446479 s
finish job: job063.pqi at 1078.6873335 s
finish job: job126.pqi at 1409.239821 s
total job time (s): 3300.1260567
run time (s): 1409.39
```

run the 6 jobs with pool_size = 6  
```
run job: job001.pqi
run job: job019.pqi
run job: job063.pqi
run job: job064.pqi
run job: job073.pqi
run job: job126.pqi
finish job: job019.pqi at 384.6590129 s
finish job: job064.pqi at 480.5692115 s
finish job: job073.pqi at 481.0660019 s
finish job: job001.pqi at 485.0253998 s
finish job: job063.pqi at 1141.0009629 s
total job time (s): 4442.5316387
finish job: job126.pqi at 1470.2110496999999 s
run time (s): 1470.43
```

run the 8 jobs with pool_size = 8 (cpu_count):  
```
run job: job001.pqi
run job: job019.pqi
run job: job040.pqi
run job: job063.pqi
run job: job064.pqi
run job: job073.pqi
run job: job100.pqi
run job: job126.pqi
finish job: job100.pqi at 438.92362230000003 s
finish job: job019.pqi at 452.8202027 s
finish job: job064.pqi at 561.3858574000001 s
finish job: job073.pqi at 561.7786804000001 s
finish job: job001.pqi at 569.0253035 s
finish job: job040.pqi at 787.2322855 s
finish job: job063.pqi at 1251.4866483 s
finish job: job126.pqi at 1574.4223771000002 s
total job time (s): 6197.0749772
run time (s): 1574.67
```