# PythonTools

## Python Version
> python3 --version

Python 3.14.6

## Install python-dotenv
> pip install python-dotenv

## .env File
> touch .env
Place the .env file in this repository.

# FileOrganizeTool
> python FileOrganizeTool.py

## PythonTools - File Organizer

A Python script that automatically organizes files in specified directories into dedicated subfolders (`Images`, `Movies`, `Documents`, etc.) based on their file extensions (`.jpg`, `.mp4`, `.pdf`, etc.).

## Features ✨
- **Effortless Cleanup**: Instantly categorizes cluttered files in a directory with a single run.
- **Multi-Directory Support**: Allows you to specify multiple target folders in the `.env` file using comma-separated values.
- **Safe Execution**: Ignores existing folders and only targets files for processing.

---

## Usage 🚀

### 1. Setup
Create a `.env` file in the root directory of the project and specify the paths of the folders you want to organize (separate multiple paths with commas `,`).

```env
TARGET_DIRECTORIES=/Users/XXXXX/Downloads,/Users/XXXXX/Documents,/Users/XXXXX/Pictures,/Users/XXXXX/Music,/Users/XXXXX/Movies