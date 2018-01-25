class DateTime:

    def dt(self):
        import datetime
        print(datetime.datetime.now().date(), datetime.datetime.now().time())

dt1 = DateTime()
print("Today's date and time:")
dt1.dt()          # prints out current date and time