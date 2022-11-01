import yaml

with open('config.yml', 'r') as file:
    prime_service = yaml.safe_load(file)

# print(prime_service['prime_numbers'][0])
# print(prime_service['rest']['prueba'][0]['env2'][0])

resultados = prime_service['rest']['prueba'][0]['env2'][1]

print(yaml.dump(resultados))