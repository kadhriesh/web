# main.py
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    department: str

employees: List[Employee] = []

@app.post("/employees", response_model=Employee)
def add_employee(employee: Employee):
    employees.append(employee)
    return employee

@app.get("/employees", response_model=List[Employee])
def get_employees():
    """Retrieve all employees.
    Returns a list of all employees in the system.
    """
    print("Retrieving all employees")
    return employees
