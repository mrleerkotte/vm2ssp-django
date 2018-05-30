from django.shortcuts import render
from pprint import pprint
import os
from subprocess import Popen, PIPE

def get_customers():
    customers = os.listdir('./customers/')

    return customers


def get_environments(customer, customer_id):
    environments = os.listdir('./customers/' + customer_id + "_" + customer)

    return environments


def get_environments_status(customer, customer_id, environments):
    status = []

    for environment in environments:
        state = {}
        p = Popen(["vagrant", "status"], cwd='./customers/' + customer_id + "_" + customer + "/" + environment, stdout=PIPE)

        (stdout, stderr) = p.communicate()

        comment = []
        state['environment'] = environment

        for line in stdout.strip().decode().splitlines():

            if "virtualbox" in line:
                # print(line)
                comment.append(line)

        pprint(stdout.decode())
        if "running" in stdout.strip().decode():
            state['created'] = True
        else:
            state['created'] = False

        state['comment'] = comment

        status.append(state)

    return status


def deploy_environment(request, customer, customer_id, environment):
    status = []
    p = Popen(["vagrant", "up"], cwd='./customers/' + customer_id + "_" + customer + "/" + environment, stdout=PIPE)

    (stdout, stderr) = p.communicate()

    for line in stdout.strip().decode().splitlines():
        status.append(line)

    context = {'customer': customer, 'customer_id': customer_id, 'environment': environment, 'status': status}
    return render(request, 'vms/deploy.html', context)


def destroy_environment(request, customer, customer_id, environment):
    status = []
    p = Popen(["vagrant", "destroy", "-f"], cwd='./customers/' + customer_id + "_" + customer + "/" + environment, stdout=PIPE)

    (stdout, stderr) = p.communicate()

    for line in stdout.strip().decode().splitlines():
        status.append(line)

    context = {'customer': customer, 'customer_id': customer_id, 'environment': environment, 'status': status}
    return render(request, 'vms/destroy.html', context)


def select_customer(request):
    customers = []
    result = get_customers()

    for customer in result:
        i = customer.split("_")
        pprint(i)
        customers.append(i)

    context = {'customers': customers}
    return render(request, 'vms/login.html', context)


# Create your views here.
def index(request):
    login = request.GET.get('customer', '')
    login = login.split("_")
    customer = login[1]
    customer_id = login[0]

    environments = get_environments(customer, customer_id)
    status = get_environments_status(customer, customer_id, environments)

    pprint(status)

    context = {'environments': environments, 'customer': customer, 'customer_id': customer_id, 'status': status}
    return render(request, 'vms/index.html', context)
