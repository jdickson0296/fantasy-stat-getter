# fantasy-stat-getter
Data collector for my fantasy football team's


## Installation
Create a virtual environment and install the requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH="$PYTHONPATH:{path}/fantasy-stat-getter"
```

## Usage
Export ESPN environment variables
```bash
export ESPN_S2=""
export SWID=""
export LEAGUE_ID=""
export YEAR=""
```

Run the script
```bash
python3 src/espn/populate.py
```