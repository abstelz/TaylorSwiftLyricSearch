import requests

# Define the GitHub repository and file path
repository = 'shaynak/taylor-swift-lyrics'
file_path = 'songs.csv'

# Construct the raw file's URL
raw_url = f"https://raw.githubusercontent.com/{repository}/main/{file_path}"

# Send a GET request to the raw file's URL
response = requests.get(raw_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the file
    file_content = response.text

    # Now, 'file_content' contains the content of 'songs.csv'
    # You can save it to a local file or process it as needed
    with open('songs.csv', 'w') as local_file:
        local_file.write(file_content)
else:
    print(f"Failed to retrieve file. Status code: {response.status_code}")
