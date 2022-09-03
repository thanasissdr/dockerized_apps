import os

ENV_VARIABLES = ["RANDOM_VARIABLE", "USERNAME"]

for env_variable in ENV_VARIABLES:
    env_variable_value = os.getenv(env_variable, "Not found")

    print(f"Environment variable {env_variable} value: {env_variable_value}")