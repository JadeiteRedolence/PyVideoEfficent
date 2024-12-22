###Your enviroment must have ffmpeg installed
###Use command "ffmpeg -version" to test ffmpeg if it is installed



"""
This module imports various functions from the 'os' and 'os.path' modules to facilitate file and directory operations, as well as command execution. It is designed for use in a Python script located at 'd:\\Proccess\\Python3\\FFMPEG\\AV Efficent\\VideoEfficentConvert.py'.
"""
from os import system as cmd, chdir, getcwd, popen as rcmd, rename, remove, _exit as exit
"""
This module imports essential functions from the 'os.path' and 'tkinter.filedialog' modules to facilitate file path manipulations and file selection dialogues, respectively. These functionalities are crucial for handling file operations within the application, such as opening files for video conversion processes.
"""
from os.path import split as sp, splitext as spt, basename as bn, exists, expanduser
"""
This line imports the `askopenfilenames` function from the `tkinter.filedialog` module and renames it as `askfls`. This function is used to open a dialog box that allows the user to select multiple files. It is typically used in GUI applications to enable file selection.
"""
from tkinter.filedialog import askopenfilenames as askfls
"""
Import the sleep function from the time module to allow for pausing execution in the code.
"""
from time import sleep
"""
Import the datetime module to facilitate date and time operations within the script.
"""
from datetime import datetime
# Importing the 'sub' function from the 're' module
# This function is used for replacing occurrences of a particular pattern
# with a replacement string, which is useful for text processing tasks
# within the VideoEfficentConvert script.
from re import sub
"""
This script initializes the Tkinter library, which is used for creating graphical user interfaces (GUIs) in Python.
"""
import tkinter as tk

"""
Sets up the main window for the application, making it always on top and initially hidden.
"""
root = tk.Tk()
root.attributes('-topmost', 1)
root.withdraw()

"""
This variable `init_dir` is initialized to the path of the user's 'Downloads' directory using the `expanduser` function. It is likely used as a starting point for file operations within the script, such as saving or loading files related to video efficient conversion.
"""
init_dir = expanduser('~\\Downloads\\')
"""
compress_rate: A float value representing the compression rate to be applied during video conversion. This value should be between 0 and 1, where 0 indicates no compression and 1 indicates maximum compression.
"""
compress_rate = 0.4
"""
This regular expression is used to validate filenames, ensuring they do not contain invalid characters. It includes a wide range of special characters, emojis, and Unicode ranges that are not permitted in filenames.
"""
invalid_filename_rule = r'[\➕\🤸\´\▽\｀\𖥦\⌯\੭\🫠\🪶\🌻\💖\🤤\🥹\⭐\☀️\＼\`\Δ\’\／\𓆡\𓆝\𓆜\𓆟\𓆞\🧧\`\Δ\🥰\🧸\⚡\<\>\🩷\ヾ\✨\～\…\!\⸜\ᴗ\-\♥︎\🉑\🤍\🤡\꒰\⸝\ɞ̴̶̷\ \·\̮ \ɞ̴̶̷\꒱\♡\^\ゞ\￣\】\【\！\？\❤】\?\.\🪐\:\*\/\?\‎\(\)\#\•\|\,\，\✧\;\🥱\❓\✔\'\\\❗\&\ \U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+'

# Executes a PowerShell command.
# 
# This function takes a string argument 's' which represents the PowerShell command
# to be executed. It uses the 'cmd' function to run the PowerShell command in the
# system shell.
#
# Parameters:
#   s (str): The PowerShell command to execute.
#
# Returns:
#   None
def powershell(s):
    cmd(f'powershell.exe;{s}')

"""
Validates and renames a filename according to specified rules.

This function splits the input filename into its base name and extension, replaces invalid characters with underscores based on the global `invalid_filename_rule`, and then renames the file accordingly.

Parameters:
- i (str): The original filename to be validated and renamed.

Returns:
- str: The new, validated filename.
"""
def validate_filename(i):
    global invalid_filename_rule
    name = spt(i)[0]
    fmt = spt(i)[-1]
    new_filename = sub(invalid_filename_rule, '_', name) + fmt
    rename(i, new_filename)
    return new_filename

"""
get_video_inputs()

This function prompts the user to select video files for processing. It uses a graphical interface to allow the selection of multiple video files with extensions .mp4, .avi, .flv, and .mkv from the initial directory specified by the global variable `init_dir`.

Returns:
    List[str]: A list of file paths for the selected video files.
"""
def get_video_inputs():
    global init_dir
    return askfls(title='Select Video You Want to Proccess', filetypes=[('Video', '*.mp4 *.avi *.flv *.mkv')], initialdir=init_dir)

"""
get_video_bitrate(vp)

Calculate the video bitrate of a given video file.

Parameters:
vp (str): The path to the video file.

Returns:
int: The video bitrate in kilobits per second (kbps).

This function uses the 'ffprobe' command-line tool to extract the video bitrate from the specified video file.
"""
def get_video_bitrate(vp):
    bitrate_reslt = rcmd(f'ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 -i \"{vp}\"').read().strip()
    return int(int(bitrate_reslt)/10**3)


"""

get_vcodec(vp)


Uses the `ffprobe` command to extract the video codec name from the provided video file path.


Parameters:

vp (str): The path to the video file.


Returns:

str: The name of the video codec used in the video file.

"""

def get_vcodec(vp):
    codec_reslt = rcmd(f'ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 "{vp}"')
    return codec_reslt.read().strip()


"""
get_metadata(title)

This function generates metadata for a video processing task. It returns a string formatted with the current time, author name, description, and the provided title. This metadata can be used to annotate the processed video file.

Parameters:
- title (str): The title of the video being processed.

Returns:
- str: A string containing the metadata formatted for FFmpeg commands.
"""
def get_metadata(title):
    current_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    author = 'PyAudioEfficent'
    description = 'This video has been proccesed by AV1 Encoder'
    return f' -metadata author=\'{author}\' -metadata description=\'{description}\' -metadata proccess_time=\'{current_time}\' -metadata title=\'{title}\' ' 


"""
Generate an FFmpeg command for efficient video compression using AV1 encoding.

This function constructs an FFmpeg command string that compresses a video file using the AV1 codec with NVENC acceleration. The compression rate is globally defined and affects the output bitrate. The output filename is generated based on the original file's name.

Parameters:
- i (str): The input video file path.

Returns:
- str: The FFmpeg command string for video compression.
"""
def gen_command(i):
    global compress_rate
    metadata = get_metadata(i)
    output_bitrate = str(get_video_bitrate(i) * compress_rate) + 'k'
    output_filename = f"AV1compressed__{spt(i)[0]}.mp4"
    return f'ffmpeg -hide_banner -i \"{i}\" -f mp4 -bufsize 32768 -threads 32 -c:v av1_nvenc {metadata} -c:a  copy -y -b:v {output_bitrate} \"{output_filename}\"'


"""
Executes video compression for a given input.

This function generates a command for video compression using the `gen_command` function,
prints the command, and then executes it using the `powershell` function.

Args:
    i (Any): The input for which video compression is to be executed.

Returns:
    None
"""
def exec_video_compress(i):
    current_command = gen_command(i)
    print(f'\n\nCurrent Command:\n{current_command}\n')
    powershell(current_command)


"""
Attempts to delete a file. If the file cannot be deleted, it catches the exception and continues without raising an error.
"""
def exec_try_delete(file):
    try:
        print(f'Try to remove {file}')
        remove(file)
    except:
        pass


"""
This script processes video files, determining their codec and performing actions based on the codec type. It supports H.264, HEVC, AV1, and VP9 codecs. For H.264 and VP9 codecs, it executes video compression. For HEVC and AV1 codecs, it renames the files with a prefix indicating the codec. After processing, it prompts the user to confirm deletion of the original files.
"""
def main():
    while True:
        video_sets = get_video_inputs()
        if video_sets:
            chdir(sp(video_sets[0])[0])
            for i in video_sets:
                i = bn(i)
                ###
                current_vcodec = get_vcodec(i)
                i = validate_filename(i)
                match current_vcodec:
                    case 'h264':
                        exec_video_compress(i)
                    case 'hevc':
                        rename(i, f'HEVC__{i}')
                    case 'av1':
                        rename(i, f'AV1__{i}')
                    case 'vp9':
                        exec_video_compress(i)
            origin_list = '\n'.join([f'{index + 1}.{video}' for index,video in enumerate(video_sets)])
            if input(f'Do you want to delete all the original files? \n{origin_list}\n\nYour Choice (y/n）： ') == 'y':
                [exec_try_delete(file) for file in video_sets]
            else:
                print('Files not deleted')
        if not input('Continue? (y/n)： ') == 'y':
            break


"""
This script serves as the entry point for the Video Efficient Convert Program. It invokes the main function to execute the conversion process and prints a message upon completion before exiting with a status code of 0, indicating successful termination.
"""
if __name__ == '__main__':
    main()
    print('\nVideo Efficient Convert Program Ended.')
    exit(0)