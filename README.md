# API Server for LogicNet Subnet 35

## Overview

This project features a FastAPI application that provides an endpoint for querying miners in **Subnet35: LogicNet** based on specific criteria. Users can send math questions to the API server, which then forwards these questions to subnet validators and returns the answers.

## Setup

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/LogicNet-Subnet/logicnet-api-server.git
   cd logicnet-api-server
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Set up your Bittensor wallet and obtain the necessary credentials.
2. Configure your environment variables or update the `config()` method in `neuron.py` with your specific settings.

## Running the Server

To start the API server, run the following command:
```
python app.py
```
