from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class employee:
    def __init__(self, name, sunday, monday, tuesday, wednesday, thursday, friday, saturday):
        self.name = name
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday

employees = []


def getInput(request):
	return render(request, "employeeDataInput.html")


def createEmployee(request):
    name = str(request.GET["employeeName"])
    sunday = str(request.GET["sunday"])
    if sunday == "Sunday":
        sunday = "11AM-7PM"
    else:
        sunday = ""
    monday = str(request.GET["monday"])
    if monday == "Monday":
        monday = "11AM-7PM"
    else:
        monday = ""
    tuesday = str(request.GET["tuesday"])
    if tuesday == "Tuesday":
        tuesday = "11AM-7PM"
    else:
        tuesday = ""
    wednesday = str(request.GET["wednesday"])
    if wednesday == "Wednesday":
        wednesday = "11AM-7PM"
    else:
        wednesday = ""
    thursday = str(request.GET["thursday"])
    if thursday == "Thursday":
        thursday = "11AM-7PM"
    else:
        thursday = ""
    friday = str(request.GET["friday"])
    if friday == "Friday":
        friday = "11AM-7PM"
    else:
        friday = ""
    saturday = str(request.GET["saturday"])
    if saturday == "Saturday":
        saturday = "11AM-7PM"
    else:
        saturday = ""
    currentEmployee = employee(name, sunday, monday, tuesday, wednesday, thursday, friday, saturday)
    employees.append(currentEmployee)
    return render(request, "employeeDataInput.html")

def createSchedule(request):
    tableBegin = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <h3>Weekly Schedule</h3>

    <table bgcolor="black">
        <tr bgcolor="grey">
            <th>Employee Name</th>
            <th>Sunday</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
            <th>Saturday</th>
        </tr>"""
    remaining = ""
    for employee in employees:
            addRow = "<tr align=\"center\" bgcolor=\"white\">" + "<td bgcolor=\"grey\">" + employee.name + "</td> <td>" + employee.sunday + "</td> <td>" + employee.monday + "</td> <td>" + employee.tuesday + "</td> <td>" + employee.wednesday + "</td> <td>" + employee.thursday + "</td> <td>" + employee.friday + "</td> <td>" + employee.saturday + "</td> </tr>"
            remaining += addRow
    tableEnd = """</table>

</body>
</html>"""
    htmlPage = tableBegin + remaining + tableEnd
    return HttpResponse(htmlPage)

def resetSchedule(request):
    employees.clear()
    return render(request, "employeeDataInput.html")
