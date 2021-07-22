import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('1% Vidio stream dataset.csv', error_bad_lines=False)

df_samples = df.sample(10)

# Data Cleaning
df.info()
# drop kolom 'city', karena tidak ada data dalam kolo,
df.drop('city', inplace=True, axis=1)

# NAN data
nan_columns = [column for column in df.columns if df[column].isnull().sum() > 1]
## Persentase nan data pada dataset
print(df[nan_columns].isnull().mean()*100)
fillna_false = ['completed', 'autoplay']
for col in fillna_false:
    df[col].fillna(False, inplace=True)
fillna_unknown = [col for col in nan_columns if col not in ['average_bitrate']]
for col in fillna_unknown:
    df[col].fillna('unknown', inplace=True) 

# mengganti tipe data pada kolom datetime and timestamp
date_columns = ['play_time', 'end_time']
for col in date_columns:
    df[col] = pd.to_datetime(df[col]).dt.tz_localize(None)

df['date_play'] = df['play_time'].dt.date
df['day_names_play'] = df['play_time'].dt.day_name()
df['hour_play'] = df['play_time'].dt.hour

# merubah boolean tipe data ke string atau object
bool_columns = [col for col in df.columns if df[col].dtypes == 'bool']
for col in bool_columns:
    df[col] = df[col].astype(str)

for col in df.columns:
    print(col + ': {}'.format(len(df[col].unique())))
    
df = df[df['end_time'] > df['play_time']]

df['total_duration'] = df['end_time'] - df['play_time']
df['total_duration'] = df['total_duration']/np.timedelta64(1, 's')

df = df[(df['buffer_duration'] + df['play_duration']) <= df['total_duration']]



# Data Analysis

# mendefinisikan Kolom ID
id_columns = ['hash_content_id', 'hash_play_id', 'hash_visit_id', 'hash_watcher_id', 'hash_film_id', 'hash_event_id']

# mendefenisikan date_time_columns
date_time_columns = ['date_play', 'day_names_play', 'hour_play']

# Kolom Numeric
num_columns = [col for col in df.columns if df[col].dtypes != "O" and col not in date_columns + date_time_columns + id_columns]
num_discrete = [col for col in num_columns if len(df[col].unique()) <= 10]
num_continue = [col for col in num_columns if col not in num_discrete]

# Kolom kategori
cat_columns = [col for col in df.columns if col not in date_columns + num_columns + date_time_columns + id_columns ]
for col in cat_columns:
    print(col + ': {}'.format(len(df[col].unique())))
    
for col in cat_columns:
    plt.figure()
    data_vis = df.groupby([col]).size().reset_index(name='total_streams').sort_values(by='total_streams', ascending=False)
    lim_data_vis = data_vis[0:10]
    sns.barplot(data=lim_data_vis, x=col, y='total_streams')
    plt.xticks(rotation=90)
    plt.tight_layout()

for col in cat_columns:
    plt.figure()
    data_vis = df.groupby([col])['play_duration'].mean().reset_index(name='play_duration').sort_values(by='play_duration', ascending=False)
    lim_data_vis = data_vis[0:10]
    sns.barplot(data=lim_data_vis, x=col, y='play_duration')
    plt.xticks(rotation=90)
    plt.tight_layout()

for col in num_continue:
    print(col + ': {}'.format(len(df[col].unique())))
for col in num_continue:
    plt.figure()
    sns.scatterplot(data=df, x=col, y='play_duration')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
df['day_names_play'] = pd.Categorical(df['day_names_play'], categories=
    ['Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
    ordered=True)

for col in date_time_columns:
    plt.figure()
    data_vis = df.groupby([col]).size().reset_index(name='total_streams').sort_values(by='total_streams', ascending=False)
    sns.lineplot(data=data_vis, x=col, y='total_streams')
    plt.xticks(rotation=90)
    plt.tight_layout()
    

