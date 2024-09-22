from invoke import Responder
from fabric import Connection
import sys  # To use sys.exit for terminating the program on error

# Establish SSH connection to the EC2 instance
c = Connection('22756463-vm')  # Replace with your EC2 instance identifier or hostname

# Create a Responder to handle the sudo password prompt
sudo_pass = Responder(
    pattern=r'\[sudo\] password:',
    response='600770\n'  # Replace with your actual sudo password
)


def update_and_install():
    try:
        # Update the instance's package lists and install necessary packages
        c.sudo('apt update -y', pty=True, watchers=[sudo_pass])  # Update package list
        c.sudo('apt upgrade -y', pty=True, watchers=[sudo_pass])  # Upgrade packages
        c.sudo('apt install -y python3-venv python3-pip nginx', pty=True, watchers=[sudo_pass])  # Install Python, pip, and Nginx
        print("Packages updated and installed successfully.")
    except Exception as e:
        print(f"Error during package installation: {e}")
        sys.exit(1)  # Exit the program if there's an error


def create_project_directory():
    try:
        # Create a directory for the Django project
        c.sudo('mkdir -p ~/opt/wwc/mysites', pty=True, watchers=[sudo_pass])  # Create directory for the Django project
        # Ensure the user has ownership of the directory
        c.sudo('chown -R ubuntu:ubuntu ~/opt/wwc/mysites', pty=True, watchers=[sudo_pass])
        print("Project directory created.")
    except Exception as e:
        print(f"Error creating project directory: {e}")
        sys.exit(1)  # Exit the program if there's an error


def setup_virtualenv_and_django():
    try:
        # Create a Python virtual environment and install Django (without sudo)
        c.run('bash -c "cd ~/opt/wwc/mysites && python3 -m venv myvenv && source myvenv/bin/activate && pip install django && django-admin startproject lab && cd lab && python manage.py startapp polls"', pty=True)  # Create virtual environment
        print("Virtual environment and Django project set up successfully.")
    except Exception as e:
        print(f"Error setting up virtual environment and Django: {e}")
        sys.exit(1)


def edit_django_files():
    try:
        # Ensure the target directories have the correct ownership
        c.sudo('chown -R ubuntu:ubuntu /home/ubuntu/opt/wwc/mysites/lab', pty=True, watchers=[sudo_pass])

        # List the directories to verify permissions and existence
        c.run('ls -lR /home/ubuntu/opt/wwc/mysites/lab', pty=True)

        # Upload files to the remote server
        result = c.put('./polls/views.py', remote='/home/ubuntu/opt/wwc/mysites/lab/polls/views.py')
        print("Uploaded {0.local} to {0.remote}".format(result))

        result = c.put('./polls/urls.py', remote='/home/ubuntu/opt/wwc/mysites/lab/polls/urls.py')
        print("Uploaded {0.local} to {0.remote}".format(result))

        result = c.put('./lab/urls.py', remote='/home/ubuntu/opt/wwc/mysites/lab/lab/urls.py')
        print("Uploaded {0.local} to {0.remote}".format(result))

        # Verify the uploaded files
        c.run('ls -l /home/ubuntu/opt/wwc/mysites/lab/polls /home/ubuntu/opt/wwc/mysites/lab/lab', pty=True)

        print("Django files uploaded successfully.")

    except Exception as e:
        print(f"Error editing Django files: {e}")
        sys.exit(1)

        print("Django files edited successfully.")
    
    except Exception as e:
        print(f"Error editing Django files: {e}")
        sys.exit(1)



def configure_nginx():
    try:
        # # Use the find command to search for the 'nginx' folder
        # result = c.sudo('find / -type d -name "nginx"', pty=True, watchers=[sudo_pass])
        # print(result)

        # # Upload file to the remote server
        # result = c.put('./default', remote='/etc/nginx/sites-enabled/default')
        # print("Uploaded {0.local} to {0.remote}".format(result))

        # Upload file to a directory where you have write permissions
        result = c.put('./default', remote='/home/ubuntu/default')
        print("Uploaded {0.local} to {0.remote}".format(result))

        # Move the file to /etc/nginx/sites-enabled/ with sudo
        c.sudo('mv /home/ubuntu/default /etc/nginx/sites-enabled/default', pty=True, watchers=[sudo_pass])

        # Use sudo to restart Nginx after verifying the configuration
        c.sudo('service nginx restart', pty=True, watchers=[sudo_pass])
        
        print("Nginx configured and restarted successfully.")
    
    except Exception as e:
        print(f"Error configuring Nginx: {e}")
        sys.exit(1)


def run_django():
    try:
        # Command to run the Django server in the background in the virtual environment
        commands = '''
        source ~/opt/wwc/mysites/myvenv/bin/activate && \
        cd ~/opt/wwc/mysites/lab && \
        python3 manage.py runserver 8000
        '''
        # Execute all the commands in one shell with activated virtualenv
        c.run(f'bash -c "{commands}"', pty=True)
        print('Django development server running on port 8000.')
    except Exception as e:
        print(f"Error running Django server: {e}")
        sys.exit(1)


def setup_django_on_ec2():
    try:
        update_and_install()  # Step 1: Update and install necessary packages
        create_project_directory()  # Step 2: Create a project directory
        setup_virtualenv_and_django()  # Step 3: Set up Python virtual environment and Django
        edit_django_files()  # Step 4: Edit necessary Django files (views, urls)
        configure_nginx()  # Step 5: Configure Nginx for proxying to the Django server
        run_django()  # Step 6: Run the Django server on port 8000
    except Exception as e:
        print(f"Error in setup: {e}")
        sys.exit(1)  # Exit the program if there's a failure in setup


# Execute the setup function
if __name__ == "__main__":
    setup_django_on_ec2()
