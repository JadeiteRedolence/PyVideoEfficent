# Video Efficient Convert

A comprehensive Python script for efficiently converting and compressing videos using FFmpeg with AV1 codec.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Technical Details](#technical-details)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Performance Considerations](#performance-considerations)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Overview

Video Efficient Convert is a sophisticated video processing tool designed to optimize video files using the advanced AV1 codec. It leverages NVIDIA's hardware acceleration to provide efficient video compression while maintaining high quality. The script intelligently analyzes input videos and applies appropriate compression settings based on the source material.

## Prerequisites

### System Requirements
- Windows operating system (PowerShell support required)
- NVIDIA GPU with AV1 encoding support
- Minimum 8GB RAM recommended
- Python 3.6 or higher

### Software Dependencies
- FFmpeg must be installed and accessible from system PATH
  - To verify installation, run `ffmpeg -version` in terminal
- Python packages:
  - tkinter (usually comes with Python)
  - os
  - datetime
  - re
  - random

## Features

### Core Functionality
- Advanced video conversion to AV1 codec using NVIDIA hardware acceleration (av1_nvenc)
- Intelligent bitrate management system
- Multi-threaded processing for optimal performance
- Batch processing capability for multiple files
- Automatic file management and organization

### Video Processing
- Smart bitrate calculation based on source video characteristics
- Maintains aspect ratio and video quality
- Preserves original audio streams (direct copy)
- Configurable compression rates (0.5 to 1.5 range)
- Minimum bitrate floor of 1500k to ensure quality
- Maximum bitrate ceiling of 15000k for efficiency

### File Management
- Automatic handling of invalid filename characters
- Smart file renaming system
- Optional cleanup of source files
- Output file organization with descriptive prefixes

### Metadata Management
- Embedded processing timestamp
- Author attribution
- Description tags
- Customizable title metadata

## Technical Details

### Codec Implementation
The script utilizes NVIDIA's AV1 encoder (av1_nvenc) with the following optimizations:
- 32MB buffer size for smooth encoding
- 32 processing threads for maximum performance
- Automatic bitrate scaling based on source material
- Intelligent codec detection and processing decisions

### File Processing Pipeline
1. Input validation and filename sanitization
2. Video analysis (duration, bitrate, codec detection)
3. Smart compression parameter calculation
4. FFmpeg command generation with optimized parameters
5. Execution and monitoring
6. Output validation and organization

### Bitrate Management
- Dynamic bitrate calculation based on source video
- Compression rate multiplier (default: 0.5)
- Minimum bitrate protection: 1500 kbps
- Maximum bitrate cap: 15000 kbps
- Special handling for already optimized videos (HEVC/AV1)

## Installation

1. Ensure Python 3.6+ is installed:
   ```bash
   python --version
   ```

2. Install FFmpeg:
   - Download from official FFmpeg website
   - Add to system PATH
   - Verify installation:
     ```bash
     ffmpeg -version
     ```

3. Clone or download the script:
   ```bash
   git clone [repository-url]
   cd video-efficient-convert
   ```

## Usage

### Basic Operation
1. Run the script:
   ```bash
   python VideoEfficentConvert.py
   ```

2. Select input videos through the file dialog
   - Supports multiple file selection
   - Handles MP4, AVI, FLV, and MKV formats

3. Monitor processing progress
   - Command window shows current operations
   - Progress indicators for each stage

4. Review results
   - Processed files are prefixed with "AV1compressed__"
   - Optional cleanup of original files

### Advanced Usage
- Batch processing multiple files:
  1. Select multiple files in the dialog
  2. Processing queue handles files sequentially
  3. Individual status updates for each file

- Custom output management:
  1. Processed files automatically named
  2. Original files optionally preserved
  3. Organized output structure

## Configuration

### Adjustable Parameters
- `compress_rate`: Default 0.5 (50% of original bitrate)
- `min_compress_rate`: Minimum compression ratio (0.5)
- `max_compress_rate`: Maximum compression ratio (1.5)
- `init_dir`: Initial directory for file dialog

### Metadata Configuration
- Author name
- Description text
- Processing timestamp format
- Output filename format

## How It Works

### Video Analysis
1. **Duration Detection**
   ```python
   def get_video_duration(vp):
       # FFprobe command extracts exact duration
       # Returns floating-point seconds
   ```

2. **Bitrate Analysis**
   ```python
   def get_video_bitrate(vp):
       # Calculates video bitrate
       # Handles cases where direct detection fails
   ```

3. **Codec Detection**
   ```python
   def get_vcodec(vp):
       # Identifies current video codec
       # Used for processing decisions
   ```

### Processing Logic
1. **File Validation**
   - Checks filename validity
   - Sanitizes special characters
   - Ensures unique output names

2. **Compression Strategy**
   - Analyzes input characteristics
   - Calculates optimal parameters
   - Generates FFmpeg command

3. **Execution Flow**
   - Processes files sequentially
   - Monitors operation status
   - Handles errors gracefully

## Performance Considerations

### Optimization Techniques
- Multi-threaded processing
- Hardware acceleration usage
- Buffer size optimization
- Smart bitrate management

### Resource Usage
- CPU: Multi-threaded operation
- GPU: NVIDIA encoder utilization
- Memory: Efficient buffer management
- Storage: Temporary file handling

### Processing Time Factors
- Input file size
- Source video complexity
- Hardware capabilities
- Chosen compression settings

## Troubleshooting

### Common Issues

1. **FFmpeg Not Found**
   - Verify FFmpeg installation
   - Check system PATH
   - Confirm ffmpeg command accessibility

2. **GPU Encoding Errors**
   - Update NVIDIA drivers
   - Verify AV1 encoding support
   - Check GPU compatibility

3. **File Access Issues**
   - Check file permissions
   - Verify file path validity
   - Ensure sufficient disk space

### Error Messages

1. **FFmpeg Errors**
   - Command syntax issues
   - Codec compatibility problems
   - Resource limitations

2. **Python Errors**
   - Module import failures
   - File operation issues
   - Permission problems

### Solutions

1. **Installation Problems**
   - Reinstall FFmpeg
   - Update Python environment
   - Verify dependencies

2. **Processing Issues**
   - Adjust compression settings
   - Check input file integrity
   - Monitor system resources

## Contributing

### Development Guidelines
1. Fork the repository
2. Create feature branch
3. Follow coding standards
4. Submit pull request

### Testing
- Verify FFmpeg compatibility
- Test with various input formats
- Validate output quality
- Check resource usage

### Documentation
- Update README for new features
- Document code changes
- Maintain version history

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FFmpeg development team
- NVIDIA for AV1 encoder
- Python community
- Open source contributors