from invoke import Responder
from fabric import Connection, task

# Establish SSH connection to the EC2 instance
c = Connection('22756463-vm')  # Replace with your EC2 instance identifier or hostname

# Create a Responder to handle the sudo password prompt
sudo_pass = Responder(
    pattern=r'\[sudo\] password:',
    response='your_password_here\n'  # Replace with your actual sudo password
)

@task
def update_and_install(ctx):
    try:
        # Update the instance's package lists and install necessary packages
        c.sudo('apt update -y', pty=True, watchers=[sudo_pass])  # Update package list
        c.sudo('apt upgrade -y', pty=True, watchers=[sudo_pass])  # Upgrade packages
        c.sudo('apt install -y python3-venv python3-pip nginx', pty=True, watchers=[sudo_pass])  # Install Python, pip, and Nginx
        print("Packages updated and installed successfully.")
    except Exception as e:
        print(f"Error during package installation: {e}")

@task
def create_project_directory(ctx):
    try:
        # Create a directory for the Django project
        c.sudo('mkdir -p ~/opt/wwc/mysites', pty=True, watchers=[sudo_pass])  # Create directory for the Django project
        print("Project directory created.")
    except Exception as e:
        print(f"Error creating project directory: {e}")

@task
def setup_virtualenv_and_django(ctx):
    try:
        # Create a Python virtual environment and install Django
        c.sudo('python3 -m venv myenv', pty=True, watchers=[sudo_pass])  # Create virtual environment
        c.sudo('source myenv/bin/activate && pip install django', pty=True, watchers=[sudo_pass])  # Activate virtualenv and install Django
        c.sudo('source myenv/bin/activate && django-admin startproject lab ~/opt/wwc/mysites/lab', pty=True, watchers=[sudo_pass])  # Create Django project

        # Create the 'polls' app
        c.sudo('cd ~/opt/wwc/mysites/lab && source ../myenv/bin/activate && python manage.py startapp polls', pty=True, watchers=[sudo_pass])
        print("Virtual environment and Django project set up successfully.")
    except Exception as e:
        print(f"Error setting up virtual environment and Django: {e}")

@task
def edit_django_files(ctx):
    try:
        # Edit polls/views.py
        polls_views = '''
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
    '''
        c.sudo("echo '{}' > ~/opt/wwc/mysites/lab/polls/views.py".format(polls_views), pty=True, watchers=[sudo_pass])

        # Edit polls/urls.py
        polls_urls = '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
        '''
        c.sudo("echo '{}' > ~/opt/wwc/mysites/lab/polls/urls.py".format(polls_urls), pty=True, watchers=[sudo_pass])

        # Edit lab/urls.py (project-level urls.py)
        lab_urls = '''
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
        '''
        c.sudo("echo '{}' > ~/opt/wwc/mysites/lab/lab/urls.py".format(lab_urls), pty=True, watchers=[sudo_pass])
        print("Django files edited successfully.")
    except Exception as e:
        print(f"Error editing Django files: {e}")

@task
def configure_nginx(ctx):
    try:
        # Configure Nginx to proxy requests to the Django development server
        c.sudo('rm /etc/nginx/sites-enabled/default', pty=True, watchers=[sudo_pass])  # Remove the default Nginx configuration
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
        c.sudo("echo '{}' | tee /etc/nginx/sites-available/myproject".format(nginx_config), pty=True, watchers=[sudo_pass])  # Write the Nginx config for Django
        c.sudo('ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/', pty=True, watchers=[sudo_pass])  # Enable the site in Nginx
        c.sudo('service nginx restart', pty=True, watchers=[sudo_pass])  # Restart Nginx to apply changes
        print("Nginx configured successfully.")
    except Exception as e:
        print(f"Error configuring Nginx: {e}")

@task
def run_django(ctx):
    try:
        # Run Django development server in the background on port 8000
        c.sudo('cd ~/opt/wwc/mysites/lab && source ../myenv/bin/activate && nohup python3 manage.py runserver 0.0.0.0:8000 &', pty=True, watchers=[sudo_pass])
        print('Django development server running on port 8000.')
    except Exception as e:
        print(f"Error running Django server: {e}")

@task
def setup_django_on_ec2(ctx):
    try:
        update_and_install(ctx)  # Step 1: Update and install necessary packages
        create_project_directory(ctx)  # Step 2: Create a project directory
        setup_virtualenv_and_django(ctx)  # Step 3: Set up Python virtual environment and Django
        edit_django_files(ctx)  # Step 4: Edit necessary Django files (views, urls)
        configure_nginx(ctx)  # Step 5: Configure Nginx for proxying to the Django server
        run_django(ctx)  # Step 6: Run the Django server on port 8000
    except Exception as e:
        print(f"Error in setup: {e}")


# Execute the setup function
if __name__ == "__main__":
    setup_django_on_ec2()
