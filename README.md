# Phyphox Connection

## Overview
Phyphox Connection is a Python library designed to interface with the Phyphox app, allowing users to collect and analyze data from smartphone sensors. This project provides tools to establish a connection, collect data in real time, and utilize various filters and processing functions.

## Features
- Real-time data collection from Phyphox enabled smartphone sensors.
- Data analysis and visualization using Python.
- Examples included for velocity graphs and seismic exploration.

## Installation
```bash
git clone <https://github.com/FeRsOmBrA/Phyphox-connection.git>
cd Phyphox-connection
# It's recommended to use a virtual environment
python -m venv venv
source venv/bin/activate
# Install required packages
pip install -r requirements.txt
```
## Usage

Here's a quick start example on how to use the library to connect to the Phyphox app and start data collection:

```python
from phyphox_connection import PhyphoxConnection

# Replace 'ip_address' with your smartphone's IP displayed in the Phyphox app
connection = PhyphoxConnection(ip_address="192.168.x.x")
connection.start_experiment()
data = connection.get_data()
print(data)
connection.stop_experiment()

```

## Desktop App

I also created a friendly Desktop App for use this library, you can do the following:

- Start/Stop data collection from several devices running Phyphox.
- Configure and apply ML filters to analyze the collected data.
- Export data to different formats for further analysis in other applications or systems.

After cloning the repository, simply run this:

```bash
python phyphox_connection.py
```


## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](notion://www.notion.so/LICENSE) file for details.

## Contact

For any queries, you can reach out to [GitHub Profile](https://github.com/FeRsOmBrA) [LinkedIn Profile](https://www.linkedin.com/in/ferney-castano/).
