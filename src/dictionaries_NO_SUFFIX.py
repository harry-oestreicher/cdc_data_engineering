import pandas as pd

sex = {
    0: "",
    1: "Female",
    2: "Male",
    3: "Other"
}

age = {
    0: "",
    1: "12 years old or younger",
    2: "13 years old",
    3: "14 years old",
    4: "15 years old",
    5: "16 years old",
    6: "17 years old",
    7: "18 years old or older"
}

grade = {
    0: "",
    1: "9th grade",
    2: "10th grade",
    3: "11th grade",
    4: "12th grade",
    5: "Ungraded or other grade"
}

race4 = {
    0: "",
    1: "White",
    2: "Black or African American",
    3: "Hispanic/Latino",
    4: "All Other Races"
}

race7 = {
    0: "",
    1: "American Indian/Alaska Native",
    2: "Asian",
    3: "Black or African American",
    4: "Hispanic/Latino",
    5: "Native Hawaiian/Other Pacific Islander",
    6: "White",
    7: "Multiple Races (Non-Hispanic)"
}

q66 = {
    0: "",
    1: "Heterosexual (straight)",
    2: "Gay or lesbian",
    3: "Bisexual",
    4: "Not sure"
}

q65 = {
    0: "",
    1: "I have never had sexual contact",
    2: "Females",
    3: "Males",
    4: "Females and males"
}

sexid = {
    1: "Heterosexual",
    2: "Gay or Lesbian",
    3: "Bisexual",
    4: "Not Sure"
}

sexidb = {
    1: "Heterosexual",
    2: "Sexual Minority",
    3: "Unsure"
}

sexpart = {
    1: "Never had sex",
    2: "Opposite sex only",
    3: "Same sex only",
    4: "Both Sexes"
}

sexpartb = {
    1: "Never had sex",
    2: "Opposite sex only",
    3: "Same sex only or both sexes"
}

q8 = {
    1: "Never",
    2: "Rarely",
    3: "Sometimes",
    4: "Most of the time",
    5: "Always"
}
q9 = {
    1: "0 times",
    2: "1 time",
    3: "2 or 3 times",
    4: "4 or 5 times",
    5: "6 or more times"
}
q10 = {
    1: "Did not drive",
    2: "0 times",
    3: "1 time",
    4: "2 or 3 times",
    5: "4 or 5 times",
    6: "6 or more times"
}
q11 = {
    1: "Did not drive",
    2: "0 days",
    3: "1 or 2 days",
    4: "3 to 5 days",
    5: "6 to 9 days",
    6: "10 to 19 days",
    7: "20 to 29 days",
    8: "All 30 days"
}
q12 = {
    1: "0 days",
    2: "1 day",
    3: "2 or 3 days",
    4: "4 or 5 days",
    5: "6 or more days"
}
q13 = {
    1: "0 days",
    2: "1 day",
    3: "2 or 3 days",
    4: "4 or 5 days",
    5: "6 or more days"
}
q14 = {
    1: "0 days",
    2: "1 day",
    3: "2 or 3 days",
    4: "4 or 5 days",
    5: "6 or more days"
}
q15 = {
    1: "0 days",
    2: "1 day",
    3: "2 or 3 days",
    4: "4 or 5 days",
    5: "6 or more days"
}
q16 = {
    1: "0 times",
    2: "1 time",
    3: "2 or 3 times",
    4: "4 or 5 times",
    5: "6 or 7 times",
    6: "8 or 9 times",
    7: "10 or 11 times",
    8: "12 or more times"
}
q17 = {
    1: "0 times",
    2: "1 time",
    3: "2 or 3 times",
    4: "4 or 5 times",
    5: "6 or 7 times",
    6: "8 or 9 times",
    7: "10 or 11 times",
    8: "12 or more times"
}
q18 = {
    1: "0 times",
    2: "1 time",
    3: "2 or 3 times",
    4: "4 or 5 times",
    5: "6 or 7 times",
    6: "8 or 9 times",
    7: "10 or 11 times",
    8: "12 or more times"
}
q19 = {
    1: "Yes",
    2: "No"
}
q20 = {
    1: "0 times",
    2: "1 time",
    3: "2 or 3 times",
    4: "4 or 5 times",
    5: "6 or more times"
}
q21 = {
    1: "Did not date",
    2: "0 times",
    3: "1 time",
    4: "2 or 3 times",
    5: "4 or 5 times",
    6: "6 or more times"
}
q22 = {
    1: "Did not date",
    2: "0 times",
    3: "1 time",
    4: "2 or 3 times",
    5: "4 or 5 times",
    6: "6 or more times"
}
q23 = {
    1: "Yes",
    2: "No"
}
q24 = {
    1: "Yes",
    2: "No"
}
q25 = {
    # 0: "", TEST
    1: "Yes",
    2: "No"
}
q26 = {
    0: "",
    1: "Yes",
    2: "No"
}
q27 = {
    0: "",
    1: "Yes",
    2: "No"
}
q28 = {
    0: "",
    1: "0 times",
    2: "1 time",
    3: "2 or 3 times",
    4: "4 or 5 times",
    5: "6 or more times"
}
q29 = {
    0: "",
    1: "Did not attempt suicide",
    2: "Yes",
    3: "No"
}
q29 = {
1: "Did not attempt suicide",
2: "Yes",
3: "No"
}

q30 = {
1: "Yes",
2: "No"
}

q31 = {
1: "Never tried cigarette smoking",
2: "8 years old or younger",
3: "9 or 10 years old",
4: "11 or 12 years old",
5: "13 or 14 years old",
6: "15 or 16 years old",
7: "17 years old or older",
}

q32 = {
1: "0 days",
2: "1 or 2 days",
3: "3 to 5 days",
4: "6 to 9 days",
5: "10 to 19 days",
6: "20 to 29 days",
7: "All 30 days"
}

q33 = {
1: "Did not smoke cigarettes",
2: "Less than 1 cigarette",
3: "1 cigarette",
4: "2 to 5 cigarettes",
5: "6 to 10 cigarettes",
6: "11 to 20 cigarettes",
7: "More than 20 cigarettes"
}

q34 = {
1: "Yes",
2: "No"
}

q35 = {
1: "0 days",
2: "1 or 2 days",
3: "3 to 5 days",
4: "6 to 9 days",
5: "10 to 19 days",
6: "20 to 29 days",
7: "All 30 days"
}

q36 = {
1: "Did not use any vapor products",
2: "Bought them in a store",
3: "I got them on the Internet",
4: "Someone else bought them",
5: "Borrowed them",
6: "Someone gave them to me",
7: "Took them from a store",
8: "Some other way"
}

q37 = {
1: "0 days",
2: "1 or 2 days",
3: "3 to 5 days",
4: "6 to 9 days",
5: "10 to 19 days",
6: "20 to 29 days",
7: "All 30 days"
}

q38 = {
1: "0 days",
2: "1 or 2 days",
3: "3 to 5 days",
4: "6 to 9 days",
5: "10 to 19 days",
6: "20 to 29 days",
7: "All 30 days",
}

q39 = {
1: "I did not use tobacco products",
2: "Yes",
3: "No"
}

q40 = {
1: "Never drank alcohol",
2: "8 years old or younger",
3: "9 or 10 years old",
4: "11 or 12 years old",
5: "13 or 14 years old",
6: "15 or 16 years old",
7: "17 years old or older"
}

q41 = {
1: "0 days",
2: "1 or 2 days",
3: "3 to 5 days",
4: "6 to 9 days",
5: "10 to 19 days",
6: "20 to 29 days",
7: "All 30 days"
}

q42 = {
1: "0 days",
2: "1 day",
3: "2 days",
4: "3 to 5 days",
5: "6 to 9 days",
6: "10 to 19 days",
7: "20 or more days"
}

q43 = {
1: "Did not drink in past 30 days",
2: "1 or 2 drinks",
3: "3 drinks",
4: "4 drinks",
5: "5 drinks",
6: "6 or 7 drinks",
7: "8 or 9 drinks",
8: "10 or more drinks"
}

q44 = {
1: "Did not drink in past 30 days",
2: "Bought in store",
3: "Bought in restaurant",
4: "Bought at public event",
5: "I gave someone money to buy",
6: "Someone gave it to me",
7: "Took from store/family",
8: "Some other way"
}

q45 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 to 99 times",
7: "100 or more times"
}

q46 = {
1: "Never tried marijuana",
2: "8 years old or younger",
3: "9 or 10 years old",
4: "11 or 12 years old",
5: "13 or 14 years old",
6: "15 or 16 years old",
7: "17 years old or older"
}

q47 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q48 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q49 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q50 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q51 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q52 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q53 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q54 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q55 = {
1: "0 times",
2: "1 or 2 times",
3: "3 to 9 times",
4: "10 to 19 times",
5: "20 to 39 times",
6: "40 or more times"
}

q56 = {
1: "0 times",
2: "1 time",
3: "2 or more times"
}

q57 = {
1: "Yes",
2: "No"
}

q58 = {
1: "Yes",
2: "No"
}

q59 = {
1: "Never had sex",
2: "11 years old or younger",
3: "12 years old",
4: "13 years old",
5: "14 years old",
6: "15 years old",
7: "16 years old",
8: "17 years old or older"
}

q60 = {
1: "Never had sex",
2: "1 person",
3: "2 people",
4: "3 people",
5: "4 people",
6: "5 people",
7: "6 or more people"
}

q61 = {
1: "Never had sex",
2: "None during past 3 months",
3: "1 person",
4: "2 people",
5: "3 people",
6: "4 people",
7: "5 people",
8: "6 or more people"
}

q62 = {
1: "Never had sex",
2: "Yes",
3: "No"
}

q63 = {
1: "Never had sex",
2: "Yes",
3: "No"
}

q64 = {
1: "Never had sex",
2: "No method was used",
3: "Birth control pills",
4: "Condoms",
5: "IUD or implant",
6: "Shot/patch/birth control ring",
7: "Withdrawal/other method",
8: "Not sure"
}

q67 = {
1: "Very underweight",
2: "Slightly underweight",
3: "About the right weight",
4: "Slightly overweight",
5: "Very overweight"
}

q68 = {
1: "Lose weight",
2: "Gain weight",
3: "Stay the same weight",
4: "Not trying to do anything"
}

q69 = {
1: "Did not drink fruit juice",
2: "1 to 3 times",
3: "4 to 6 times",
4: "1 time per day",
5: "2 times per day",
6: "3 times per day",
7: "4 or more times per day"
}

q70 = {
1: "Did not eat fruit",
2: "1 to 3 times",
3: "4 to 6 times",
4: "1 time per day",
5: "2 times per day",
6: "3 times per day",
7: "4 or more times per day",
}

q71 = {
1: "Did not eat green salad",
2: "1 to 3 times",
3: "4 to 6 times",
4: "1 time per day",
5: "2 times per day",
6: "3 times per day",
7: "4 or more times per day"
}

q72 = {
1: "Did not eat potatoes",
2: "1 to 3 times",
3: "4 to 6 times",
4: "1 time per day",
5: "2 times per day",
6: "3 times per day",
7: "4 or more times per day"
}

q73 = {
1: "Did not eat carrots",
2: "1 to 3 times",
3: "4 to 6 times",
4: "1 time per day",
5: "2 times per day",
6: "3 times per day",
7: "4 or more times per day"
}

q74 = {
1: "Did not eat other vegetables",
2: "1 to 3 times",
3: "4 to 6 times",
4: "1 time per day",
5: "2 times per day",
6: "3 times per day",
7: "4 or more times per day"
}

q75 = {
1: "Did not drink soda or pop",
2: "1 to 3 times",
3: "4 to 6 times",
4: "1 time per day",
5: "2 times per day",
6: "3 times per day",
7: "4 or more times per day"
}

q76 = {
1: "Did not drink milk",
2: "1 to 3 glasses",
3: "4 to 6 glasses",
4: "1 glass per day",
5: "2 glasses per day",
6: "3 glasses per day",
7: "4 or more glasses per day"
}

q77 = {
1: "0 days",
2: "1 day",
3: "2 days",
4: "3 days",
5: "4 days",
6: "5 days",
7: "6 days",
8: "7 days"
}

q78 = {
1: "0 days",
2: "1 day",
3: "2 days",
4: "3 days",
5: "4 days",
6: "5 days",
7: "6 days",
8: "7 days"
}

q79 = {
1: "No TV on average school day",
2: "Less than 1 hour per day",
3: "1 hour per day",
4: "2 hours per day",
5: "3 hours per day",
6: "4 hours per day",
7: "5 or more hours per day"
}

q80 = {
1: "No playing video/computer game",
2: "Less than 1 hour per day",
3: "1 hour per day",
4: "2 hours per day",
5: "3 hours per day",
6: "4 hours per day",
7: "5 or more hours per day"
}

q81 = {
1: "0 days",
2: "1 day",
3: "2 days",
4: "3 days",
5: "4 days",
6: "5 days"
}

q82 = {
1: "0 teams",
2: "1 team",
3: "2 teams",
4: "3 or more teams"
}

q83 = {
1: "0 times",
2: "1 time",
3: "2 times",
4: "3 times",
5: "4 or more times"
}

q84 = {
    1: "Yes",
    2: "No",
    3: "Not sure"
}

q85 = {
1: "Yes",
2: "No",
3: "Not sure"
}

q86 = {
1: "During the past 12 months",
2: "Between 12 and 24 months ago",
3: "More than 24 months ago",
4: "Never",
5: "Not sure"
}

q87 = {
1: "Yes",
2: "No",
3: "Not sure"
}

q88 = {
1: "4 or less hours",
2: "5 hours",
3: "6 hours",
4: "7 hours",
5: "8 hours",
6: "9 hours",
7: "10 or more hours"
}

q89 = {
1: "Mostly A's",
2: "Mostly B's",
3: "Mostly C's",
4: "Mostly D's",
5: "Mostly F's",
6: "None of these grades",
7: "Not sure"
}
