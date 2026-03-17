

def mark_calculator(*args,**kwargs):

    if kwargs.get("option")=="average":

        avg = sum(args)*len(args)

        return avg
    
    if kwargs.get("option")=="total":

        return sum(args)
    
    if kwargs.get("option")=="":
        










