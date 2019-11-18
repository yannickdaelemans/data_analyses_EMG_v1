# imports
import matplotlib.pyplot as plt
from bokeh.layouts import column
from bokeh.plotting import figure, show


# start of code

# opening the files
f = open("01/2_raw_data_13-13_22.03.16.txt", "r")
f_all = open("allData.txt", "w")
f_0 = open("0_Data.txt", "w")
f_1 = open("1_Data.txt", "w")
f_2 = open("2_Data.txt", "w")
f_3 = open("3_Data.txt", "w")
f_4 = open("4_Data.txt", "w")
f_5 = open("5_Data.txt", "w")
f_6 = open("6_Data.txt", "w")
f_7 = open("7_Data.txt", "w")

# reading file
content = f.readlines()

# making all the necessary lists (10)
time = []
emg1_data = []
emg2_data = []
emg3_data = []
emg4_data = []
emg5_data = []
emg6_data = []
emg7_data = []
emg8_data = []
label = []
# list of all the lists for easier future programming
list_of_list = [time, emg1_data, emg2_data, emg3_data, emg4_data, emg5_data, emg6_data, emg7_data, emg8_data, label]
# list of the averages
averages = []
#list of files to write into
files_list = [f_0, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_all]


#################################################################
# The code below will adjust data in the files, to make them    #
# better suitable for the use in the machine learning algo.     #
# Mainly we normalise the data (so to get it all between -1 and #
# 1)                                                            #
#################################################################
def getAverage(int_label):
    average = 0
    count = 0
    y = 0
    print "the averages for ", int_label, "are: "
    for y in range(len(list_of_list)-1):
        if y != 0 and y != len(list_of_list)-1:
            for x in range(len(label)-1):
                if int(label[x]) == int_label:
                    average = average + list_of_list[y][x]
                    count = count + 1
            average = average /count
            print average
            averages.append(average)
    print " "
    print averages

def normalise(emg_data):
    x = 0
    maximum = float(max(emg_data))
    minimum = float(min(emg_data))

    if maximum < (minimum*(-1)):
        maximum = minimum*(-1)

    for x in range(len(emg_data)-1):
        emg_data[x] = emg_data[x]/maximum

def normaliseEverything():
    for x in range(len(list_of_list)-1):
        if x != 0 and x != len(list_of_list)-1 :
            normalise(list_of_list[x])
        x = x+1


#################################################################
# From here on out, the code will be for showing statistics in  #
# the Terminal.                                                 #
# This is being done to make some statistics regarding the data #
# more visible.                                                 #
#################################################################
def printMaximumInformation():
    print "In this file there are: " , int(len(label)) , " datapoints"
    print "for EMG 1 we have a max off: " , max(emg1_data), " and a min of: ", min(emg1_data)
    print "for EMG 2 we have a max off: " , max(emg2_data), " and a min of: ", min(emg2_data)
    print "for EMG 3 we have a max off: " , max(emg3_data), " and a min of: ", min(emg3_data)
    print "for EMG 4 we have a max off: " , max(emg4_data), " and a min of: ", min(emg4_data)
    print "for EMG 5 we have a max off: " , max(emg5_data), " and a min of: ", min(emg5_data)
    print "for EMG 6 we have a max off: " , max(emg6_data), " and a min of: ", min(emg6_data)
    print "for EMG 7 we have a max off: " , max(emg7_data), " and a min of: ", min(emg7_data)
    print "for EMG 8 we have a max off: " , max(emg8_data), " and a min of: ", min(emg8_data)
    print " "

def getLabelAmounts():
    x = 0
    print "total amount of labels: ", len(label)
    print "of which: "
    for x in range(8):
        print "there are: ", label.count(x), " of label", x
    print " "

def getLabelStatistics():
    x = 0
    maximum = len(label)
    for x in range(8):
        percentage = float(label.count(x)*100/maximum)
        print "there are: ", float(percentage), "% of label", x
    print " "


#################################################################
# From here on out, the code is for making the plots.           #
# This is being done to make the data more visible, and         #
# less abstract                                                 #
#################################################################
def plotEMG(emg_data):
    fig = figure(title='EMG-data',
             plot_height=800, plot_width=1200,
             x_axis_label='EMG Data', y_axis_label='Time',
             x_minor_ticks= 'auto', x_range=(0, 60000), y_range=(-1, 1.1),
             toolbar_location=None)

    fig.line(x=time, y=emg_data,
         color='gray', line_width=1,
         legend='EMG data normalised')

    show(fig)

def plotAllEMG():
    s1 = figure(title='EMG-data sensor 1',
                 plot_height=800, plot_width=1200,
                 x_axis_label='EMG Data', y_axis_label='Time',
                 x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                 toolbar_location=None)
    s2 = figure(title='EMG-data sensor 2',
                plot_height=800, plot_width=1200,
                x_axis_label='EMG Data', y_axis_label='Time',
                x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                toolbar_location=None)
    s3 = figure(title='EMG-data sensor 3',
                plot_height=800, plot_width=1200,
                x_axis_label='EMG Data', y_axis_label='Time',
                x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                toolbar_location=None)
    s4 = figure(title='EMG-data sensor 4',
                plot_height=800, plot_width=1200,
                x_axis_label='EMG Data', y_axis_label='Time',
                x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                toolbar_location=None)
    s5 = figure(title='EMG-data sensor 5',
                plot_height=800, plot_width=1200,
                x_axis_label='EMG Data', y_axis_label='Time',
                x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                toolbar_location=None)
    s6 = figure(title='EMG-data sensor 6',
                plot_height=800, plot_width=1200,
                x_axis_label='EMG Data', y_axis_label='Time',
                x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                toolbar_location=None)
    s7 = figure(title='EMG-data sensor 7',
                plot_height=800, plot_width=1200,
                x_axis_label='EMG Data', y_axis_label='Time',
                x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                toolbar_location=None)
    s8 = figure(title='EMG-data sensor 8',
                plot_height=800, plot_width=1200,
                x_axis_label='EMG Data', y_axis_label='Time',
                x_minor_ticks='auto', x_range=(0, 70), y_range=(-1, 1.1),
                toolbar_location=None)

    s1.line(x=time, y=emg1_data,
             color='gray', line_width=1,
             legend_label='Cumulative')
    s2.line(x=time, y=emg1_data,
            color='gray', line_width=1,
            legend_label='Cumulative')
    s3.line(x=time, y=emg1_data,
            color='gray', line_width=1,
            legend_label='Cumulative')
    s4.line(x=time, y=emg1_data,
            color='gray', line_width=1,
            legend_label='Cumulative')
    s5.line(x=time, y=emg1_data,
            color='gray', line_width=1,
            legend_label='Cumulative')
    s6.line(x=time, y=emg1_data,
            color='gray', line_width=1,
            legend_label='Cumulative')
    s7.line(x=time, y=emg1_data,
            color='gray', line_width=1,
            legend_label='Cumulative')
    s8.line(x=time, y=emg1_data,
            color='gray', line_width=1,
            legend_label='Cumulative')

    show(column(s1, s2, s3, s4, s5, s6, s7, s8))


#################################################################
# From here on out, the code starts to remove unwanted          #
# zeroes, we do this because otherwise there would be too       #
# many zeroes, which would throw the machine learning           #
# algorithm off balance                                         #
#################################################################
def removeAllZero():
    print "Started removinging zeroes"
    print " "
    index = 0
    for i in range(len(label)-1):
        if list_of_list[9][index] == 0:
            if removeZero(index):
                i = i + 1
            else:
                index = index + 1
        else:
            index = index + 1
    print index

def removeZero(index):
    for x in range(len(list_of_list)-1):
        if x != 0 and x != len(list_of_list)-1:
            if list_of_list[x][index] > abs(averages[x-1])*10 or list_of_list[x][index] < abs(averages[x-1])*(-10):
                removeRow(index)
                return True
    return False

def removeRow(index):
    for listing in list_of_list:
        listing.pop(index)


#################################################################
# Code from here on is for File Handling                        #
# The first method will read in all the files,                  #
# From the second method on, data is being put back into the    #
# Files.                                                        #
# There are 9 new files being made;                             #
# 0_Data    => all the data for label 0                         #
# 1_Data    => all the data for label 1                         #
# 2_Data    => all the data for label 2                         #
# 3_Data    => all the data for label 3                         #
# 4_Data    => all the data for label 4                         #
# 5_Data    => all the data for label 5                         #
# 6_Data    => all the data for label 6                         #
# 7_Data    => all the data for label 7                         #
# allData   => all the data                                     #
#################################################################
def readInFile():
    i = 0
    for x in content:
        data = x.split("\t")
        if i != 0:
            time.append(float(float(data[0])/1000))
            emg1_data.append(float(data[1]))
            emg2_data.append(float(data[2]))
            emg3_data.append(float(data[3]))
            emg4_data.append(float(data[4]))
            emg5_data.append(float(data[5]))
            emg6_data.append(float(data[6]))
            emg7_data.append(float(data[7]))
            emg8_data.append(float(data[8]))
            label.append(int(data[9]))
        i = i+1

def makeAllTheDifferentFiles():
    for x in range(8):
        putInFileMethod(files_list[x], x)
        files_list[x].close()
    putAllInFile()

def putInFileMethod(file_name, labeling):
    for x in range(len(label)-1):
        if label[x] == labeling:
            putLineInFile(file_name, x)

def putLineInFile(file_name, x):
    file_name.write("%f\t" % emg1_data[x])
    file_name.write("%f\t" % emg2_data[x])
    file_name.write("%f\t" % emg3_data[x])
    file_name.write("%f\t" % emg4_data[x])
    file_name.write("%f\t" % emg5_data[x])
    file_name.write("%f\t" % emg6_data[x])
    file_name.write("%f\t" % emg7_data[x])
    file_name.write("%f\t" % emg8_data[x])
    file_name.write("%s\n" % label[x])

def putAllInFile():
    for x in range(len(emg1_data)-1):
        putLineInFile(f_all, x)
    f_all.close()




# From here on out, we call all the methods for what we want to be doing.
readInFile()
printMaximumInformation()
getLabelAmounts()
getLabelStatistics()
normaliseEverything()
getAverage(0)
#getAverage(2)
#plotAllEMG()
removeAllZero()
getLabelAmounts()
getLabelStatistics()
#plotAllEMG()
makeAllTheDifferentFiles()

print "finished"


