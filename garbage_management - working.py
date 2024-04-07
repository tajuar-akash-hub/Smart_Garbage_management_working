
Garbage_types = ['Biodegradeable_garbage','non_Biodegradeable_garbage']
Garbage_sub_types = ['recyclable','non_recyclable']
# garbage_source= ['Household garbage','SME','Industrial garbage','GO','Industrial garbage']

#it returns a dictionary after selection garbage 
def garbage_type_and_amount_selection():
    for i in range (2):
        print(f'select {i} for {Garbage_types[i]}')

    select = int(input("Enter any number : "))

    if select == 0:
        amount = int(input("Enter garbage amount : "))
        garbage_name = Garbage_types[select]
        # user_garbage_collection_in_source.append({'garbage_name':garbage_name,'amount':amount}) 
        garbage_dict ={'garbage_name':garbage_name,'amount':amount}
        return garbage_dict

    elif select == 1:
        print("Please select any subtypes from here")
        for i in range(2):
            print(f'select {i} for {Garbage_sub_types[i]}')
        subtype_select = int(input("Enter any number : "))
        amount = int(input("Enter garbage amount "))
        garbage_name = Garbage_sub_types[subtype_select]
        garbage_type_name = 'non_Biodegradeable_garbage'
        garbage_dict = {'garbage_name':garbage_name,'amount':amount,'garbage_type':garbage_type_name} 
        return garbage_dict

#billing 
def billing_calculation(garbage):
    
    bill_list = []
    garbage_list_for_billing = []
    garbage_list_for_billing.append(garbage)
    
    
    for grbg in garbage_list_for_billing:
            grbg_name = grbg['garbage_name']
            grbg_amount = grbg['amount']
            bill = 0
          
            if grbg_name == 'Biodegradeable_garbage':
                bill = grbg_amount*0
                print("and bill = ",bill)
                

            elif grbg_name=='non_recyclable':
                bill = grbg_amount*5
                print("and bill = ",bill)
                

            elif grbg_name == 'recyclable':
                bill = grbg_amount*2
                print("and bill = ",bill)

             # Append billing information to the bill_list
            bill_info = {'garbage_type': grbg_name, 'amount': grbg_amount, 'bill': bill}
            bill_list.append(bill_info)


            # Append bill_list to total_bill
            user_obj.total_bill.extend(bill_list)
            bill_list.clear()

            #clearing bill list
            
#for login mechanism 


#for login mechanism ends

class User:
    user_list = []
    def __init__(self,name,email,address,password) :
        self.user_name = name
        self.user_address = address
        self.email = email
        self.password = password
        self.total_bill=[]

        User.user_list.append(self)

    @classmethod 
    def user_exists(cls,email,password):
        for user in cls.user_list:
            if user.email == email and user.password == password :
                return user
        return None

class Admin:
    def __init__(self) -> None:
        pass
    def admin_login(self):
        username = input("Admin Username: ")
        password = input("Admin Password: ")
        return username == "admin" , password == "admin"
    
    def create_account(self,name,email,address):
        user = User(name, email, address)
        User.user_list.append(user)

    def see_user_Accounts(self):
        for user in User.user_list:
            print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.Balance}\n")

    def print_user_details(self):
        print("--------------- Printing user detials -----------\n")
        print(f'{self.user_name} , {self.user_address} , {self.total_bill}')
    
    def total_bill_calculation(self):
        sum=0
        for total_bill_amount in self.total_bill:
            amount = total_bill_amount['amount']
            sum+=amount
        print(sum)





 
class source_bin:
    
    source_garbage= []

    def receive_garbage(self,garbage):
        #checking capacity 
        if garbage['amount'] >10 :
            print("********warning:**Sorry 10 garbage at a time****")
        else :
            self.source_garbage.append(garbage)
             #billing start
            billing_calculation(garbage) #passing a dictinary
            #billing ends 

    def printing_all_garbage(self):
        print("Printing garbage details in source bin --------")
        for grbg in self.source_garbage:
            print(grbg)
        print("source bin printing ends------------------------")

    def sending_garbage_to_GMP(self):
        gmp_bin_obj = GMP_Bin()
        gmp_bin_obj.receive_garbage_from_source(self.source_garbage)

        #test code start ----------
        gmp_bin_obj.printing_gmp_garbage()
        
        gmp_bin_obj.allocation_of_garbage_to_bins()
        
        #test code ends --------------

class GMP_Bin: #underground tunnel city corp. bin
    def __init__(self) :
        self.GMP_garbage = []
        self.capacity = 10
    # GMP_garbage=[]
    def receive_garbage_from_source(self,garbage_from_source):
        self.GMP_garbage.extend(garbage_from_source)
        # test function
    def printing_gmp_garbage(self):
        print("****printing all garbage in gmp bins------\n")
        # print(self.GMP_garbage)
        for grbg in self.GMP_garbage:
            print(grbg)
        print("gmp bin garbage prints ends---------------\n")

    def allocation_of_garbage_to_bins(self):
        bio_garbage_temp=[]
        N_bio_garbage_temp=[]

        for grbg in self.GMP_garbage:
            grbg_name = grbg['garbage_name']
            grbg_amount = grbg['amount']
            
            if grbg_name=='non_recyclable' or grbg_name == 'recyclable':
                grbg_type = grbg['garbage_type']

        
        #billing starts here
                
                
        #billing ends here 

            if grbg_name == 'Biodegradeable_garbage':
                bio_garbage_dictionary = {'garbage_type':grbg_name,'amount':grbg_amount}
                #bio bin work start----------
                bio_garbage_temp.append(bio_garbage_dictionary)
                bio_bin_obj.add_garbage(bio_garbage_temp)

               
            
            elif grbg_type == 'non_Biodegradeable_garbage':
                N_bio_garbage_dictionary = {'garbage_type':grbg_name,'amount':grbg_amount}
                N_bio_garbage_temp.append(N_bio_garbage_dictionary)
                Non_Bio_bin_obj.add_garbage(N_bio_garbage_temp)
               

    #here calculate the billing 

class Bio_bin:
    bio_main_garbage_collection = []
    def add_garbage(self,garbage):
        self.bio_main_garbage_collection=garbage

class Non_Bio_bin:
     Non_bio_bin_garbage_collection = []
     def add_garbage(self,garbage):
         self.Non_bio_bin_garbage_collection=garbage

     def allocation_of_garbage(self):
         r_garbage_temp=[]
         nr_garbage_temp=[]
         for grbg in self.Non_bio_bin_garbage_collection:
             grbg_name = grbg['garbage_name']
             grbg_amount = grbg['amount']
             if grbg_name=="recyclable":
                 r_garbage_dictionary = {'garbage_type':grbg_name,'amount':grbg_amount}
                 r_garbage_temp.append(r_garbage_dictionary)
                 r_bin_obj.add_garbage(r_garbage_temp)


             elif grbg_name == "non_recyclable":
                  nr_garbage_dictionary = {'garbage_type':grbg_name,'amount':grbg_amount}
                  nr_garbage_temp.append(nr_garbage_dictionary)
                  nr_bin_obj.add_garbage(nr_garbage_temp)

                  #non recyclable billing start
                  bill = grbg_amount*5
                  bill_info = {'garbage_type':grbg_name,'amount':grbg_amount,'bill':bill}
                #   user_obj = user()
                  user_obj.total_bill.append(bill_info)

                  #non recyclable billing ends 

             
     def printing_garbage(self):
         for grbg in self.Non_bio_bin_garbage_collection:
             print(grbg)
     
class Recyclable_bin:
    r_garbage_collection = []
    def add_garbage(self,garbage):
        self.r_garbage_collection=garbage

class Non_Recyclable_bin:
    nr_garbage_collection = []
    def add_garbage(self,garbage):
        self.nr_garbage_collection=garbage

#test start

bio_bin_obj=Bio_bin()
Non_Bio_bin_obj = Non_Bio_bin()
r_bin_obj = Recyclable_bin()
nr_bin_obj = Non_Recyclable_bin()


#test 

#login system implementation 
user_obj = None 
Admin = Admin()
#login system implementation ends 

while(True):
    if user_obj is None:
        print("Please login to use our service!---")
        op=input('Login or Register or Admin (L/R/A): ')
        if op=='R':
            name=input('Name: ')
            email=input('Email: ')
            address=input('Address: ')
            password = input('password: ')
            user_obj=User(name,email,address,password)
            User.user_list.append(user_obj)
            print("Registration successfull")

        elif op=='L':
                email=input('Email: ')
                password = input('password: ')
                user_obj = User.user_exists(email,password)
                if user_obj is None:
                    print("Account dosn't exist.")
                else:
                    print("login successfull")

    else:
        print("-----Enter any number from below----")

        print("***1 :to check user details Enter ***")
        print("\n***2 :to enter garbage to source bin Enter :***")
        print("\n***3 : To send garbage source to GMP_bin  Enter***")
        print("\n***4 : print all the garbage in bio garbage***")  #for testing
        print("\n***6 : print non bio bin garbage ***")  #for testing

        print("***\n5 :to logout  ***")

        choice = int(input("choice : "))
        
        if choice == 1:
            # user_obj = user()
            user_obj.total_bill_calculation()
        elif choice == 2 :
            print("\nplease select garbage type first")
            garbage_type_selection_and_amount_dict = garbage_type_and_amount_selection()  
        
        #work of source bin obj start ----
            source_bin_obj = source_bin()
            source_bin_obj.receive_garbage(garbage_type_selection_and_amount_dict)
            # source_bin_obj.printing_all_garbage()
            source_bin_obj.sending_garbage_to_GMP()
            #work of source bin obj ends ----------
            
        elif choice == 3:
            pass
        elif choice == 4:
            for grbg in bio_bin_obj.bio_main_garbage_collection:
                print(grbg)


        elif choice == 6:
            print("printing non bio bin all garbage--------")
            Non_Bio_bin_obj.printing_garbage()


        elif choice == 5:
            print("Logging out ------")
            user_obj=None

                
                    
                
               
        






    
    
    



