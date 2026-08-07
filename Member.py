class Member:
    def __init__(self, member_name, member_id):
        self.name=member_name
        self.id=member_id
        self.list_of_current_loans=[]

    def __str__(self):
            return(f"Member Name: {self.name}",
                   f"Member ID: {self.id}")    
