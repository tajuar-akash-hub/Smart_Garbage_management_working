print("\n welcome to smart garbage maanagement system")
Garbage_types = ['Biodegradeable_garbage','non_Biodegradeable_garbage']
Garbage_sub_types = ['recyclable','non_recyclable']

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
        # user_garbage_collection_in_source.append({'garbage_name':garbage_name,'amount':amount})
        garbage_dict = {'garbage_name':garbage_name,'amount':amount} 
        return garbage_dict

#for login mechanism 
garbage_source= ['Household garbage','SME','Industrial garbage','GO','Industrial garbage']

#for login mechanism ends

class user:
    name=[]
    address = []
    total_bill=[]
    warning_msg = []
    billing_catalog=[]

    def print_user_details(self):
        print("--------------- Printing user detials -----------\n")
        print(f'{self.name} , {self.address} , {self.total_bill}')

    def total_bill_calculation(self):
        pass

class source_bin:
    # def __init__(self):
    #     self.source_garbage=[]
    #     self.capacity = 10
    source_garbage= []

    def receive_garbage(self,garbage):
        if garbage['amount'] >10 :
            print("********warning:**Sorry 10 garbage at a time****")
        else :
            self.source_garbage.append(garbage)
        #check capacty 

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
            # print("printing from allocation ",grbg_name,grbg_amount)
            if grbg_name == 'Biodegradeable_garbage':
                #billing test aprt
                bill= grbg_amount*0 
                #billing test part ends
                bio_garbage_dictionary = {'garbage_type':grbg_name,'amount':grbg_amount}
                # print("printing bio bin dictionary ",bio_garbage_dictionary)

                #bio bin work start----------
                bio_garbage_temp.append(bio_garbage_dictionary)
                # print("printing bio garbage temp ",bio_garbage_temp)
                
                bio_bin_obj.add_garbage(bio_garbage_temp)
            
            if grbg_name == 'non_Biodegradeable_garbage':
    
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
         #also calculate billing
     #here allocate garbage to r bin and NR bin
         pass
     def printing_garbage(self):
         pass
     
class Recyclable_bin:
    r_garbage_collection = []
    def receive_garbage(self,r_garbage):
        pass

class Non_Recyclable_bin:
     def __init__(self,garbage) :
        self.non_recyclable_garbage= garbage
        non_recyclable_garbage_collection = []

class user_billing_calculation:
    #let's start calculating user billing mechanism : 
    pass

class user_billing_history:
    pass

#user related stuffs here           
# user1=user("admin","dhaka","empty","empty")
#user related stuffs ends

#test start

bio_bin_obj=Bio_bin()
Non_Bio_bin_obj = Non_Bio_bin()

#test 
while(True):
    print("-----Enter any number from below----")
    print("***1 :to check user details Enter ***")
    print("\n***2 :to enter garbage to source bin Enter :***")
    print("\n***3 : To send garbage source to GMP_bin  Enter***")
    print("\n***4 : print all the garbage in bio garbage***")  #for testing
    print("\n***6 : print non bio bin garbage ***")  #for testing

    print("***\n5 :to logout  ***")

    choice = int(input("choice : "))
    
    if choice == 1:
        pass
    elif choice == 2 :
        print("\nplease select garbage type first")
        garbage_type_selection_and_amount_dict = garbage_type_and_amount_selection()  
       
       #work of source bin obj start ----
        source_bin_obj = source_bin()
        source_bin_obj.receive_garbage(garbage_type_selection_and_amount_dict)
        source_bin_obj.printing_all_garbage()
        source_bin_obj.sending_garbage_to_GMP()
        #work of source bin obj ends ----------
    elif choice == 3:
        pass
    elif choice == 4:
        for grbg in bio_bin_obj.bio_main_garbage_collection:
            print(grbg)
    elif choice == 6:
        print("printing non bio bin all garbage--------")
        for grbg in Non_Bio_bin_obj.Non_bio_bin_garbage_collection:
            print(grbg)
    elif choice == 5:
        print("Logging out ------")
        break
    



