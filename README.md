[![Board Status](https://dev.azure.com/harryoestreicher/7e5aab40-4601-4e56-926a-9c0ce9bc4644/c8f7a99a-4db7-4b32-bd8f-3f27692c8d39/_apis/work/boardbadge/8b8aeca1-4478-4191-b8ab-1f466943a8ac)](https://dev.azure.com/harryoestreicher/7e5aab40-4601-4e56-926a-9c0ce9bc4644/_boards/board/t/c8f7a99a-4db7-4b32-bd8f-3f27692c8d39/Microsoft.RequirementCategory)
# YRBSS Exploratory Data Analysis

## Background

The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of health-related behaviors that contribute to the leading causes of death and disability among youth and adults, including:
- Behaviors that contribute to unintentional injuries and violence
- Sexual behaviors related to unintended pregnancy and sexually transmitted diseases, including HIV infection
- Alcohol and other drug use
- Tobacco use
- Unhealthy dietary behaviors
- Inadequate physical activity

YRBSS also measures the prevalence of obesity and asthma and other health-related behaviors plus sexual identity and sex of sexual contacts.

YRBSS is a system of surveys. It includes 1) a national school-based survey conducted by CDC and state, territorial, tribal, and 2) local surveys conducted by state, territorial, and local education and health agencies and tribal governments. `src:` [CDC.gov](https://www.cdc.gov/healthyyouth/data/yrbs/data.htm?s_cid=hy-YRBS-2020-3)

## WIP Project
- perform analysis using jupyter notebooks with visualizations (ANOVA, 
- build web UI to consume data from clou-hosted api

#### Measurement Levels

These levels of measurement determine how survey questions could be measured and which statistical analysis could be performed.

- **Nominal Scale** - Nominal scales classify data without any quantitative value, similar to labels. An example of a nominal scale is, "Select your car's brand from the list below." The choices have no relationship to each other. Due to the lack of numerical significance, you can only keep track of how many respondents chose each option and which option was selected the most.

- **Ordinal Scale** - Ordinal scales are used to depict the order of values. For this scale, there's a quantitative value because one rank is higher than another. An example of an ordinal scale is, "Rank the reasons for using your laptop." You can analyze both mode and median from this type of scale, and ordinal scales can be analyzed through cross-tabulation analysis.

- **Interval Scale** - Interval scales depict both the order and difference between values. These scales have quantitative value because data intervals remain equivalent along the scale, but there's no true zero point. An example of an interval scale is in an IQ test. You can analyze mode, median, and mean from this type of scale and analyze the data through ANOVA, t-tests, and correlation analyses. ANOVA tests the significance of survey results, while t-tests and correlation analyses determine if datasets are related.

- **Ratio Scale** - Ratio scales depict the order and difference between values, but unlike interval scales, they do have a true zero point. With ratio scales, there's quantitative value because the absence of an attribute can still provide information. For example, a ratio scale could be, "Select the average amount of money you spend online shopping." You can analyze mode, median, and mean with this type of scale and ratio scales can be analyzed through t-tests, ANOVA, and correlation analyses as well.


## ANOVA

We will take independent random samples from each group in the dataset, then compute the sample means for each group.

Then we'll compare the variation of sample means among the groups to the variation within the groups. Finally, make a decision based on a test statistic, whether the means of the groups are all equal or not.



We've will start off by creating a single SQLLite db for the three "tables" of data in teh CSV files.

- National
- District
- State (large enough for the CDC to split into two files. we'll import the data, then concatenate into a single `STATE` table in our db.

## Requirements

Python
Pandas
SQLAlchemy
HVPlot

## Get Started

1. Clone this repository:

2. Download the converted data (CSV format) These were converted from MS ACCESS files [CDC.gov](https://www.cdc.gov/healthyyouth/data/yrbs/data.htm)
  - *[Download from local server](https://rhel8.test/cdc_origin_data_2022-09-07.tar.gz)*

3. Extract the CSV files into the `/origin_data` folder.

4. From the repository root, launch `jupyter lab`



