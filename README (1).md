
# Sparkify Song Analytics Datamart

The purpose of this project is to perform data anlaysis to identify user engagement on Sparkify's application.
This datamart will provide Sparkify analytics team an easy and intututive way of querying data by modeling the raw dataset into Star Schema.
This will satisfy their core analytical use cases of identifying what songs are played by which users and will also support other analytical use cases.

## Sytem Design Details :

### DataModel:

    The source data can be categorized as follows:
1. Dimensions: Song_data holds the metadata, which will act as the source for Songs and Artists dimension tables.
    
    **Songs:** This is a dimension table for all Songs available in the Sparkify app with song_id as the primary_key
    
    **Artists:** This is a dimension table for all distinct artists, this is ensured by making artist_id as the primary_key.
     Although the target tables have no foreign key constraints, typical in a datawarehousing system it gets handled as part of ETL transformation logic to reduce latency in data loading.
    Also in this case both songs and artists are derived from the same source and the join column artist_id 
   
   We are also deriving couple of other dimensions Time and Users which will help us identify which users are playing what songs and at what time.
   
   **TIME**: The time dimension is derived from the log timestamp columns to facilitate data analysis using various time part or calendar data.
   
   **Users**: The user dimension is derived from Logs data, with user_id being the primary key.
   
2. Fact: Log data contains the event data of users playing songs. This will be the source for the fact table Songplays.
    
    **SongPlays**: The songplays table will store all user activity. Each user activity is identified by a unique identifier songplay_id which is a Postgres serial 
      column, this will serve as the primary key for this table.
       
### Data Pipeline design:
 
 The data pipeline has two ingestion streams, one for Songs and the other for processing logs data.
 Each process will loop through the files in data directory and will derive the required data to load dimensions and fact table.
 
 
### Sample Queries and resultset:
 
 SongPlay Table:

sql SELECT * FROM songplays  where song_id != 'None' order by song_id asc LIMIT 5;

    Songplay_id  start_time    user_id  level  song_id              artist_id        session_id location                             user_agent
    4108         1542837407796  15      None   SOZCTXZ12AB0182364   AR5KOSW1187FB35FF4 818       Chicago-Naperville-Elgin, IL-IN-WI  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"
 
 Users:
 
 SELECT * FROM users where user_id = 15
 
     user_id first_name    last_name    gender    level
      15        Lily         Koch        F        paid
 
 Songs:
 
    SELECT * FROM songs where song_id = 'SOZCTXZ12AB0182364';

    song_id             title             artist_id        year duration
    SOZCTXZ12AB0182364	Setanta matins	AR5KOSW1187FB35FF4	0	269.58322

Artists:

    SELECT * FROM artists where artist_id = 'AR5KOSW1187FB35FF4';
    artist_id            name	location    latitude            longitude
    AR5KOSW1187FB35FF4	Elena	Dubai UAE	49.803879999999999	15.474909999999999

 
Time:

    SELECT * FROM time where start_time = 1542837407796;

    start_time      hour  day   week   month   year  weekday
    1542837407796	21    21    47      11     2018  2


