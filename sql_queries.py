# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS;"
user_table_drop = "DROP TABLE IF EXISTS USERS;"
song_table_drop = "DROP TABLE IF EXISTS SONGS;"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS;"
time_table_drop = "DROP TABLE IF EXISTS TIME;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS SONGPLAYS (songplay_id serial PRIMARY KEY ,start_time bigint, user_id integer,level varchar(50),song_id varchar(50), artist_id varchar(50), session_id varchar(50),  location varchar(100), user_agent varchar(300));""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS (user_id integer PRIMARY KEY, first_name varchar(100), last_name varchar(100), gender char(1), level varchar(50));""")

song_table_create = ("CREATE TABLE IF NOT EXISTS SONGS (song_id VARCHAR(100) PRIMARY KEY, title VARCHAR(250), artist_id VARCHAR(50), year bigint, duration decimal(12,5));")

artist_table_create = ("CREATE TABLE IF NOT EXISTS ARTISTS (artist_id VARCHAR(100) PRIMARY KEY, name VARCHAR(100), location VARCHAR(100), latitude VARCHAR(50), longitude VARCHAR(50));")

time_table_create = ("CREATE TABLE IF NOT EXISTS TIME (start_time bigint PRIMARY KEY, hour INTEGER, day integer, week integer, month integer, year INTEGER, weekday INTEGER);")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time,user_id,song_id,artist_id,session_id,location,user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")

user_table_insert = ("""INSERT INTO USERS(user_id,first_name,last_name,gender,level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")

song_table_insert = ("""INSERT INTO SONGS (song_id, title, artist_id,year,duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")
 
artist_table_insert = ("""INSERT INTO ARTISTS (artist_id,name,location,latitude,longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""")


time_table_insert = ("""INSERT INTO TIME (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""Select s.song_id, s.artist_id from songs s join artists a on s.artist_id = a.artist_id where s.title = %s and a.name = %s and s.duration = %s ;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]