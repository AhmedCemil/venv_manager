import os
import subprocess

def create_venv(venv_name, subprocess_count = 3):
  """Creates a new Python virtual environment

  Args:
    venv_name: The name of the Python virtual environment.
  """
  if os.path.exists(rf"{os.getcwd()}\{venv_name}"):
    print(rf"Warning: The directory ({os.getcwd()}\{venv_name}) exists! Process aborted.")
    return False
  else:
    print(f"\nProcess 1/{subprocess_count}: Creating a Python virtual environment ({venv_name})")
    subprocess.run(args=f"python -m venv {venv_name}", check=True)
    print(f"\nA Python virtual environment ({venv_name}) is created.\n\nProcess 2/{subprocess_count}: Making pip the most up-to-date version.\n")
    subprocess.run(args=rf"{venv_name}\Scripts\python.exe -m pip install --upgrade pip", check=True)
    print(f"\npip has been upgraded successfully.\n\nProcess 3/{subprocess_count}: Making setuptools and wheel the most up-to-date version.\n")
    subprocess.run(args=rf"{venv_name}\Scripts\pip.exe install --upgrade setuptools wheel", check=True)
    print(f"""\nsetuptools and wheel have been upgraded successfully.\n""")
    if subprocess_count == 3:
      print("Done.\n")
    return True
  
def create_venv_by_req(venv_name, req_txt_file):
  """Creates a new Python virtual environment and installs all of the required packages from a requirements.txt file.

  Args:
    venv_name: The name of the new Python virtual environment.
    req_txt_file: The path to the requirements.txt file.
  """
  if create_venv(venv_name, subprocess_count=4):
    print(f"\nProcess 4/4: Installing all packages in {req_txt_file}\n")
    subprocess.run(args=rf"{venv_name}\Scripts\pip.exe install --upgrade -r {req_txt_file}", check=True)
    print("\nDone.\n")

def create_req_by_venv(req_txt_file, venv_name):
  """Creates a requirements.txt file contains all of the required packages from a python virtual enviroment.

  Args:
    req_txt_file: The path to the requirements.txt file.
    venv_name: The name of the Python virtual environment.
  """
  print(f"\nCreating a {req_txt_file} file.\n")
  subprocess.run(args=rf"{venv_name}\Scripts\pip.exe pip freeze | grep -v # | sort > {req_txt_file}", check=True)
  print("\nDone.\n")

def delete_venv(venv_name):
  """Deletes a python virtual enviroment.

  Args:
    venv_name: The name of the Python virtual environment.
  """
  if os.path.exists(rf"{os.getcwd()}\{venv_name}"):
    print(f"\nDeleting python virtual environment ({venv_name}).\n")
    subprocess.run(args=rf"rmdir /s /q {os.getcwd()}\{venv_name}", shell=True, check=True)
    print("Done.\n")
  else:
    print(rf"Warning: The directory ({os.getcwd()}\{venv_name}) not exists! Process aborted.")

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description="Automate the creation and management of Python virtual environments.")
  parser.add_argument("--create-venv", nargs=1, metavar=("VENV_NAME"), help="Creates a new Python virtual environment.")
  parser.add_argument("--create-venv-by-req", nargs=2, metavar=("VENV_NAME", "REQ_TXT_FILE"), help="Creates a new Python virtual environment and installs all of the required packages from a requirements.txt file.")
  parser.add_argument("--create-req-by-venv", nargs=2, metavar=("REQ_TXT_FILE", "VENV_NAME"), help="Creates a requirements.txt file contains all of the required packages from a python virtual enviroment.")
  parser.add_argument("--delete-venv", nargs=1, metavar=("VENV_NAME"), help="Deletes a python virtual enviroment.")

  args = parser.parse_args()

  if args.create_venv:
    venv_name = args.create_venv
    create_venv(venv_name[0])
  elif args.create_venv_by_req:
    venv_name, req_txt_file = args.create_venv_by_req
    create_venv_by_req(venv_name[0], req_txt_file[0])
  elif args.create_req_by_venv:
    req_txt_file, venv_name = args.create_req_by_venv
    create_req_by_venv(req_txt_file[0], venv_name[0])
  elif args.delete_venv:
    venv_name = args.delete_venv
    delete_venv(venv_name[0])
  else:
    parser.print_help()
