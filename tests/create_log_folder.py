import os

from click.testing import CliRunner

from app.cli import create_log_folder

runner = CliRunner()

def test_create_log_folder():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, './logs')
    log_file = os.path.join(root, './logs')
    # make a directory if it doesn't exist, checks if the logdir exists
    assert os.path.exists(logdir) == False
    # make a file and directory if they don't exist, checks if the log_file and the logdir exist
