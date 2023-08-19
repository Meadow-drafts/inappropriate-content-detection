# Inappropriate Content Detection Repository

![Repository Banner](repository_banner.png)

Welcome to the Inappropriate Content Detection Repository! This repository contains a Python-based solution for detecting whether an uploaded image contains inappropriate or sensitive content. The system assigns a probability score to indicate the likelihood of the image belonging to various categories. The content of the image is assessed for appropriateness, and the results are provided to help users make informed decisions based on the content of the image.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Image content assessment for appropriateness and sensitivity.
- Probability scores for different categories to indicate the likelihood of content being inappropriate.
- Supports image loading from both local disk and HTTP links.
- User-friendly interface for quick and easy content evaluation.

## Getting Started

Follow these steps to set up and use the Inappropriate Content Detection system on your local machine.

### Prerequisites

- Python 3.x
- Pip package manager

### Installation

1. Clone this repository to your local machine or download the ZIP file.

```bash
git clone https://github.com/your-username/inappropriate-content-detection.git
```
2.Navigate to repository

```bash
cd inappropriate-content-detection
```
3.Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```
### Usage

Run the detect_inappropriate_content.py script to use the inappropriate content detection system. 
The script takes the path to an image file or an HTTPS link to an image as a command-line argument. 
It processes the image and displays the probability scores for different categories of content.
