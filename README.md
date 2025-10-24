# Speedy - Internet Speed Tester 🚀

A lightweight Python CLI tool for testing your internet speed with network information display.

```
________                 _________        
__  ___/_______________________  /____  __
_____ \___  __ \  _ \  _ \  __  /__  / / /
____/ /__  /_/ /  __/  __/ /_/ / _  /_/ / 
/____/ _  .___/\___/\___/\__,_/  _\__, /  
       /_/                       /____/   
```

## Features

- 📊 Download & Upload speed testing
- 🛜 Ping latency measurement
- 🌐 Local and public IP display
- ⚡ Fast and simple to use
- 🖥️ Cross-platform (Windows, macOS, Linux)

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/speedy.git
cd speedy

# Install dependencies
pip install speedtest-cli requests
```

## Usage

```bash
python speedtest.py
```

Press Enter when prompted, and the tool will display your network info and run the speed test.

## Example Output

```
Network Information:
--------------------------------------------------
🌐 Local IP Address:  192.168.1.100
🌍 Public IP Address: 203.0.113.45
--------------------------------------------------

...Starting test...
📉Download Speed: 245.67 Mbps
⬆️Upload Speed: 98.34 Mbps
🛜Ping: 12.45 ms
```

## Requirements

- Python 3.6+
- `speedtest-cli` - Speed testing
- `requests` - Public IP detection

## How It Works

1. Detects your local IP via socket connection
2. Fetches your public IP from ipify.org API
3. Runs speed test using speedtest.net servers
4. Displays results in Mbps with 2 decimal precision

## Troubleshooting

**Public IP not showing?** Check your internet connection or firewall settings.

**Speed test fails?** Ensure `speedtest-cli` is installed: `pip install --upgrade speedtest-cli`

## Contributing

Pull requests are welcome! Feel free to fork and improve.

## License

MIT License - See LICENSE file for details.

---

Made with ❤️ | Stay speedy! 🚀
