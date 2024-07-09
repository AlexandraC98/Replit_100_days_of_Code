import csv, contextlib, os

def sanitize_foldername(name):
  return name.strip()

try:
  with open("100MostStreamedSongs.csv") as file:
    reader=csv.DictReader(file)
    
    for row in reader:
      artist_name=sanitize_foldername(row["Artist(s)"])
      song_name=sanitize_foldername(row["Song"])

      #Create folder for each artist if it doesn't exist
      with contextlib.suppress(FileExistsError):
        os.mkdir(artist_name)

      #Create a .txt file with a song from each artist
      filesong=os.path.join(f"{artist_name}/", f"{song_name}.txt")
      with open(filesong, "w") as f:
        pass
        
except FileNotFoundError:
  print("Error")
except csv.Error as e:
  print(f"Error reading CSV file: {e}")
