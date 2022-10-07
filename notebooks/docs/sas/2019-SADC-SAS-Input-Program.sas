/****************************************************************************************/
/*  This SAS program reads ASCII format (text format) 2019 SADC data and creates a      */
/*  formatted and labeled SAS dataset.                                                  */
/*                                                                                      */
/*  Change the file location specifications from 'c:\SADC2019' to the location where    */
/*  you downloaded, unzipped, and stored the SADC ASCII data file and the format        */
/*  library before you run this program.  Change the location specification in three    */
/*  places - in the 'filename' statement and in the two 'libname' statements at the     */
/*  top of the program.                                                                 */
/*                                                                                      */
/*  Change "xxxxxxx" in the 'filename' statement and the 'data' statement to            */
/*  'national', 'district', 'state_a_m', or 'state_n_z' depending on which file         */
/*  you are analyzing.                                                                  */
/*                                                                                      */
/*  Note: Run '2019 SADC SAS Formats Program.sas' BEFORE you run                        */
/*  '2019 SADC SAS Input Program.sas' to create the 2019SADC dataset.                   */
/****************************************************************************************/
 
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
year 114-121
survyear 122-124
weight 125-134
stratum 135-142
PSU 143-150
record 151-158
age 159-161
sex 162-164
grade 165-167
race4 168-170
race7 171-173
stheight 174-181
stweight 182-189
bmi 190-197
bmipct 198-205
qnobese 206-208
qnowt 209-211
q66 $ 212-212
q65 $ 213-213
sexid 214-221
sexid2 222-229
sexpart 230-237
sexpart2 238-245
q8 $ 246-246
q9 $ 247-247
q10 $ 248-248
q11 $ 249-249
q12 $ 250-250
q13 $ 251-251
q14 $ 252-252
q15 $ 253-253
q16 $ 254-254
q17 $ 255-255
q18 $ 256-256
q19 $ 257-257
q20 $ 258-258
q21 $ 259-259
q22 $ 260-260
q23 $ 261-261
q24 $ 262-262
q25 $ 263-263
q26 $ 264-264
q27 $ 265-265
q28 $ 266-266
q29 $ 267-267
q30 $ 268-268
q31 $ 269-269
q32 $ 270-270
q33 $ 271-271
q34 $ 272-272
q35 $ 273-273
q36 $ 274-274
q37 $ 275-275
q38 $ 276-276
q39 $ 277-277
q40 $ 278-278
q41 $ 279-279
q42 $ 280-280
q43 $ 281-281
q44 $ 282-282
q45 $ 283-283
q46 $ 284-284
q47 $ 285-285
q48 $ 286-286
q49 $ 287-287
q50 $ 288-288
q51 $ 289-289
q52 $ 290-290
q53 $ 291-291
q54 $ 292-292
q55 $ 293-293
q56 $ 294-294
q57 $ 295-295
q58 $ 296-296
q59 $ 297-297
q60 $ 298-298
q61 $ 299-299
q62 $ 300-300
q63 $ 301-301
q64 $ 302-302
q67 $ 303-303
q68 $ 304-304
q69 $ 305-305
q70 $ 306-306
q71 $ 307-307
q72 $ 308-308
q73 $ 309-309
q74 $ 310-310
q75 $ 311-311
q76 $ 312-312
q77 $ 313-313
q78 $ 314-314
q79 $ 315-315
q80 $ 316-316
q81 $ 317-317
q82 $ 318-318
q83 $ 319-319
q84 $ 320-320
q85 $ 321-321
q86 $ 322-322
q87 $ 323-323
q88 $ 324-324
q89 $ 325-325
qn8 326-328
qn9 329-331
qn10 332-334
qn11 335-337
qn12 338-340
qn13 341-343
qn14 344-346
qn15 347-349
qn16 350-352
qn17 353-355
qn18 356-358
qn19 359-361
qn20 362-364
qn21 365-367
qn22 368-370
qn23 371-373
qn24 374-376
qn25 377-379
qn26 380-382
qn27 383-385
qn28 386-388
qn29 389-391
qn30 392-394
qn31 395-397
qn32 398-400
qn33 401-403
qn34 404-406
qn35 407-409
qn36 410-412
qn37 413-415
qn38 416-418
qn39 419-421
qn40 422-424
qn41 425-427
qn42 428-430
qn43 431-433
qn44 434-436
qn45 437-439
qn46 440-442
qn47 443-445
qn48 446-448
qn49 449-451
qn50 452-454
qn51 455-457
qn52 458-460
qn53 461-463
qn54 464-466
qn55 467-469
qn56 470-472
qn57 473-475
qn58 476-478
qn59 479-481
qn60 482-484
qn61 485-487
qn62 488-490
qn63 491-493
qn64 494-496
qn67 497-499
qn68 500-502
qn69 503-505
qn70 506-508
qn71 509-511
qn72 512-514
qn73 515-517
qn74 518-520
qn75 521-523
qn76 524-526
qn77 527-529
qn78 530-532
qn79 533-535
qn80 536-538
qn81 539-541
qn82 542-544
qn83 545-547
qn84 548-550
qn85 551-553
qn86 554-556
qn87 557-559
qn88 560-562
qn89 563-565
qnfrcig 566-568
qndaycig 569-571
qnfrevp 572-574
qndayevp 575-577
qnfrcgr 578-585
qndaycgr 586-593
qntb2 594-596
qntb3 597-599
qntb4 600-602
qntb5 603-605
qniudimp 606-608
qnothhpl 609-611
qndualbc 612-614
qnbcnone 615-617
qnfr0 618-620
qnfr1 621-623
qnfr2 624-626
qnveg0 627-629
qnveg1 630-632
qnveg2 633-635
qnveg3 636-638
qnsoda1 639-641
qnsoda2 642-644
qnmilk1 645-647
qnmilk3 648-650
qnbk7day 651-653
qnpa0day 654-656
qnpa7day 657-659
qndlype 660-662
qnnodnt 663-665
qbikehelmet $ 666-666
qdrivemarijuana $ 667-667
qcelldriving $ 668-668
qpropertydamage $ 669-669
qbullyweight $ 670-670
qbullygender $ 671-671
qbullygay $ 672-672
qchokeself $ 673-673
qcigschool $ 674-674
qchewtobschool $ 675-675
qalcoholschool $ 676-676
qtypealcohol2 $ 677-677
qhowmarijuana $ 678-678
qmarijuanaschool $ 679-679
qcurrentopioid $ 680-680
qcurrentcocaine $ 681-681
qcurrentheroin $ 682-682
qcurrentmeth $ 683-683
qhallucdrug $ 684-684
qprescription30d $ 685-685
qgenderexp $ 686-686
qtaughtHIV $ 687-687
qtaughtsexed $ 688-688
qtaughtstd $ 689-689
qtaughtcondom $ 690-690
qtaughtbc $ 691-691
qdietpop $ 692-692
qcoffeetea $ 693-693
qsportsdrink $ 694-694
qenergydrink $ 695-695
qsugardrink $ 696-696
qwater $ 697-697
qfastfood $ 698-698
qfoodallergy $ 699-699
qwenthungry $ 700-700
qmusclestrength $ 701-701
qsunscreenuse $ 702-702
qindoortanning $ 703-703
qsunburn $ 704-704
qconcentrating $ 705-705
qcurrentasthma $ 706-706
qwheresleep $ 707-707
qspeakenglish $ 708-708
qtransgender $ 709-709
qnbikehelmet 710-712
qndrivemarijuana 713-715
qncelldriving 716-718
qnpropertydamage 719-721
qnbullyweight 722-724
qnbullygender 725-727
qnbullygay 728-730
qnchokeself 731-733
qncigschool 734-736
qnchewtobschool 737-739
qnalcoholschool 740-742
qntypealcohol2 743-745
qnhowmarijuana 746-748
qnmarijuanaschool 749-751
qncurrentopioid 752-754
qncurrentcocaine 755-757
qncurrentheroin 758-760
qncurrentmeth 761-763
qnhallucdrug 764-766
qnprescription30d 767-769
qnillict 770-772
qngenderexp 773-775
qntaughtHIV 776-778
qntaughtsexed 779-781
qntaughtstd 782-784
qntaughtcondom 785-787
qntaughtbc 788-790
qndietpop 791-793
qncoffeetea 794-796
qnsportsdrink 797-799
qnspdrk1 800-802
qnspdrk2 803-805
qnenergydrink 806-808
qnsugardrink 809-811
qnwater 812-814
qnwater1 815-817
qnwater2 818-820
qnwater3 821-823
qnfastfood 824-826
qnfoodallergy 827-829
qnwenthungry 830-832
qnmusclestrength 833-835
qnsunscreenuse 836-838
qnindoortanning 839-841
qnsunburn 842-844
qnconcentrating 845-847
qncurrentasthma 848-850
qnwheresleep 851-853
qnspeakenglish 854-856
qntransgender 857-859
;
 
/****************************************/
/*   Assign formats to SAS variables    */
/****************************************/
;
format
sitecode $SITE.
age AGE.
sex SEX.
grade GRADE.
race4 RACE.
race7 RACE7S.
q66 $H66S.
q65 $H65S.
sexid SEXID.
sexid2 SEXIDB.
sexpart SEXPART.
sexpart2 SEXPARTB.
q8 $H8S.
q9 $H9S.
q10 $H10S.
q11 $H11S.
q12 $H12S.
q13 $H13S.
q14 $H14S.
q15 $H15S.
q16 $H16S.
q17 $H17S.
q18 $H18S.
q19 $H19S.
q20 $H20S.
q21 $H21S.
q22 $H22S.
q23 $H23S.
q24 $H24S.
q25 $H25S.
q26 $H26S.
q27 $H27S.
q28 $H28S.
q29 $H29S.
q30 $H30S.
q31 $H31S.
q32 $H32S.
q33 $H33S.
q34 $H34S.
q35 $H35S.
q36 $H36S.
q37 $H37S.
q38 $H38S.
q39 $H39S.
q40 $H40S.
q41 $H41S.
q42 $H42S.
q43 $H43S.
q44 $H44S.
q45 $H45S.
q46 $H46S.
q47 $H47S.
q48 $H48S.
q49 $H49S.
q50 $H50S.
q51 $H51S.
q52 $H52S.
q53 $H53S.
q54 $H54S.
q55 $H55S.
q56 $H56S.
q57 $H57S.
q58 $H58S.
q59 $H59S.
q60 $H60S.
q61 $H61S.
q62 $H62S.
q63 $H63S.
q64 $H64S.
q67 $H67S.
q68 $H68S.
q69 $H69S.
q70 $H70S.
q71 $H71S.
q72 $H72S.
q73 $H73S.
q74 $H74S.
q75 $H75S.
q76 $H76S.
q77 $H77S.
q78 $H78S.
q79 $H79S.
q80 $H80S.
q81 $H81S.
q82 $H82S.
q83 $H83S.
q84 $H84S.
q85 $H85S.
q86 $H86S.
q87 $H87S.
q88 $H88S.
q89 $H89S.
qbikehelmet $BIKE.
qdrivemarijuana $DRVMARJ.
qcelldriving $CELLDRV.
qpropertydamage $PROPDAM.
qbullyweight $BULLWGT.
qbullygender $BULLGEND.
qbullygay $BULLGAY.
qchokeself $CHOKE.
qcigschool $CIGS.
qchewtobschool $CHEWTOB.
qalcoholschool $ALCSCH.
qtypealcohol2 $ALCTYPE.
qhowmarijuana $HOWMARJ.
qmarijuanaschool $MARIJSCH.
qcurrentopioid $CURROPI.
qcurrentcocaine $CURRCOC.
qcurrentheroin $CURRHER.
qcurrentmeth $CURRMETH.
qhallucdrug $LSD.
qprescription30d $DRUG30D.
qgenderexp $EXPRESS.
qtaughtHIV $THIV.
qtaughtsexed $TSEXED.
qtaughtstd $TSTD.
qtaughtcondom $TCOND.
qtaughtbc $TBC.
qdietpop $DIETPOP.
qcoffeetea $COFFEE.
qsportsdrink $SPRTDRNK.
qenergydrink $ENRGDRNK.
qsugardrink $SGRDRNK.
qwater $WATER.
qfastfood $FASTFOOD.
qfoodallergy $ALLERGY.
qwenthungry $HUNGRY.
qmusclestrength $MUSCLE.
qsunscreenuse $SUNSCR.
qindoortanning $SUNTAN.
qsunburn $SUNBURN.
qconcentrating $CONCEN.
qcurrentasthma $CURRASTH.
qwheresleep $WHSLP.
qspeakenglish $ENGLISH.
qtransgender $TRNS.
;
 
/****************************************/
/*   Assign labels to SAS variables    */
/****************************************/
;
label
sitecode="Site code"
sitename="Site name"
sitetype="Site type"
sitetypenum="1=District, 2=State, 3=National"
year="4-digit Year of survey"
survyear="1=1991...15=2019"
weight="Analysis weight"
stratum="Analysis stratum"
PSU="Analysis primary sampling unit"
record="Record ID"
age="1= <=12...7=18+ years old"
sex="1=Female, 2=Male"
grade="1=9th...4=12th grade"
race4="4-level race variable"
race7="7-level race variable"
stheight="Height in meters"
stweight="Weight in kilograms"
bmi="Body Mass Index"
bmipct="BMI percentile"
qnobese="Had obesity"
qnowt="Were Overweight"
q66="Sexual identity"
q65="Sex of sexual contacts"
sexid="Sexual identity"
sexid2="Collapsed sexual identity"
sexpart="Sex of sex contact(s)"
sexpart2="Collapsed sex of sex contact(s)"
q8="Seat belt use"
q9="Riding with a drinking driver"
q10="Drinking and driving"
q11="Texting and driving"
q12="Weapon carrying"
q13="Weapon carrying at school"
q14="Gun carrying past 12 mos"
q15="Safety concerns at school"
q16="Threatened at school"
q17="Physical fighting"
q18="Physical fighting at school"
q19="Forced sexual intercourse"
q20="Sexual violence"
q21="Sexual dating violence"
q22="Physical dating violence"
q23="Bullying at school"
q24="Electronic bullying"
q25="Sad or hopeless"
q26="Considered suicide"
q27="Made a suicide plan"
q28="Attempted suicide"
q29="Injurious suicide attempt"
q30="Ever cigarette use"
q31="Initiation of cigarette smoking"
q32="Current cigarette use"
q33="Smoked >10 cigarettes"
q34="Electronic vapor product use"
q35="Current electronic vapor product use"
q36="EVP from store"
q37="Current smokeless tobacco use"
q38="Current cigar use"
q39="All tobacco product cessation"
q40="Initiation of alcohol use"
q41="Current alcohol use"
q42="Current binge drinking"
q43="Largest number of drinks"
q44="Source of alcohol"
q45="Ever marijuana use"
q46="Initiation of marijuana use"
q47="Current marijuana use"
q48="Ever synthetic marijuana use"
q49="Ever prescription pain medicine use"
q50="Ever cocaine use"
q51="Ever inhalant use"
q52="Ever heroin use"
q53="Ever methamphetamine use"
q54="Ever ecstasy use"
q55="Ever steroid use"
q56="Illegal injected drug use"
q57="Illegal drugs at school"
q58="Ever sexual intercourse"
q59="Sex before 13 years"
q60="Multiple sex partners"
q61="Current sexual activity"
q62="Alcohol/drugs and sex"
q63="Condom use"
q64="Birth control pill use"
q67="Perception of weight"
q68="Weight loss"
q69="Fruit juice drinking"
q70="Fruit eating"
q71="Green salad eating"
q72="Potato eating"
q73="Carrot eating"
q74="Other vegetable eating"
q75="No soda drinking"
q76="No milk drinking"
q77="Breakfast eating"
q78="Physical activity >= 5 days"
q79="Television watching"
q80="Computer use"
q81="PE attendance"
q82="Sports team participation"
q83="Concussion"
q84="HIV testing"
q85="STD testing"
q86="Oral health care"
q87="Asthma"
q88="Sleep"
q89="Grades in school"
qn8="Rarely or never wore a seat belt"
qn9="Rode with a driver who had been drinking alcohol"
qn10="Drove when drinking alcohol"
qn11="Texted or e-mailed while driving a car or other vehicle"
qn12="Carried a weapon"
qn13="Carried a weapon on school property"
qn14="Carried a gun"
qn15="Did not go to school because they felt unsafe at school or on their way to or from school"
qn16="Were threatened or injured with a weapon on school property"
qn17="Were in a physical fight"
qn18="Were in a physical fight on school property"
qn19="Were ever physically forced to have sexual intercourse"
qn20="Experienced sexual violence"
qn21="Experienced sexual dating violence"
qn22="Experienced physical dating violence"
qn23="Were bullied on school property"
qn24="Were electronically bullied"
qn25="Felt sad or hopeless"
qn26="Seriously considered attempting suicide"
qn27="Made a plan about how they would attempt suicide"
qn28="Attempted suicide"
qn29="Had a suicide attempt that resulted in an injury, poisoning, or overdose that had to be treated by a doctor or nurse"
qn30="Ever tried cigarette smoking"
qn31="First tried cigarette smoking before age 13 years"
qn32="Currently smoked cigarettes"
qn33="Smoked more than 10 cigarettes per day"
qn34="Ever used an electronic vapor product"
qn35="Currently used an electronic vapor product"
qn36="Usually got their own electronic vapor products by buying them in a store"
qn37="Currently used smokeless tobacco"
qn38="Currently smoked cigars"
qn39="Tried to quit using all tobacco products"
qn40="Had their first drink of alcohol before age 13 years"
qn41="Currently drank alcohol"
qn42="Currently were binge drinking"
qn43="Reported that the largest number of drinks they had in a row was 10 or more"
qn44="Usually got the alcohol they drank by someone giving it to them"
qn45="Ever used marijuana"
qn46="Tried marijuana for the first time before age 13 years"
qn47="Currently used marijuana"
qn48="Ever used synthetic marijuana"
qn49="Ever took prescription pain medicine without a doctor's prescription or differently than how a doctor told them to use it"
qn50="Ever used cocaine"
qn51="Ever used inhalants"
qn52="Ever used heroin"
qn53="Ever used methamphetamines"
qn54="Ever used ecstasy"
qn55="Ever took steroids without a doctor's prescription"
qn56="Ever injected any illegal drug"
qn57="Were offered, sold, or given an illegal drug on school property"
qn58="Ever had sexual intercourse"
qn59="Had sexual intercourse for the first time before age 13 years"
qn60="Had sexual intercourse with four or more persons during their life"
qn61="Were currently sexually active"
qn62="Drank alcohol or used drugs before last sexual intercourse"
qn63="Used a condom during last sexual intercourse"
qn64="Used birth control pills before last sexual intercourse"
qn67="Described themselves as slightly or very overweight"
qn68="Were trying to lose weight"
qn69="Did not drink fruit juice"
qn70="Did not eat fruit"
qn71="Did not eat green salad"
qn72="Did not eat potatoes"
qn73="Did not eat carrots"
qn74="Did not eat other vegetables"
qn75="Did not drink a can, bottle, or glass of soda or pop"
qn76="Did not drink milk"
qn77="Did not eat breakfast"
qn78="Were physically active at least 60 minutes per day on 5 or more days"
qn79="Watched television 3 or more hours per day"
qn80="Played video or computer games or used a computer 3 or more hours per day"
qn81="Attended physical education (PE) classes on 1 or more days"
qn82="Played on at least one sports team"
qn83="Had a concussion from playing a sport or being physically active"
qn84="Were ever tested for human immunodeficiency virus (HIV)"
qn85="Were ever testing for an STD"
qn86="Saw a dentist"
qn87="Had ever been told by a doctor or nurse that they had asthma"
qn88="Got 8 or more hours of sleep"
qn89="Described their grades in school as mostly A's or B's"
qnfrcig="Currently smoked cigarettes frequently"
qndaycig="Currently smoked cigarettes daily"
qnfrevp="Currently used an electronic vapor product frequently"
qndayevp="Currently used an elecctronic vapor product daily"
qnfrcgr="Currently smoked cigars frequently"
qndaycgr="Currently smoked cigars daily"
qntb2="Currently smoked cigarettes or cigars"
qntb3="Currently smoked cigarettes or cigars or used smokeless tobacco"
qntb4="Currently smoked cigarettes or cigars or used smokeless tobacco or electronic vapor products"
qntb5="Currently smoked cigarettes or used electronic vapor products"
qniudimp="Used an IUD (e.g., Mirena or ParaGard) or implant (e.g., Implanon or Nexplanon) before last sexual intercourse"
qnothhpl="Used birth control pills; an IUD (such as Mirena or ParaGard) or implant (such as Implanon or Nexplanon); or a shot (such as Depo-Provera), patch (such as OrthoEvra), or birth control ring (such as NuvaRing) before last sexual intercourse"
qndualbc="Used both a condom during last sexual intercourse and birth control pills; an IUD (such as Mirena or ParaGard) or implant (such as Implanon or Nexplanon); or a shot (such as Depo-Provera), patch (such as OrthoEvra), or birth control ring (such as NuvaRing)"
qnbcnone="Did not use any method to prevent pregnancy during last sexual intercourse"
qnfr0="Did not eat fruit or drink 100% fruit juices"
qnfr1="Ate fruit or drank 100% fruit juices one or more times per day"
qnfr2="Ate fruit or drank 100% fruit juices two or more times per day"
qnveg0="Did not eat vegetables"
qnveg1="Ate vegetables one or more times per day"
qnveg2="Ate vegetables two or more times per day"
qnveg3="Ate vegetables three or more times per day"
qnsoda1="Drank a can, bottle, or glass of soda or pop one or more times per day"
qnsoda2="Drank a can, bottle, or glass of soda or pop two or more times per day"
qnmilk1="Drank one or more glasses per day of milk"
qnmilk3="Drank three or more glasses per day of milk"
qnbk7day="Ate breakfast on all 7 days"
qnpa0day="Did not participate in at least 60 minutes of physical activity on at least 1 day"
qnpa7day="Were physically active at least 60 minutes per day on all 7 days"
qndlype="Attended physical education (PE) classes on all 5 days"
qnnodnt="Never saw a dentist"
qbikehelmet="Bicycle helmet use"
qdrivemarijuana="Drive when using marijuana"
qcelldriving="Cell phone use while driving"
qpropertydamage="Property stolen at school >= 1 time"
qbullyweight="Victim of teasing b/c of physical appearance"
qbullygender="Victim of gender teasing"
qbullygay="Ever been teased b/c labeled GLB"
qchokeself="Ever been choked/choked self on purpose"
qcigschool="Currently smoke at school >=1 days"
qchewtobschool="Current snuff @ school"
qalcoholschool="Current drink at school"
qtypealcohol2="Type of alcohol drink most often"
qhowmarijuana="Usual use of marijuana"
qmarijuanaschool="Marijuana use at school"
qcurrentopioid="Times take pain medicine w/o prescription 30d"
qcurrentcocaine="Current cocaine use"
qcurrentheroin="Current heroin use"
qcurrentmeth="Current meth use"
qhallucdrug="Ever used hallucinogenic drugs"
qprescription30d="Times take drug w/o prescription 30d"
qgenderexp="Others description of your masc/fem"
qtaughtHIV="Ever taught about AIDS/HIV at school"
qtaughtsexed="Ever had sex education in school"
qtaughtstd="Ever been taught in school about STDs"
qtaughtcondom="Ever been taught in school about how to use condom"
qtaughtbc="Ever been taught about BC methods in sch"
qdietpop="Diet soda drinking >=1 time/day"
qcoffeetea="Coffee/tea drinking >=1 time/day"
qsportsdrink="Sports drinks"
qenergydrink="Energy drink >=1 time/day"
qsugardrink="Sugar-sweetened beverage >=1 time/day"
qwater="Plain water"
qfastfood="Meal/snack fast food >= 3 days"
qfoodallergy="Food allergies"
qwenthungry="How often went hungry"
qmusclestrength="Muscle strengthening"
qsunscreenuse="Sunscreen use outside"
qindoortanning="Indoor tanning"
qsunburn="Sunburn"
qconcentrating="Difficulty concentrating"
qcurrentasthma="Current asthma"
qwheresleep="Homelessness"
qspeakenglish="How well speak English"
qtransgender="Transgender"
qnbikehelmet="Rarely or never wore a bicycle helmet"
qndrivemarijuana="Drove a car or other vehicle when they had been using marijuana"
qncelldriving="Talked on a cell phone use while driving"
qnpropertydamage="Reported that their property had been stolen or deliberately damaged on school property one or more times"
qnbullyweight="Have been the victim of teasing or name calling because of their weight, size, or physical appearance"
qnbullygender="Have been the victim of teasing or name calling because of their gender"
qnbullygay="Have been the victim of teasing or name calling because someone thought they were gay, lesbian, or bisexual"
qnchokeself="Have ever been choked by someone or tried to choke themselves on purpose"
qncigschool="Smoked cigarettes on school property"
qnchewtobschool="Used chewing tobacco, snuff, or dip on school property"
qnalcoholschool="Currently had at least one drink of alcohol on school property"
qntypealcohol2="Reported liquor as the type of alcohol they drank most often"
qnhowmarijuana="Usually used marijuana by smoking it in a joint, bong, pipe, or blunt"
qnmarijuanaschool="Used marijuana on school property"
qncurrentopioid="Currently took prescription pain medicine without a doctor's prescription"
qncurrentcocaine="Currently used any form of cocaine"
qncurrentheroin="Currently used heroin"
qncurrentmeth="Currently used methamphetamines"
qnhallucdrug="Ever used hallucinogenic drugs"
qnprescription30d="Currently took a prescription drug without a doctor's prescription"
qnillict="Ever used select illicit drugs"
qngenderexp="Think other people at school would describe them as equally feminine and masculine"
qntaughtHIV="Have been taught about AIDS or HIV infection in school"
qntaughtsexed="Have had sex education in school"
qntaughtstd="Have been taught in school about sexually transmitted diseases (STDs)"
qntaughtcondom="Have ever been taught in school about how to use a condom to prevent pregnancy or sexually transmitted diseases (STDs)"
qntaughtbc="Have been taught in school about birth control methods"
qndietpop="Drank a can, bottle, or glass of diet soda or pop"
qncoffeetea="Drank a cup, can, or bottle of coffee, coffee drinks, or any kind of tea"
qnsportsdrink="Did not drink a can, bottle, or glass of a sports drink"
qnspdrk1="Drank a can, bottle, or glass of a sports drink one or more times per day"
qnspdrk2="Drank a can, bottle, or glass of a sports drink two or more times per day"
qnenergydrink="Drank a can, bottle, or glass of an energy drink"
qnsugardrink="Drank a can, bottle, or glass of a sugar-sweetened beverage"
qnwater="Did not drink a bottle or glass of plain water"
qnwater1="Drank one or more glasses per day of plain water"
qnwater2="Drank two or more glasses per day of plain water"
qnwater3="Drank three or more glasses per day of plain water"
qnfastfood="Ate at least one meal or snack from a fast food restaurant"
qnfoodallergy="Have to avoid some foods because eating the food could cause an allergic reaction"
qnwenthungry="Most of the time or always went hungry because there was not enough food in their home"
qnmusclestrength="Did exercises to strengthen or tone their muscles on three or more days"
qnsunscreenuse="Most of the time or always wear sunscreen"
qnindoortanning="Used an indoor tanning device"
qnsunburn="Had a sunburn"
qnconcentrating="Have serious difficulty concentrating, remembering, or making decisions"
qncurrentasthma="Had been told by a doctor or nurse that they had asthma and who still have asthma"
qnwheresleep="Did not usually sleep in their parent's or guardian's home"
qnspeakenglish="Speak English well or very well"
qntransgender="Are transgender"
;
run;
