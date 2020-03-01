#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello World! My name is Homeira')

if __name__ == '__main__':
    hello()