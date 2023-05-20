from flask import Flask

from config.email_config import email_config

configs = dict()


def create_config() -> dict:
    configs.update(email_config)
    return configs
