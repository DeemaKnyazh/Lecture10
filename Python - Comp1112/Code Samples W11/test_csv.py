import csv_processor

loaded_csv = csv_processor.load_csv("MontrealWeather.csv")

for row in loaded_csv:
    rowString = ""
    for item in row:
        if item != "":
            rowString += f"{item} - "
    print(rowString[:-3])