days = int(input("enter days : "))
years = days//365
remaing_days =days-years*365
months = remaing_days // 30
remaing_days =remaing_days-months*30
weeks = remaing_days // 7
remaining_days = days-weeks*7

daysu =remaing_days

print(years,"years",months,"months",weeks,"weeks ",daysu,"daysu")
