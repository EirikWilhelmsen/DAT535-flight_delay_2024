try:
    csv_file_path = "data/flights_2.csv"
    output_file_path = "data/flights_unstructured.txt"

    with open(csv_file_path, 'r') as file:
        # Read the header
        header = file.readline().strip()
        columns = header.split(',')

        # Identify relevant column indices
        departure_delay_index = columns.index("DEPARTURE_DELAY")
        tail_number_index = columns.index("TAIL_NUMBER")

        content = file.readlines()

    modified_lines = []
    count = 0

    for line in content:
        count += 1
        line = line.strip()
        modified_lines.append(line.replace(',', ' '))  # Replace commas with spaces
        
        # Apply modifications every 10th line
        if count % 10 == 0:
            # Split line into fields for modification
            fields = line.split(',')
            
            # Action 1: Duplicate the line
            if count % 30 == 10:
                modified_lines.append(line.replace(',', ' '))
            
            # Action 2: Duplicate and set DEPARTURE_DELAY > 1000
            elif count % 30 == 20:
                fields[departure_delay_index] = '1001'
                modified_lines.append(' '.join(fields))
            
            # Action 3: Duplicate and set TAIL_NUMBER to empty
            elif count % 30 == 0:
                fields[tail_number_index] = ''
                modified_lines.append(' '.join(fields))
    
    # Write the modified content to the output file
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(modified_lines))

    print(f"File '{output_file_path}' successfully written with modifications.")
except Exception as e:
    print(f"Error: {e}")
