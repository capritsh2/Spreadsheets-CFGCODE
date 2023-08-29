# import csv
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# def read_data():
#     data = []
#     with open('sales.csv','r') as sales_csv:
#         spreadsheet = csv.DictReader(sales_csv)
#         for row in spreadsheet:
#             data.append(row)
#     return data
#
# def run():
#     data = read_data()
#     sales = {}
#     MonthlyChanges = []
#     Count = 0
#
#     for row in data:
#         sales.update({int(row['Sales']) : row['Month']})
#         Count+=1
#         prevRow = int(row['Sales'])
#         if(Count>0):
#             MonthlyChanges.append(prevRow)
#
#     total = sum(sales)
#     average = total/Count
#     print('Total sales: ' + str(total))
#     SummariseSpreadSheet(total,average,sales)
#
# def SummariseSpreadSheet(TotalSales,average,SaleData):
#     TotalHeader = ["Total Sales:", TotalSales]
#     AverageHeader = ["Average Sales:", average]
#     with open('SalesSummary.csv','w+') as sales_csv:
#         writer = csv.writer((sales_csv))
#         writer.writerow(TotalHeader)
#         writer.writerow(AverageHeader)
#         Summary = [TotalSales,average]
#         writer.writerow(Summary)
#
#         nHighestMonths = input("Please enter a number to see the n months with the highest sales")
#         Header = ["Months with highest sales"]
#         writer.writerow(Header)
#         HighestSales = GetNMonthsHighestSales(int(nHighestMonths),SaleData)
#         for sale in HighestSales:
#             Data = [sale, SaleData.get(sale)]
#             writer.writerow(Data)
#
#         nLowestMonths = input("Please enter a number to see the n months with the lowest sales")
#         Header = ["Months with lowest sales"]
#         writer.writerow(Header)
#         LowestSales = GetNMonthsLowestSales(int(nLowestMonths), SaleData)
#         for sale in LowestSales:
#             Data = [SaleData.get(sale),sale]
#             writer.writerow(Data)
#
#         Header = ["Percentage Difference each month"]
#         writer.writerow(Header)
#         PercentageDiff = GetPercentageChange(SaleData)
#         PlotScatterPercentageDiff(PercentageDiff)
#         for Percentage in PercentageDiff:
#             Data = [Percentage, PercentageDiff.get(Percentage)]
#             writer.writerow(Data)
#
# def GetNMonthsHighestSales(n,SaleData):
#     DataKeys =list(SaleData.keys())
#     DataKeys.sort()
#     NMonthsHighestSales = []
#     for i in range(len(DataKeys)-1, len(DataKeys)-1-n, -1):
#         NMonthsHighestSales.append(DataKeys[i])
#         print(DataKeys[i])
#     return NMonthsHighestSales
#
# def GetNMonthsLowestSales(n,SaleData):
#     DataKeys = list(SaleData.keys())
#     DataKeys.sort()
#     DataKeys.remove(0)
#     NMonthsLowestSales = []
#     for i in range(0,n):
#         NMonthsLowestSales.append(DataKeys[i])
#         print(DataKeys[i])
#     return NMonthsLowestSales
#
# def GetPercentageChange(SaleData):
#     DataKeys = list(SaleData.keys())
#     PercentageChange = {}
#     for i in range(1, len(DataKeys)):
#         if int(DataKeys[i]) == 0:
#             break
#         Difference = int(DataKeys[i]) - int(DataKeys[i-1])
#         PercentageDifference = (Difference / int(DataKeys[i])) * 100
#         DifferenceKey = "From: " + str(DataKeys[i-1]) + " To: " + str(DataKeys[i])
#         Entry = {DifferenceKey:PercentageDifference}
#         PercentageChange.update(Entry)
#     return PercentageChange
#
# def PlotGraph():
#     df = pd.read_csv("sales.csv")
#     df.plot(kind='bar', x='Month', y='Sales') # scatter plot
#     # df.plot() # plots all columns against index
#     #df.plot(kind='hist', x='Month', y='Sales') # scatter plot
#     plt.show()
#
# def PlotHighestSalesInYearGraph():
#     data = pd.read_csv('sales.csv')
#     df = pd.DataFrame(data)
#     df1 = df.groupby((['Year ', 'Month'])).sum().reset_index()
#     ax = plt.axes()
#     ax.bar(df1['Year '], df1['Sales'])
#     plt.xticks(np.arange(min(df1['Year ']), max(df1['Year ']+1), step=1))
#     ax.set_xlabel('Year')
#     ax.set_ylabel('Sales')
#     plt.title('Highest Selling Month in Year')
#     plt.show()
#
#
# def PlotScatterPercentageDiff(PercentageDict):
#     DataKeys = list(PercentageDict.values())
#     MonthNo = []
#     for i in range(1, len(DataKeys)+1):
#         MonthNo.append(i)
#     ax = plt.axes()
#     plt.scatter(MonthNo,DataKeys,c=DataKeys)
#     plt.xticks(np.arange(1, len(DataKeys)+1,step=1))
#     ax.set_xlabel('Time (Months)')
#     ax.set_ylabel('Sales Difference From Last Month (%)')
#     plt.title('Sales Percentage Change By Month')
#     plt.show()
#
# run()
# PlotGraph()
# PlotHighestSalesInYearGraph()
