# PyVideoEfficient

A Python-based tool for efficient video conversion to the AV1 codec using FFmpeg on Windows.

## Description

This project provides a streamlined workflow for transcoding large video files to the highly efficient AV1 codec, significantly reducing file sizes while maintaining acceptable quality. Designed for Windows environments, it leverages the power of FFmpeg through Python scripting to automate the conversion process. This is ideal for archiving, sharing, and streaming videos with reduced storage and bandwidth requirements.

## Key Features

*   **AV1 Encoding:** Converts videos to the cutting-edge AV1 codec for optimal compression.
*   **Windows Compatibility:** Specifically designed and tested for Windows systems.
*   **Automated Workflow:** Python scripts automate the entire conversion process, from file selection to post-processing.
*   **Codec Detection:** Automatically detects the input video's codec (e.g., H.264, HEVC, VP9, AV1) and applies appropriate handling.
*   **Post-Processing Options:** Offers the option to delete original files after successful conversion.
*   **User-Friendly Interface:** Uses a simple file selection dialog for easy input.

## Installation

1.  **FFmpeg:** Ensure FFmpeg is installed and accessible from your system's PATH environment variable. You can download pre-built binaries from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/) (or other reliable sources).
2.  **Python:** Make sure you have Python 3 installed.
3.  **Clone the Repository:**
    ```bash
    git clone [invalid URL removed]
    cd PyVideoEfficient
    ```

## Usage

1.  Run the script: `python VideoEfficientConvert.py`
2.  A file selection dialog will appear. Choose the video file(s) you wish to convert.
3.  The script will process the selected files, displaying progress information in the console.
4.  After conversion, you will be prompted to delete the original files.

## Planned Features (Roadmap)

*   **Batch Processing:** Support for converting multiple videos simultaneously.
*   **Customizable Encoding Settings:** Allow users to adjust encoding parameters like bitrate, CRF, and preset.
*   **Progress Bar:** Implement a more user-friendly progress display within the GUI.
*   **Cross-Platform Support:** Explore compatibility with other operating systems (e.g., Linux, macOS).

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

## License

[MIT License](LICENSE) (or specify your chosen license)

## Acknowledgements

*   [FFmpeg](https://ffmpeg.org/): The powerful command-line tool that makes this project possible.