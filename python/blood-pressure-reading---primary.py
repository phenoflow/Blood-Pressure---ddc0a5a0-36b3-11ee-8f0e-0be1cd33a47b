# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2023.

import sys, csv, re

codes = [{"code":"246..00","system":"readv2"},{"code":"246..11","system":"readv2"},{"code":"2461","system":"readv2"},{"code":"2462","system":"readv2"},{"code":"2467","system":"readv2"},{"code":"2468","system":"readv2"},{"code":"246J.00","system":"readv2"},{"code":"246Z.00","system":"readv2"},{"code":"246g.00","system":"readv2"},{"code":"6623","system":"readv2"},{"code":"R1y3.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('blood-pressure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["blood-pressure-reading---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["blood-pressure-reading---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["blood-pressure-reading---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
