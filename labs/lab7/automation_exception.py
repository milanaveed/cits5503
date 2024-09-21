from fabric import Connection
from fabric.transfer import Transfer
import os

# Establish SSH connection to the EC2 instance
c = Connection('22756463-vm')  # Replace with your EC2 instance identifier or hostname

def update_and_install():
    try:
        # Update the instance's package lists and install necessary packages
        c.sudo('apt update -y')  # Update package list
        c.sudo('apt upgrade -y')  # Upgrade packages
        c.sudo('apt install -y python3-venv python3-pip nginx')  # Install Python virtual environment, pip, and Nginx
        print("Packages updated and installed successfully.")
    except Exception as e:
        print(f"Error during package installation: {e}")

def create_project_directory():
    try:
        # Create a directory for the Django project
        c.sudo('mkdir -p ~/opt/wwc/mysites')  # Create directory for the Django project
        print("Project directory created.")
    except Exception as e:
        print(f"Error creating project directory: {e}")

def setup_virtualenv_and_django():
    try:
        # Create a Python virtual environment and install Django
        c.sudo('python3 -m venv myenv')  # Create virtual environment
        c.sudo('source myenv/bin/activate && pip install django')  # Activate virtualenv and install Django
        c.sudo('source myenv/bin/activate && django-admin startproject lab ~/opt/wwc/mysites/lab')  # Create Django project

        # Create the 'polls' app
        c.sudo('cd ~/opt/wwc/mysites/lab && source ../myenv/bin/activate && python manage.py startapp polls')
        print("Virtual environment and Django project set up successfully.")
    except Exception as e:
        print(f"Error setting up virtual environment and Django: {e}")

def edit_django_files():
    try:
        # Edit polls/views.py
        polls_views = '''
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
    '''
        c.sudo("echo '{}' > ~/opt/wwc/mysites/lab/polls/views.py".format(polls_views))

        # Edit polls/urls.py
        polls_urls = '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
        '''
        c.sudo("echo '{}' > ~/opt/wwc/mysites/lab/polls/urls.py".format(polls_urls))

        # Edit lab/urls.py (project-level urls.py)
        lab_urls = '''
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
        '''
        c.sudo("echo '{}' > ~/opt/wwc/mysites/lab/lab/urls.py".format(lab_urls))
        print("Django files edited successfully.")
    except Exception as e:
        print(f"Error editing Django files: {e}")

def configure_nginx():
    try:
        # Configure Nginx to proxy requests to the Django development server
        c.sudo('rm /etc/nginx/sites-enabled/default')  # Remove the default Nginx configuration
        nginx_config = '''
        server {
            listen 80;
            server_name 22756463-vm;

            location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
        '''
        c.sudo("echo '{}' | tee /etc/nginx/sites-available/myproject".format(nginx_config))  # Write the Nginx config for Django
        c.sudo('ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/')  # Enable the site in Nginx
        c.sudo('service nginx restart')  # Restart Nginx to apply changes
        print("Nginx configured successfully.")
    except Exception as e:
        print(f"Error configuring Nginx: {e}")

def run_django():
    try:
        # Run Django development server in the background on port 8000
        c.sudo('cd /opt/wwc/mysites/lab && source ../myenv/bin/activate && nohup python3 manage.py runserver 0.0.0.0:8000 &')
        print('Django development server running on port 8000.')
    except Exception as e:
        print(f"Error running Django server: {e}")

# Main function to orchestrate the setup
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

# Execute the setup function
if __name__ == "__main__":
    setup_django_on_ec2()
