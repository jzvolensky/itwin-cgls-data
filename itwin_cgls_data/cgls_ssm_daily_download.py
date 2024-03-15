from datetime import datetime
import datetime as dt
import os
from getpass import getpass

def get_inputs(prompt, password=False) -> str:
    """
    Some basic input validation. If the user input is empty, it will ask the user to enter again.
    Does not handle cases of invalid input, such as entering a string when a number is expected.
    """
    while True:
        if password:
            user_input = getpass(prompt)
        else:
            user_input = input(prompt)
        if user_input == "":
            print("Oh no, this can't be empty. Please enter again.")
        else:
            return user_input

def download_cgls_data() -> None:
    """
    Disclaimer: This is a dirty and unsafe way exposing credentials and what not. I hate it but since the
    service api is a pain to use, I'm doing it this way. I'm sorry. Delete the file .sh after running it.
    """
    start_date_input = get_inputs("Enter the start date (YYYY-MM-DD): ")
    end_date_input = get_inputs("Enter the end date (YYYY-MM-DD): ")

    if start_date_input > end_date_input:
        raise ValueError("The start date must be before the end date.")
    
    start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()

    base_url = "https://land.copernicus.vgt.vito.be/PDF/datapool/Vegetation/Surface_Soil_Moisture/Daily_SSM_1km_Europe_V1/"

    username = get_inputs("Enter your username: ")
    password = get_inputs("Enter your password: ", password=True)
    output_path = get_inputs("Enter your desired output path (e.g., /home/user/downloads or downloads): ")
    cov = get_inputs("Enter the type of product to download (tile, cont, glob): ")

    # fixed coordinates
    minx = 5.075000
    miny = 43.616667
    maxx = 15.858333
    maxy = 50.031229
    coords = f"{minx},{miny},{maxx},{maxy}"

    with open("download_data.sh", "w") as f:
        f.write("#!/bin/bash\n")
        date = start_date
        while date <= end_date:
            year = date.strftime("%Y")
            month = date.strftime("%m")
            day = date.strftime("%d")
            url = f"{base_url}{year}/{year}{month}/{year}{month}{day}/c_gls_SSM1km_{year}{month}{day}0000_CEURO_S1CSAR_V1.1.1.nc?cov={cov}&coord={coords}"
            f.write(f"wget --user={username} --password={password} -c -P {output_path} {url}\n")
            f.write(f"find {output_path} -name 'robots.txt' -delete\n")  # Add this line
            date += dt.timedelta(days=1)
    
    with open("download_data.sh", "a") as f:
        os.system("chmod +x download_data.sh")

    print("The download_data.sh file has been created and is executable. Run it to download the data.")


if __name__ == "__main__":
    download_cgls_data()