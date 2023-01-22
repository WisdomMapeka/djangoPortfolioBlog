import json

with open('../../../portfoliosite.json') as config_file:
    config = json.load(config_file)

print(config['SECRET_KEY'])