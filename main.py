import os
import shutil
from deepface import DeepFace

data_dir = "Celebrity Faces Dataset"

for directory in os.listdir(data_dir):
    first_file = os.listdir(os.path.join(data_dir, directory))[1]
    shutil.copyfile(os.path.join(data_dir, directory, first_file), os.path.join("Sample", f"{directory}.jpg"))

smallest_distance = None
for file in os.listdir("Sample"):
    if file.endswith(".jpg"):
        result = DeepFace.verify("person3.jpg", f"Sample/{file}")
        if result['verified']:
            print("This person looks exactly like", file.split(".")[0])
            break
        if smallest_distance is None:
            smallest_distance = (file.split(".")[0], result['distance'])
        else:
            smallest_distance = (file.split(".")[0], result['distance']) if result['distance'] < smallest_distance[1] else smallest_distance
else:
    print(f"No exact match found! Closest match is {smallest_distance[0]}")

