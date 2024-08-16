# C0dex Security

## Description

C0dex Security is a tool that uses the VirusTotal API to check the security of URLs. It offers a simple graphical interface using Tkinter, where users can enter a URL and receive information about possible threats.

## Features

- Checking URLs using VirusTotal API.
- User-friendly graphical interface with Tkinter.

## Prerequisites

-Python 3.x
- Python libraries: `requests`, `tkinter`
- VirusTotal API Keys

##Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/kayquec0dex/codex-security.git
   cd codex-security
   ```

2. Install dependencies:

   ```sh
   pip installation requests
   pip install tkinter
   ```

3. Add your API keys to the `config.json` file:

   ```json
   {
     "API_KEY_VIRUSTOTAL": "YOUR_API_KEY_VIRUSTOTAL"
   }
   ```

## Usage

1. Run the main script:

   ```sh
   python main.py
   ```

2. Enter the URL you want to check in the graphical interface and click "Check".

## Project Structure

```plain text
codex security/
│
├──config.json
├── icon.png
├── main.py
└── README.md
```

## Contribution

1. Project fork
2. Create a branch for your feature (git checkout -b feature/nova-feature)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to a branch (git push origin feature/nova-feature)
5. Create a new pull request

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
