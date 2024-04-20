# Scalable Bloom Filter for Frequency Estimation

## Overview
This project demonstrates the use of scalable Bloom filters for efficiently estimating item frequencies in large data streams. It includes a Python implementation of scalable Bloom filters and provides a simulation of item frequency distributions.

## Features
- Implementation of scalable Bloom filters for memory-efficient frequency estimation
- Simulation of item frequency distributions based on given parameters
- Estimation of item frequencies from simulated data streams
- Example usage and results

## Requirements
- Python 3.x
- pybloom-live library

## Installation
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your_username/scalable-bloom-filter.git
   ```
2. Install the required dependencies:
   ```
   pip install pybloom-live
   ```

## Usage
1. Run the `frequency_estimation.py` script to simulate item frequency distributions and estimate frequencies using scalable Bloom filters.
   ```
   python frequency_estimation.py
   ```

## Results
- The script outputs the number of items that appear four or more times and the items along with their estimated frequencies.
