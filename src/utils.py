import pandas as pd

"""
TEST

"""
def column_formatter(col_in):

    if col_in == "site":
        site = {
            "AB": "Albuquerque, NM",
            "AK": "Alaska",
            "AL": "Alabama",
            "AR": "Arkansas",
            "AZB": "Arizona",
            "CA": "California",
            "CC": "Clark County, NV",
            "CE": "Cleveland, OH",
            "CH": "Chicago, IL",
            "CM": "Charlotte-Mecklenburg County, NC",
            "CO": "Colorado",
            "CT": "Connecticut",
            "DA": "Dallas, TX",
            "DE": "Delaware",
            "DU": "Duval County, FL",
            "EA": "Eaton Consortium, MI",
            "FL": "Florida",
            "FT": "Broward County, FL",
            "FW": "Fort Worth, TX",
            "GA": "Georgia",
            "GE": "Genesee Consortium, MI",
            "GS": "Gaston County, NC",
            "HI": "Hawaii",
            "HL": "Hillsborough County, FL",
            "IA": "Iowa",
            "ID": "Idaho",
            "IL": "Illinois",
            "KS": "Kansas",
            "KY": "Kentucky",
            "LA": "Louisiana",
            "LO": "Los Angeles, CA",
            "MD": "Maryland",
            "ME": "Maine",
            "MI": "Michigan",
            "ML": "Milwaukee, WI",
            "MM": "Miami-Dade County, FL",
            "MO": "Missouri",
            "MS": "Mississippi",
            "MT": "Montana",
            "NC": "North Carolina",
            "ND": "North Dakota",
            "NE": "Nebraska",
            "NH": "New Hampshire",
            "NJ": "New Jersey",
            "NM": "New Mexico",
            "NO": "New Orleans, LA",
            "NV": "Nevada",
            "NW": "Newark, NJ",
            "NY": "New York",
            "NYC": "New York City, NY",
            "NYG": "Borough of Bronx, NY",
            "NYH": "Borough of Brooklyn, NY",
            "NYI": "Borough of Manhattan, NY",
            "NYJ": "Borough of Queens, NY",
            "NYK": "Borough of Staten Island, NY",
            "OA": "Oakland, CA",
            "OK": "Oklahoma",
            "OL": "Orange County, FL",
            "PA": "Pennsylvania",
            "PB": "Palm Beach County, FL",
            "PH": "Philadelphia, PA",
            "PO": "Portland, OR",
            "PS": "Pasco County, FL",
            "RI": "Rhode Island",
            "SA": "San Diego, CA",
            "SB": "San Bernardino, CA",
            "SC": "South Carolina",
            "SD": "South Dakota",
            "SE": "Seattle, WA",
            "SF": "San Francisco, CA",
            "SP": "Spartanburg County, SC",
            "ST": "Shelby County, TN",
            "TN": "Tennessee",
            "TX": "Texas",
            "UT": "Utah",
            "VA": "Virginia",
            "VT": "Vermont",
            "WI": "Wisconsin",
            "WV": "West Virginia",
            "WY": "Wyoming",
            "XX": "United States",
        }
        val = site.get(col_in)

    elif col_in == "age":
        age = {
            1: "12 years old or younger",
            2: "13 years old",
            3: "14 years old",
            4: "15 years old",
            5: "16 years old",
            6: "17 years old",
            7: "18 years old or older",
        }
        val = age.get(col_in)

    elif col_in == "sex":
        sex = {
            1: "Female",
            2: "Male",
        }
        val = sex.get(col_in)

    elif col_in == "grade":
        grade = {
            1: "9th",
            2: "10th",
            3: "11th",
            4: "12th",
        }
        val = grade.get(col_in)

    elif col_in == "race4":
        race4 = {
            1: "White",
            2: "Black or African American",
            3: "Hispanic/Latino",
            4: "All other races",
        }
        val = race4.get(col_in)

    elif col_in == "race7":
        sex = {
            1: "Female",
            2: "Male",
        }
        val = sex.get(col_in)
    elif col_in == "q66":
        sex = {
            1: "Female",
            2: "Male",
        }
        val = sex.get(col_in)
    elif col_in == "q65":
        sex = {
            1: "Female",
            2: "Male",
        }
        val = sex.get(col_in)
    elif col_in == "sex":
        sex = {
            1: "Female",
            2: "Male",
        }
        val = sex.get(col_in)
    elif col_in == "sex":
        sex = {
            1: "Female",
            2: "Male",
        }
        val = sex.get(col_in)



value GRADE

value RACE

value RACE7S
1="Am Indian / Alaska Native"
2="Asian"
3="Black or African American"
4="Hispanic/Latino"
5="Native Hawaiian/other PI"
6="White"
7="Multiple - Non-Hispanic";
value $H66S
" "="Missing"
"1"="Heterosexual (straight)"
"2"="Gay or lesbian"
"3"="Bisexual"
"4"="Not sure"
other="** Data Error **";
value $H65S
" "="Missing"
"1"="Never had sexual contact"
"2"="Females"
"3"="Males"
"4"="Females and males"
other="** Data Error **";
value SEXID
1="Heterosexual"
2="Gay or Lesbian"
3="Bisexual"
4="Not Sure";   
value SEXIDB
1="Heterosexual"
2="Sexual Minority"
3="Unsure";
value SEXPART
1="Never had sex"
2="Opposite sex only"
3="Same sex only"
4="Both Sexes";
value SEXPARTB
1="Never had sex"
2="Opposite sex only"
3="Same sex only or both sexes";

















    return val
