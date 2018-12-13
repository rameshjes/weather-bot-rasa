# weather-bot-rasa

## Installation


Create new python3.5 environment and run ```pip install -r requirements.txt```
Install spacy language model: python -m spacy download en

## Usage

In One terminal run: ```python -m rasa_core_sdk.endpoint --actions actions```

In second terminal: ``` python -m rasa_core.run -d models/dialogue/ -u projects/default/default/rasa_bot/ --endpoints endpoints.yml ``` (You can send queries from this terminal) (To check possible queries find ```lucy/queries.txt```)
