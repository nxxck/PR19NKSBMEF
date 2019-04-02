from csv import DictReader
import collections

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

def read_csv(file_name):
    global reader
    fp = open('data-project/'+file_name, encoding="ISO-8859-1")
    reader = DictReader(fp)

#MONTH AND SEASON BASED DISTRIBUTIONS AND GRAPHS


#porazdelitev napadov po mesecih
#porazdelitev napadov po sezonah (letni casi)


def placeholder():
    read_csv('globaloffensive.csv')
    list_of_months = []
    for row in reader:
        list_of_months.append(row['imonth'])
    month_to_nEvents = collections.defaultdict(int)
    for cifra in list_of_months:
        if int(cifra) == 0: pass
        else:
            month_to_nEvents[int(cifra)] += 1

    return month_to_nEvents
z = placeholder()
g = collections.OrderedDict(sorted(z.items()))
month_lst = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
events_lst=[]
for key, value in g.items():
    events_lst.append(value)



def num_atk_by_month():
    plt.plot(month_lst,events_lst, color='m')
    f, ax = plt.subplots(1)
    xdata = month_lst
    ydata = events_lst
    bars = np.arange(len(xdata))
    ax.bar(xdata, ydata, color=(0.2, 0.4, 0.6, 0.5))
    # ax.set_ylim(bottom=10000)
    ax.plot(xdata, ydata,color=(0.9, 0.1, 0.6, 0.6))
    plt.xticks(xdata, xdata, color='black', rotation=90)
    plt.subplots_adjust(bottom=0.2)
    plt.title("Number of attacks distributed by month")

    plt.show(f)


summer_atks = sum(events_lst[5:8])
autumn_atks = sum(events_lst[9:11])
spring_atks = sum(events_lst[2:5])
winter_atks = sum(events_lst[0:2])+events_lst[11]

seasons_names=["Winter", "Spring", "Summer", "Autumn"]
seasons_events=[winter_atks, spring_atks, summer_atks, autumn_atks]

def num_atk_by_season():
    plt.plot(month_lst,events_lst, color='m')
    f, ax = plt.subplots(1)
    xdata = seasons_names
    ydata = seasons_events
    bars = np.arange(len(xdata))
    ax.bar(xdata, ydata, color=(0.2, 0.4, 0.6, 0.5))
    # ax.set_ylim(bottom=10000)
    ax.plot(xdata, ydata,color=(0.9, 0.1, 0.6, 0.6))
    plt.xticks(xdata, xdata, color='black', rotation=90)
    plt.subplots_adjust(bottom=0.2)
    plt.title("Number of attacks distributed by seasons")
    plt.savefig('EuropeTOP6TerrorGroups.png')

    plt.show(f)
#
print(num_atk_by_season())

#REGION BASED DISTRIBUTIONS AND GRAPHS
#pojdi isto kot pri zgornjih funkcijah, le da sedaj glej regijo / mesto
def placeholder():
    read_csv('globaloffensive.csv')
    nAttacks_byRegion = []
    nAttacks_byGroup = []
    region_to_nEvents = collections.defaultdict(list)
    group_to_nEvents = collections.defaultdict(int)
    for row in reader:
        region_to_nEvents[row['region_txt']].append(row['gname'])


    Western_Europe = []
    Eastern_Europe = []
    North_America = []
    South_America = []
    East_Asia =[]
    South_Asia =[]
    Central_Asia =[]
    Australasia_Oceania =[]
    Middle_East = []
    Sub_Saharan_Africa = []
    all_Groups=[]

    for region in region_to_nEvents:
        print(region)
        if region == "Western Europe":


            for atk in region_to_nEvents[region]:
                if atk != "Unknown":
                    Western_Europe.append(atk)
        if region == "Middle East & North Africa":


            for atk in region_to_nEvents[region]:
                if atk != "Unknown":
                    Middle_East.append(atk)

        if region == "Sub-Saharan Africa":

            for atk in region_to_nEvents[region]:
                if atk != "Unknown":
                    Sub_Saharan_Africa.append(atk)

        if region == "North America":

            for atk in region_to_nEvents[region]:
                if atk != "Unknown":
                    North_America.append(atk)
        if region == "Eastern Europe":

            for atk in region_to_nEvents[region]:
                if atk != "Unknown":
                    Eastern_Europe.append(atk)
        if region == "South America":

            for atk in region_to_nEvents[region]:
                if atk != "Unknown":
                    South_America.append(atk)
        if region == "South America":

            for atk in region_to_nEvents[region]:
                if atk != "Unknown":
                    South_America.append(atk)


# #WE
#     all_Groups.extend(Middle_East)
#     all_Groups.extend(Sub_Saharan_Africa)
#     # all_Groups.extend(North_America)
#     # all_Groups.extend(South_America)
# ##middle easte
#     group, values = zip(*collections.Counter(Middle_East).most_common(6))
#     indexes = np.arange(len(group))
#     width = 0.5
#     plt.figure(figsize=(6, 8))
#     plt.rc('xtick', labelsize=5)
#
#     # plt.subplot(1, 2, 1)
#     plt.bar(group,values, color='orange')
#     plt.xticks(all_Groups, all_Groups, color='blue', rotation=90)
#     # plt.xticks(group, group, color='black', rotation=90)
#
#
#
# #subsaharan
#     group, values = zip(*collections.Counter(Sub_Saharan_Africa).most_common(6))
#     indexes = np.arange(len(group))
#
#
#
#     # plt.subplot(1, 2, 2)
#     plt.bar(group, values)
#     # plt.xticks(group, group, color='blue', rotation=90)
#     # plt.title("Eastern Europe")

#
# #northamerica
#     group, values = zip(*collections.Counter(North_America).most_common(6))
#     indexes = np.arange(len(group))
#
#
#
#     # plt.subplot(1, 2, 2)
#     plt.bar(group, values)
#     # plt.xticks(group, group, color='blue', rotation=90)
#     # plt.title("Eastern Europe")
#
# #southamerica
#     group, values = zip(*collections.Counter(South_America).most_common(6))
#     indexes = np.arange(len(group))
#
#     # plt.subplot(1, 2, 2)
#     plt.bar(group, values)



    plt.savefig('EuropeTOP6TerrorGroups.png')
    plt.show()



# #NA
#     group, values = zip(*collections.Counter(North_America).most_common(6))
#     indexes = np.arange(len(group))
#
#
#
#     plt.subplot(1, 2, 2)
#     plt.bar(group, values)
#     plt.xticks(group, group, color='black', rotation=90)
# #
# # #SA
#     group, values = zip(*collections.Counter(South_America).most_common(6))
#     indexes = np.arange(len(group))
#     width = 0.5
#
#
#
#     plt.subplot(1, 2, 2)
#     plt.bar(group, values)
#     plt.xticks(group, group, color='black', rotation=90)
#     plt.title("South America")
#
#
#
#     plt.savefig('foo.png')
#     plt.show()


    #za vsako regijo naredi top6 big terror groupov in prikazi s piechartom
    #za vse regije dej skup nato na en skupen big boy graph










    # plt.bar(region_to_nEvents.keys(), region_to_nEvents.values(), color='m')

    #     f, ax = plt.subplots(1)
    #     xdata = seasons_names
    #     ydata = seasons_events
    #     bars = np.arange(len(xdata))
    #     ax.bar(xdata, ydata, color=(0.2, 0.4, 0.6, 0.5))
    #     # ax.set_ylim(bottom=10000)
    #     ax.plot(xdata, ydata,color=(0.9, 0.1, 0.6, 0.6))
    #     plt.xticks(xdata, xdata, color='black', rotation=90)
    #     plt.subplots_adjust(bottom=0.2)
    #     plt.title("Number of attacks distributed by seasons")
    # plt.show()
print(placeholder())







#ideas for graphs
#porazdelitev napadov glede na regijo kjer je bil napad izveden
#porazdelitev napadov glede na ethnicity assailantov
#porazdelitev glede na dejansko uro napada, zjutraj popoldne, noc...
