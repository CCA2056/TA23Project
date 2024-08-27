# Django Project - Local Setup Guide

## Overview

This document outlines the steps required to set up and run this Django project on your local machine.

## Prerequisites

Before you begin, ensure that your system has the following installed:

- **Python 3.12**
- **pip** (Python package installer)

## Installation and Setup

### 1. Download the repository

First, download the repository. You will need to know what branch you are downloading from first.
You can go here to look at all the branches, and click on the one that you want to download from: https://github.com/illonion/FIT5120-Project/branches.

Once on the page, you'll see the big green "Code" button. Click on it, and click on "Download ZIP", which will download the folder into you directory. Make sure to unzip the file once you have downloaded it.
![image](https://github.com/user-attachments/assets/6b1d05e6-099c-4a9a-8030-52c1b73be808)

Go to the directory which you downloaded, and unzip it. Using the command line, go to the folder in which the "manage.py" file is located and run this command: pip install -r requirements.txt

### 2. Run the local server
Within the same directory, run: python manage.py runserver

### 3. Access the website!
You can do so here:
http://127.0.0.1:8000/
