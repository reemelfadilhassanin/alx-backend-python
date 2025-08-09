# Async Comprehension Project

## Description

This project demonstrates the use of asynchronous programming in Python using async generators and async comprehensions. It includes several tasks that showcase how to generate random numbers asynchronously and measure runtime.

## Tasks

1. **Async Generator**: 
   - A coroutine that yields 10 random numbers between 0 and 10, waiting for 1 second between each yield.
   - **File**: `0-async_generator.py`

2. **Async Comprehensions**: 
   - Collects 10 random numbers from the async generator using async comprehension.
   - **File**: `1-async_comprehension.py`

3. **Measure Runtime**: 
   - Measures the runtime of executing the async comprehension coroutine four times in parallel.
   - **File**: `2-measure_runtime.py`

## Usage

To run the code, ensure you have Python 3.7 or later installed. Execute the provided main scripts:

```bash
# For task 0
python3 0-main.py

# For task 1
python3 1-main.py

# For task 2
python3 2-main.py
