

library(DBI)
con <- dbConnect(RSQLite::SQLite(), dbname = "~/Development/Portfolio/cdc_data_engineering/data/yrbss_data.db")
tables = dbListTables(con)
mylist = dbGetQuery(con, "SELECT year, age, stheight FROM DISTRICT LIMIT 100;")
print(mylist)
