import pandas as pd
import datetime

start_date = datetime.date(2017, 1, 1)
end_date = datetime.date(2022, 12, 31)
delta = datetime.timedelta(days=1)

date_ranges = []
while start_date <= end_date:
    year = start_date.year
    month = start_date.month
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year
    end_of_month = datetime.date(next_year, next_month, 1) - delta
    date_ranges.append((start_date.strftime("%Y-%m-%d"), end_of_month.strftime("%Y-%m-%d")))
    start_date = datetime.date(next_year, next_month, 1)

for x in date_ranges:
    url = "https://repogempa.bmkg.go.id/getEvent?"\
            "date_range=2023-01-01T00:00:00&" \
            "min_date=" + x[0] + "T00:00:00&" \
            "max_date=" + x[1] + "T23:59:59&" \
            "minmag=0.0&maxmag=10.0&" \
            "mindepth=0&maxdepth=1000&" \
            "north=6&west=95&east=141&south=-11&" \
            "eventtype=preliminaryeq&parameter=origin&" \
            "email=dummy@gmail.com&institution=BMKG"
    try:
        data = pd.read_html(url)
        with open('data_gempa.csv', 'a') as f:
            data[0].to_csv(f, header=False)
    except:
        with open("log_error.txt", "a") as f:
            f.write("Error : " + x[0] + " - " + x[1] + "\n")