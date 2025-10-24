# Internet Speed Tester 🚀

A powerful and easy-to-use Python application for testing your internet connection speed. Get accurate measurements of download speed, upload speed, and ping latency with detailed results and logging capabilities.

## Features

- **Download Speed Testing** - Measure your download bandwidth in Mbps
- **Upload Speed Testing** - Measure your upload bandwidth in Mbps
- **Ping Latency** - Check your connection latency in milliseconds
- **Server Selection** - Automatic selection of the best server or manual selection
- **Result Logging** - Save test results to CSV for historical tracking
- **Command-Line Interface** - Simple and intuitive CLI for quick tests
- **Cross-Platform** - Works on Windows, macOS, and Linux

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the required package directly:

```bash
pip install speedtest-cli
```

## Usage

### Basic Usage

Run a simple speed test:

```bash
python speed_tester.py
```

### Command-Line Options

```bash
# Run test with results saved to file
python speed_tester.py --save

# Display available servers
python speed_tester.py --list-servers

# Use specific server
python speed_tester.py --server 12345

# Run test without upload test
python speed_tester.py --no-upload

# Display version
python speed_tester.py --version
```

## Example Output

```
Testing internet speed...
=====================================
Server: Speedtest.net - City, Country
Ping: 12.45 ms
Download: 245.67 Mbps
Upload: 98.34 Mbps
=====================================
Test completed successfully!
```

## Project Structure

```
internet-speed-tester/
│
├── speed_tester.py      # Main application file
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
├── LICENSE             # License information
└── results/            # Directory for saved test results
    └── speed_tests.csv
```

## Configuration

You can customize the behavior by modifying the configuration variables in `speed_tester.py`:

```python
# Number of tests to run
TEST_COUNT = 1

# Enable/disable upload testing
ENABLE_UPLOAD = True

# Result file path
RESULT_FILE = "results/speed_tests.csv"
```

## Requirements

- `speedtest-cli` - Official Speedtest.net CLI client

See `requirements.txt` for the complete list of dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/internet-speed-tester.git`
3. Create a feature branch: `git checkout -b feature-name`
4. Make your changes and commit: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a Pull Request

## Testing

Run tests using pytest:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [speedtest-cli](https://github.com/sivel/speedtest-cli) by Matt Martz
- Inspired by the need for simple, reliable internet speed testing

## Support

If you encounter any issues or have questions:

- Open an [issue](https://github.com/yourusername/internet-speed-tester/issues)
- Check existing issues for solutions
- Contribute to discussions

## Roadmap

- [ ] Add GUI interface
- [ ] Implement scheduled testing
- [ ] Add email notifications for slow speeds
- [ ] Create detailed graphs and visualizations
- [ ] Support for multiple test runs with averaging

## Author

Your Name - [@yourhandle](https://twitter.com/yourhandle)

Project Link: [https://github.com/yourusername/internet-speed-tester](https://github.com/yourusername/internet-speed-tester)

---

Made with ❤️ by [Your Name]
