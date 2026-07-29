import json
import logging

import azure.functions as func

app = func.FunctionApp(
    http_auth_level=func.AuthLevel.ANONYMOUS
)


@app.route(
    route="health",
    methods=["GET"]
)
def health(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Health endpoint was called.")

    response = {
        "status": "healthy",
        "service": "CloudX Employee API"
    }

    return func.HttpResponse(
        body=json.dumps(response),
        status_code=200,
        mimetype="application/json"
    )


@app.route(
    route="employees",
    methods=["GET"]
)
def get_employees(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Employees endpoint was called.")

    employees = [
        {
            "id": 1,
            "name": "John Smith",
            "department": "Cloud Engineering"
        },
        {
            "id": 2,
            "name": "Sarah Johnson",
            "department": "Cybersecurity"
        },
        {
            "id": 3,
            "name": "Michael Brown",
            "department": "Platform Operations"
        }
    ]

    response = {
        "application": "CloudX Employee API",
        "count": len(employees),
        "employees": employees
    }

    return func.HttpResponse(
        body=json.dumps(response),
        status_code=200,
        mimetype="application/json"
    )


@app.route(
    route="employees/{employee_id:int}",
    methods=["GET"]
)
def get_employee(req: func.HttpRequest) -> func.HttpResponse:
    employee_id = req.route_params.get("employee_id")

    employees = {
        "1": {
            "id": 1,
            "name": "John Smith",
            "department": "Cloud Engineering"
        },
        "2": {
            "id": 2,
            "name": "Sarah Johnson",
            "department": "Cybersecurity"
        },
        "3": {
            "id": 3,
            "name": "Michael Brown",
            "department": "Platform Operations"
        }
    }

    employee = employees.get(str(employee_id))

    if employee is None:
        return func.HttpResponse(
            body=json.dumps(
                {
                    "error": "Employee not found",
                    "employee_id": employee_id
                }
            ),
            status_code=404,
            mimetype="application/json"
        )

    return func.HttpResponse(
        body=json.dumps(employee),
        status_code=200,
        mimetype="application/json"
    )