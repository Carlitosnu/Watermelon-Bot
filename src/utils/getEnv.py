from os import getenv
from dotenv import load_dotenv


def getEnv(envName):
    return getenv(envName)


def load_env():
    load_dotenv()
