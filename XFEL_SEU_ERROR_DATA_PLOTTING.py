###-------------------------------------------------------------------------#####
#-----------------------------################----------------------------------#

# Name    : Md Rahat Ibna Kamal
# Project : XFEL ERROR DATA ANALYSIS
# Date    : 10th OCT,2019
# File Des: Analysing all data from master csv (Total SEU Error log). Compare it with radiation data and plotting figure
###-------------------------------------------------------------------------#####
#-----------------------------################----------------------------------#


import csv
import datetime
import os
import matplotlib.pyplot as plt
import pandas  as pd
import numpy as np
from statistics import mean



def trendline(xd, yd, order=2, c='r', alpha=1, Rval=False):

    #Calculate trendline
    coeffs = np.polyfit(xd, yd, order)

    intercept = coeffs[-1]
    slope = coeffs[-2]
    power = coeffs[0] if order == 2 else 0

    minxd = np.min(xd)
    maxxd = np.max(xd)

    xl = np.array([minxd, maxxd])
    yl = power * xl ** 2 + slope * xl + intercept

    #Plot trendline
    plt.plot(xl, yl, c, alpha=alpha)

    #Calculate R Squared
    p = np.poly1d(coeffs)

    ybar = np.sum(yd) / len(yd)
    ssreg = np.sum((p(xd) - ybar) ** 2)
    sstot = np.sum((yd - ybar) ** 2)
    Rsqr = ssreg / sstot

    if not Rval:
        #Plot R^2 value
        plt.text(0.8 * maxxd + 0.2 * minxd, 0.8 * np.max(yd) + 0.2 * np.min(yd),
                 '$R^2 = %0.2f$' % Rsqr)
    else:
        #Return the R^2 value:
        return Rsqr
def csv_file_write(host,board,crcErr,crcErrCnt,eccErrCnt,Error_info):

    date_in=datetime.datetime.now();
    file_name=str(date_in.day)+'-'+str(date_in.month)+'-'+str(date_in.year)+".csv"
    file_exists = os.path.isfile(file_name)
    with open(file_name,'a') as csvfile:
        header = ['DATE','TIME','HOST','BOARD','CRC', 'CRC_CNT', 'ECC_CNT','ERROR_INFO']
        filewriter=csv.DictWriter(csvfile,fieldnames=header,lineterminator=os.linesep);
        if not file_exists:
             filewriter.writeheader()
        filewriter.writerow({'DATE': str(date_in.day)+'-'+str(date_in.month)+'-'+str(date_in.year) ,'TIME':str(date_in.minute)+'-'+str(date_in.second)+'-'+str(date_in.hour),'HOST':host,'BOARD':board,'CRC':crcErr,'CRC_CNT':crcErrCnt,'ECC_CNT':eccErrCnt,'ERROR_INFO':Error_info})
def ECC_csv_Read_file (file_name):
    if '\0' in open(file_name).read():
        print ("you have null bytes in your input file")
    else:
        print ("you don't")
    with open(file_name,mode='r') as csv_file :
        csv_reader= csv.DictReader(x.replace('\0', '') for x in csv_file)


        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')

                line_count += 1
            #print(f'\t{row[""]} works in the {row["hostname"]} department, and was born in {row["board"]}.')
            line_count += 1
            hostname.append(row["hostname"])
            timestamp.append(int(row["timestamp"]))
            board.append(row["board"])
            crc.append(row["CRC"])
            crcCnt.append(int(row["CrcCnt"]))
            eccCnt.append(row["EccCnt"])
            Syndrome.append('{:013b}'.format(int(row["SynDrome"])))
            #print('{:013b}'.format(int(row[" SynDrome"])))
            FAR.append(row["FAR"])
            Synword.append(row["SynWord"])
            Synbit.append(row["SynBit"])
            #Date_ECC.append(row[" Date"])
            #print(row["hostname"])
        print(f'Processed {line_count} lines.')
def CAL_DOSE(cpm):

    cpmcal=1/210
    if cpm<600:
        doserate=cpmcal*(cpm+np.exp((cpm+15)/110)-np.exp(15/110))
    else:

        doserate=600
    return doserate

def DOSE_csv_Read_file (file_name):
    if '\0' in open(file_name).read():
        print ("you have null bytes in your input file")
    else:
        print ("you don't")
    with open(file_name,mode='r') as csv_file :
        csv_reader= csv.DictReader(x.replace('\0', '') for x in csv_file)


        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')

                line_count += 1
            #print(f'\t{row[""]} works in the {row["hostname"]} department, and was born in {row["board"]}.')
            line_count += 1
            xfelcpullah1i1.append(float(row["xfelcpullah1i1"]))
            xfelcpulla2m.append(float(row["xfelcpulla2m"]))
            xfelcpulla3m.append(float(row["xfelcpulla3m"]))
            xfelcpulla4m.append(float(row["xfelcpulla4m"]))
            xfelcpulla5m.append(float(row["xfelcpulla5m"]))
            xfelcpulla6m.append(float(row["xfelcpulla6m"]))
            xfelcpulla7m.append(float(row["xfelcpulla7m"]))
            xfelcpulla8m.append(float(row["xfelcpulla8m"]))
            xfelcpulla9m.append(float(row["xfelcpulla9m"]))
            xfelcpulla10m.append(float(row["xfelcpulla10m"]))
            xfelcpulla11m.append(float(row["xfelcpulla11m"]))
            xfelcpulla12m.append(float(row["xfelcpulla12m"]))
            xfelcpulla13m.append(float(row["xfelcpulla13m"]))
            xfelcpulla14m.append(float(row["xfelcpulla14m"]))
            xfelcpulla15m.append(float(row["xfelcpulla15m"]))
            xfelcpulla16m.append(float(row["xfelcpulla16m"]))
            xfelcpulla17m.append(float(row["xfelcpulla17m"]))
            xfelcpulla18m.append(float(row["xfelcpulla18m"]))
            xfelcpulla19m.append(float(row["xfelcpulla19m"]))
            xfelcpulla20m.append(float(row["xfelcpulla20m"]))
            xfelcpulla21m.append(float(row["xfelcpulla21m"]))
            xfelcpulla22m.append(float(row["xfelcpulla22m"]))
            xfelcpulla23m.append(float(row["xfelcpulla23m"]))
            xfelcpulla24m.append(float(row["xfelcpulla24m"]))
            xfelcpulla25m.append(float(row["xfelcpulla25m"]))
            xfelcpulla26m.append(float(row["xfelcpulla26m"]))
            xfelcpulla2s.append(float(row["xfelcpulla2s"]))
            xfelcpulla3s.append(float(row["xfelcpulla3s"]))
            xfelcpulla4s.append(float(row["xfelcpulla4s"]))
            xfelcpulla5s.append(float(row["xfelcpulla5s"]))
            xfelcpulla6s.append(float(row["xfelcpulla6s"]))
            xfelcpulla7s.append(float(row["xfelcpulla7s"]))
            xfelcpulla8s.append(float(row["xfelcpulla8s"]))
            xfelcpulla9s.append(float(row["xfelcpulla9s"]))
            xfelcpulla10s.append(float(row["xfelcpulla10s"]))
            xfelcpulla11s.append(float(row["xfelcpulla11s"]))
            xfelcpulla12s.append(float(row["xfelcpulla12s"]))
            xfelcpulla13s.append(float(row["xfelcpulla13s"]))
            xfelcpulla14s.append(float(row["xfelcpulla14s"]))
            xfelcpulla15s.append(float(row["xfelcpulla15s"]))
            xfelcpulla16s.append(float(row["xfelcpulla16s"]))
            xfelcpulla17s.append(float(row["xfelcpulla17s"]))
            xfelcpulla18s.append(float(row["xfelcpulla18s"]))
            xfelcpulla19s.append(float(row["xfelcpulla19s"]))
            xfelcpulla20s.append(float(row["xfelcpulla20s"]))
            xfelcpulla21s.append(float(row["xfelcpulla21s"]))
            xfelcpulla22s.append(float(row["xfelcpulla22s"]))
            xfelcpulla23s.append(float(row["xfelcpulla23s"]))
            xfelcpulla24s.append(float(row["xfelcpulla24s"]))
            xfelcpulla25s.append(float(row["xfelcpulla25s"]))
            xfelcpulla26s.append(float(row["xfelcpulla26s"]))
            Date.append(row["Date"])


            #print(row["hostname"])
        print(f'Processed {line_count} lines.')
host_name=["xfelcpullah1i1","xfelcpulla2m" ,"xfelcpulla3m","xfelcpulla4m","xfelcpulla5m","xfelcpulla6m","xfelcpulla7m","xfelcpulla8m","xfelcpulla9m","xfelcpulla10m","xfelcpulla11m","xfelcpulla12m","xfelcpulla13m","xfelcpulla14m","xfelcpulla15m","xfelcpulla16m","xfelcpulla17m","xfelcpulla18m","xfelcpulla19m","xfelcpulla20m","xfelcpulla21m","xfelcpulla22m","xfelcpulla23m","xfelcpulla24m","xfelcpulla25m","xfelcpulla26m","xfelcpulla2s","xfelcpulla3s","xfelcpulla4s","xfelcpulla5s","xfelcpulla6s","xfelcpulla7s","xfelcpulla8s","xfelcpulla9s","xfelcpulla10s","xfelcpulla11s","xfelcpulla12s","xfelcpulla13s","xfelcpulla14s","xfelcpulla15s","xfelcpulla16s","xfelcpulla17s","xfelcpulla18s","xfelcpulla19s","xfelcpulla20s","xfelcpulla21s","xfelcpulla22s","xfelcpulla23s","xfelcpulla24s","xfelcpulla25s","xfelcpulla26s"]
host_name_sum=["1i1","a2m" ,"a3m","a4m","a5m","a6m","a7m","a8m","a9m","a10m","a11m","a12m","a13m","a14m","a15m","a16m","a17m","a18m","a19m","a20m","a21m","a22m","a23m","a24m","a25m","a26m","a2s","a3s","a4s","a5s","a6s","a7s","a8s","a9s","a10s","a11s","a12s","a13s","a14s","a15s","a16s","a17s","a18s","a19s","a20s","a21s","a22s","a23s","a24s","a25s","a26s"]
board_name=[" SIS7"," SIS8"," SIS9"," SIS10"," SIS11"," SIS12"]
dot=["--","--","--","--","-","--"]
hostname=list()
timestamp=list()
board=list()
crc=list()
crcCnt=list()
eccCnt=list()
Syndrome=list()
FAR=list()
Synword=list()
Synbit=list()
Date_ECC=list()

xfelcpullah1i1=list()
xfelcpulla2m=list()
xfelcpulla3m=list()
xfelcpulla4m=list()
xfelcpulla5m=list()
xfelcpulla6m=list()
xfelcpulla7m=list()
xfelcpulla8m=list()
xfelcpulla9m=list()
xfelcpulla10m=list()
xfelcpulla11m=list()
xfelcpulla12m=list()
xfelcpulla13m=list()
xfelcpulla14m=list()
xfelcpulla15m=list()
xfelcpulla16m=list()
xfelcpulla17m=list()
xfelcpulla18m=list()
xfelcpulla19m=list()
xfelcpulla20m=list()
xfelcpulla21m=list()
xfelcpulla22m=list()
xfelcpulla23m=list()
xfelcpulla24m=list()
xfelcpulla25m=list()
xfelcpulla26m=list()
xfelcpulla2s=list()
xfelcpulla3s=list()
xfelcpulla4s=list()
xfelcpulla5s=list()
xfelcpulla6s=list()
xfelcpulla7s=list()
xfelcpulla8s=list()
xfelcpulla9s=list()
xfelcpulla10s=list()
xfelcpulla11s=list()
xfelcpulla12s=list()
xfelcpulla13s=list()
xfelcpulla14s=list()
xfelcpulla15s=list()
xfelcpulla16s=list()
xfelcpulla17s=list()
xfelcpulla18s=list()
xfelcpulla19s=list()
xfelcpulla20s=list()
xfelcpulla21s=list()
xfelcpulla22s=list()
xfelcpulla23s=list()
xfelcpulla24s=list()
xfelcpulla25s=list()
xfelcpulla26s=list()
Date=list()
DOSE_csv_Read_file('Dose_rate_09_07_to_10_10.csv') ##Dose_rate_27_08_to_10_10.csv Dose_rate_09_07_to_20_08.csv
print(len(xfelcpulla3m))
print(sum(xfelcpullah1i1))
dose_sum=[sum(xfelcpullah1i1),sum(xfelcpulla2m),sum(xfelcpulla2s),sum(xfelcpulla3m),sum(xfelcpulla3s),sum(xfelcpulla4m),sum(xfelcpulla4s),sum(xfelcpulla5m),sum(xfelcpulla5s),sum(xfelcpulla6m),sum(xfelcpulla6s),sum(xfelcpulla7m),sum(xfelcpulla7s),sum(xfelcpulla8m),sum(xfelcpulla8s),sum(xfelcpulla9m),sum(xfelcpulla9s),sum(xfelcpulla10m),sum(xfelcpulla10s),sum(xfelcpulla11m),sum(xfelcpulla11s),sum(xfelcpulla12m),sum(xfelcpulla12s),sum(xfelcpulla13m),sum(xfelcpulla13s),sum(xfelcpulla14m),sum(xfelcpulla14s),sum(xfelcpulla15m),sum(xfelcpulla15s),sum(xfelcpulla16m),sum(xfelcpulla16s),sum(xfelcpulla17m),sum(xfelcpulla17s),sum(xfelcpulla18m),sum(xfelcpulla18s),sum(xfelcpulla19m),sum(xfelcpulla19s),sum(xfelcpulla20m),sum(xfelcpulla20s),sum(xfelcpulla21m),sum(xfelcpulla21s),sum(xfelcpulla22m),sum(xfelcpulla22s),sum(xfelcpulla23m),sum(xfelcpulla23s),sum(xfelcpulla24m),sum(xfelcpulla24s),sum(xfelcpulla25m),sum(xfelcpulla25s),sum(xfelcpulla26m),sum(xfelcpulla26s)]

no_error=0
single_bit=0
multiple_bit=0
parity_bit=0
double_bit=0
ECC_csv_Read_file('ecc_2019-07-09_to_2019-10-10.csv') ###  ecc_2019-08-27_to_2019-10-10.csv ecc_all_20_08_2019
print("length of syndrome  : ",len(Syndrome))
print("length od ecc       : ", len(eccCnt))
hostname_array = np.asarray(hostname)
board_array = np.asarray(board)
eccCnt_array=np.asarray(eccCnt)
timestamp_array=np.asarray(timestamp)
syndrome_array=np.asarray(Syndrome)




#syndrome_sum_list=list()
#for i in range (len(Syndrome)):
 #   print(Syndrome[i])
  #  print(int(Syndrome[i],2))
   # if (int(Syndrome[i],2)!= 0):
    #    syndrome_sum_list.append(int(Syndrome[i],2))

    #print(Syndrome[i][0])
    #print(Syndrome[i][1])
    #if(Syndrome[i][0]=='{0:01b}'.format(0) and Syndrome[i][1:13]=='{0:012b}'.format(0) ):
     #   no_error=no_error+1
      #  print("no_error")
    #elif(Syndrome[i][0]=='{0:01b}'.format(1) and Syndrome[i][1:13]!='{0:012b}'.format(0) ):
     #   single_bit=single_bit+1
      #  print("single bit")
    #elif(Syndrome[i][0]=='{0:01b}'.format(1) and Syndrome[i][1:13]=='{0:012b}'.format(0) ):
     #   parity_bit=parity_bit+1
      #  print("parity_bit")
    #else:
     #   multiple_bit=multiple_bit+1
      #  print(Syndrome[i])
       # print(int(Syndrome[i],2))
        #print("multiple")
#print("Final NO Error")
#print(no_error)
#print("Final Single bit: ")
#print(single_bit)
#print("Multibit Error")
#print(multiple_bit)
#print("Parity bit")
#print(parity_bit)



#Date_ECC=[i[:-8].strip() for i in Date_ECC]
#print (len(Date_ECC))
print(len(timestamp))
print(len(hostname))
print(board[2])
print(type(timestamp_array[2]))
print(eccCnt_array[1])
Total_error=list()
final_Board=list()
warning_list=list()
Total_single_bit_error=list()
Total_no_error=list()
Total_multibit_error=list()
Total_parity_bit_error=list()
Current_board_name=list()
Current_station_name= list()
Total_double_bit=list()

for host_CNT in range(len(host_name)):
    print(host_name[host_CNT])


    sum=0
    for board_CNT in range(len(board_name)):
        print(board_name[board_CNT])
        Station_board_CRC=list()
        syndrome_list=list()
        Total_time=list()
        for x in range (len(hostname_array)):

            if board[x]==board_name[board_CNT] and hostname[x]==host_name[host_CNT]:
                Station_board_CRC.append(int(eccCnt_array[x]))
                Total_time.append((int(timestamp_array[x])-int(timestamp_array[1]))/(60*60));
                syndrome_list.append(syndrome_array[x])
        Station_board_CRC_array=np.asarray(Station_board_CRC)
        Total_time_array=np.asarray(Total_time)
        syndrome_new_array=np.asarray(syndrome_list)
        print("Inside the loop for checking unexpected value")
        print("checking value for list ", Station_board_CRC)
        for y in range (len(Station_board_CRC)):
            if(int(Station_board_CRC[y])==4294967294):
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Station board CRC value found", Station_board_CRC[y])
                Station_board_CRC[y]=0;





        if (int(max(Station_board_CRC))-(int(Station_board_CRC_array[0]))!= 0):
            #print("--*----***-*****************")
            #print(int(Station_board_CRC_array[len(Station_board_CRC)-1])-(int(Station_board_CRC_array[0])))
            #print(Station_board_CRC)
            if host_CNT<26 :
                plt.figure(host_CNT)
                plt.subplot(2,1,1)
                plt.title("STATION : "+host_name[host_CNT])
                plt.xlabel("TIME STAMP(Hour)")
                plt.ylabel("ECC ERROR COUNT")
                plt.yscale("linear")

                if (max(Station_board_CRC)>= 4294967295):
                    plt.text(int(max(Total_time))/2,5,r"Board Failure :"+host_name[host_CNT]+'_'+board_name[board_CNT],  horizontalalignment='center', verticalalignment='top',fontsize=8,color='r')
                    warning_list.append(("Board Failure :"+host_name[host_CNT]+'_'+board_name[board_CNT]))
                    for n, i in enumerate(Station_board_CRC):
                        if i == 4294967295:
                            Station_board_CRC[n] = 0
                            print(Station_board_CRC[n])

                print(Station_board_CRC)
                plt.plot(Total_time,Station_board_CRC,dot[board_CNT],label=host_name[host_CNT]+'_'+board_name[board_CNT])
                plt.legend()
                plt.grid(True)


                fig1 = plt.figure(3000+host_CNT)

                ax=fig1.add_subplot(211, label="1")
                ax2=fig1.add_subplot(211, label="2", frame_on=False)


                ax.plot(Total_time,Station_board_CRC,dot[board_CNT],label=host_name[host_CNT]+'_'+board_name[board_CNT])
                ax.legend(loc='best', shadow=True, fontsize=6)



                ax.set_title("STATION : "+host_name[host_CNT])
                ax.set_title("STATION : "+ host_name[host_CNT])
                ax.set_xlabel('ECC Eroor', color="C0")
                ax.set_ylabel('Time (hour)[9th july to 10th oct]', color="C0")
                ax.tick_params(axis='x', colors="C0")
                ax.tick_params(axis='y', colors="C0")


                ax2.plot(Date, eval(host_name[host_CNT]), color='k')
                ax2.xaxis.tick_top()
                ax2.yaxis.tick_right()
                ax2.set_xticklabels(Date,fontsize=6,rotation=90)
                ax2.set_xlabel('Date [9th july to 10th oct]', color="C1")
                ax2.set_ylabel('Detection Rate (cpm)', color="C1")
                ax2.xaxis.set_label_position('top')
                ax2.yaxis.set_label_position('right')
                ax2.tick_params(axis='x', colors="C1")
                ax2.tick_params(axis='y', colors="C1")


                #ax = fig1.add_subplot(111)
                #ax.plot(Total_time,Station_board_CRC,dot[board_CNT],label=host_name[host_CNT]+'_'+board_name[board_CNT])

                #ax2 = ax.twinx()

                #ax2.plot(Date, eval(host_name[host_CNT]), '-r', label = 'temp')
                #ax.legend(loc=0)
                #ax.grid()
                #ax.set_xlabel("Time (h)")
                #ax.set_ylabel(r"Radiation ($MJ\,m^{-2}\,d^{-1}$)")
                #ax2.set_ylabel(r"Temperature ($^\circ$C)")




            if host_CNT>=26:
                plt.figure(host_CNT-25)
                plt.subplot(2,1,2)
                plt.title("STATION : "+host_name[host_CNT])
                plt.xlabel("TIME STAMP (Hour)")
                plt.ylabel("ECC ERROR COUNT")
                plt.yscale("linear")

                if (max(Station_board_CRC)>= 4294967295):
                    plt.text(int(max(Total_time))/2,5,r"Board Failure :"+host_name[host_CNT]+'_'+board_name[board_CNT],  horizontalalignment='center', verticalalignment='top',fontsize=8,color='r')
                    warning_list.append(("Board Failure :"+host_name[host_CNT]+'_'+board_name[board_CNT]))
                    for n, i in enumerate(Station_board_CRC):
                        if i == 4294967295:
                            Station_board_CRC[n] = 0
                            print(Station_board_CRC[n])


                plt.plot(Total_time,Station_board_CRC,dot[board_CNT],label=host_name[host_CNT]+'_'+board_name[board_CNT])
                plt.legend()
                plt.grid(True)

                fig1 = plt.figure(3000+host_CNT-25)

                ax=fig1.add_subplot(212, label="1")
                ax2=fig1.add_subplot(212, label="2", frame_on=False)

                ax.plot(Total_time,Station_board_CRC,dot[board_CNT],label=host_name[host_CNT]+'_'+board_name[board_CNT])
                ax.legend(loc='best', shadow=True, fontsize=6)

                # Put a nicer background color on the legend.


                ax.set_title("STATION : "+host_name[host_CNT])
                ax.set_xlabel('ECC Eroor', color="C0")
                ax.set_ylabel('Time (hour)[9th july to 10th oct]', color="C0")
                ax.tick_params(axis='x', colors="C0")
                ax.tick_params(axis='y', colors="C0")


                ax2.plot(Date, eval(host_name[host_CNT]), color='k')
                ax2.xaxis.tick_top()
                ax2.yaxis.tick_right()
                ax2.set_xticklabels(Date,fontsize=6,rotation=90)
                ax2.set_xlabel('Date [9th july to 10th oct]', color="C1")
                ax2.set_ylabel('Detection Rate (cpm)', color="C1")
                ax2.xaxis.set_label_position('top')
                ax2.yaxis.set_label_position('right')
                ax2.tick_params(axis='x', colors="C1")
                ax2.tick_params(axis='y', colors="C1")

        x='{0:013b}'.format(0)
        for i in range (len(syndrome_list)):
            y=syndrome_list[i]
            if (x!=y):
                if(syndrome_list[i][0]=='{0:01b}'.format(0) and syndrome_list[i][1:13]=='{0:012b}'.format(0) ):
                    no_error=no_error+1
                    print("no_error")
                elif(syndrome_list[i][0]=='{0:01b}'.format(1) and syndrome_list[i][1:13]!='{0:012b}'.format(0) ):
                    single_bit=single_bit+1
                    x=syndrome_list[i]
                    print("single bit")
                elif(syndrome_list[i][0]=='{0:01b}'.format(0) and syndrome_list[i][1:13]!='{0:012b}'.format(0) ):
                    double_bit=double_bit+1
                    x=syndrome_list[i]
                    print("single bit")

                elif(syndrome_list[i][0]=='{0:01b}'.format(1) and syndrome_list[i][1:13]=='{0:012b}'.format(0) ):
                    parity_bit=parity_bit+1
                    print("parity_bit")
                else:
                    multiple_bit=multiple_bit+1
                    print(Syndrome[i])
                    print(int(Syndrome[i],2))
                    print("multiple")
            else:
                no_error=no_error+1

        Total_double_bit.append(double_bit)
        Total_single_bit_error.append(single_bit)
        Total_multibit_error.append(multiple_bit)
        Total_no_error.append(no_error)
        Total_parity_bit_error.append(parity_bit)
        Current_station_name.append(host_name[host_CNT])
        print(Total_single_bit_error)
        print(Total_multibit_error)
        print(Total_parity_bit_error)
        print(Total_no_error)
        Current_board_name.append(board_name[board_CNT])
        sum=sum+max(Station_board_CRC)
        print("sum is : {0}",sum)
        no_error=0
        single_bit=0
        multiple_bit=0
        parity_bit=0
    Total_error.append(sum)
    final_Board.append(host_name[host_CNT])

for z in range (len(Current_board_name)):
    print("Station Namme {0} , Board Name {1}, Single Bit_error = {2}, Multiple bit Error = {3} Parity bit Error = {4} ,No Error = {5}, Double bit ={6}".format(Current_station_name[z],Current_board_name[z],Total_single_bit_error[z],Total_multibit_error[z],Total_parity_bit_error[z],Total_no_error[z],Total_double_bit[z]))
print(Total_error)
print(final_Board)
Total_error_x=list()
final_Board_x=list()
for j in range(0,51):
    Total_error_x.append(j)
    final_Board_x.append("Empty")
for i in range (0,26):

    if i==0:
        Total_error_x[i]=Total_error[i]
        final_Board_x[i]=final_Board[i]
    if  i <25 :
        Total_error_x[2*i+1]=Total_error[i+1]
        final_Board_x[2*i+1]=final_Board[i+1]

    if 0<i<26 :
        Total_error_x[2*i]=Total_error[25+i]
        final_Board_x[2*i]=final_Board[25+i]


print(Total_error_x)

print(final_Board_x)
print(len(Total_error))
print(len(Total_error_x))
Total_error_x = [i/2 for i in Total_error_x]
print("Total Error List : ",Total_error_x)

sum_total_error_x=sum(Total_error_x)
print("Total Error sum : ",sum_total_error_x)

mean_per_station= mean(Total_error_x)
print("Average per station : " , mean_per_station)
print("Total time: ",Total_time)
mean_per_day=sum_total_error_x/(max(Total_time)/24)
print("Average_per_day",mean_per_day)
mean_per_station_per_day=mean_per_station/(max(Total_time)/24)
print ("Average_per_day_per_station",mean_per_station_per_day)
print(len(Total_error_x))
plt.figure(2000)
plt.title("Station vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Station")
plt.ylabel("Detection Rate Of ionization Incident(cpm) ")
plt.yscale("linear")
plt.xticks(fontsize=6, rotation=90)
plt.bar(final_Board_x,dose_sum,color='r')
plt.grid(True)

plt.figure(2001)
plt.title("xfelcpulla19s: Time vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Date")
plt.ylabel("Detection Rate (cpm)")
plt.xticks(fontsize=6, rotation=90)
plt.bar(Date,xfelcpulla19s,color='y')
plt.grid(True)

plt.figure(2002)
plt.title("xfelcpulla11m: Time vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Date")
plt.ylabel("Detection Rate (cpm)")
plt.xticks(fontsize=6, rotation=90)
plt.bar(Date,xfelcpulla11m,color='y')
plt.grid(True)

plt.figure(2003)
plt.title("xfelcpulla12m: Time vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Date")
plt.ylabel("Detection Rate (cpm)")
plt.xticks(fontsize=6, rotation=90)
plt.bar(Date,xfelcpulla12m,color='y')
plt.grid(True)


plt.figure(2004)
plt.title("xfelcpulla13s: Time vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Date")
plt.ylabel("Detection Rate (cpm)")
plt.xticks(fontsize=6, rotation=90)
plt.bar(Date,xfelcpulla13s,color='y')
plt.grid(True)




plt.figure(2005)
plt.title("xfelcpulla16m: Time vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Date")
plt.ylabel("Detection Rate (cpm)")
plt.xticks(fontsize=6, rotation=90)
plt.bar(Date,xfelcpulla16m,color='y')
plt.grid(True)

plt.figure(2006)
plt.title("xfelcpulla16s: Time vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Date")
plt.ylabel("Detection Rate (cpm)")
plt.xticks(fontsize=6, rotation=90)
plt.bar(Date,xfelcpulla16s,color='y')
plt.grid(True)

plt.figure(2007)
plt.title("xfelcpulla23m: Time vs Detection rate  [9th july to 10th oct]")
plt.xlabel("Date")
plt.ylabel("Detection Rate (cpm)")
plt.xticks(fontsize=6, rotation=90)
plt.bar(Date,xfelcpulla23m,color='y')
plt.grid(True)

plt.figure(1000)
plt.title("Station vs Error [9th july to 10th oct]")
plt.xlabel("Station")
plt.ylabel("Total ECC Error Count For All Board ")
plt.yscale("linear")
plt.xticks(fontsize=6, rotation=90)
print(final_Board)
print(Total_error)
print(max(Station_board_CRC))
#for n, i in enumerate(warning_list):
#   plt.text('xfelcpulla26m',10, warning_list[i],  horizontalalignment='center', verticalalignment='top',fontsize=8,color='r')
plt.bar(final_Board_x,Total_error_x)
plt.grid(True)

plt.xlabel("Station")



fig = plt.figure(1001) # Create matplotlib figure
plt.title("Station vs Error [9th july to 10th oct]")
plt.yscale("linear")
plt.xticks(fontsize='large', rotation=90, fontweight='bold')

ax1 = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax1.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.4
df = pd.DataFrame({'Total_ECC_Error_Count': Total_error_x,'Detection_Rate': dose_sum}, index=final_Board_x)

df.Total_ECC_Error_Count.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)
ax2.set_ylabel('Total ECC Error Count For All Board')
ax2.legend(loc=1)
df.Detection_Rate.plot(kind='bar', color='red', ax=ax1, width=width, position=1)
ax1.set_ylabel('Detection Rate (cpm)')

ax1.legend(loc=0)

ax1.grid()


print(final_Board_x)
print(dose_sum)
print(Total_error_x)
Total_error_x.remove(float(50))
dose_sum.remove(float(204391.0))
plt.figure(1002)


#x_new = np.linspace(Total_error_x[0], Total_error_x[-1],50)
#y_new = prediction(x_new)


#x = symbols("x")
#poly = sum(S("{:6.2f}".format(v))*x**i for i, v in enumerate(co_eff[::-1]))
#eq_latex = sympy.printing.latex(poly)

plt.scatter(Total_error_x,dose_sum)
#plt.plot(x_new,y_new,label="${}$".format(eq_latex))
#plt.figtext(co_eff)
#trendline(Total_error_x,dose_sum)
co_eff=np.polyfit(Total_error_x,dose_sum,5)
print(co_eff)
prediction = np.poly1d(co_eff)
trendline(Total_error_x,dose_sum)

plt.show()






