

# Scrape Data Gempa BMKG

This project is designed to scrape earthquake data from the Indonesian Meteorology, Climatology, and Geophysics Agency (BMKG) website.
The program will scrape the earthquake data from a user-specified time period and store it in a CSV file. 

## Source

The data is scraped from the BMKG website at [https://repogempa.bmkg.go.id/](https://repogempa.bmkg.go.id/). 

## Requirements

This project requires Python 3.x to run.

## Usage

1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the necessary requirements by running the following command in your terminal:

```
pip install -r requirements.txt
```

4. Set your date `start_date` and `end_date` that you want in file `main.py`. 

5. Run the script by running the following command in your terminal:

```
python3 main.py
```

6. The script will save the scraped earthquake data to a CSV file named `data_gempa.csv` in the project directory.

## Output

The program will output the following files:

- `data_gempa.csv`: The earthquake data scraped from the BMKG website. The CSV file will contain the following columns:

  - `No` : Event number of list of events
  - `Event ID` : The event id of the earthquake.
  - `Date Time`: The date of the earthquake in YYYY-MM-DDT format.
  - `Latitude`: The latitude of the earthquake.
  - `Longitude`: The longitude of the earthquake.
  - `Magnitude`: The magnitude of the earthquake.
  - `Mag Type`: Type of earthquake magnitude such as Mlv, Mw, MwP etc.
  - `Depth`: Depth of earthquake, the place inside earth where an earthquake occurred in kilometers.
  - `Phase Count`: Number of station phase arrival of an earthquake.
  - `Azimuth Gap`: The maximum angle separating two adjacent seismic stations, both measured from the epicenter of an earthquake.
  - `Location`: The region where the earthquake occurred.
  - `Agency`: The official institution responsible for producing of earthquake information (BMKG).

- `log_error.txt`: A log file that records any period errors that occurred during the scraping process. If the scraping process completed successfully, this file will be empty.

## Disclaimer

This project is for educational purposes only. Please use the scraped data responsibly and do not misuse it in any way that may cause harm.
