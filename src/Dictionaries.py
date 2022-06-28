
monthConversion = {
    "Jan": "January",
    "Feb": "Februar",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

monthConversionNumerical = {
    1: "January",
    2: "Februar",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",

}

print(monthConversion["Aug"])
print(monthConversion.get("Oct"))

print(monthConversionNumerical[1])
print(monthConversionNumerical.get(6))
