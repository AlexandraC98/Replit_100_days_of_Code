class job:
  name=None
  salary=None
  hours=None

  def __init__(self,name,salary,hours):
    self.name=name
    self.salary=salary
    self.hours=hours

  def print(self):
    print(f"""Job type: {self.name}
Salary: {self.salary}
Hours worked: {self.hours}""")


class doctor(job):
  speciality=None
  years=None

  def __init__(self,salary, hours, speciality,years):
    self.name="Doctor"
    self.salary=salary
    self.hours=hours
    self.speciality=speciality
    self.years=years

  def print(self):
    print(f"""Job type: {self.name}
Salary: {self.salary}
Hours worked: {self.hours}
Speciality: {self.speciality}
Years of experience: {self.years}""")


class teacher(job):
  subject=None
  position=None

  def __init__(self,salary,hours,subject,position):
    self.name="CS Teacher"
    self.salary=salary
    self.hours=hours
    self.subject=subject
    self.position=position

  def print(self):
    print(f"""Job type: {self.name}
Salary: {self.salary}
Hours worked: {self.hours}
Suvject: {self.subject}
Position: {self.position}""")

lawyer=job("Lawyer","Squillions","60")
lawyer.print()

print()

doc=doctor("Doing very nicely after some years","Definitely >50 per week", "Paedriatitian", "A lot")
doc.print()

print()

teach=teacher("I bet not enough","All of them","CS","CS Teacher")
teach.print()
