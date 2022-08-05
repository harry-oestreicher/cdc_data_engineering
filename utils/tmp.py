
int_list = ["qnobese", "qnowt", "q66", "q65", "sexid", "sexid2", "sexpart", "sexpart2", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31", "q32", "q33", "q34", "q35", "q36", "q37", "q38", "q39", "q40", "q41", "q42", "q43", "q44", "q45", "q46", "q47", "q48", "q49", "q50", "q51", "q52", "q53", "q54", "q55", "q56", "q57", "q58", "q59", "q60", "q61", "q62", "q63", "q64", "q67", "q68", "q69", "q70", "q71", "q72", "q73", "q74", "q75", "q76", "q77", "q78", "q79", "q80", "q81", "q82", "q83", "q84", "q85", "q86", "q87", "q88", "q89", "qbikehelmet", "qdrivemarijuana", "qcelldriving", "qpropertydamage", "qbullyweight", "qbullygender", "qbullygay", "qchokeself", "qcigschool", "qchewtobschool", "qalcoholschool", "qtypealcohol2", "qhowmarijuana", "qmarijuanaschool", "qcurrentopioid", "qcurrentcocaine", "qcurrentheroin", "qcurrentmeth", "qhallucdrug", "qprescription30d", "qgenderexp", "qtaughtHIV", "qtaughtsexed", "qtaughtstd", "qtaughtcondom", "qtaughtbc", "qdietpop", "qcoffeetea", "qsportsdrink", "qenergydrink", "qsugardrink", "qwater", "qfastfood", "qfoodallergy", "qwenthungry", "qmusclestrength", "qsunscreenuse", "qindoortanning", "qsunburn", "qconcentrating", "qcurrentasthma", "qwheresleep", "qspeakenglish", "qtransgender"]


# Function? :( maybe not
def use_dict(column_in, value_in):
    """
    Translates values into understandable output.
    """
    if column_in == "age":
        age ={
            1: "12 years old or younger",
            2: "13 years old",
            3: "14 years old",
            4: "15 years old",
            5: "16 years old",
            6: "17 years old",
            7: "18 years old or older"
        }
        val = age.get(value_in)

    elif column_in == "sex":
        sex ={
            1: "Female",
            2: "Male",
            3: "Other"
        }
        val = sex.get(value_in)
        
    elif column_in == "grade":
        grade = {
            1: "9th grade",
            2: "10th grade",
            3: "11th grade",
            4: "12th grade",
            5: "Ungraded or other grade"
        }
        val = grade.get(value_in)

    elif column_in == "race4":
        race4 = {
            1: "White",
            2: "Black or African American",
            3: "Hispanic/Latino",
            4: "All Other Races"
        }
        val = race4.get(value_in)

    elif column_in == "grarace7de":
        race7 = {
            1: "American Indian/Alaska Native",
            2: "Asian",
            3: "Black or African American",
            4: "Hispanic/Latino",
            5: "Native Hawaiian/Other Pacific Islander",
            6: "White",
            7: "Multiple Races (Non-Hispanic)"
        }
        val = race7.get(value_in)
        
    elif column_in == "q66":
        q66 = {
            1: "Heterosexual (straight)",
            2: "Gay or lesbian",
            3: "Bisexual",
            4: "Not sure"
        }
        val = q66.get(value_in)
        
    elif column_in == "q65":
        q65 = {
            1: "I have never had sexual contact",
            2: "Females",
            3: "Males",
            4: "Females and males"
        }
        val = q65.get(value_in)
        
       
        
    return val

print(use_dict("age", 6))