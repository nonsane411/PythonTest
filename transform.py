import pandas as pd
from datetime import datetime
from datetime import timedelta
df1=pd.read_csv('c', nrows=19)
df2=pd.read_csv('C:\Users\siddh\Downloads\Sample Input - Sample.csv.csv',skiprows=20)#,parse_dates={"event_timestamp":["Date","Time"]} )
print(df1.shape)
print(df2.shape)
f_time=df2['Time'][0]

cols=["Date","Time"]
df2['event_timestamp']=pd.to_datetime(df2[cols].apply(lambda x: ' '.join(x.values.astype(str)), axis="columns"), format='%d-%m-%Y %H:%M:%S').dt.strftime('%d/%m/%Y %H:%M:%S')
df2['event_timestamp']=pd.to_datetime(df2['event_timestamp'], format='%d/%m/%Y %H:%M:%S')


val=0
columns=[x for x in df2.columns if 'L_' in x]
Final_data=pd.DataFrame(columns=['event_timestamp','tag__id','tag__name','tag__desc','tag__value','tag__unit','device_identifier'])

for col in columns:
    val=0
    f_time=df2['event_timestamp'][0]
    while(val == 0):
        
        str_time=f_time
        n_time=str_time+timedelta(seconds=10)
        if n_time not in df2['event_timestamp'].values:
            val=1
        dat=max(df2.loc[(df2['event_timestamp']>=f_time) & (df2['event_timestamp']<n_time),col])
        tag_desc=df1.loc[df1['ItemName']==col,'Comment'].values[0]
        tag_id=df1.loc[df1['ItemName']==col,'ItemId'].values [0]
        evn_tmstmp=str_time 
        tag_nm=col
        tag_val=dat 
        arr=[evn_tmstmp,tag_id,tag_nm,tag_desc,tag_val,0,'R2SD_ProcessDatabase']
        Final_data.loc[len(Final_data.index)]=arr
    
        f_time=n_time

Final_data.to_csv('C:\Users\siddh\Downloads\Sample Input - output.csv')