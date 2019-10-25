###-------------------------------------------------------------------------#####
#-----------------------------################----------------------------------#

# Name    : Md Rahat Ibna Kamal
# Project : XFEL ERROR DATA ANALYSIS
# Date    : 30th Sept,2019
# File Des: Joing Multiple csv file. Each csv file represents data for each day.
###-------------------------------------------------------------------------#####
#-----------------------------################----------------------------------#


import csv
# name of all csv file  for each day
file_name=['2019-07-09_ecc.csv',
           '2019-07-10_ecc.csv',
           '2019-07-11_ecc.csv',
           '2019-07-12_ecc.csv',
           '2019-07-13_ecc.csv',
           '2019-07-14_ecc.csv',
           '2019-07-15_ecc.csv',
           '2019-07-16_ecc.csv',
           '2019-07-17_ecc.csv',
           '2019-07-18_ecc.csv',
           '2019-07-19_ecc.csv',
           '2019-07-20_ecc.csv',
           '2019-07-21_ecc.csv',
           '2019-07-22_ecc.csv',
           '2019-07-23_ecc.csv',
           '2019-07-24_ecc.csv',
           '2019-07-25_ecc.csv',
           '2019-07-26_ecc.csv',
           '2019-07-27_ecc.csv',
           '2019-07-28_ecc.csv',
           '2019-07-29_ecc.csv',
           '2019-07-31_ecc.csv',
           '2019-08-01_ecc.csv',
           '2019-08-02_ecc.csv',
           '2019-08-03_ecc.csv',
           '2019-08-04_ecc.csv',
           '2019-08-05_ecc.csv',
           '2019-08-06_ecc.csv',
           '2019-08-07_ecc.csv',
           '2019-08-08_ecc.csv',
           '2019-08-09_ecc.csv',
           '2019-08-10_ecc.csv',
           '2019-08-11_ecc.csv',
           '2019-08-12_ecc.csv',
           '2019-08-13_ecc.csv',
           '2019-08-14_ecc.csv',
           '2019-08-15_ecc.csv',
           '2019-08-16_ecc.csv',
           '2019-08-17_ecc.csv',
           '2019-08-18_ecc.csv',
           '2019-08-19_ecc.csv',
           '2019-08-20_ecc.csv',
           '2019-08-21_ecc.csv',
           '2019-08-22_ecc.csv',
           '2019-08-23_ecc.csv',
           '2019-08-24_ecc.csv',
           '2019-08-25_ecc.csv',
           '2019-08-26_ecc.csv',
           '2019-08-27_ecc.csv',
           '2019-08-28_ecc.csv',
           '2019-08-29_ecc.csv',
           '2019-08-30_ecc.csv',
           '2019-09-01_ecc.csv',
           '2019-09-02_ecc.csv',
           '2019-09-03_ecc.csv',
           '2019-09-04_ecc.csv',
           '2019-09-05_ecc.csv',
           '2019-09-06_ecc.csv',
           '2019-09-07_ecc.csv',
           '2019-09-08_ecc.csv',
           '2019-09-09_ecc.csv',
           '2019-09-10_ecc.csv',
           '2019-09-11_ecc.csv',
           '2019-09-12_ecc.csv',
           '2019-09-13_ecc.csv',
           '2019-09-14_ecc.csv',
           '2019-09-15_ecc.csv',
           '2019-09-16_ecc.csv',
           '2019-09-17_ecc.csv',
           '2019-09-18_ecc.csv',
           '2019-09-19_ecc.csv',
           '2019-09-20_ecc.csv',
           '2019-09-21_ecc.csv',
           '2019-09-22_ecc.csv',
           '2019-09-23_ecc.csv',
           '2019-09-24_ecc.csv',
           '2019-09-25_ecc.csv',
           '2019-09-26_ecc.csv',
           '2019-09-27_ecc.csv',
           '2019-09-28_ecc.csv',
           '2019-09-29_ecc.csv',
           '2019-09-30_ecc.csv',
           '2019-10-01_ecc.csv',
           '2019-10-02_ecc.csv',
           '2019-10-03_ecc.csv',
           '2019-10-04_ecc.csv',
           '2019-10-05_ecc.csv',
           '2019-10-06_ecc.csv',
           '2019-10-07_ecc.csv',
           '2019-10-08_ecc.csv',
           '2019-10-09_ecc.csv',
           '2019-10-10_ecc.csv']

### making new csv file and writting all data from each csv sequentially..

with open('ecc_2019-07-09_to_2019-10-10.csv', 'w',newline="") as csvfile:    ## Name of new csv file (Master CSV) which is created

    fieldnames = ['hostname', 'timestamp', 'board', 'CRC', 'CrcCnt','EccCnt,ECC', 'EccSingleCnt', 'FAR', 'SynBit', 'SynDrome', 'SynWord']   ## Name of Row
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (len(file_name)):                                        ## Making loop to take each file to read and write them again in master csv file
        with open(file_name[i]) as csv_file:
            print(file_name[i])
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    writer.writerow({'hostname':row[0], 'timestamp':row[1], 'board':row[2], 'CRC':row[3], 'CrcCnt':row[4],'EccCnt,ECC':row[5], 'EccSingleCnt':row[6], 'FAR':row[7], 'SynBit':row[8], 'SynDrome':row[9], 'SynWord':row[10]})
                    line_count += 1

