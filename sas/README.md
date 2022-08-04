# SAS Infile & Format Code Conversion

These will be used to create Pandas dictionaries that can be used throughotu the data exploration phase.

``` SAS Input File sample
filename datain 'c:\SADC2019\sadc_2019_xxxxxxx.dat';
libname dataout 'c:\SADC2019';
libname library 'c:\SADC2019';
data dataout.sadc_2019_xxxxxxx;
infile datain lrecl=900;
input
sitecode $ 1-5
sitename $ 6-55
sitetype $ 56-105
sitetypenum 106-113
...
...
```

``` SAS Proc Format sample
proc format library=library;
value $SITE
"AB" = "Albuquerque, NM" 
"AK" = "Alaska"
"AL" = "Alabama"
"AR" = "Arkansas"
"AZB" = "Arizona"


```

