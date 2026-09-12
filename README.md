# MaxProfitFinder

A simple Python script that finds the **maximum profit** from a list of monthly profits and losses.

Each value in the list represents the profit or loss for a particular month:

* **Positive values** → Profit
* **Negative values** → Loss

A `key` is used as a constraint to specify the number of **consecutive months** to consider when calculating the maximum profit.

## Example

```python
months_profit = [2, -9, 3, 4, 8, -7, -3, 2]
key = 6
```

Here, `key = 6` means that the program compares consecutive groups of **6 months** and finds the group with the highest total profit.

For the example above:

```text
[2, -9, 3, 4, 8, -7] = 1
[-9, 3, 4, 8, -7, -3] = -4
[3, 4, 8, -7, -3, 2] = 7
```

Therefore, the maximum profit is:

```text
7
```

## Features

* Finds the maximum profit over a fixed number of consecutive months.
* Supports both positive and negative values.
* Simple Python implementation.
* Uses a configurable `key` value.
* Useful for practicing array/list manipulation and algorithmic problem solving.

## Getting Started

### Prerequisites

Make sure you have **Python 3.8+** installed.

Check your Python version:

```bash
python --version
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/mwchuchu/Maxprofitfinder.git
cd Maxprofitfinder
```

No external Python packages are required.

## Usage

Run the Python script:

```bash
python maxprofitfinder.py
```

You can modify the monthly profits and `key` according to your requirements:

```python
months_profit = [2, -9, 3, 4, 8, -7, -3, 2]
key = 6
```

The program will calculate the maximum total profit for any consecutive sequence of `key` months.

## How It Works

The algorithm uses a **sliding window** approach.

Instead of calculating the sum of every group of `key` months from scratch, the algorithm:

1. Calculates the sum of the first `key` months.
2. Moves the window one month forward.
3. Removes the value leaving the window.
4. Adds the new value entering the window.
5. Keeps track of the maximum sum.
6. Continues until all possible consecutive groups have been evaluated.

### Example

Given:

```text
months_profit = [2, -9, 3, 4, 8, -7, -3, 2]
key = 6
```

The possible windows are:

```text
Window 1: [2, -9, 3, 4, 8, -7] = 1

Window 2: [-9, 3, 4, 8, -7, -3] = -4

Window 3: [3, 4, 8, -7, -3, 2] = 7
```

Maximum profit:

```text
7
```

## Algorithm Complexity

If there are `n` months and the window size is `key`:

**Time Complexity:**

```text
O(n)
```

**Space Complexity:**

```text
O(1)
```

The sliding-window technique makes the solution more efficient than repeatedly calculating the sum of each window.

## Project Structure

```text
Maxprofitfinder/
│
├── maxprofitfinder.py
├── README.md
└── LICENSE
```

## Input Requirements

The program expects:

* A list containing numerical profit/loss values.
* A `key` representing the number of consecutive months to compare.
* `key` should be greater than `0`.
* `key` should not be greater than the number of months in the list.

Example:

```python
months_profit = [10, -5, 20, -2, 15]
key = 3
```

## Possible Applications

This type of algorithm can be useful for:

* Financial analysis
* Monthly business performance analysis
* Revenue trend analysis
* Investment analysis
* Sales performance monitoring
* Time-series calculations
* Learning sliding-window algorithms

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new feature"
```

5. Push the branch:

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

## License

This project is licensed under the **MIT License**.

You are free to use, modify, distribute, and contribute to this project, subject to the terms of the MIT License.

See the [LICENSE](LICENSE) file for the complete license text.

## Author

**Muhammad Maawaz**

GitHub: `mwchuchu`

---

⭐ If you find this project useful, consider giving the repository a star!
