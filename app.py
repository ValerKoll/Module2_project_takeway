from lib.database_connection import DatabaseConnection
#from lib.takeaway_app import TakeawayApp

# connect to the DATABASE
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/resturants_data.sql")

# create takeaway app and run it
# app = TakeawayApp()
# app.run()



# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)