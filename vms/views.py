from django.shortcuts import render
from pprint import pprint
import os, vagrant
from subprocess import Popen, PIPE

from .models import Customer, EnvironmentType, Environment


def get_environments(customer_id):
    environments = os.listdir('./customers/' + customer_id)


# Create your views here.
def index(request):
    customer = "Leerkotte"
    customer_id = "1"
    status = []

    customers = os.listdir("./customers")
    environments = os.listdir("./customers/1")

    current_environments = []
    current_environment = "./customers/1/gold"

    p = Popen(["vagrant", "status"], cwd=current_environment, stdout=PIPE)

    (stdout, stderr) = p.communicate()

    for line in stdout.strip().decode().splitlines():
        if "virtualbox" in line:
            print(line)
            status.append(line)

    #pprint(customers)
    #pprint(environments)

    context = { 'environments': environments, 'customer': customer, 'status': status }
    return render(request, 'vms/index.html', context)