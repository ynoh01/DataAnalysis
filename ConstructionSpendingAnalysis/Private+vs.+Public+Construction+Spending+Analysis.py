
# coding: utf-8

# We will try to find two interesting patterns in ConstructionTimeSeriesData.csv. 
#  This is time series data for public (governmental) construction spending and private construction spending in each month from January, 2002 to February 2014. Note that January and February have one additional data point than the others. 
#  
# Some approaches can be:
# 1. Compare total construction spending of public and private 
# 2. Calculate the percentage of public and private over total construction
# 3. See if there's any seasonality
# 4. For each public and private, see if construction spending is concentrated in certain month or year 
# 

# In[6]:

import pandas as pd


# In[7]:

get_ipython().magic(u'matplotlib inline')


# In[39]:

df = pd.read_csv('ConstructionTimeSeriesDataV2.csv')


# In[40]:

df.head()


# In[41]:

import matplotlib.pyplot as plt


# In[42]:

totalsum = sum(df['Total Construction'])
totalprivate = sum(df['Private Construction'])
totalpublic = sum(df['Public Construction'])
print "Sum of Total Construction:", totalsum
print "Total Private Construction:", totalprivate
print "Total Public Construction:", totalpublic

print "Percentage of Private Construction is ", (float(totalprivate)/float(totalsum))*100, "%"
print "Percentage of Public Construction is ", (float(totalpublic)/float(totalsum))*100, "%"


# In[43]:

data = [totalsum,totalprivate,totalpublic]
objects = ['Total Construction', 'Private Construction', 'Public Construction']

fig, ax = plt.subplots()
total = ax.bar(1,totalsum, 0.45)
private = ax.bar(2, totalprivate,0.4)
public = ax.bar(3, totalpublic, 0.4)


ax.set_xticklabels(objects)
ax.set_xticks([1.0, 2.0, 3.0])
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.yaxis.set_label_text('Construction Spending')

fig.suptitle('Private vs Public Construction Spending Comparison')           
ax.text(1.9,9000000,"72.2%")
ax.text(2.88,4000000,"27.8%")

plt.savefig('percentage comparison.jpg')


# We found that private construction spending is much higher than that of public. Let's go deeper into the data and see what we can find.

# In[44]:

x = df.Month
y = df['Public Construction']
y1 = df['Private Construction']

fig, ax = plt.subplots()

ax.plot(x,y,label='Public Construction') 
ax.plot(x,y1,label='Private Construction')
ax.xaxis.set_label_text('Month')                     
ax.yaxis.set_label_text('Construction Spending') 
ax.axis([x.min(),x.max(),0,1.1*y1.max()])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.legend()

fig.suptitle('Private vs. Public')
plt.savefig('public private seasonal.jpg')


# We found that the both private and public construction spending shows some seasonality. Private construction spending is higher in the earlier months and decrease a little around 80th month,which is August 2008. Public Construction spending is relatively steady and lower than private spending all the way. 
# 
# Now we will try to see if the spending is concentrated in certain month/season of the year.

# In[45]:

total_month =[]
private_month =[]
public_month =[]

for i in range(12):
    total_month.append(sum(df['Total Construction'][i::12]))
for j in range(12):
    private_month.append(sum(df['Private Construction'][j::12]))
for k in range(12):
    public_month.append(sum(df['Public Construction'][k::12]))

fig, ax = plt.subplots()
x = [1,2,3,4,5,6,7,8,9,10,11,12]
x_labels = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
y = total_month
y1 = private_month
y2 = public_month

ax.plot(x,y,label='Total Construction')
ax.plot(x,y1,label='Private Construction')
ax.plot(x,y2,label='Public Construction')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.legend(loc = 'upper right', prop = {'size':'small'})
ax.set_xlim(0,13)
ax.set_ylim(0,1500000)

ax.xaxis.set_label_text('Month')
ax.xaxis.set_ticks(range(0,13))
ax.xaxis.set_ticklabels(x_labels)
ax.xaxis.set_tick_params(which ='both', top ='off', bottom ='on', labelleft = 'on')

ax.yaxis.set_label_text('Construction Spending')
ax.yaxis.set_tick_params(which ='both', right ='off', left ='on', labelleft ='on')

fig.suptitle("Private vs. Public Spending Monthly Comparison")
plt.savefig('monthly comparison.jpg')


# We can observe that construction spending is higher in summer (June, July, August) and lower in both ends (winter) for both private and public. Total Construction plot shows this trend more clearly. Although January and February have one additional data point than the others, those are still lower than the spending in the other months. We can definitely tell warmer weather means construction season. 
# 
# Now we will try to see if the spending if concentrated in certain year.

# In[46]:

total_year=[]
private_year=[]
public_year=[]

for i in range(0,len(df['Total Construction']),12):
     total_year.append(sum(df['Total Construction'][i:i+12:]))
for j in range(0,len(df['Private Construction']),12):
     private_year.append(sum(df['Private Construction'][j:j+12:]))
for k in range(0,len(df['Public Construction']),12):
     public_year.append(sum(df['Public Construction'][k:k+12:]))

fig, ax = plt.subplots()
x = [2,3,4,5,6,7,8,9,10,11,12,13,14]
y = total_year
y1 = private_year
y2 = public_year

ax.plot(x,y,label='Total Construction')
ax.plot(x,y1,label='Private Construction')
ax.plot(x,y2,label='Public Construction')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.legend(loc = 'upper right', prop = {'size':'small'})
ax.set_xlim(0,15)
ax.set_ylim(0,1500000)

ax.xaxis.set_label_text('Year(2000)')
ax.xaxis.set_ticks(range(2,15))
ax.xaxis.set_ticklabels(x)
ax.xaxis.set_tick_params(which ='both', top ='off', bottom ='on', labelleft = 'on')

ax.yaxis.set_label_text('Construction Spending')
ax.yaxis.set_tick_params(which ='both', right ='off', left ='on', labelleft ='on')

fig.suptitle("Private vs. Public Spending Yearly Comparison")
plt.savefig('yearly comparison.jpg')


# From the total construction graph, we can observe that the spending is higher in 2006 and 2013 and lower in 2011. This result, however, is heavily influenced by Private Spending data. Public Spending looks rather steady. We can see that the shape of two graphs are almost identical. Note that 2014 data looks plummet because it only contains January and February data. 
# 

# From this analysis, we have observed three intersting points. 
# 
# First, Private Construction spending is much greater than Public Construction spending. In fact, 72.2% of total construction spending was used in Private construction. 
# 
# Second, Both construction spending tends to be higher in summer time, from June to October. 
# 
# Third, Private Construstion spending shows peaks and valleys. Highest in 2006 and the lowest in 2011. Public Construction spending plots is steady. 

# In[ ]:



