# youtube-downloader
This Python script allows you to download a YouTube video and split it into segments based on chapter timestamps. It uses the `pytube` library to download the video and the `moviepy` library to perform the splitting.

## Requirements

- Python 3.x
- `pytube` library
- `moviepy` library

Install the required libraries using the following commands:

```bash
pip install pytube moviepy
```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

   ```bash
   python youtube_downloader.py
   ```

4. Follow the prompts to provide the YouTube video URL and set the chapter timestamps.

5. The script will download the video and split it into segments based on the provided timestamps.

## Configuration

- Modify the `video_url` variable to specify the YouTube video URL you want to download.

- Edit the `chapter_timestamps` dictionary to set the start and end timestamps for each chapter.

- Set the `download_location` variable to define the directory where downloaded videos and segments will be saved.

## Notes

- Make sure you have the necessary permissions to download and manipulate the video content.

- The script will create a virtual environment named `myenv` in the same directory to manage dependencies.

- For more information about the libraries used, refer to the documentation for [pytube](https://pypi.org/project/pytube/) and [moviepy](https://zulko.github.io/moviepy/).

- This script is provided as a basic example and might require adjustments for specific use cases.

## License

This script is licensed under the [MIT License](LICENSE).
```

Replace any placeholders with actual content from your script and project. This documentation will help users understand how to use your script, what dependencies are required, and how to configure it according to their needs. Make sure to adjust the URLs, paths, and other details to match your actual project structure.
