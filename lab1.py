from dataclasses import dataclass
from datetime import date
import string 
import random 

@dataclass 
class file:
    file_name : str 
    file_date: date
    file_size: int

@dataclass
class S3_bucket:
    bucket_name:str 
    bucket_location:str 
    bucket_size:int 
    bucket_creation_date:date 
    bucket_owner:str 
    bucket_owner_id:str 
    bucket_owner_display_name:str 
    bucket_owner_principal_arn:str 
    bucket_owner_principal_id:str 
    
def random_file_generation():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    years = ["2023", "2024", "2025"]
    file_full_name = "year={}/{}.parquet"
    files_list = []
    for _ in range(100):
        name = ""
        for _ in range(10):
            name += random.choice(characters)
        year = random.choice(years)
        path = file_full_name.format(year, name)
        files_list.append(
            file(
                file_name=path,
                file_date=date.today(),
                file_size=150,
            )
        )
    return files_list


local_buffer = random_file_generation()
for item in local_buffer:
    print(item.file_name)

