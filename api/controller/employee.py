# main.py
from typing import List

from api.controller import router
from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    department: str

employees: List[Employee] = []

@router.post("/employees", response_model=Employee)
def add_employee(employee: Employee):
    employees.routerend(employee)
    return employee

@router.get("/employees", response_model=List[Employee])
def get_employees():
    """Retrieve all employees.
    Returns a list of all employees in the system.
    """
    print("Retrieving all employees")
    return employees
