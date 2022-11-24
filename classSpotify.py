class Spotify:
  def __init__(self,li):
    print("Welcome to Spotify!")
    self.s_list =li
    self.name=""

  def playing_number(self,song_num):


    if len(self.s_list)>=(song_num):
      print("############################")
      self.name=self.s_list[song_num-1]
      return (f"Playing {song_num} number song for you\nSong name: {self.name}")
    else:
      return (f"{song_num} number song not found. Your playlist has {len(self.s_list)} songs only.")

  def add_to_playlist(self,add):
    self.s_list.append(add)

user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))
