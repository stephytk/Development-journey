

def employee_detail(**kwargs:dict): #{"name":"hari","dept":"hr","salary":2500}

    print(kwargs.get("name"))


employee_detail(name="hari",dept="hr",salary=25000)