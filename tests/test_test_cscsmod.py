#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `test_cscsmod` package."""
import pytest
import logging
from click.testing import CliRunner

from test_cscsmod import test_cscsmod
from test_cscsmod import cli
from test_cscsmod import utils


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'test_cli_project.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output
    dry_run_result = runner.invoke(cli.main, ['-n'])
    assert dry_run_result.exit_code == 0
    assert 'Is dry run' in dry_run_result.output
    version_result = runner.invoke(cli.main, ['-V'])
    assert version_result.exit_code == 0
    assert cli.__version__ in version_result.output


def test_count_to_log_level():
    assert utils.count_to_log_level(0) == logging.ERROR
    assert utils.count_to_log_level(1) == logging.WARNING
    assert utils.count_to_log_level(2) == logging.INFO
    assert utils.count_to_log_level(3) == logging.DEBUG
