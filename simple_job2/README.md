# Second Simple Test Job

## Modification Guide
Check file encoding "Beerling_Clean_V3.pqi" with notepad: UTF-8  

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
* Thermodynamic
Quartz, Plagioclase, Apatite, Diopside_Mn, Diopside, Olivine, Alkali-feldspar, Montmorillonite, Ilmenite, Glass, Al(OH)3(a), Calcite, SiO2(a), Gibbsite, Goethite, Kaolinite, Fe(OH)3(a), Pyrolusite 
+/- one order of magnitude  (19*3 = 57)  
Examples:
    * Quartz: log_k change to -4.98 and -2.98 : [-3.98, -4.98, -2.98]
    * Plagioclase: log_k change to 15.34 and 17.34 : [16.34, 15.34, 17.34]
    * Apatite: log_k change to -4.421 and -2.421 : [-3.421, -4.421, -2.421] 
* Kinetics  
MikeSorghum, Quartz, Plagioclase, Apatite, Diopside_Mn, Diopside, Olivine, Alkali-feldspar, Montmorillonite, Ilmenite, Glass (12*3 = 36)
+/- two orders of magnitude for mineral phases; x10 or x0.1 (MikeSorghum one order of magnitude)
Examples:  
    * Quartz:  
    270 rate = (a0/v)*(M/M0)^0.67*r_all*(1-SR("Quartz"))  
    270 rate = (a0/v)*(M/M0)^0.67*r_all*(1-SR("Quartz"))*0.1  
    270 rate = (a0/v)*(M/M0)^0.67*r_all*(1-SR("Quartz"))*10  

### Total Simulations
2 * 7 * 9 * 57 * 36 = 258552 

