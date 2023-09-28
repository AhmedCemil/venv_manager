import subprocess

def get_req_by_venv(venv_name, req_txt_file):
  """Activates a Python virtual environment and generates a requirements.txt file listing all of the installed packages.

  Args:
    venv_name: The name of the Python virtual environment.
    req_txt_file: The path to the requirements.txt file.
  """

  subprocess.run(["source", f"{venv_name}/bin/activate"], check=True)
  subprocess.run(["pip", "freeze", "|", "grep", "-v", "#", "|", "sort", ">", req_txt_file], check=True)

def create_venv_by_req(venv_name, req_txt_file):
  """Creates a new Python virtual environment and installs all of the required packages from a requirements.txt file.

  Args:
    venv_name: The name of the new Python virtual environment.
    req_txt_file: The path to the requirements.txt file.
  """

  subprocess.run(["python3", "-m", "venv", venv_name], check=True)
  subprocess.run(["pip", "install", "--upgrade", "pip", "setuptools", "wheel"], check=True)
  subprocess.run(["pip", "install", "-r", req_txt_file], check=True)

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description="Automate the creation and management of Python virtual environments.")
  parser.add_argument("--get-req-by-venv", nargs=2, metavar=("VENV_NAME", "REQ_TXT_FILE"), help="Activates a Python virtual environment and generates a requirements.txt file listing all of the installed packages.")
  parser.add_argument("--create-venv-by-req", nargs=2, metavar=("VENV_NAME", "REQ_TXT_FILE"), help="Creates a new Python virtual environment and installs all of the required packages from a requirements.txt file.")

  args = parser.parse_args()

  if args.get_req_by_venv:
    venv_name, req_txt_file = args.get_req_by_venv
    get_req_by_venv(venv_name, req_txt_file)
  elif args.create_venv_by_req:
    venv_name, req_txt_file = args.create_venv_by_req
    create_venv_by_req(venv_name, req_txt_file)
  else:
    parser.print_help()
