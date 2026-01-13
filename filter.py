import csv

def filter_station_platforms(input_file, output_file):
    """
    Filter stops.txt to only include rows where stop_name contains
    both 'station' and 'platform' (case-insensitive).
    """
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        
        # Find the index of stop_name column
        stop_name_index = header.index('stop_name')
        parent_station_index = header.index('parent_station')
        
        # Filter rows where stop_name contains both 'station' and 'platform'
        filtered_rows = []
        for row in reader:
            stop_name = row[stop_name_index].lower()
            parent_station = row[parent_station_index].lower()
            if 'station' in stop_name and 'platform' in stop_name:
                # if 'bus' not in stop_name and 'bs' not in parent_station and 'bwy' not in parent_station: 
                    filtered_rows.append(row)
    
    # Write filtered data to output file
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(filtered_rows)
    
    print(f"Filtered {len(filtered_rows)} rows containing 'station' and 'platform'")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    input_file = "filtered_stops.txt"
    output_file = "train_stations.txt"
    filter_station_platforms(input_file, output_file)