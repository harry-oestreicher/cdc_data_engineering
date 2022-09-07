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

## Problem

The data available from the CDC is proprietary. You must own a software copy or license for MS ACCESS or SAS.  We're interested in usign python to do our data mining. By converting the Access databases to csv files, we can import the data into our own database to be more OpenSourcy.  SQLAlchemy is a fine too for establishign database connections to a variety of backends.  We will start off by creating a single SQLLite db for the three "tables" of data in teh CSV files.

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
  *[Download from local server](https://rhel8.test/cdc_origin_data_2022-09-07.tar.gz)*

3. Extract the CSV files into the `/origin_data` folder.

4. From the repository root, launch `jupyter lab`



