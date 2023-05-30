class Date:

    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def formatted_date(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:4d}"


# date_obj = Date(10, 9, 2023)
# print(date_obj.formatted_date(), "\n")

# date_obj_2 = Date(11, "03", 2020)
# print(date_obj_2.formatted_date(), "\n")
