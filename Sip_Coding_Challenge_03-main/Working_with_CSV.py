import csv

years = []
months = []
CO2_values = []

# Minimum / Maximum / Mean Values:

with open("C:\Sip_EVS528\Sip_CodingChallenge_03\co2-ppm-daily_csv.csv") as CO2:
    csv_reader = csv.reader(CO2, delimiter=',')
    line_counter = 0
    header_skip = next(CO2)
    print(header_skip)

    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in years:
            years.append(year)
        if month not in months:
            months.append(month)

        CO2_values.append(float(row[1]))
        line_counter = line_counter + 1

print("The maximum CO2 value from the list is " + str(max(CO2_values)))
print("\nThe minimum CO2 value from the list is " + str(min(CO2_values)))
print("\nThe average of all CO2 values from the list is " + str(round((float(sum(CO2_values) / int(line_counter))), 2)))

# Annual Averages:

years_dict = {}

for year in years:
    years_list = []
    with open("C:\Sip_EVS528\Sip_CodingChallenge_03\co2-ppm-daily_csv.csv") as CO2:
        csv_reader = csv.reader(CO2, delimiter=',')
        header_skip = next(CO2)

        for row in csv_reader:
            CO2_year, CO2_month, CO2_day = row[0].split("-")
            if CO2_year == year:
                years_list.append(float(row[1]))

    years_dict[year] = str(str(sum(years_list) / len(years_list)))

print("\nThe following are average annual CO2 values from 1958-2019:\n" + str(years_dict))

# Seasonal Averages:

spring_list = []
summer_list = []
autumn_list = []
winter_list = []

with open("C:\Sip_EVS528\Sip_CodingChallenge_03\co2-ppm-daily_csv.csv") as CO2:
    csv_reader = csv.reader(CO2, delimiter=',')
    header_skip = next(CO2)

    for row in csv_reader:
        CO2_year, CO2_month, CO2_day = row[0].split("-")
        if CO2_month == '03' or CO2_month == '04' or CO2_month == '05':
            spring_list.append(float(row[1]))
        if CO2_month == '06' or CO2_month == '07' or CO2_month == '08':
            summer_list.append(float(row[1]))
        if CO2_month == '09' or CO2_month == '10' or CO2_month == '11':
            autumn_list.append(float(row[1]))
        if CO2_month == '12' or CO2_month == '01' or CO2_month == '02':
            winter_list.append(float(row[1]))

print("\nThe average CO2 value throughout Spring months in this dataset = " + str(round((float(sum(spring_list) / len(spring_list))), 3)))
print("\nThe average CO2 value throughout Summer months in this dataset = " + str(round((float(sum(summer_list) / len(summer_list))), 3)))
print("\nThe average CO2 value throughout Autumn months in this dataset = " + str(round((float(sum(autumn_list) / len(autumn_list))), 3)))
print("\nThe average CO2 value throughout Winter months in this dataset = " + str(round((float(sum(winter_list) / len(winter_list))), 3)))

print("\n")