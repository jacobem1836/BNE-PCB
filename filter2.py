import csv

STATIONS_FILE = "stations.txt"
STOPS_FILE = "stops.txt"
OUTPUT_FILE = "filtered_stops.txt"


def load_station_ids(path):
    """Load station IDs from the first column of stations.txt"""
    station_ids = set()
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:  # skip empty lines
                station_ids.add(row[0])
    return station_ids


def filter_stops(stops_path, station_ids, output_path):
    """Write only stops whose parent_station exists in station_ids"""
    with open(stops_path, newline="", encoding="utf-8") as infile, \
         open(output_path, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        parent_station_index = header.index("parent_station")
        

        for row in reader:
            parent_station = row[parent_station_index].strip()
            if parent_station in station_ids:
                writer.writerow(row)


def main():
    station_ids = load_station_ids(STATIONS_FILE)
    filter_stops(STOPS_FILE, station_ids, OUTPUT_FILE)
    print(f"Filtered stops written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
