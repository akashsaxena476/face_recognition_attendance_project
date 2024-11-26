import subprocess

def run_script(script_name):
    try:
        result = subprocess.run(['python', script_name], check=True)
        print(f"Successfully ran {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    scripts = ['create_update_schema.py', 'capture_faces.py', 'train_model.py', 'recognize_faces.py']
    
    for script in scripts:
        run_script(script)
