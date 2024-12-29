"""
欢迎使用 PyVideoEfficent - 高级视频压缩工具！
Welcome to PyVideoEfficent - Advanced Video Compression Tool!

作者/Author: Volkath@amazoncloud
仓库/Repository: https://gitee.com/amazoncloud/py-video-efficent
版本/Version: 1.0.1
构建日期/Build Date: 2024.12.28

这是一个简单易用但功能强大的视频压缩工具。它可以:
This is an easy-to-use yet powerful video compression tool. It can:

✓ 使用先进的AV1编码器压缩视频,同时保持高画质
  Compress videos using advanced AV1 codec while maintaining high quality
✓ 利用NVIDIA显卡加速处理,速度更快
  Leverage NVIDIA GPU acceleration for faster processing  
✓ 智能分析视频并自动选择最佳压缩设置
  Intelligently analyze videos and choose optimal compression settings
✓ 支持批量处理多个文件
  Support batch processing of multiple files
✓ 自动管理输出文件
  Automatically manage output files

使用前请确保:
Before using, please ensure:

1. 已安装FFmpeg(在命令行输入"ffmpeg -version"测试)
   FFmpeg is installed (test by typing "ffmpeg -version" in command line)
2. 拥有支持AV1编码的NVIDIA显卡
   You have an NVIDIA GPU that supports AV1 encoding

详细使用说明请参考README.md文件
For detailed instructions, please refer to README.md
"""

from os import system as cmd, chdir, getcwd, popen as rcmd, rename, remove, _exit as quit
from os.path import split as sp, splitext as spt, basename as bn, exists, expanduser
from tkinter.filedialog import askopenfilenames as askfls
from time import sleep
from datetime import datetime
from re import sub
import tkinter as tk
from random import uniform

root = tk.Tk()
root.attributes('-topmost', 1)
root.withdraw()

init_dir = expanduser('~\\Downloads\\')
compress_rate = 0.5
min_compress_rate = 0.5
max_compress_rate = 1.5

#metadata
author = 'Volkath@amazoncloud'
encoder = 'PyVideoEfficent v1.0.1 Build 2024.12.28'
description = f'This video has been proccesed by {encoder}'

# Regular expression pattern for invalid filename characters:
# [^\w\s\-\.]+ means:
# ^ - Match any character that is NOT in the following set
# \w - Match word characters (letters, numbers, underscore)
# \s - Match whitespace characters (space, tab)
# \- - Match hyphen/dash
# \. - Match literal dot/period
# + - Match one or more occurrences
# This pattern will match any characters that are not alphanumeric, whitespace, hyphen or period
invalid_filename_rule = r'[^\w\s\-\.]+'

def powershell(s):
    cmd(f'powershell.exe;{s}')

def str_replace(s):
    s = sub(r'[\“\”]+', ' - ', s)
    # s = sub(r'[\""]+', '', s)
    return s

def validate_filename(i):
    global invalid_filename_rule
    name = spt(i)[0]
    new_filename = sub(invalid_filename_rule, '_', name)
    new_filename = str_replace(new_filename) + '.mp4'
    rename(i, new_filename)
    return new_filename

def get_video_duration(vp):
    cmd_parts = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        f'"{vp}"'
    ]
    duration_reslt = rcmd(' '.join(cmd_parts)).read().strip()
    return float(duration_reslt)

def get_video_filesize(vp):
    cmd_parts = [
        'ffprobe',
        '-v', 'error', 
        '-show_entries', 'format=size',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        '-i', f'"{vp}"'
    ]
    filesize_reslt = rcmd(' '.join(cmd_parts)).read().strip()
    return int(filesize_reslt)

def get_video_inputs():
    global init_dir
    return askfls(
        title='Select Video You Want to Proccess',
        filetypes=[('Video', '*.mp4 *.avi *.flv *.mkv')],
        initialdir=init_dir
    )

def get_video_bitrate(vp):
    cmd_parts = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=bit_rate',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        '-i', f'"{vp}"'
    ]
    bitrate_reslt = rcmd(' '.join(cmd_parts)).read().strip()
    try:
        return int(int(bitrate_reslt)/10**3)
    except:
        video_birate = (get_video_filesize(vp) * 8 / get_video_duration(vp) / 10**3) * 0.9
        return int(video_birate)

def get_vcodec(vp):
    cmd_parts = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0', 
        '-show_entries', 'stream=codec_name',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        f'"{vp}"'
    ]
    codec_reslt = rcmd(' '.join(cmd_parts))
    return codec_reslt.read().strip()

def get_metadata(title):
    global author, encoder, description
    current_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    metadata_parts = [
        '-metadata', f'artist=\'{author}\'',
        '-metadata', f'description=\'{description}\'',
        '-metadata', f'\'proccess_time={current_time}\'',
        '-metadata', f'title=\'{title}\'',
        '-metadata', f'\'software={encoder}\' ',
        '-metadata', f'date=\'{current_time}\' '
    ]
    return ' '.join(metadata_parts)

def gen_command(i):
    # Get metadata and calculate target bitrate
    metadata = get_metadata(i)
    origin_bitrate = get_video_bitrate(i)
    if origin_bitrate > 1500:
        target_bitrate = min(max(int(origin_bitrate * compress_rate), 1500), 15000)
    else:
        target_bitrate = origin_bitrate*0.9
    
    output_filename = f"AV1compressed__{spt(i)[0]}.mp4"

    # Build ffmpeg command
    ffmpeg_cmd = (
        f'ffmpeg -hide_banner -v info '
        f'-i \'{i}\' '
        f'-f mp4 '
        f'-bufsize 32768 '
        f'-threads 32 '
        f'-c:v av1_nvenc '
        f'{metadata} '
        f'-c:a copy '
        f'-b:v {target_bitrate}k '
        f'-y \'{output_filename}\' '
    )
    
    return ffmpeg_cmd

def exec_video_compress(i):
    current_command = gen_command(i)
    print(f'\n\nCurrent Command:\n{current_command}\n\n')
    powershell(current_command)

def exec_try_delete(file):
    try:
        print(f'Try to remove {file}')
        remove(file)
    except:
        pass

def main():
    while True:
        video_sets = get_video_inputs()
        if video_sets:
            chdir(sp(video_sets[0])[0])
            for video in video_sets:
                video = bn(video)
                video = validate_filename(video)
                codec = get_vcodec(video)
                
                # Process based on codec and bitrate
                if codec in ['hevc', 'av1'] and get_video_bitrate(video) <= 8000:
                    print(f'[Info] Detect {codec} video codec with low bitrate, skipping.\n')
                    rename(video, f'{codec.upper()}__{video}')
                else:
                    exec_video_compress(video)
            
            # Handle file deletion
            origin_list = '\n'.join(f'{i+1}.{v}' for i,v in enumerate(video_sets))
            powershell('Start-Process .')
            if input(f'[Command] Do you want to delete all the original files? \n{origin_list}\n\nYour Choice (y/n）： ') == 'y':
                [exec_try_delete(file) for file in video_sets]
            else:
                print('Files not deleted')
                
        choice = input('\nWould you like to process more videos? (y/n): ')
        if choice.lower() != 'y':
            print('\nThank you for using PyVideoEfficient!')
            break

if __name__ == '__main__':
    main()
    print('\nVideo Efficient Convert Program Ended.')
    quit(0)