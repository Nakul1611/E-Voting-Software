# %%
import pandas as pd
import numpy as np
import sys , os
import time 
current_time = time.strftime("%d/%m/%Y %H:%M:%S",time.localtime())
print(current_time)

# %%
voters_csv = pd.read_csv("votersid.csv")
admins_csv = pd.read_csv("adminsid.csv")
campaign_csv = pd.read_csv("campaign.csv")
candidate_csv = pd.read_csv("candidate.csv")
givenvote_csv = pd.read_csv("givenvote.csv")

# %%
def login_portal():
    # os.system("cls")
    print("\n||************ Welcome to Election Portal ************ ||\n")
    print("=>> Enter 1 for Admin login :")
    print("=>> Enter 2 for Voter login :")
    print("=>> Enter 3 To EXIT : ")
    login_portal_count = 0 
    while(login_portal_count < 3 ):
        login_choosen = input("=>> Enter your Choice ::  ")
        if login_choosen == "1":
            admin_login()
        elif login_choosen == "2":
            voter_login()
        elif login_choosen == "3":
            print("\nExiting Portal .....")
            sys.exit() #print("sys.exit()") un commment this in py file
            # break # comment this 
        else:
            login_portal_count += 1
            print("----- WRONG CHOICE -----\n")
    # print("Exiting Portal .....")

# login_portal()


# %%
def admin_login():
    print("||************ ADMIN LOGIN ID and PASSWORD ************||")
    login_count = 0
    while(login_count<3):
        admin_login_id = input("=>> Enter Admin's Login Id : ")
        admin_login_password = input("=>> Enter Password : ")

        admin_id_present = np.where(admins_csv["admin_login_id"] == admin_login_id , True , False)
        admin_id_present = np.where(True in admin_id_present , True, False)

        if admin_id_present:
            password = admins_csv.set_index(admins_csv["admin_login_id"]).loc[admin_login_id][1]
            if (admin_login_password == password):
                print("welcome to admin view ") # comment this 
                admin_view()
                break

        else:
            print("||--Invalid Cerdentials---||\n")
        login_count +=1
    # os.system('cls')
    login_portal()
# admin_login()

# %%
def voter_login():
    print("||************ Voter Login and Password ************||")
    login_count = 0
    while(login_count<3):
        voter_login_id = input("=>>Enter Voter's login id :  ")
        voter_login_password = input("=>>Enter Password :  ")

        voter_id_present = np.where(voters_csv["voter login id"] == voter_login_id , True , False)
        voter_id_present = np.where(True in voter_id_present , True, False)
        
        if voter_id_present:
            password = voters_csv.set_index(voters_csv["voter login id"]).loc[voter_login_id][1]
            if (voter_login_id and (voter_login_password == password)):
                print("welcome to voter view") #comment this after
                voter_view(voter_login_id)
                break
        else:
            print("||--- Incorrect Cerdentials---||\n")
        login_count +=1
    # os.system('cls')
    login_portal()

# voter_login()

# %%
def admin_view():
    print("||********** List of all Campaign *********||")
    # print("\t List of all Campaign  : \t")  #remove this
    a=str(campaign_csv)
    if a.split()[0] == "Empty":
        print("||---Currently, no campaign is running---||")
        print("==>> Enter 1 to ADD NEW CAMPAIGN : ")
        print("==>> Enter 3 to Exit :")
        # admin_view_chioce = int(input("==>> ENTER CHOICE : "))
    else:
        print(campaign_csv)
        print("==>> Enter 1 to ADD NEW CAMPAIGN :")
        print("==>> Enter 2 to CHOOSE CAMPAIGN :")
        print("==>> Enter 3 to Exit :")

        # admin_view_chioce = int(input("==>> ENTER CHOICE : "))
    admin_view_count = 0
    while(admin_view_count < 3 ):
        admin_view_chioce = int(input("==>> ENTER CHOICE : "))
        if admin_view_chioce == 1 :
            add_campaign()
            admin_view()
            break
            
        elif a.split()[0] != "Empty" and admin_view_chioce == 2:
            campaign_choosen = input("==>> Enter Campaign Id to Choose Campaign : ")
            # checking choosen campaign is in camp id or not 
            b = np.where(campaign_csv["camp_id"] == int(campaign_choosen) , True , False)
            c  = np.where(True in b , True, False)
            # print(c)  # c = True / false

            if c:
                # print("you have choosen" , campaign_choosen)
                print("==>> 1 for Add candidate ")
                print("==>> 2 for declare result ")
                action = int(input("==>> Enter Choice :"))
                action_count = 0 
                while (action_count < 3 ):
                    if action ==1 :
                        add_candidate(campaign_choosen)
                        # admin_view()
                        break
                    elif action == 2:
                        declare_result(campaign_choosen)
                        # admin_view()
                        break
                    else:
                        print("||---Invalid Choice---||")
                        action_count += 1 
                # os.system("cls")
                login_portal()
            else:
                print("||---Wrong Campaign Choosen---||")

        elif admin_view_chioce == 3 :
            print("Exiting portal....")
            sys.exit() #print("sys.exit()")
            # break

        else:
            print("!!!! choice incorrect !!!!")
            admin_view_count += 1 
    # os.system('cls')
    login_portal()

# admin_view()

# %%
def add_campaign():
    new_capmpaign_id = input("CAMPAIGN ID : ")
    new_capmpaign_name = input("CAMPAIGN NAME : ")
    new_capmpaign_startdate = input("CAMPAIGN START DATE (DD/MM/YYYY) : ")
    new_capmpaign_startingtime = input("CAMPAIGN START TIME (HH:MM:SS) : ")
    new_capmpaign_endingdate = input("CAMPAIGN END DATE (DD/MM/YYYY) : ")
    new_capmpaign_endingtime = input("CAMPAIGN END TIME (HH:MM:SS) : ")

    new_campaign_details = {"camp_id":new_capmpaign_id , "camp_name":new_capmpaign_name,"start_date":new_capmpaign_startdate,"start_time":new_capmpaign_startingtime, "end_date":new_capmpaign_endingdate,"end_time":new_capmpaign_endingtime}

    CSV =",".join([v for k,v in new_campaign_details.items()]) 
    #You can store this CSV string variable to file as below
    with open("campaign.csv", "a") as file:
        file.write(CSV + "\n")
    print("Campaign Added successfully !!!")

# add_campaign()

# %%
def add_candidate(campaign_choosen):
    print("||----------ENTER NEW CANDIDATE DETAILS----------||")
    candidate_id  = input("Candidate Id :")
    candidate_name = input("Candidate Name :")
    candidate_party = input("Candidate Party Name :")
    candidate_gender = input("Candidate Gender ( M / F ):")
    # making dict variable
    new_candidate = {"campaign_name":str(campaign_choosen), "candidate_id":candidate_id,"candidate_name":candidate_name, "candidate_party":candidate_party,"candidate_gender":candidate_gender,"no of votes" :"0"}

    # making string to save details in csv 
    CSV =",".join([v for k,v in new_candidate.items()]) 
        #You can store this CSV string variable to file as below
    with open("candidate.csv", "a") as file:
        file.write(CSV+"\n")
    print("New Candidate Added Succesfully !!!\n")

# add_candidate()

# %%
def declare_result(choosen_campaign):
    # print("")
    print("|******************* Result of " , int(choosen_campaign) , "*******************|")
    df = candidate_csv[candidate_csv["campaign id"]== int(choosen_campaign)]
    print(df)
    winner = df["no of votes"].max()
    # print(winner)
    print("WINNER IS ")
    print(df[df["no of votes"] == winner])

# declare_result(777)

# %%
def voter_view(voter_login_id):
    print("\n||**********List of all Campaign**********||\n")
    # print("\t \t List of all Campaign => ") #remove this line
    a=str(campaign_csv)
    if a.split()[0] == "Empty":
        print("\n Currently, no campaign is running  \n ")
    else:
        date_mask =( ((campaign_csv["start_date"] + " " +  campaign_csv["start_time"]) <= current_time) & ( (campaign_csv["end_date"] + " " +  campaign_csv["end_time"]) >= current_time))
        current_campaign = campaign_csv.loc[date_mask]
        a=str(current_campaign)
        if a.split()[0] == "Empty":
            print("\n Currently, no campaign is running ")
            print("\n||---Press enter to exit---||\n ")
            # x = input("\n <<<Press enter to exit >>> \n ")

        else:
            print(current_campaign)
            print("=>> Enter 1 to Vote : \n=>> Enter 2 to Exit : ")
            # x = input("To VOTE Enter 1 : \n To EXIT Enter 2 : \n YOU ENTERED : ")
    # x = input("To VOTE Enter 1 : \n To EXIT Enter 2 : \n YOU ENTERED : ")
    x = input("==> YOU ENTERED : ")
    # x = input("enter 1 to vote \n enter 2 to exit ")
    if x=="1" and a.split()[0] != "Empty" : 
        i=0
        while(i < 3 ):
            choose_campaign = int(input("\n=>> Enter Campaign ID : "))
            b = np.where(current_campaign["camp_id"] == choose_campaign, True , False)
            c  = np.where(True in b , True, False)
            if c:
                # print("yes")
                give_vote(str(choose_campaign),str(voter_login_id))
                break
            else:
                print("||---Wrong Campaign Id Entered---||")
                i+=1

    else:
        # print("exiting.... ")
        # os.system("cls")
        login_portal()
# voter_view(154)

# %%
def give_vote( choosen_campaign , voter_login_id):
    vote_done = False
    for index , row in givenvote_csv.iterrows():
        # print( row[0]  , row[1]  )
        if str(row[0]) == (choosen_campaign) and str(row[1]) == (voter_login_id):
            print("\n Your vote is already regitered !!!\n ")
            vote_done = True
            break
        else:
            # print("vote not register")
            vote_done = False
    # print(vote_done)
    if vote_done ==False:
         # showing the list of all candidate in choosen campaign 
        print("\n||**********List of all candidate in Campaign**********|| \n")
        df1 = candidate_csv[candidate_csv["campaign id"] == int(choosen_campaign)]
        a = str(df1)
        if a.split()[0] == "Empty":
            print("Empty , no  candidate registered . ")
        else : 
            print(df1[["campaign id", "candidate id", "candidate name","candidate party","candidate gender"]]) #candidate_csv[candidate_csv["campaign name"] == int(choosen_campaign) ] 
            print("\n==>> Choose Candidate to Vote :\n ")
            candidate_choosen = int(input("==>> Enter Candidate ID  to Vote : "))
            # checking if candidate id choosen is in candidate list
            # print(df1["candidate id"])
            b = np.where(df1["candidate id"] == candidate_choosen , True , False)
            c  = np.where(True in b , True, False)
            # print(c)
            if c :
                # confirm the candidate by showing his detail
                print("\n |***********Candidate you have Choosen**********|")
                # print("\n==>> Candidate you have Choosen : \n ")
                df = candidate_csv.loc[candidate_csv["candidate id"] == int(candidate_choosen)]
                print(df[["campaign id", "candidate id", "candidate name","candidate party","candidate gender"]])
                df = candidate_csv
                df["no of votes"] = np.where((df["candidate id"]==int(candidate_choosen)) , df["no of votes"] + 1 , df["no of votes"] )
                df.to_csv("candidate.csv", index=False)
                # saving new voter voting details in given vote csv
                new_voting = {"camp_id": str(choosen_campaign) ,"voter_login_id": str(voter_login_id) }
                new_vooting_str =",".join([v for k,v in new_voting.items()]) 
                #You can store this CSV string variable to file as below
                with open("givenvote.csv", "a") as file:
                    file.write(new_vooting_str+"\n")
                print("\n Your Vote is Registered Succesfully ....\n ")
            else:
                print("||---Wrong Candiate Choosen---||\n")

# give_vote(777,"voter123")

login_portal()