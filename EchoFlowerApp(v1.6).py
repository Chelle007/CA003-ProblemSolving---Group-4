import database
import txt_reader
import os
import platform
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

directory = os.getcwd()
if platform.system() == "Windows":
    directory += "\\Image\\"
else:
    directory += "/Image/"

def login_page():
    loginPage = customtkinter.CTk()
    loginPage.geometry("1536 x 790")
    loginPage.minsize(1536, 790)
    loginPage.maxsize(1536, 790)
    loginPage.title('Log in')
    loginPage.after(0, lambda: loginPage.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open((directory+"login_page.png"), mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=loginPage, image=img1, text="")
    l1.pack()

    #frame
    frame1=customtkinter.CTkFrame(master=loginPage,
                                  corner_radius=0,
                                  fg_color="white",
                                  width=100)

    #username
    username_label = customtkinter.CTkLabel(master=loginPage,
                                            text="Username",
                                            font=("Ink Free", 45),
                                            bg_color="#FFFFFF")
    username_label.place(relx=0.03, rely=0.37)

    entry1=customtkinter.CTkEntry(master=loginPage,
                                width=400,
                                font=("Ink Free", 40),
                                placeholder_text="Enter the username",
                                bg_color="#FFFFFF")
    entry1.pack()
    entry1.place(relx=0.03, rely=0.44)

    #password
    password_label = customtkinter.CTkLabel(master=loginPage,
                                            text="Password",
                                            font=("Ink Free", 45),
                                            bg_color="#FFFFFF")
    password_label.place(relx=0.03, rely=0.55)

    entry2=customtkinter.CTkEntry(master=loginPage,
                                width=400,
                                font=("Ink Free", 40),
                                placeholder_text="Enter the password",
                                bg_color="#FFFFFF")
    entry2.pack()
    entry2.place(relx=0.03, rely=0.62)

    #login button
    def login_function():
        username = entry1.get()
        password = entry2.get()
        user = database.mst_user(username, password, "", "", "", "", "")
        user = database.mst_user.return_account(user)
        if user == None :
            error_label = customtkinter.CTkLabel(master=loginPage,
                                                text="Invalid username/password",
                                                text_color="red",
                                                font=("Ink Free", 37),
                                                bg_color="#FFFFFF")
            error_label.place(relx=0.03, rely=0.86)
        elif user[2] == "customer":
            user = list(user)
            loginPage.destroy()
            customer_home(user, bought=False)
        elif user[2] == "seller":
            user = list(user)
            loginPage.destroy()
            seller_home(user, False)

    login_button = customtkinter.CTkButton(master=loginPage,
                                    text="Log In",
                                    width=190,
                                    font=("Ink Free", 45),
                                    bg_color="#FFFFFF",
                                    fg_color="#f494fc",
                                    hover_color="#c358cc",
                                    command=login_function)
    login_button.place(relx=0.03, rely=0.76)

    #signup button
    def signup_function():
        loginPage.destroy()
        sign_up()

    signup_button = customtkinter.CTkButton(master=loginPage,
                                    text="Sign Up",
                                    width=190,
                                    font=("Ink Free", 45),
                                    bg_color="#FFFFFF",
                                    fg_color="#c3e397",
                                    hover_color="#b1ce8b",
                                    command=signup_function)
    signup_button.place(relx=0.166, rely=0.76)

    loginPage.mainloop()

def sign_up():
    signUp = customtkinter.CTk()
    signUp.after(0, lambda: signUp.wm_state('zoomed'))
    signUp.geometry("1536 x 790")
    signUp.minsize(1536, 790)
    signUp.maxsize(1536, 790)
    signUp.title("Sign Up")

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"sign_up.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=signUp, image=img1, text="")
    l1.pack()

    #username
    username_label = customtkinter.CTkLabel(master=signUp,
                                            text="Username",
                                            font=("Ink Free", 25),
                                            bg_color="#FFFFFF")
    username_label.place(relx=0.03, rely=0.26)

    entry1=customtkinter.CTkEntry(master=signUp,
                                width=425,
                                font=("Ink Free", 20),
                                placeholder_text="Enter the username",
                                bg_color="#FFFFFF")
    entry1.pack()
    entry1.place(relx=0.03, rely=0.30)

    #password
    password_label = customtkinter.CTkLabel(master=signUp,
                                            text="Password",
                                            font=("Ink Free", 25),
                                            bg_color="#FFFFFF")
    password_label.place(relx=0.03, rely=0.36)

    entry2=customtkinter.CTkEntry(master=signUp,
                                width=425,
                                font=("Ink Free", 20),
                                placeholder_text="Enter the password",
                                bg_color="#FFFFFF")
    entry2.pack()
    entry2.place(relx=0.03, rely=0.40)

    #full name
    fullname_label = customtkinter.CTkLabel(master=signUp,
                                            text="Full name",
                                            font=("Ink Free", 25),
                                            bg_color="#FFFFFF")
    fullname_label.place(relx=0.03, rely=0.46)

    entry3=customtkinter.CTkEntry(master=signUp,
                                width=425,
                                font=("Ink Free", 20),
                                placeholder_text="Enter your full name",
                                bg_color="#FFFFFF")
    entry3.pack()
    entry3.place(relx=0.03, rely=0.50)

    #email
    email_label = customtkinter.CTkLabel(master=signUp,
                                            text="Email",
                                            font=("Ink Free", 25),
                                            bg_color="#FFFFFF")
    email_label.place(relx=0.03, rely=0.56)

    entry4=customtkinter.CTkEntry(master=signUp,
                                width=425,
                                font=("Ink Free", 20),
                                placeholder_text="Enter your email",
                                bg_color="#FFFFFF")
    entry4.pack()
    entry4.place(relx=0.03, rely=0.60)

    #contact number
    contactnumber_label = customtkinter.CTkLabel(master=signUp,
                                            text="Contact number",
                                            font=("Ink Free", 25),
                                            bg_color="#FFFFFF")
    contactnumber_label.place(relx=0.03, rely=0.66)

    entry5=customtkinter.CTkEntry(master=signUp,
                                width=425,
                                font=("Ink Free", 20),
                                placeholder_text="Enter your contact number",
                                bg_color="#FFFFFF")
    entry5.pack()
    entry5.place(relx=0.03, rely=0.70)

    #address
    address_label = customtkinter.CTkLabel(master=signUp,
                                            text="Address",
                                            font=("Ink Free", 25),
                                            bg_color="#FFFFFF")
    address_label.place(relx=0.03, rely=0.76)

    entry6=customtkinter.CTkEntry(master=signUp,
                                width=425,
                                font=("Ink Free", 20),
                                placeholder_text="Enter your contact address",
                                bg_color="#FFFFFF")
    entry6.pack()
    entry6.place(relx=0.03, rely=0.80)

    #return button
    def return_function():
        signUp.destroy()
        login_page()

    login_button = customtkinter.CTkButton(master=signUp,
                                    text="Return",
                                    width=190,
                                    font=("Ink Free", 45),
                                    bg_color="#FFFFFF",
                                    fg_color="#f494fc",
                                    hover_color="#c358cc",
                                    command=return_function)
    login_button.place(relx=0.03, rely=0.9)

    #username taken
    username_taken = customtkinter.CTkLabel(master=signUp,
                                             text="*Username has been taken",
                                             text_color="red",
                                             font=("Ink Free", 25),
                                             bg_color="#FFFFFF")
    
    #signup button
    def signup_function():
        username = entry1.get()
        password = entry2.get()
        full_name = entry3.get()
        email = entry4.get()
        contact_number = entry5.get()
        address = entry6.get()
        error = False
        
        if username == "" or password == "" or full_name == "" or email == "" or contact_number == "" or address == "":
            invalid = customtkinter.CTkLabel(master=signUp,
                                             text="*Data is not complete",
                                             text_color="red",
                                             font=("Ink Free", 25),
                                             bg_color="#FFFFFF")
            invalid.place(relx=0.03, rely=0.85)
            error = True

        if database.mst_user.check_username(username):
            username_taken.place(relx=0.12, rely=0.26)
            error = True

        if not database.mst_user.check_username(username):
            username_taken.place_forget()

        if not error:
            new_account = database.mst_user(username, password, "customer", full_name, email, contact_number, address)
            database.mst_user.create_account(new_account)
            signUp.destroy()
            login_page()

    signup_button = customtkinter.CTkButton(master=signUp,
                                    text="Sign Up",
                                    width=190,
                                    font=("Ink Free", 45),
                                    bg_color="#FFFFFF",
                                    fg_color="#c3e397",
                                    hover_color="#b1ce8b",
                                    command=signup_function)
    signup_button.place(relx=0.18, rely=0.9)

    signUp.mainloop()

#CUSTOMER
def customer_home(user, bought):
    customerHome = customtkinter.CTk()
    customerHome.after(0, lambda: customerHome.wm_state('zoomed'))
    customerHome.geometry("1536 x 790")
    customerHome.minsize(1536, 790)
    customerHome.maxsize(1536, 790)
    customerHome.title("Home Page")

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"home_page.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=customerHome, image=img1, text="")
    l1.pack()

    #create order text
    l2=customtkinter.CTkLabel(master=customerHome,
                              text="Create order",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #view order button
    def vieworder_function():
        customerHome.destroy()
        view_order(user)

    vieworder_button = customtkinter.CTkButton(master=customerHome,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.83, rely=0.02)

    #profile button
    def profile_function():
        customerHome.destroy()
        customer_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=customerHome,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    def clear_label():
        bought_label.configure(text="")

    #bought label
    if bought == True:
        bought_label = customtkinter.CTkLabel(master=customerHome,
                                            bg_color="#F8F8FF",
                                            fg_color="#D4BBDD",
                                            text="*Successfully bought the flower",
                                            font=("TT Commons Medium", 30),
                                            text_color="#5E376D")
        bought_label.place(relx=0.6, rely=0.5)
        customerHome.after(2000, clear_label)

    #search bar
    def search_function():
        keyword = search_entry.get()
        item_data = database.mst_item.search_name(keyword)
        if sortby_combobox.get()=="Name":
            item_data.sort(key=lambda x: x[2])
        elif sortby_combobox.get()=="Price":
            item_data.sort(key=lambda x: x[4])
        if category_combobox.get()!="All" and category_combobox.get()!="Category":
            item_data = filter(lambda x: x[3]==category_combobox.get(), item_data)
            item_data = list(item_data)
        show_list(item_data)

    search_frame = customtkinter.CTkFrame(master=customerHome,
                                          height=40,
                                          width=350,
                                          bg_color="#D4BBDD",
                                          fg_color="#F8F8FF")
    search_frame.place(relx=0.015, rely=0.495)

    search_entry = customtkinter.CTkEntry(master=search_frame,
                                          placeholder_text="Search...",
                                          font=("TT Commons Medium", 20),
                                          bg_color="#D4BBDD",
                                          fg_color="#F8F8FF",
                                          border_width=2,
                                          border_color="#000000",
                                          height=40,
                                          width=305.6)
    search_entry.place(relx=0, rely=0)

    search_image = customtkinter.CTkImage(Image.open(directory+"search_button.png", mode="r"), size=(30,30))
    search_button = customtkinter.CTkButton(master=search_frame,
                                             width=0,
                                             text="",
                                             bg_color="#D4BBDD",
                                             fg_color="#5E376D",
                                             hover_color="#5E376D",
                                             border_width=2,
                                             border_color="#000000",
                                             image=search_image,
                                             command=search_function)
    search_button.place(relx=0.865, rely=0)

    #sort by
    sortby_var = customtkinter.StringVar(value="Sort by")

    sortby_combobox = customtkinter.CTkComboBox(master=customerHome,
                                                height=40,
                                                width=200,
                                                font=("Arial", 20),
                                                bg_color="#D4BBDD",
                                                fg_color="#F8F8FF",
                                                dropdown_font=("TT Commons Medium", 20),
                                                dropdown_fg_color="#F8F8FF",
                                                dropdown_hover_color="#cd9ede",
                                                border_width=2,
                                                border_color="#000000",
                                                button_color="#5E376D",
                                                button_hover_color="#5E376D",
                                                values=["Name", "Price"],
                                                state="readonly",
                                                variable = sortby_var)
    sortby_combobox.place(relx=0.257, rely=0.495)

    #category
    category_var = customtkinter.StringVar(value="Category")

    category_combobox = customtkinter.CTkComboBox(master=customerHome,
                                                height=40,
                                                width=200,
                                                font=("Arial", 20),
                                                bg_color="#D4BBDD",
                                                fg_color="#F8F8FF",
                                                dropdown_font=("TT Commons Medium", 20),
                                                dropdown_fg_color="#F8F8FF",
                                                dropdown_hover_color="#cd9ede",
                                                border_width=2,
                                                border_color="#000000",
                                                button_color="#5E376D",
                                                button_hover_color="#5E376D",
                                                state="readonly",
                                                values=["All", "Anniversary", "Birthday", "Condolence", "Grand Opening", "Romantic"],
                                                variable = category_var)
    category_combobox.place(relx=0.4, rely=0.495)

    #items
    def show_list(item_data):
        item_frame = customtkinter.CTkScrollableFrame(master=customerHome,
                                                        orientation="horizontal",
                                                        height=318,
                                                        width=1494,
                                                        bg_color="#D4BBDD",
                                                        fg_color="#D4BBDD")
        item_frame.place(relx=0.01, rely=0.57)
        
        if item_data == []:
            no_item = customtkinter.CTkLabel(master=customerHome,
                                             text="Sorry, couldn't find item.\nTry searching again in different keyword.",
                                             justify="center",
                                             font=("TT Commons Medium", 35),
                                             text_color="#866492",
                                             corner_radius=0,
                                             fg_color="#D4BBDD")
            no_item.place(relx=0.5, rely=0.75, anchor="center")

        else:
            def buy_function(i):
                def inner_buy_function():
                    customerHome.destroy()
                    buy_item(user, item_data[i])
                return inner_buy_function
            
            eachitem_image = []

            for i in range(len(item_data)):
                eachitem_frame = customtkinter.CTkFrame(master=item_frame,
                                                        height=315,
                                                        width=200,
                                                        fg_color="#D4BBDD")
                eachitem_frame.grid(row=0, column=i, padx=25, pady=0)

                eachitem_img = customtkinter.CTkFrame(master=eachitem_frame,
                                                    corner_radius=0,
                                                    height=250,
                                                    width=200)
                eachitem_img.place(relx=0, rely=0)

                try:
                    eachitem_image.append(customtkinter.CTkImage(Image.open(directory+item_data[i][1]+".jpg", mode="r"), size=(200, 285.5)))
                except FileNotFoundError:
                    eachitem_image.append(customtkinter.CTkImage(Image.open(directory+"no_image.png", mode="r"), size=(200, 285.5)))

                image_label = customtkinter.CTkLabel(master=eachitem_img, text="", image=eachitem_image[i])
                image_label.pack()

                eachitem_desc = customtkinter.CTkFrame(master=eachitem_frame,
                                                    corner_radius=0,
                                                    height=106,
                                                    width=188,
                                                    fg_color="white",
                                                    bg_color="white")
                eachitem_desc.place(relx=0.03, rely=0.55)

                eachitem_text = customtkinter.CTkLabel(master=eachitem_desc,
                                                    corner_radius=0,
                                                    height=106,
                                                    width=188,
                                                    fg_color="white",
                                                    font=("Calibri", 15),
                                                    text=("{name}\n#{category}\n${price}\nStock: {quantity}".format(name = item_data[i][2], price = item_data[i][4], quantity = item_data[i][5], category = item_data[i][3])),
                                                    text_color="#5E376D")
                eachitem_text.place(relx=0, rely=-0.065)

                buy_button = customtkinter.CTkButton(master=eachitem_frame,
                                                    corner_radius=0,
                                                    height=40,
                                                    width=100,
                                                    text="BUY",
                                                    font=("TT Commons Medium", 15),
                                                    bg_color="#866492",
                                                    fg_color="#866492",
                                                    hover_color="#674b70",
                                                    command=buy_function(i))
                
                cannotbuy_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    corner_radius=0,
                                                    height=40,
                                                    width=100,
                                                    text="BUY",
                                                    font=("TT Commons Medium", 15),
                                                    bg_color="gray",
                                                    fg_color="gray",
                                                    text_color="white")
                
                if item_data[i][5] == "Available":
                    buy_button.place(relx=0.25, rely=0.83)
                else:
                    cannotbuy_label.place(relx=0.25, rely=0.83)


    item_data = database.mst_item.sort_item_name()
    show_list(item_data)

    customerHome.mainloop()

def customer_profile(user):
    cprofilePage = customtkinter.CTk()
    cprofilePage.geometry("1536 x 790")
    cprofilePage.minsize(1536, 790)
    cprofilePage.maxsize(1536, 790)
    cprofilePage.title("Profile Page")
    cprofilePage.after(0, lambda: cprofilePage.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=cprofilePage, image=img1, text="")
    l1.pack()

    #profile text
    l2=customtkinter.CTkLabel(master=cprofilePage,
                              text="Profile",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #view order button
    def vieworder_function():
        cprofilePage.destroy()
        view_order(user)

    vieworder_button = customtkinter.CTkButton(master=cprofilePage,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.74, rely=0.02)

    #create order button
    def customerhome_function():
        cprofilePage.destroy()
        customer_home(user, bought=False)

    customerhome_button = customtkinter.CTkButton(master=cprofilePage,
                                               text="Create Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=customerhome_function)
    customerhome_button.place(relx=0.87, rely=0.02)
    
    #change profile button
    def cchangeprofile_function():
        cprofilePage.destroy()
        cchange_profile(user)
    
    cchangeprofile_button = customtkinter.CTkButton(master=cprofilePage,
                                            text="Change Profile",
                                            width=250,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#866492",
                                            hover_color="#674b70",
                                            command=cchangeprofile_function)
    cchangeprofile_button.place(relx=0.81, rely=0.79)

    #logout button
    def logout_function():
        cprofilePage.destroy()
        login_page()
    
    logout_button = customtkinter.CTkButton(master=cprofilePage,
                                            text="Log out",
                                            width=250,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#ff3131",
                                            hover_color="#de1b1b",
                                            command=logout_function)
    logout_button.place(relx=0.81, rely=0.88)

    #personal information
    detail_frame = customtkinter.CTkFrame(master=cprofilePage,
                                          height=625,
                                          width=1150,
                                          bg_color="#FFFFFF",
                                          fg_color="#FFFFFF")
    detail_frame.place(relx=0.03, rely=0.15)

    personalinfo_label = customtkinter.CTkLabel(master=detail_frame,
                                                text="Personal Information",
                                                font=("TT Commons Medium", 55))
    personalinfo_label.place(relx=0.03, rely=0.04)

    username1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Username",
                                            font=("TT Commons Medium", 40))
    username1_label.place(relx=0.03, rely=0.18)

    username2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[0],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    username2_label.place(relx=0.33, rely=0.18)

    password1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Password",
                                            font=("TT Commons Medium", 40))
    password1_label.place(relx=0.03, rely=0.28)

    password2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text="*" * len(user[1]),
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    password2_label.place(relx=0.33, rely=0.28)

    identity1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Identity",
                                            font=("TT Commons Medium", 40))
    identity1_label.place(relx=0.03, rely=0.38)

    identity2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[2],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    identity2_label.place(relx=0.33, rely=0.38)

    fullname1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Full name",
                                            font=("TT Commons Medium", 40))
    fullname1_label.place(relx=0.03, rely=0.48)

    fullname2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[3],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    fullname2_label.place(relx=0.33, rely=0.48)

    email1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Email",
                                            font=("TT Commons Medium", 40))
    email1_label.place(relx=0.03, rely=0.58)

    email2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[4],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    email2_label.place(relx=0.33, rely=0.58)

    phonenumber1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Phone number",
                                            font=("TT Commons Medium", 40))
    phonenumber1_label.place(relx=0.03, rely=0.68)

    phonenumber2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[5],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    phonenumber2_label.place(relx=0.33, rely=0.68)

    address1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Address",
                                            font=("TT Commons Medium", 40))
    address1_label.place(relx=0.03, rely=0.78)

    address2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[6],
                                             wraplength=720,
                                             justify = "left",
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    address2_label.place(relx=0.33, rely=0.78)

    cprofilePage.mainloop()

def cchange_profile(user):
    cchangeProfile = customtkinter.CTk()
    cchangeProfile.geometry("1536 x 790")
    cchangeProfile.minsize(1536, 790)
    cchangeProfile.maxsize(1536, 790)
    cchangeProfile.title("Change Profile")
    cchangeProfile.after(0, lambda: cchangeProfile.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=cchangeProfile, image=img1, text="")
    l1.pack()

    #change profile text
    l2=customtkinter.CTkLabel(master=cchangeProfile,
                              text="Change Profile",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #view order button
    def vieworder_function():
        cchangeProfile.destroy()
        view_order(user)

    vieworder_button = customtkinter.CTkButton(master=cchangeProfile,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.74, rely=0.02)

    #create order button
    def customerhome_function():
        cchangeProfile.destroy()
        customer_home(user, bought=False)

    customerhome_button = customtkinter.CTkButton(master=cchangeProfile,
                                               text="Create Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=customerhome_function)
    customerhome_button.place(relx=0.87, rely=0.02)
    
    #change detail frame
    changedetail_frame = customtkinter.CTkFrame(master=cchangeProfile,
                                                height=580,
                                                width=1440,
                                                bg_color="#FFFFFF",
                                                fg_color="#FFFFFF")
    changedetail_frame.place(relx=0.03, rely=0.15)

    username1_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Username",
                                            font=("TT Commons Medium", 50))
    username1_label.place(relx=0.03, rely=0.05)

    username2_label = customtkinter.CTkLabel(master=changedetail_frame,
                                             text=user[0],
                                             font=("TT Commons Medium", 50),
                                             text_color="#97928D")
    username2_label.place(relx=0.3, rely=0.05)

    password_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Password",
                                            font=("TT Commons Medium", 50))
    password_label.place(relx=0.03, rely=0.2)

    password_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text="*"*len(user[1]),
                                            font=("TT Commons Medium", 50))
    password_entry.place(relx=0.3, rely=0.2)

    fullname_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Full name",
                                            font=("TT Commons Medium", 50))
    fullname_label.place(relx=0.03, rely=0.35)

    fullname_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text=user[3],
                                            font=("TT Commons Medium", 50))
    fullname_entry.place(relx=0.3, rely=0.35)

    email_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Email",
                                            font=("TT Commons Medium", 50))
    email_label.place(relx=0.03, rely=0.5)

    email_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text=user[4],
                                            font=("TT Commons Medium", 50))
    email_entry.place(relx=0.3, rely=0.5)

    phonenumber_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Phone number",
                                            font=("TT Commons Medium", 50))
    phonenumber_label.place(relx=0.03, rely=0.65)

    phonenumber_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text=user[5],
                                            font=("TT Commons Medium", 50))
    phonenumber_entry.place(relx=0.3, rely=0.65)

    address_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Address",
                                            font=("TT Commons Medium", 50))
    address_label.place(relx=0.03, rely=0.8)

    address_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                           width = 950,
                                           placeholder_text=user[6],
                                           font=("TT Commons Medium", 50))
    address_entry.place(relx=0.3, rely=0.8)

    #save button
    def save_function():
        nonlocal user
        if password_entry.get() == "":
            pass
        else:
            user[1] = password_entry.get()
        if fullname_entry.get() == "":
            pass
        else:
            user[3] = fullname_entry.get()
        if email_entry.get() == "":
            pass
        else:
            user[4] = email_entry.get()
        if phonenumber_entry.get() == "":
            pass
        else:
            user[5] = phonenumber_entry.get()
        if address_entry.get() == "":
            pass
        else:
            user[6] = address_entry.get()
        database.mst_user.change_account_detail(user)
        cchangeProfile.destroy()
        customer_profile(user)

    save_button = customtkinter.CTkButton(master=cchangeProfile,
                                            text="Save",
                                            width=180,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#866492",
                                            hover_color="#674b70",
                                            command=save_function)
    save_button.place(relx=0.722, rely=0.911)
    
    #return button
    def return_function():
        cchangeProfile.destroy()
        customer_profile(user)
    
    return_button = customtkinter.CTkButton(master=cchangeProfile,
                                            text="Return",
                                            width=180,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#ff3131",
                                            hover_color="#de1b1b",
                                            command=return_function)
    return_button.place(relx=0.852, rely=0.911)

    cchangeProfile.mainloop()

def view_order(user):
    viewOrder = customtkinter.CTk()
    viewOrder.geometry("1536 x 790")
    viewOrder.minsize(1536, 790)
    viewOrder.maxsize(1536, 790)
    viewOrder.title("View Order")
    viewOrder.after(0, lambda: viewOrder.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=viewOrder, image=img1, text="")
    l1.pack()

    #view order text
    l2=customtkinter.CTkLabel(master=viewOrder,
                              text="View order",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #create order button
    def createorder_function():
        viewOrder.destroy()
        customer_home(user, bought=False)

    createorder_button = customtkinter.CTkButton(master=viewOrder,
                                               text="Create Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=createorder_function)
    createorder_button.place(relx=0.83, rely=0.02)

    #profile button
    def profile_function():
        viewOrder.destroy()
        customer_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=viewOrder,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    #items
    orders = database.trx_sales.return_order(user[0])
    ordered_orders = []
    prepared_orders = []
    itemdata_list = []
    itemdata_list2 = []
    addons_list = []
    addons_list2 = []
    opencancel_button = []
    itemstatus_label = []

    for i in range(len(orders)):
        if orders[i][10] == "Open" or orders[i][10] == "Cancelled":
            ordered_orders.append(orders[i])
        else:
            prepared_orders.append(orders[i])   
    
    #ordered
    ordered_label=customtkinter.CTkLabel(master=viewOrder,
                              text="Ordered",
                              font=("TT Commons Medium", 50),
                              bg_color="#D4BBDD")
    ordered_label.place(relx=0.19, rely=0.13)

    if ordered_orders == []:
        no_ordered = customtkinter.CTkLabel(master=viewOrder,
                                             text="No order available.\nClick create order to make order.",
                                             justify="center",
                                             font=("TT Commons Medium", 35),
                                             text_color="#866492",
                                             corner_radius=0,
                                             fg_color="#D4BBDD")
        no_ordered.place(relx=0.246, rely=0.55, anchor="center")
    else:
        ordered_frame = customtkinter.CTkScrollableFrame(master=viewOrder,
                                                    orientation="vertical",
                                                    height=590,
                                                    width=680,
                                                    bg_color="#D4BBDD",
                                                    fg_color="#D4BBDD")
        ordered_frame.place(relx=0.02, rely=0.2)

        def edit_function(i):
            viewOrder.destroy()
            edit_order(user, ordered_orders[i], addons_list[i])

        eachitem_image = []

        for i in range(len(ordered_orders)):

            def opencancel_function(i):
                if ordered_orders[i][10]=="Open":
                    database.trx_sales.edit_status("Cancelled", i+1)
                    opencancel_button[i].configure(text="Open order",
                                                    fg_color="#30cc84",
                                                    hover_color="#10945c",
                                                    font=("TT Commons Medium", 20))
                    
                    itemstatus_label[i].configure(text="Status: Cancelled",
                                            text_color="red")

                    ordered_orders[i] = list(ordered_orders[i])
                    ordered_orders[i][10] = "Cancelled"
                    ordered_orders[i] = tuple(ordered_orders[i])

                else:
                    database.trx_sales.edit_status("Open", i+1)
                    opencancel_button[i].configure(text="Cancel order",
                                                font=("TT Commons Medium", 20),
                                                fg_color="#ff3131",
                                                hover_color="#de1b1b")
                    
                    itemstatus_label[i].configure(text="Status: Open",
                                            text_color="#30cc84")

                    ordered_orders[i] = list(ordered_orders[i])
                    ordered_orders[i][10] = "Open"
                    ordered_orders[i] = tuple(ordered_orders[i])
                
            item_data = database.mst_item.return_item(ordered_orders[i][2])
            item_data = list(item_data)
            itemdata_list.append(item_data)
            addons_data = database.sales_addon.return_addon_code(ordered_orders[i][0])
            addons_data = list(addons_data)
            addons_list.append(addons_data)
            if addons_list[i] == []:
                addons_strings = "-"
            else:
                addons_strings = ", ".join([database.mst_item.return_itemname(addon[0]) for addon in addons_list[i]])

            eachitem_frame = customtkinter.CTkFrame(master=ordered_frame,
                                                    height=280,
                                                    width=670,
                                                    fg_color="#FFFFFF")
            eachitem_frame.grid(row=i, column=0, padx=0, pady=10)

            eachitem_img = customtkinter.CTkFrame(master=eachitem_frame,
                                                corner_radius=0,
                                                height=250,
                                                width=200)
            eachitem_img.place(relx=0.03, rely=0.04)

            try:
                eachitem_image.append(customtkinter.CTkImage(Image.open(directory+ordered_orders[i][2]+".jpg", mode="r"), size=(200, 250)))
            except FileNotFoundError:
                eachitem_image.append(customtkinter.CTkImage(Image.open(directory+"no_image2.png", mode="r"), size=(200, 250)))

            image_label = customtkinter.CTkLabel(master=eachitem_img, text="", image=eachitem_image[i])
            image_label.pack()

            itemname_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text=itemdata_list[i][1],
                                                    font=("TT Commons Medium", 30))
            itemname_label.place(relx=0.35, rely=0.02)

            itemprice_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="$"+str(ordered_orders[i][9]),
                                                    font=("TT Commons Medium", 25))
            itemprice_label.place(relx=0.35, rely=0.14)

            itemstatus_label.append(customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="Status: "+ordered_orders[i][10],
                                                    text_color="#30cc84",
                                                    font=("TT Commons Medium", 25)))
            if ordered_orders[i][10]=="Cancelled":
                itemstatus_label[i].configure(text_color="red")
            itemstatus_label[i].place(relx=0.35, rely=0.23)

            itemaddons_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="Add-ons: "+addons_strings,
                                                    font=("TT Commons Medium", 18))
            itemaddons_label.place(relx=0.35, rely=0.33)

            recipientname_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="Recipient: "+ordered_orders[i][6],
                                                    font=("TT Commons Medium", 18))
            recipientname_label.place(relx=0.35, rely=0.415)

            msg_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="Message: "+ordered_orders[i][8],
                                                    font=("TT Commons Medium", 18))
            msg_label.place(relx=0.35, rely=0.5)

            choice_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="Choice: "+ordered_orders[i][3]+" (Same day: "+ordered_orders[i][5]+")",
                                                    font=("TT Commons Medium", 18))
            choice_label.place(relx=0.35, rely=0.585)
            
            deliverydate_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="Delivery date: "+ordered_orders[i][4],
                                                    font=("TT Commons Medium", 18))
            deliverydate_label.place(relx=0.35, rely=0.67)

            deliveryaddress_label = customtkinter.CTkLabel(master=eachitem_frame,
                                                    text="Delivery address: "+ordered_orders[i][7],
                                                    wraplength=275,
                                                    justify = "left",
                                                    font=("TT Commons Medium", 18))
            deliveryaddress_label.place(relx=0.35, rely=0.755)

            edit_button = customtkinter.CTkButton(master=eachitem_frame,
                                                corner_radius=0,
                                                height=40,
                                                width=125,
                                                text="Edit order",
                                                font=("TT Commons Medium", 20),
                                                fg_color="#97928D",
                                                hover_color="#7d7974",
                                                command=lambda i=i: edit_function(i))
            edit_button.place(relx=0.78, rely=0.6)

            opencancel_button.append(customtkinter.CTkButton(master=eachitem_frame,
                                                corner_radius=0,
                                                height=40,
                                                width=125,
                                                text="Cancel order",
                                                font=("TT Commons Medium", 20),
                                                fg_color="#ff3131",
                                                hover_color="#de1b1b",
                                                command=lambda i=i: opencancel_function(i)))
            opencancel_button[i].place(relx=0.78, rely=0.78)

            if ordered_orders[i][10]=="Cancelled":
                opencancel_button[i].configure(text="Open order",
                                            fg_color="#30cc84",
                                            hover_color="#10945c",
                                            font=("TT Commons Medium", 20))

    #prepared
    prepared_label=customtkinter.CTkLabel(master=viewOrder,
                              text="Prepared",
                              font=("TT Commons Medium", 50),
                              bg_color="#D4BBDD")
    prepared_label.place(relx=0.7, rely=0.13)

    if prepared_orders == []:
        no_prepared = customtkinter.CTkLabel(master=viewOrder,
                                             text="No order has been prepared.",
                                             justify="center",
                                             font=("TT Commons Medium", 35),
                                             text_color="#866492",
                                             corner_radius=0,
                                             fg_color="#D4BBDD")
        no_prepared.place(relx=0.757, rely=0.55, anchor="center")
    else:
        prepared_frame = customtkinter.CTkScrollableFrame(master=viewOrder,
                                                    orientation="vertical",
                                                    height=590,
                                                    width=680,
                                                    bg_color="#D4BBDD",
                                                    fg_color="#D4BBDD")
        prepared_frame.place(relx=0.52, rely=0.2)

        eachitem_image2 = []

        for i in range(len(prepared_orders)):
            item_data2 = database.mst_item.return_item(prepared_orders[i][2])
            item_data2 = list(item_data2)
            itemdata_list2.append(item_data2)
            addons_data2 = database.sales_addon.return_addon_code(prepared_orders[i][0])
            addons_data2 = list(addons_data2)
            addons_list2.append(addons_data2)
            
            if addons_list2[i] == []:
                addons_strings = "-"
            else:
                addons_strings = ", ".join([database.mst_item.return_itemname(addon[0]) for addon in addons_list2[i]])

            eachitem_frame2 = customtkinter.CTkFrame(master=prepared_frame,
                                                    height=280,
                                                    width=670,
                                                    fg_color="#FFFFFF")
            eachitem_frame2.grid(row=i, column=0, padx=0, pady=10)

            eachitem_img2 = customtkinter.CTkFrame(master=eachitem_frame2,
                                                corner_radius=0,
                                                height=250,
                                                width=200)
            eachitem_img2.place(relx=0.03, rely=0.04)

            try:
                eachitem_image2.append(customtkinter.CTkImage(Image.open(directory+prepared_orders[i][2]+".jpg", mode="r"), size=(200, 250)))
            except FileNotFoundError:
                eachitem_image2.append(customtkinter.CTkImage(Image.open(directory+"no_image2.png", mode="r"), size=(200, 250)))

            image_label2 = customtkinter.CTkLabel(master=eachitem_img2, text="", image=eachitem_image2[i])
            image_label2.pack()

            itemname_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text=itemdata_list2[i][1],
                                                    font=("TT Commons Medium", 30))
            itemname_label2.place(relx=0.35, rely=0.02)

            itemprice_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="$"+str(prepared_orders[i][9]),
                                                    font=("TT Commons Medium", 25))
            itemprice_label2.place(relx=0.35, rely=0.14)

            itemstatus_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="Status: "+prepared_orders[i][10],
                                                    text_color="#30cc84",
                                                    font=("TT Commons Medium", 25))
            itemstatus_label2.place(relx=0.35, rely=0.23)
            if prepared_orders[i][10] == "Closed":
                itemstatus_label2.configure(text_color="red")

            itemaddons_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="Add-ons: "+addons_strings,
                                                    font=("TT Commons Medium", 18))
            itemaddons_label2.place(relx=0.35, rely=0.33)

            recipientname_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="Recipient: "+prepared_orders[i][6],
                                                    font=("TT Commons Medium", 18))
            recipientname_label2.place(relx=0.35, rely=0.415)

            msg_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="Message: "+prepared_orders[i][8],
                                                    font=("TT Commons Medium", 18))
            msg_label2.place(relx=0.35, rely=0.5)

            choice_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="Choice: "+prepared_orders[i][3]+" (Same day: "+prepared_orders[i][5]+")",
                                                    font=("TT Commons Medium", 18))
            choice_label2.place(relx=0.35, rely=0.585)
            
            deliverydate_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="Delivery date: "+prepared_orders[i][4],
                                                    font=("TT Commons Medium", 18))
            deliverydate_label2.place(relx=0.35, rely=0.67)

            deliveryaddress_label2 = customtkinter.CTkLabel(master=eachitem_frame2,
                                                    text="Delivery address: "+prepared_orders[i][7],
                                                    wraplength=430,
                                                    justify = "left",
                                                    font=("TT Commons Medium", 18))
            deliveryaddress_label2.place(relx=0.35, rely=0.755)

    viewOrder.mainloop()

def buy_item(user, item_data):
    buyItem = customtkinter.CTk()
    buyItem.geometry("1536 x 790")
    buyItem.minsize(1536, 790)
    buyItem.maxsize(1536, 790)
    buyItem.title("Buy Item")
    buyItem.after(0, lambda: buyItem.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=buyItem, image=img1, text="")
    l1.pack()

    #create order text
    l2=customtkinter.CTkLabel(master=buyItem,
                              text="Create order",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #view order button
    def vieworder_function():
        buyItem.destroy()
        view_order(user)

    vieworder_button = customtkinter.CTkButton(master=buyItem,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.83, rely=0.02)

    #back button
    def back_function():
        buyItem.destroy()
        customer_home(user, bought=False)

    back_button = customtkinter.CTkButton(master=buyItem,
                                               text="Back",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=back_function)
    back_button.place(relx=0.705, rely=0.02)

    #profile button
    def profile_function():
        buyItem.destroy()
        customer_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=buyItem,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    #frame
    frame = customtkinter.CTkFrame(master=buyItem,
                                   corner_radius=0,
                                   height=630,
                                   width=1380,
                                   bg_color="#D4BBDD",
                                   fg_color="white")
    frame.place(relx=0.05, rely=0.15)

    #item
    eachitem_img = customtkinter.CTkFrame(master=frame,
                                            corner_radius=0,
                                            height=420,
                                            width=400)
    eachitem_img.place(relx=0.02, rely=0.04)

    try:
        eachitem_image = customtkinter.CTkImage(Image.open(directory+item_data[1]+".jpg", mode="r"), size=(400, 420))
    except FileNotFoundError:
        eachitem_image = customtkinter.CTkImage(Image.open(directory+"no_image2.png", mode="r"), size=(400, 420))

    image_label = customtkinter.CTkLabel(master=eachitem_img, text="", image=eachitem_image)
    image_label.pack()

    item_name = customtkinter.CTkLabel(master=frame,
                                       text=item_data[2],
                                       font=("TT Commons Medium", 55))
    item_name.place(relx=0.025, rely=0.73)
    
    item_price = customtkinter.CTkLabel(master=frame,
                                       text=("$"+str(item_data[4])),
                                       font=("TT Commons Medium", 60))
    item_price.place(relx=0.025, rely=0.83)

    #addons
    addons_frame = customtkinter.CTkScrollableFrame(master=frame,
                                                    orientation="horizontal",
                                                    height=50,
                                                    width=880,
                                                    bg_color="white",
                                                    fg_color="#f9f9fa")
    addons_frame.place(relx=0.33, rely=0.04)

    addon_data = database.mst_item.return_addon()

    var_list = []
    addon_list = []

    def eachaddon_function(i):
        addon_price = 0
        if var_list[i].get() == "on":
            addon_price += addon_data[i][4]
            addon_list.append(addon_data[i])
        else:
            addon_price -= addon_data[i][4]
            addon_list.remove(addon_data[i])
        update_totalprice("addon", addon_price)

    for i in range(len(addon_data)):

        var = customtkinter.StringVar(value="off")
        var_list.append(var)

        eachaddon_frame = customtkinter.CTkFrame(master=addons_frame,
                                                fg_color="#f9f9fa")
        eachaddon_frame.grid(row=0, column=i, padx=20, pady=5)

        eachaddon_checkbox = customtkinter.CTkCheckBox(master=eachaddon_frame,
                                                       text=addon_data[i][2]+" ($"+str(addon_data[i][4])+")",
                                                       font=("TT Commons Medium", 32),
                                                       corner_radius=36,
                                                       border_width=3,
                                                       hover_color="#30cc84",
                                                       command=lambda i=i: eachaddon_function(i),
                                                       variable=var,
                                                       onvalue="on",
                                                       offvalue="off")
        eachaddon_checkbox.pack()

    #other details
    recipientname_label = customtkinter.CTkLabel(master=frame,
                                                text="Recipient name",
                                                font=("TT Commons Medium", 38))
    recipientname_label.place(relx=0.33, rely=0.17)

    recipientname_entry = customtkinter.CTkEntry(master=frame,
                                                 width=540,
                                                font=("TT Commons Medium", 35))
    recipientname_entry.place(relx=0.585, rely=0.17)

    msg_label = customtkinter.CTkLabel(master=frame,
                                        text="Message for recipient",
                                        justify="left",
                                        wraplength=350,
                                        font=("TT Commons Medium", 38))
    msg_label.place(relx=0.33, rely=0.27)

    msg_textbox = customtkinter.CTkTextbox(master=frame,
                                           width=540,
                                           height=100,
                                           border_color="#949ca4",
                                           border_width=2,
                                           font=("TT Commons Medium", 32))
    msg_textbox.place(relx=0.585, rely=0.27)

    total_price = item_data[4]

    def update_totalprice(type, value):
        nonlocal total_price
        nonlocal prev_sameday
        if type == "sameday":
            if value == "Yes":
                total_price += 35
            elif value == "No":
                total_price -= 35
        if type == "pickupordelivery":
            if value == "Delivery":
                total_price += 35
            elif value == "Pick up":
                if prev_sameday == "Yes":
                    prev_sameday = "No"
                    total_price -= 70
                else:
                    total_price -= 35
        if type == "addon":
            total_price += value
        totalprice_label.configure(text="Total: $" + str(total_price))
    
    prev_sameday = "No"

    def sameday_function(choice):
        nonlocal prev_sameday
        if choice == "Yes" and prev_sameday == "No":
            update_totalprice("sameday", choice)
            prev_sameday = "Yes"
        elif choice == "No" and prev_sameday == "Yes":
            update_totalprice("sameday", choice)
            prev_sameday = "No"

    sameday_label = customtkinter.CTkLabel(master=frame,
                                                text="Same day?",
                                                font=("TT Commons Medium", 38))
    
    sameday_var = customtkinter.StringVar(value="No")
        
    sameday_combobox = customtkinter.CTkComboBox(master=frame,
                                                    height=40,
                                                    width=125,
                                                    font=("TT Commons Medium", 32),
                                                    border_color="#949ca4",
                                                    border_width=2,
                                                    bg_color="white",
                                                    fg_color="white",
                                                    dropdown_font=("TT Commons Medium", 32),
                                                    dropdown_fg_color="white",
                                                    dropdown_hover_color="#cd9ede",
                                                    button_color="#cd9ede",
                                                    button_hover_color="#cd9ede",
                                                    values=["No", "Yes"],
                                                    state="readonly",
                                                    variable=sameday_var,
                                                    command=sameday_function)

    deliveryaddress_label = customtkinter.CTkLabel(master=frame,
                                                text="Delivery address",
                                                font=("TT Commons Medium", 38))
    deliveryaddress_label.place(relx=0.33, rely=0.54)

    deliveryaddress_label2 = customtkinter.CTkLabel(master=frame,
                                                text="-",
                                                font=("TT Commons Medium", 35))
    deliveryaddress_label2.place(relx=0.585, rely=0.54)

    deliveryaddress_entry = customtkinter.CTkEntry(master=frame,
                                                width=540,
                                                font=("TT Commons Medium", 35))

    deliverydate_label = customtkinter.CTkLabel(master=frame,
                                                text="Delivery date",
                                                font=("TT Commons Medium", 38))
    deliverydate_label.place(relx=0.33, rely=0.64)

    deliverydate_label2 = customtkinter.CTkLabel(master=frame,
                                                text="-",
                                                font=("TT Commons Medium", 35))
    deliverydate_label2.place(relx=0.585, rely=0.64)

    deliverydate_entry = customtkinter.CTkEntry(master=frame,
                                                width=540,
                                                placeholder_text="DD/MM/YYYY",
                                                font=("TT Commons Medium", 35))

    prev_pickupordelivery = "Pick up"

    def pickupordelivery_function(choice):
        nonlocal prev_pickupordelivery
        if choice == "Delivery" and prev_pickupordelivery == "Pick up":
            update_totalprice("pickupordelivery", choice)
            prev_pickupordelivery = "Delivery"
        elif choice == "Pick up" and prev_pickupordelivery == "Delivery":
            update_totalprice("pickupordelivery", choice)
            prev_pickupordelivery = "Pick up"
        
        if choice == "Delivery":
            sameday_label.place(relx=0.755, rely=0.44)
            sameday_combobox.place(relx=0.885, rely=0.447)
            deliveryaddress_label2.place_forget()
            deliverydate_label2.place_forget()
            deliveryaddress_entry.place(relx=0.585, rely=0.54)
            deliverydate_entry.place(relx=0.585, rely=0.64)

        else:
            sameday_combobox.set("No")
            sameday_label.place_forget()
            sameday_combobox.place_forget()
            deliveryaddress_entry.place_forget()
            deliverydate_entry.place_forget()
            deliveryaddress_label2.place(relx=0.585, rely=0.54)
            deliverydate_label2.place(relx=0.585, rely=0.64)
    
    pickupordelivery_label = customtkinter.CTkLabel(master=frame,
                                                    text="Pick up or delivery?",
                                                    font=("TT Commons Medium", 38))
    pickupordelivery_label.place(relx=0.33, rely=0.44)

    pickupordelivery_var = customtkinter.StringVar(value="Pick up")

    pickupordelivery_combobox = customtkinter.CTkComboBox(master=frame,
                                                            height=40,
                                                            width=200,
                                                            font=("TT Commons Medium", 32),
                                                            border_color="#949ca4",
                                                            border_width=2,
                                                            bg_color="white",
                                                            fg_color="white",
                                                            dropdown_font=("TT Commons Medium", 32),
                                                            dropdown_fg_color="white",
                                                            dropdown_hover_color="#cd9ede",
                                                            button_color="#cd9ede",
                                                            button_hover_color="#cd9ede",
                                                            values=["Pick up", "Delivery"],
                                                            variable=pickupordelivery_var,
                                                            state="readonly",
                                                            command=pickupordelivery_function)
    pickupordelivery_combobox.place(relx=0.585, rely=0.447)

    totalprice_label = customtkinter.CTkLabel(master=frame,
                                       text=("Total: $"+str(total_price)),
                                       font=("TT Commons Medium", 60))
    totalprice_label.place(relx=0.33, rely=0.83)

    #buy
    def buy_function():
        order = database.trx_sales("", "", "", "", "", "", "", "", "", "", "")
        order.order_id = database.trx_sales.get_orderid()
        order.user_id = user[0]
        order.bloom_code = item_data[1]
        order.pickup_or_delivery = pickupordelivery_combobox.get()
        if order.pickup_or_delivery == "Delivery":
            order.same_day_delivery = sameday_combobox.get()
            order.delivery_date = deliverydate_entry.get()
            order.recipient_address = deliveryaddress_entry.get()
        else:
            order.same_day_delivery = "-"
            order.delivery_date = "-"
            order.recipient_address = "-"
        order.recipient_name = recipientname_entry.get()
        order.msg_for_recipient = msg_textbox.get("1.0", "end-1c")
        if order.msg_for_recipient == "":
            order.msg_for_recipient = "-"
        order.total_sales = total_price
        order.order_status = "Open"
        if order.delivery_date == "" or order.same_day_delivery == "" or order.recipient_address == "" or order.recipient_name == "":
            incomplete_label = customtkinter.CTkLabel(master = frame,
                                                    text="*Data is not complete",
                                                    text_color="red",
                                                    font=("TT Commons Medium", 35),
                                                    bg_color="#FFFFFF")
            incomplete_label.place(relx=0.975, rely=0.77, anchor="e")
        else:
            for i in range(len(addon_list)):
                database.sales_addon.connect_addon(order.order_id, addon_list[i][1])
            database.trx_sales.add_order(order)
            buyItem.destroy()
            customer_home(user, bought=True)

    buy_button = customtkinter.CTkButton(master=frame,
                                         corner_radius=30,
                                         width=100,
                                         text = "Buy now",
                                         font=("TT Commons Medium", 60),
                                         command = buy_function)
    buy_button.place(relx=0.803, rely=0.82)

    buyItem.mainloop()

def edit_order(user, ordered_order, addons):
    editOrder = customtkinter.CTk()
    editOrder.geometry("1536 x 790")
    editOrder.minsize(1536, 790)
    editOrder.maxsize(1536, 790)
    editOrder.title("Buy Item")
    editOrder.after(0, lambda: editOrder.wm_state('zoomed'))

    item_data = database.mst_item.return_item(ordered_order[2])

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=editOrder, image=img1, text="")
    l1.pack()

    #Edit order text
    l2=customtkinter.CTkLabel(master=editOrder,
                              text="Edit order",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #create order button
    def createorder_function():
        editOrder.destroy()
        customer_home(user, False)

    createorder_button = customtkinter.CTkButton(master=editOrder,
                                               text="Create Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=createorder_function)
    createorder_button.place(relx=0.83, rely=0.02)

    #back button
    def back_function():
        editOrder.destroy()
        view_order(user)

    back_button = customtkinter.CTkButton(master=editOrder,
                                               text="Back",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=back_function)
    back_button.place(relx=0.705, rely=0.02)

    #profile button
    def profile_function():
        editOrder.destroy()
        customer_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=editOrder,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    #frame
    frame = customtkinter.CTkFrame(master=editOrder,
                                   corner_radius=0,
                                   height=630,
                                   width=1380,
                                   bg_color="#D4BBDD",
                                   fg_color="white")
    frame.place(relx=0.05, rely=0.15)

    #item
    eachitem_img = customtkinter.CTkFrame(master=frame,
                                            corner_radius=0,
                                            height=420,
                                            width=400)
    eachitem_img.place(relx=0.02, rely=0.04)

    try:
        eachitem_image = customtkinter.CTkImage(Image.open(directory+ordered_order[2]+".jpg", mode="r"), size=(400, 420))
    except FileNotFoundError:
        eachitem_image = customtkinter.CTkImage(Image.open(directory+"no_image2.png", mode="r"), size=(400, 420))

    image_label = customtkinter.CTkLabel(master=eachitem_img, text="", image=eachitem_image)
    image_label.pack()

    item_name = customtkinter.CTkLabel(master=frame,
                                       text=item_data[1],
                                       font=("TT Commons Medium", 55))
    item_name.place(relx=0.025, rely=0.73)
    
    item_price = customtkinter.CTkLabel(master=frame,
                                       text=("$"+str(item_data[3])),
                                       font=("TT Commons Medium", 60))
    item_price.place(relx=0.025, rely=0.83)

    #addons
    addons_frame = customtkinter.CTkScrollableFrame(master=frame,
                                                    orientation="horizontal",
                                                    height=50,
                                                    width=880,
                                                    bg_color="white",
                                                    fg_color="#f9f9fa")
    addons_frame.place(relx=0.33, rely=0.04)

    addon_data = database.mst_item.return_addon()

    var_list = []
    addon_list = []
    
    def eachaddon_function(i):
        addon_price = 0
        if var_list[i].get() == "on":
            addon_price += addon_data[i][4]
            addon_list.append(addon_data[i])
        else:
            addon_price -= addon_data[i][4]
            addon_list.remove(addon_data[i])
        update_totalprice("addon", addon_price)

    addon_name = []

    for i in range(len(addons)):
        addon_name.append(database.mst_item.return_itemname(addons[i][0]))

    for i in range(len(addon_data)):

        if addon_data[i][2] in addon_name:
            var = customtkinter.StringVar(value="on")
            addon_list.append(addon_data[i])
        else:
            var = customtkinter.StringVar(value="off")
        
        var_list.append(var)

        eachaddon_frame = customtkinter.CTkFrame(master=addons_frame,
                                                fg_color="#f9f9fa")
        eachaddon_frame.grid(row=0, column=i, padx=20, pady=5)

        eachaddon_checkbox = customtkinter.CTkCheckBox(master=eachaddon_frame,
                                                       text=addon_data[i][2]+" ($"+str(addon_data[i][4])+")",
                                                       font=("TT Commons Medium", 32),
                                                       corner_radius=36,
                                                       border_width=3,
                                                       hover_color="#30cc84",
                                                       command=lambda i=i: eachaddon_function(i),
                                                       variable=var,
                                                       onvalue="on",
                                                       offvalue="off")
        eachaddon_checkbox.pack()

    #other details
    recipientname_label = customtkinter.CTkLabel(master=frame,
                                                text="Recipient name",
                                                font=("TT Commons Medium", 38))
    recipientname_label.place(relx=0.33, rely=0.17)

    recipientname_entry = customtkinter.CTkEntry(master=frame,
                                                 width=540,
                                                 placeholder_text=ordered_order[6],
                                                 font=("TT Commons Medium", 35))
    recipientname_entry.place(relx=0.585, rely=0.17)

    msg_label = customtkinter.CTkLabel(master=frame,
                                        text="Message for recipient",
                                        justify="left",
                                        wraplength=350,
                                        font=("TT Commons Medium", 38))
    msg_label.place(relx=0.33, rely=0.27)

    msg_textbox = customtkinter.CTkTextbox(master=frame,
                                           width=540,
                                           height=100,
                                           border_color="#949ca4",
                                           border_width=2,
                                           font=("TT Commons Medium", 32))
    msg_textbox.place(relx=0.585, rely=0.27)

    total_price = ordered_order[9]

    def update_totalprice(type, value):
        nonlocal total_price
        nonlocal prev_sameday
        if type == "sameday":
            if value == "Yes":
                total_price += 35
            elif value == "No":
                total_price -= 35
        if type == "pickupordelivery":
            if value == "Delivery":
                total_price += 35
            elif value == "Pick up":
                if prev_sameday == "Yes":
                    prev_sameday = "No"
                    total_price -= 70
                else:
                    total_price -= 35
        if type == "addon":
            total_price += value
        totalprice_label.configure(text="Total: $" + str(total_price))
    
    sameday_var = customtkinter.StringVar(value=ordered_order[5]) 
    prev_sameday = ordered_order[5]
    if prev_sameday == "-":
        sameday_var = customtkinter.StringVar(value="No")
        prev_sameday = "No"

    def sameday_function(choice):
        nonlocal prev_sameday
        if choice == "Yes" and prev_sameday == "No":
            update_totalprice("sameday", choice)
            prev_sameday = "Yes"
        elif choice == "No" and prev_sameday == "Yes":
            update_totalprice("sameday", choice)
            prev_sameday = "No"

    sameday_label = customtkinter.CTkLabel(master=frame,
                                                text="Same day?",
                                                font=("TT Commons Medium", 38))
        
    sameday_combobox = customtkinter.CTkComboBox(master=frame,
                                                    height=40,
                                                    width=125,
                                                    font=("TT Commons Medium", 32),
                                                    border_color="#949ca4",
                                                    border_width=2,
                                                    bg_color="white",
                                                    fg_color="white",
                                                    dropdown_font=("TT Commons Medium", 32),
                                                    dropdown_fg_color="white",
                                                    dropdown_hover_color="#cd9ede",
                                                    button_color="#cd9ede",
                                                    button_hover_color="#cd9ede",
                                                    values=["No", "Yes"],
                                                    variable=sameday_var,
                                                    state="readonly",
                                                    command=sameday_function)

    deliveryaddress_label = customtkinter.CTkLabel(master=frame,
                                                text="Delivery address",
                                                font=("TT Commons Medium", 38))
    deliveryaddress_label.place(relx=0.33, rely=0.54)

    deliveryaddress_label2 = customtkinter.CTkLabel(master=frame,
                                                text="-",
                                                font=("TT Commons Medium", 35))
    deliveryaddress_label2.place(relx=0.585, rely=0.54)

    deliveryaddress_entry = customtkinter.CTkEntry(master=frame,
                                                width=540,
                                                placeholder_text=ordered_order[7],
                                                font=("TT Commons Medium", 35))

    deliverydate_label = customtkinter.CTkLabel(master=frame,
                                                text="Delivery date",
                                                font=("TT Commons Medium", 38))
    deliverydate_label.place(relx=0.33, rely=0.64)

    deliverydate_label2 = customtkinter.CTkLabel(master=frame,
                                                text="-",
                                                font=("TT Commons Medium", 35))
    deliverydate_label2.place(relx=0.585, rely=0.64)

    deliverydate_entry = customtkinter.CTkEntry(master=frame,
                                                width=540,
                                                placeholder_text=ordered_order[4],
                                                font=("TT Commons Medium", 35))
    
    pickupordelivery_var = customtkinter.StringVar(value=ordered_order[3]) 
    prev_pickupordelivery = ordered_order[3]

    if ordered_order[3] == "Delivery":
        sameday_label.place(relx=0.755, rely=0.44)
        sameday_combobox.place(relx=0.885, rely=0.447)
        deliveryaddress_label2.place_forget()
        deliverydate_label2.place_forget()
        deliveryaddress_entry.place(relx=0.585, rely=0.54)
        deliverydate_entry.place(relx=0.585, rely=0.64)

    def pickupordelivery_function(choice):
        nonlocal prev_pickupordelivery
        if choice == "Delivery" and prev_pickupordelivery == "Pick up":
            update_totalprice("pickupordelivery", choice)
            prev_pickupordelivery = "Delivery"
        elif choice == "Pick up" and prev_pickupordelivery == "Delivery":
            update_totalprice("pickupordelivery", choice)
            prev_pickupordelivery = "Pick up"
        
        if choice == "Delivery":
            sameday_label.place(relx=0.755, rely=0.44)
            sameday_combobox.place(relx=0.885, rely=0.447)
            deliveryaddress_label2.place_forget()
            deliverydate_label2.place_forget()
            deliveryaddress_entry.place(relx=0.585, rely=0.54)
            deliverydate_entry.place(relx=0.585, rely=0.64)

        else:
            sameday_combobox.set("No")
            sameday_label.place_forget()
            sameday_combobox.place_forget()
            deliveryaddress_entry.place_forget()
            deliverydate_entry.place_forget()
            deliveryaddress_label2.place(relx=0.585, rely=0.54)
            deliverydate_label2.place(relx=0.585, rely=0.64)
    
    pickupordelivery_label = customtkinter.CTkLabel(master=frame,
                                                    text="Pick up or delivery?",
                                                    font=("TT Commons Medium", 38))
    pickupordelivery_label.place(relx=0.33, rely=0.44)

    pickupordelivery_combobox = customtkinter.CTkComboBox(master=frame,
                                                            height=40,
                                                            width=200,
                                                            font=("TT Commons Medium", 32),
                                                            border_color="#949ca4",
                                                            border_width=2,
                                                            bg_color="white",
                                                            fg_color="white",
                                                            dropdown_font=("TT Commons Medium", 32),
                                                            dropdown_fg_color="white",
                                                            dropdown_hover_color="#cd9ede",
                                                            button_color="#cd9ede",
                                                            button_hover_color="#cd9ede",
                                                            values=["Pick up", "Delivery"],
                                                            variable=pickupordelivery_var,
                                                            state="readonly",
                                                            command=pickupordelivery_function)
    pickupordelivery_combobox.place(relx=0.585, rely=0.447)

    totalprice_label = customtkinter.CTkLabel(master=frame,
                                       text=("Total: $"+str(total_price)),
                                       font=("TT Commons Medium", 60))
    totalprice_label.place(relx=0.33, rely=0.83)

    #save
    def save_function():
        invalid_error = False
        order = database.trx_sales("", "", "", "", "", "", "", "", "", "", "")
        order.order_id = ordered_order[0]
        order.pickup_or_delivery = pickupordelivery_combobox.get()

        if order.pickup_or_delivery == "Delivery":
            order.same_day_delivery = sameday_combobox.get()

            order.delivery_date = deliverydate_entry.get()
            if order.delivery_date == "":
                order.delivery_date = ordered_order[4]

            order.recipient_address = deliveryaddress_entry.get()
            if order.recipient_address == "":
                order.recipient_address = ordered_order[7]

            if ordered_order[3] == "Pick up":
                if order.delivery_date == "-" or order.recipient_address == "-":
                    incomplete_label = customtkinter.CTkLabel(master = frame,
                                                    text="*Data is not complete",
                                                    text_color="red",
                                                    font=("TT Commons Medium", 45),
                                                    bg_color="#FFFFFF")
                    incomplete_label.place(relx=0.697, rely=0.73)
                    invalid_error = True

        else:
            order.same_day_delivery = "-"
            order.delivery_date = "-"
            order.recipient_address = "-"

        order.recipient_name = recipientname_entry.get()
        if order.recipient_name == "":
            order.recipient_name = ordered_order[6]

        order.msg_for_recipient = msg_textbox.get("1.0", "end-1c")

        if order.msg_for_recipient == "":
            order.msg_for_recipient = ordered_order[8]

        order.total_sales = total_price

        if invalid_error == False:
            database.sales_addon.edit_addon(order.order_id, addon_list)
            database.trx_sales.edit_order(order)
            editOrder.destroy()
            view_order(user)

    save_button = customtkinter.CTkButton(master=frame,
                                         corner_radius=30,
                                         width=100,
                                         text = "Save edit",
                                         font=("TT Commons Medium", 60),
                                         command = save_function)
    save_button.place(relx=0.795, rely=0.82)

    editOrder.mainloop()

#SELLER
def seller_home(user, edited):
    sellerHome = customtkinter.CTk()
    sellerHome.geometry("1536 x 790")
    sellerHome.minsize(1536, 790)
    sellerHome.maxsize(1536, 790)
    sellerHome.title("Home Page")
    sellerHome.after(0, lambda: sellerHome.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"home_page.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=sellerHome, image=img1, text="")
    l1.pack()

    #Edit item text
    l2=customtkinter.CTkLabel(master=sellerHome,
                              text="Edit Item",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #add item button
    def additem_function():
        sellerHome.destroy()
        add_item(user)

    additem_button = customtkinter.CTkButton(master=sellerHome,
                                               text="Add Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=additem_function)
    additem_button.place(relx=0.705, rely=0.02)

    #view order button
    def ordertable_function():
        sellerHome.destroy()
        order_table(user)

    ordertable_button = customtkinter.CTkButton(master=sellerHome,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=ordertable_function)
    ordertable_button.place(relx=0.83, rely=0.02)

    #profile button
    def profile_function():
        sellerHome.destroy()
        seller_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=sellerHome,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    def clear_label():
        edited_label.configure(text="")

    #edited label
    if edited == True:
        edited_label = customtkinter.CTkLabel(master=sellerHome,
                                            bg_color="#F8F8FF",
                                            fg_color="#D4BBDD",
                                            text="*Changes saved",
                                            font=("TT Commons Medium", 30),
                                            text_color="#5E376D")
        edited_label.place(relx=0.55, rely=0.5)
        sellerHome.after(2000, clear_label)

    #search bar
    def search_function():
        keyword = search_entry.get()
        item_data = database.mst_item.search_name(keyword)
        if sortby_combobox.get()=="Name":
            item_data.sort(key=lambda x: x[2])
        elif sortby_combobox.get()=="Price":
            item_data.sort(key=lambda x: x[4])
        if category_combobox.get()!="All" and category_combobox.get()!="Category":
            item_data = filter(lambda x: x[3]==category_combobox.get(), item_data)
            item_data = list(item_data)
        show_list(item_data)

    search_frame = customtkinter.CTkFrame(master=sellerHome,
                                          height=40,
                                          width=350,
                                          bg_color="#D4BBDD",
                                          fg_color="#F8F8FF")
    search_frame.place(relx=0.015, rely=0.495)

    search_entry = customtkinter.CTkEntry(master=search_frame,
                                          placeholder_text="Search...",
                                          font=("TT Commons Medium", 20),
                                          bg_color="#D4BBDD",
                                          fg_color="#F8F8FF",
                                          border_width=2,
                                          border_color="#000000",
                                          height=40,
                                          width=305.6)
    search_entry.place(relx=0, rely=0)

    search_image = customtkinter.CTkImage(Image.open(directory+"search_button.png", mode="r"), size=(30,30))
    search_button = customtkinter.CTkButton(master=search_frame,
                                             width=0,
                                             text="",
                                             bg_color="#D4BBDD",
                                             fg_color="#5E376D",
                                             hover_color="#5E376D",
                                             border_width=2,
                                             border_color="#000000",
                                             image=search_image,
                                             command=search_function)
    search_button.place(relx=0.865, rely=0)

    #sort by
    sortby_var = customtkinter.StringVar(value="Sort by")

    sortby_combobox = customtkinter.CTkComboBox(master=sellerHome,
                                                height=40,
                                                width=200,
                                                font=("Arial", 20),
                                                bg_color="#D4BBDD",
                                                fg_color="#F8F8FF",
                                                dropdown_font=("TT Commons Medium", 20),
                                                dropdown_fg_color="#F8F8FF",
                                                dropdown_hover_color="#cd9ede",
                                                border_width=2,
                                                border_color="#000000",
                                                button_color="#5E376D",
                                                button_hover_color="#5E376D",
                                                values=["Name", "Price"],
                                                state="readonly",
                                                variable = sortby_var)
    sortby_combobox.place(relx=0.257, rely=0.495)

    #category
    category_var = customtkinter.StringVar(value="Category")

    category_combobox = customtkinter.CTkComboBox(master=sellerHome,
                                                height=40,
                                                width=200,
                                                font=("Arial", 20),
                                                bg_color="#D4BBDD",
                                                fg_color="#F8F8FF",
                                                dropdown_font=("TT Commons Medium", 20),
                                                dropdown_fg_color="#F8F8FF",
                                                dropdown_hover_color="#cd9ede",
                                                border_width=2,
                                                border_color="#000000",
                                                button_color="#5E376D",
                                                button_hover_color="#5E376D",
                                                values=["All", "Anniversary", "Birthday", "Condolence", "Grand Opening", "Romantic"],
                                                variable = category_var)
    category_combobox.place(relx=0.4, rely=0.495)

    #edit addons
    def editaddons_function():
        sellerHome.destroy()
        edit_addons(user)

    editaddons_button = customtkinter.CTkButton(master=sellerHome,
                                               text="Edit add-ons",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#D4BBDD",
                                               fg_color="#866492",
                                               hover_color="#674b70",
                                               command=editaddons_function)
    editaddons_button.place(relx=0.87, rely=0.495)

    #items
    def show_list(item_data):
        item_frame = customtkinter.CTkScrollableFrame(master=sellerHome,
                                                    orientation="horizontal",
                                                    height=318,
                                                    width=1494,
                                                    bg_color="#D4BBDD",
                                                    fg_color="#D4BBDD")
        item_frame.place(relx=0.01, rely=0.57)

        if item_data == []:
            no_item = customtkinter.CTkLabel(master=sellerHome,
                                             text="Sorry, couldn't find item.\nTry searching again in different keyword or adding the item in 'Add Item'.",
                                             justify="center",
                                             font=("TT Commons Medium", 35),
                                             text_color="#866492",
                                             corner_radius=0,
                                             fg_color="#D4BBDD")
            no_item.place(relx=0.5, rely=0.75, anchor="center")

        else:
            def edit_function(i):
                def inner_edit_function():
                    sellerHome.destroy()
                    edit_item(user, item_data[i])

                return inner_edit_function
            
            eachitem_image = []

            for i in range(len(item_data)):
                eachitem_frame = customtkinter.CTkFrame(master=item_frame,
                                                        height=315,
                                                        width=200,
                                                        fg_color="#D4BBDD")
                eachitem_frame.grid(row=0, column=i, padx=25, pady=0)

                eachitem_img = customtkinter.CTkFrame(master=eachitem_frame,
                                                    corner_radius=0,
                                                    height=250,
                                                    width=200)
                eachitem_img.place(relx=0, rely=0)

                try:
                    eachitem_image.append(customtkinter.CTkImage(Image.open(directory+item_data[i][1]+".jpg", mode="r"), size=(200, 285.5)))
                except FileNotFoundError:
                    eachitem_image.append(customtkinter.CTkImage(Image.open(directory+"no_image.png", mode="r"), size=(200, 285.5)))

                image_label = customtkinter.CTkLabel(master=eachitem_img, text="", image=eachitem_image[i])
                image_label.pack()

                eachitem_desc = customtkinter.CTkFrame(master=eachitem_frame,
                                                    corner_radius=0,
                                                    height=106,
                                                    width=188,
                                                    fg_color="white",
                                                    bg_color="white")
                eachitem_desc.place(relx=0.03, rely=0.55)

                eachitem_text = customtkinter.CTkLabel(master=eachitem_desc,
                                                    corner_radius=0,
                                                    height=106,
                                                    width=188,
                                                    fg_color="white",
                                                    font=("Calibri", 15),
                                                    text=("{name}\n#{category}\n${price}\nStock: {quantity}".format(name = item_data[i][2], price = item_data[i][4], quantity = item_data[i][5], category = item_data[i][3])),
                                                    text_color="#5E376D")
                eachitem_text.place(relx=0, rely=-0.065)

                edit_button = customtkinter.CTkButton(master=eachitem_frame,
                                                    corner_radius=0,
                                                    height=40,
                                                    width=100,
                                                    text="Edit",
                                                    font=("TT Commons Medium", 15),
                                                    bg_color="#866492",
                                                    fg_color="#866492",
                                                    hover_color="#674b70",
                                                    command=edit_function(i))
                edit_button.place(relx=0.25, rely=0.83)

    item_data = database.mst_item.sort_item_name()
    show_list(item_data)

    sellerHome.mainloop()

def seller_profile(user):
    sprofilePage = customtkinter.CTk()
    sprofilePage.geometry("1536 x 790")
    sprofilePage.minsize(1536, 790)
    sprofilePage.maxsize(1536, 790)
    sprofilePage.title("Profile Page")
    sprofilePage.after(0, lambda: sprofilePage.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=sprofilePage, image=img1, text="")
    l1.pack()

    #profile text
    l2=customtkinter.CTkLabel(master=sprofilePage,
                              text="Profile",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #add item button
    def additem_function():
        sprofilePage.destroy()
        add_item(user)

    additem_button = customtkinter.CTkButton(master=sprofilePage,
                                               text="Add Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=additem_function)
    additem_button.place(relx=0.61, rely=0.02)

    #view order button
    def ordertable_function():
        sprofilePage.destroy()
        order_table(user)

    ordertable_button = customtkinter.CTkButton(master=sprofilePage,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=ordertable_function)
    ordertable_button.place(relx=0.74, rely=0.02)

    #Edit item button
    def sellerhome_function():
        sprofilePage.destroy()
        seller_home(user, False)

    sellerhome_button = customtkinter.CTkButton(master=sprofilePage,
                                               text="Edit Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=sellerhome_function)
    sellerhome_button.place(relx=0.87, rely=0.02)
    
    #change profile button
    def schangeprofile_function():
        sprofilePage.destroy()
        schange_profile(user)
    
    cchangeprofile_button = customtkinter.CTkButton(master=sprofilePage,
                                            text="Change Profile",
                                            width=250,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#866492",
                                            hover_color="#674b70",
                                            command=schangeprofile_function)
    cchangeprofile_button.place(relx=0.81, rely=0.79)

    #logout button
    def logout_function():
        sprofilePage.destroy()
        login_page()
    
    logout_button = customtkinter.CTkButton(master=sprofilePage,
                                            text="Log out",
                                            width=250,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#ff3131",
                                            hover_color="#de1b1b",
                                            command=logout_function)
    logout_button.place(relx=0.81, rely=0.88)

    #personal information
    detail_frame = customtkinter.CTkFrame(master=sprofilePage,
                                          height=625,
                                          width=1150,
                                          bg_color="#FFFFFF",
                                          fg_color="#FFFFFF")
    detail_frame.place(relx=0.03, rely=0.15)

    personalinfo_label = customtkinter.CTkLabel(master=detail_frame,
                                                text="Personal Information",
                                                font=("TT Commons Medium", 55))
    personalinfo_label.place(relx=0.03, rely=0.04)

    username1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Username",
                                            font=("TT Commons Medium", 40))
    username1_label.place(relx=0.03, rely=0.18)

    username2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[0],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    username2_label.place(relx=0.33, rely=0.18)

    password1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Password",
                                            font=("TT Commons Medium", 40))
    password1_label.place(relx=0.03, rely=0.28)

    password2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text="*" * len(user[1]),
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    password2_label.place(relx=0.33, rely=0.28)

    identity1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Identity",
                                            font=("TT Commons Medium", 40))
    identity1_label.place(relx=0.03, rely=0.38)

    identity2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[2],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    identity2_label.place(relx=0.33, rely=0.38)

    fullname1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Full name",
                                            font=("TT Commons Medium", 40))
    fullname1_label.place(relx=0.03, rely=0.48)

    fullname2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[3],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    fullname2_label.place(relx=0.33, rely=0.48)

    email1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Email",
                                            font=("TT Commons Medium", 40))
    email1_label.place(relx=0.03, rely=0.58)

    email2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[4],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    email2_label.place(relx=0.33, rely=0.58)

    phonenumber1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Phone number",
                                            font=("TT Commons Medium", 40))
    phonenumber1_label.place(relx=0.03, rely=0.68)

    phonenumber2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[5],
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    phonenumber2_label.place(relx=0.33, rely=0.68)

    address1_label = customtkinter.CTkLabel(master=detail_frame,
                                            text="Address",
                                            font=("TT Commons Medium", 40))
    address1_label.place(relx=0.03, rely=0.78)

    address2_label = customtkinter.CTkLabel(master=detail_frame,
                                             text=user[6],
                                             wraplength=720,
                                             justify = "left",
                                             font=("TT Commons Medium", 40),
                                             text_color="#97928D")
    address2_label.place(relx=0.33, rely=0.78)

    sprofilePage.mainloop()

def schange_profile(user):
    schangeProfile = customtkinter.CTk()
    schangeProfile.geometry("1536 x 790")
    schangeProfile.minsize(1536, 790)
    schangeProfile.maxsize(1536, 790)
    schangeProfile.title("Change Profile")
    schangeProfile.after(0, lambda: schangeProfile.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+r"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=schangeProfile, image=img1, text="")
    l1.pack()

    #change profile text
    l2=customtkinter.CTkLabel(master=schangeProfile,
                              text="Change Profile",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #add item button
    def additem_function():
        schangeProfile.destroy()
        add_item(user)

    additem_button = customtkinter.CTkButton(master=schangeProfile,
                                               text="Add Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=additem_function)
    additem_button.place(relx=0.61, rely=0.02)

    #view order button
    def ordertable_function():
        schangeProfile.destroy()
        order_table(user)

    ordertable_button = customtkinter.CTkButton(master=schangeProfile,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=ordertable_function)
    ordertable_button.place(relx=0.74, rely=0.02)

    #Edit item button
    def sellerhome_function():
        schangeProfile.destroy()
        seller_home(user, False)

    sellerhome_button = customtkinter.CTkButton(master=schangeProfile,
                                               text="Edit Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=sellerhome_function)
    sellerhome_button.place(relx=0.87, rely=0.02)
    
    #change detail frame
    changedetail_frame = customtkinter.CTkFrame(master=schangeProfile,
                                                height=580,
                                                width=1440,
                                                bg_color="#FFFFFF",
                                                fg_color="#FFFFFF")
    changedetail_frame.place(relx=0.03, rely=0.15)

    username1_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Username",
                                            font=("TT Commons Medium", 50))
    username1_label.place(relx=0.03, rely=0.05)

    username2_label = customtkinter.CTkLabel(master=changedetail_frame,
                                             text=user[0],
                                             font=("TT Commons Medium", 50),
                                             text_color="#97928D")
    username2_label.place(relx=0.3, rely=0.05)

    password_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Password",
                                            font=("TT Commons Medium", 50))
    password_label.place(relx=0.03, rely=0.2)

    password_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text="*"*len(user[1]),
                                            font=("TT Commons Medium", 50))
    password_entry.place(relx=0.3, rely=0.2)

    fullname_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Full name",
                                            font=("TT Commons Medium", 50))
    fullname_label.place(relx=0.03, rely=0.35)

    fullname_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text=user[3],
                                            font=("TT Commons Medium", 50))
    fullname_entry.place(relx=0.3, rely=0.35)

    email_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Email",
                                            font=("TT Commons Medium", 50))
    email_label.place(relx=0.03, rely=0.5)

    email_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text=user[4],
                                            font=("TT Commons Medium", 50))
    email_entry.place(relx=0.3, rely=0.5)

    phonenumber_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Phone number",
                                            font=("TT Commons Medium", 50))
    phonenumber_label.place(relx=0.03, rely=0.65)

    phonenumber_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                            width = 950,
                                            placeholder_text=user[5],
                                            font=("TT Commons Medium", 50))
    phonenumber_entry.place(relx=0.3, rely=0.65)

    address_label = customtkinter.CTkLabel(master=changedetail_frame,
                                            text="Address",
                                            font=("TT Commons Medium", 50))
    address_label.place(relx=0.03, rely=0.8)

    address_entry = customtkinter.CTkEntry(master=changedetail_frame,
                                           width = 950,
                                           placeholder_text=user[6],
                                           font=("TT Commons Medium", 50))
    address_entry.place(relx=0.3, rely=0.8)

    #save button
    def save_function():
        nonlocal user
        if password_entry.get() == "":
            pass
        else:
            user[1] = password_entry.get()
        if fullname_entry.get() == "":
            pass
        else:
            user[3] = fullname_entry.get()
        if email_entry.get() == "":
            pass
        else:
            user[4] = email_entry.get()
        if phonenumber_entry.get() == "":
            pass
        else:
            user[5] = phonenumber_entry.get()
        if address_entry.get() == "":
            pass
        else:
            user[6] = address_entry.get()
        database.mst_user.change_account_detail(user)
        schangeProfile.destroy()
        seller_profile(user)

    save_button = customtkinter.CTkButton(master=schangeProfile,
                                            text="Save",
                                            width=180,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#866492",
                                            hover_color="#674b70",
                                            command=save_function)
    save_button.place(relx=0.722, rely=0.911)
    
    #return button
    def return_function():
        schangeProfile.destroy()
        seller_profile(user)
    
    return_button = customtkinter.CTkButton(master=schangeProfile,
                                            text="Return",
                                            width=180,
                                            font=("TT Commons Medium", 35),
                                            border_color="#000000",
                                            bg_color="#D4BBDD",
                                            fg_color="#ff3131",
                                            hover_color="#de1b1b",
                                            command=return_function)
    return_button.place(relx=0.852, rely=0.911)

    schangeProfile.mainloop()

def order_table(user):
    orderTable = customtkinter.CTk()
    orderTable.geometry("1536 x 790")
    orderTable.minsize(1536, 790)
    orderTable.maxsize(1536, 790)
    orderTable.title("View Order")
    orderTable.after(0, lambda: orderTable.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=orderTable, image=img1, text="")
    l1.pack()

    #edit item text
    l2=customtkinter.CTkLabel(master=orderTable,
                              text="View Order",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #add item button
    def additem_function():
        orderTable.destroy()
        add_item(user)

    additem_button = customtkinter.CTkButton(master=orderTable,
                                               text="Add Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=additem_function)
    additem_button.place(relx=0.705, rely=0.02)

    #edit item button
    def edititem_function():
        orderTable.destroy()
        seller_home(user, False)

    edititem_button = customtkinter.CTkButton(master=orderTable,
                                               text="Edit Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=edititem_function)
    edititem_button.place(relx=0.83, rely=0.02)

    #profile button
    def profile_function():
        orderTable.destroy()
        seller_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=orderTable,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    #table
    table_frame = customtkinter.CTkScrollableFrame(master=orderTable,
                                                    corner_radius=0,
                                                    height=600,
                                                    width=1430,
                                                    bg_color="#D4BBDD",
                                                    fg_color="white")
    table_frame.place(relx=0.03, rely=0.15)

    order = database.trx_sales.return_all_order()

    order_combobox = []

    for y in range(len(order)+1):
        for x in range(12):
            if y == 0:
                header_frame = customtkinter.CTkFrame(master=table_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      width=90,
                                                      fg_color="#5E376D")
                header_frame.grid(row=0, column=x, padx=0.3, pady=0.4)
                header_label = customtkinter.CTkLabel(master=header_frame,
                                                      corner_radius=0,
                                                      fg_color="#5E376D",
                                                      font=("TT Commmons Medium", 14),
                                                      text_color="white")
                header_label.place(relx=0.5, rely=0.5, anchor="center")
                if x == 0:
                    header_frame.configure(width=60)
                    header_label.configure(text="Order ID")
                if x == 1:
                    header_label.configure(text="Username")
                if x == 2:
                    header_label.configure(text="Bloom Code")
                if x == 3:
                    header_frame.configure(width=185)
                    header_label.configure(text="Add-ons Code")
                if x == 4:
                    header_label.configure(text="Choice")
                if x == 5:
                    header_label.configure(text="Delivery Date")
                if x == 6:
                    header_label.configure(text="Same Day")
                if x == 7:
                    header_label.configure(text="Recipient")
                if x == 8:
                    header_frame.configure(width=210)
                    header_label.configure(text="Address")
                if x == 9:
                    header_frame.configure(width=215)
                    header_label.configure(text="Message")
                if x == 10:
                    header_label.configure(text="Total Price")
                if x == 11:
                    header_frame.configure(width=128)
                    header_label.configure(text="Status")
            else:
                order_frame = customtkinter.CTkFrame(master=table_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      width=90,
                                                      fg_color="#f9f9fa")
                order_frame.grid(row=y, column=x, padx=0.3, pady=0.4)
                order_label = customtkinter.CTkLabel(master=order_frame,
                                                      wraplength=90,
                                                      corner_radius=0,
                                                      fg_color="#f9f9fa",
                                                      font=("TT Commmons Medium", 15),
                                                      text_color="black")
                order_label.place(relx=0.5, rely=0.5, anchor="center")
                if x == 0:
                    order_frame.configure(width=60)
                    order_label.configure(text=order[y-1][0], wraplength=60)
                if x == 1:
                    order_label.configure(text=order[y-1][1])
                if x == 2:
                    order_label.configure(text=order[y-1][2])
                if x == 3:
                    order_frame.configure(width=185)
                    addon_codes = database.sales_addon.return_addon_code(order[y-1][0])
                    addons_strings = ", ".join(str(addon_code[0]) for addon_code in addon_codes)
                    if addons_strings == "":
                        addons_strings = "-"
                    order_label.configure(text=addons_strings, wraplength=185)
                if x == 4:
                    order_label.configure(text=order[y-1][3])
                if x == 5:
                    order_label.configure(text=order[y-1][4])
                if x == 6:
                    order_label.configure(text=order[y-1][5])
                if x == 7:
                    order_label.configure(text=order[y-1][6])
                if x == 8:
                    order_frame.configure(width=210)
                    order_label.configure(text=order[y-1][7], wraplength=210)
                if x == 9:
                    order_frame.configure(width=215)
                    order_label.configure(text=order[y-1][8], wraplength=215)
                if x == 10:
                    order_label.configure(text=order[y-1][9])
                if x == 11:
                    order_frame.configure(width=128)
                    order_label.place_forget()
                    
                    status_var=customtkinter.StringVar(value=order[y-1][10])
                    order_combobox.append(customtkinter.CTkComboBox(master=order_frame,
                                                               corner_radius=0,
                                                               border_width=0,
                                                               height=40,
                                                               width=128,
                                                               fg_color="#f9f9fa",
                                                               font=("TT Commmons Medium", 15),
                                                               text_color="black",
                                                               button_color="#cd9ede",
                                                               button_hover_color="#b382c4",
                                                               values=["Open", "Cancelled", "Preparing", "Ready", "Closed"],
                                                               dropdown_font=("TT Commmons Medium", 15),
                                                               dropdown_hover_color="#cd9ede",
                                                               dropdown_text_color="black",
                                                               state="readonly",
                                                               variable=status_var))
                    order_combobox[y-1].place(relx=0.5, rely=0.5, anchor="center")
    
    #save
    def save_function():
        for i in range(len(order)):
            database.trx_sales.edit_status(order_combobox[i].get(), order[i][0])

        def clear_label():
            edited_label.configure(text="")

        edited_label = customtkinter.CTkLabel(master=orderTable,
                                            bg_color="#F8F8FF",
                                            fg_color="#D4BBDD",
                                            text="*Changes saved",
                                            font=("TT Commons Medium", 30),
                                            text_color="#5E376D")
        edited_label.place(relx=0.72, rely=0.928)
        orderTable.after(2000, clear_label)
    
    save_button = customtkinter.CTkButton(master=orderTable,
                                         corner_radius=30,
                                         width=100,
                                         text="Save edit",
                                         bg_color="#D4BBDD",
                                         font=("TT Commons Medium", 30),
                                         command=save_function)
    save_button.place(relx=0.875, rely=0.925)

    orderTable.mainloop()

def edit_item(user, item_data):
    editItem = customtkinter.CTk()
    editItem.geometry("1536 x 790")
    editItem.minsize(1536, 790)
    editItem.maxsize(1536, 790)
    editItem.title("Edit Item")
    editItem.after(0, lambda: editItem.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=editItem, image=img1, text="")
    l1.pack()

    #edit item text
    l2=customtkinter.CTkLabel(master=editItem,
                              text="Edit item",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #back button
    def back_function():
        editItem.destroy()
        seller_home(user, False)

    back_button = customtkinter.CTkButton(master=editItem,
                                               text="Back",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=back_function)
    back_button.place(relx=0.58, rely=0.02)

    #add item button
    def additem_function():
        editItem.destroy()
        add_item(user)

    additem_button = customtkinter.CTkButton(master=editItem,
                                               text="Add Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=additem_function)
    additem_button.place(relx=0.705, rely=0.02)

    #view order button
    def vieworder_function():
        editItem.destroy()
        order_table(user)

    vieworder_button = customtkinter.CTkButton(master=editItem,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.83, rely=0.02)

    #profile button
    def profile_function():
        editItem.destroy()
        seller_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=editItem,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    #frame
    frame = customtkinter.CTkFrame(master=editItem,
                                   corner_radius=0,
                                   height=630,
                                   width=1380,
                                   bg_color="#D4BBDD",
                                   fg_color="white")
    frame.place(relx=0.05, rely=0.15)

    #item
    eachitem_img = customtkinter.CTkFrame(master=frame,
                                            corner_radius=0,
                                            height=420,
                                            width=400)
    eachitem_img.place(relx=0.02, rely=0.04)

    try:
        eachitem_image = customtkinter.CTkImage(Image.open(directory+item_data[1]+".jpg", mode="r"), size=(400, 420))
    except FileNotFoundError:
        eachitem_image = customtkinter.CTkImage(Image.open(directory+"no_image2.png", mode="r"), size=(400, 420))

    image_label = customtkinter.CTkLabel(master=eachitem_img, text="", image=eachitem_image)
    image_label.pack()

    item_code = customtkinter.CTkLabel(master=frame,
                                       text="Code: "+str(item_data[1]),
                                       font=("TT Commons Medium", 75))
    item_code.place(relx=0.03, rely=0.77)

    #name
    itemname_label = customtkinter.CTkLabel(master=frame,
                                            text="Name",
                                            font=("TT Commons Medium", 70))
    itemname_label.place(relx=0.35, rely=0.05)

    itemname_entry = customtkinter.CTkEntry(master=frame,
                                            width=530,
                                            placeholder_text=item_data[2],
                                            font=("TT Commons Medium", 65))
    itemname_entry.place(relx=0.595, rely=0.05)
    
    #price
    itemprice_label = customtkinter.CTkLabel(master=frame,
                                            text="Price",
                                            font=("TT Commons Medium", 70))
    itemprice_label.place(relx=0.35, rely=0.22)

    itemprice_entry = customtkinter.CTkEntry(master=frame,
                                            width=530,
                                            placeholder_text=item_data[4],
                                            font=("TT Commons Medium", 65))
    itemprice_entry.place(relx=0.595, rely=0.22)

    #category
    itemcategory_label = customtkinter.CTkLabel(master=frame,
                                            text="Category",
                                            font=("TT Commons Medium", 70))
    itemcategory_label.place(relx=0.35, rely=0.4)

    itemcategory_var = customtkinter.StringVar(value=item_data[3])

    itemcategory_combobox = customtkinter.CTkComboBox(master=frame,
                                                height=100,
                                                width=530,
                                                font=("TT Commons Medium", 65),
                                                bg_color="white",
                                                dropdown_font=("TT Commons Medium", 65),
                                                dropdown_fg_color="#F8F8FF",
                                                dropdown_hover_color="#cd9ede",
                                                border_width=2,
                                                border_color="#000000",
                                                button_color="#cd9ede",
                                                button_hover_color="#b382c4",
                                                values=["Anniversary", "Birthday", "Condolence", "Grand Opening", "Romantic"],
                                                state="readonly",
                                                variable = itemcategory_var)
    itemcategory_combobox.place(relx=0.595, rely=0.39)

    #stock
    itemstock_label = customtkinter.CTkLabel(master=frame,
                                            text="Stock",
                                            font=("TT Commons Medium", 70))
    itemstock_label.place(relx=0.35, rely=0.58)

    itemstock_var = customtkinter.StringVar(value=item_data[5])

    itemstock_combobox = customtkinter.CTkComboBox(master=frame,
                                                height=100,
                                                width=530,
                                                font=("TT Commons Medium", 65),
                                                bg_color="white",
                                                dropdown_font=("TT Commons Medium", 65),
                                                dropdown_fg_color="#F8F8FF",
                                                dropdown_hover_color="#cd9ede",
                                                border_width=2,
                                                border_color="#000000",
                                                button_color="#cd9ede",
                                                button_hover_color="#b382c4",
                                                values=["Available", "Not Available"],
                                                state="readonly",
                                                variable = itemstock_var)
    itemstock_combobox.place(relx=0.595, rely=0.58)

    #delete
    def delete_function():
        txt_reader.removeitem_txt("Products.txt", item_data[1])
        database.mst_item.remove_item(item_data[1])
        editItem.destroy()
        seller_home(user, True)

    delete_button = customtkinter.CTkButton(master=frame,
                                            corner_radius=30,
                                            width=200,
                                            text="Delete",
                                            fg_color="#ff3131",
                                            hover_color="#de1b1b",
                                            font=("TT Commons Medium", 60),
                                            command = delete_function)
    delete_button.place(relx=0.62, rely=0.83)

    #save
    def save_function():
        priceerror_label = customtkinter.CTkLabel(master=frame,
                                                      text="*Please input positive number for item's price",
                                                      font=("TT Commons Medium", 30),
                                                      text_color="red")
        
        err = False
        item = database.mst_item(item_data[1], "", "", "", "", "bloom")
        item.item_name = itemname_entry.get()
        item.price = itemprice_entry.get()
        item.category = itemcategory_combobox.get()
        item.stock = itemstock_combobox.get()
        if item.item_name == "":
            item.item_name = item_data[2]
        if itemprice_entry.get() == "":
            item.price = item_data[4]
        else:
            try:
                if float(itemprice_entry.get()) < 0:
                    priceerror_label.place(relx=0.55, rely=0.755)
                    err = True
                else:
                    err = False
            except ValueError:
                priceerror_label.place(relx=0.55, rely=0.755)
                err = True
        if itemcategory_combobox.get() == None:
            item.category = item_data[3]
        if itemstock_combobox.get() == None:
            item.stock = item_data[5]
        if err == False:
            txt_reader.edititem_txt("Products.txt", item)
            database.mst_item.change_item_info(item)
            editItem.destroy()
            seller_home(user, True)

    save_button = customtkinter.CTkButton(master=frame,
                                         corner_radius=30,
                                         width=150,
                                         text = "Save edit",
                                         font=("TT Commons Medium", 60),
                                         command = save_function)
    save_button.place(relx=0.78, rely=0.83)

    editItem.mainloop()

def edit_addons(user):
    editAddons = customtkinter.CTk()
    editAddons.geometry("1536 x 790")
    editAddons.minsize(1536, 790)
    editAddons.maxsize(1536, 790)
    editAddons.title("Edit Add-ons")
    editAddons.after(0, lambda: editAddons.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=editAddons, image=img1, text="")
    l1.pack()

    #edit item text
    l2=customtkinter.CTkLabel(master=editAddons,
                              text="Edit Add-ons",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #back button
    def back_function():
        editAddons.destroy()
        seller_home(user, False)

    back_button = customtkinter.CTkButton(master=editAddons,
                                               text="Back",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=back_function)
    back_button.place(relx=0.58, rely=0.02)

    #add item button
    def additem_function():
        editAddons.destroy()
        add_item(user)

    additem_button = customtkinter.CTkButton(master=editAddons,
                                               text="Add Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=additem_function)
    additem_button.place(relx=0.705, rely=0.02)

    #view order button
    def vieworder_function():
        editAddons.destroy()
        order_table(user)

    vieworder_button = customtkinter.CTkButton(master=editAddons,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.83, rely=0.02)

    #profile button
    def profile_function():
        editAddons.destroy()
        seller_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=editAddons,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    def show_table():
        #table
        table_frame = customtkinter.CTkScrollableFrame(master=editAddons,
                                                        corner_radius=0,
                                                        height=570,
                                                        width=1430,
                                                        bg_color="#D4BBDD",
                                                        fg_color="white")
        table_frame.place(relx=0.03, rely=0.15)

        addons = database.mst_item.return_addon()

        name_entry = []
        price_entry = []
        delete_button = []

        for y in range(len(addons)+1):
            for x in range(4):
                if y == 0:
                    header_frame = customtkinter.CTkFrame(master=table_frame,
                                                        corner_radius=0,
                                                        height=80,
                                                        width=370,
                                                        fg_color="#5E376D")
                    header_frame.grid(row=0, column=x, padx=3, pady=3)
                    header_label = customtkinter.CTkLabel(master=header_frame,
                                                        corner_radius=0,
                                                        fg_color="#5E376D",
                                                        font=("TT Commmons Medium", 50),
                                                        text_color="white")
                    header_label.place(relx=0.5, rely=0.5, anchor="center")
                    if x == 0:
                        header_label.configure(text="Add-on Code")
                    if x == 1:
                        header_frame.configure(width=680)
                        header_label.configure(text="Name")
                    if x == 2:
                        header_frame.configure(width=280)
                        header_label.configure(text="Price")
                    if x == 3:
                        header_frame.configure(width=77, fg_color="white")
                        header_label.place_forget()
                else:
                    addons_frame = customtkinter.CTkFrame(master=table_frame,
                                                        corner_radius=0,
                                                        height=80,
                                                        width=370,
                                                        fg_color="#f9f9fa")
                    addons_frame.grid(row=y, column=x, padx=3, pady=3)
                    if x == 0:
                        addons_label = customtkinter.CTkLabel(master=addons_frame,
                                                        corner_radius=0,
                                                        fg_color="#f9f9fa",
                                                        text=addons[y-1][1],
                                                        font=("TT Commmons Medium", 50),
                                                        text_color="black")
                        addons_label.place(relx=0.5, rely=0.5, anchor="center")
                    if x == 1:
                        addons_frame.configure(width=680)
                        name_entry.append(customtkinter.CTkEntry(master=addons_frame,
                                                                height=80,
                                                                width=680,
                                                                corner_radius=0,
                                                                fg_color="#f9f9fa",
                                                                placeholder_text=addons[y-1][2],
                                                                font=("TT Commmons Medium", 50),
                                                                text_color="black"))
                        name_entry[y-1].place(relx=0.5, rely=0.5, anchor="center")
                    if x == 2:
                        addons_frame.configure(width=280)
                        price_entry.append(customtkinter.CTkEntry(master=addons_frame,
                                                                height=80,
                                                                width=280,
                                                                corner_radius=0,
                                                                fg_color="#f9f9fa",
                                                                placeholder_text=addons[y-1][4],
                                                                font=("TT Commmons Medium", 50),
                                                                text_color="black"))
                        price_entry[y-1].place(relx=0.5, rely=0.5, anchor="center")
                    if x == 3:
                        def delete_function(i):
                            txt_reader.removeaddon_txt("Addons.txt", addons[i][1])
                            database.mst_item.remove_item(addons[i][1])
                            table_frame.destroy()
                            save_button.destroy()
                            show_table()

                        addons_frame.configure(width=77)
                        delete_button.append(customtkinter.CTkButton(master=addons_frame,
                                                                    corner_radius=0,
                                                                    height=80,
                                                                    width=77,
                                                                    text="X",
                                                                    font=("TT Commmons Medium", 50),
                                                                    text_color="white",
                                                                    fg_color="#ff3131",
                                                                    hover_color="#de1b1b",
                                                                    command=lambda i=y-1:delete_function(i)))
                        delete_button[y-1].place(relx=0.5, rely=0.5, anchor="center")

        #save
        def save_function():
            priceerror_label = customtkinter.CTkLabel(master=editAddons,
                                                            text="*Please input positive number for item's price",
                                                            font=("TT Commons Medium", 30),
                                                            bg_color="#D4BBDD",
                                                            fg_color="#D4BBDD",
                                                            text_color="red")
            
            err = False
            for i in range(len(addons)):
                new_addons = database.mst_item(addons[i][1], name_entry[i].get(), addons[i][3], 0, addons[i][5], addons[i][6])
                if name_entry[i].get() == "":
                    new_addons.item_name = addons[i][2]
                if price_entry[i].get() == "":
                    new_addons.price = addons[i][4]

                else:
                    try:
                        if float(price_entry[i].get()) < 0:
                            priceerror_label.place(relx=0.44, rely=0.91)
                            err = True
                            break
                        else:
                            new_addons.price = price_entry[i].get()
                    except ValueError:
                        priceerror_label.place(relx=0.44, rely=0.91)
                        err = True
                        break
                
                if err == False:
                    txt_reader.editaddon_txt("Addons.txt", new_addons)
                    database.mst_item.change_item_info(new_addons)

            if err == False:
                editAddons.destroy()
                seller_home(user, True)

        save_button = customtkinter.CTkButton(master=editAddons,
                                            corner_radius=30,
                                            width=100,
                                            text="Save edit",
                                            bg_color="#D4BBDD",
                                            font=("TT Commons Medium", 50),
                                            command=save_function)
        save_button.place(relx=0.83, rely=0.895)

    show_table()

    editAddons.mainloop()

def add_item(user):
    addItem = customtkinter.CTk()
    addItem.geometry("1536 x 790")
    addItem.minsize(1536, 790)
    addItem.maxsize(1536, 790)
    addItem.title("Add Item")
    addItem.after(0, lambda: addItem.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=addItem, image=img1, text="")
    l1.pack()

    #Add item text
    l2=customtkinter.CTkLabel(master=addItem,
                              text="Add Item",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #view order button
    def vieworder_function():
        addItem.destroy()
        order_table(user)

    vieworder_button = customtkinter.CTkButton(master=addItem,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.83, rely=0.02)

    #edit item button
    def edititem_function():
        addItem.destroy()
        seller_home(user, False)

    edititem_button = customtkinter.CTkButton(master=addItem,
                                               text="Edit Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=edititem_function)
    edititem_button.place(relx=0.705, rely=0.02)

    #txt file
    def txt_function():
        addItem.destroy()
        txt_add(user)

    txt_button = customtkinter.CTkButton(master=addItem,
                                         width=180,
                                         bg_color="#F8F8FF",
                                         fg_color="#866492",
                                         hover_color="#674b70",
                                         text="Txt File",
                                         font=("TT Commons Medium", 30),
                                         command = txt_function)
    txt_button.place(relx=0.58, rely=0.02)

    #profile button
    def profile_function():
        addItem.destroy()
        seller_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=addItem,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    #frame
    frame = customtkinter.CTkFrame(master=addItem,
                                   corner_radius=0,
                                   height=630,
                                   width=1380,
                                   bg_color="#D4BBDD",
                                   fg_color="white")
    frame.place(relx=0.05, rely=0.15)

    #image
    item_img = customtkinter.CTkFrame(master=frame,
                                        corner_radius=0,
                                        height=420,
                                        width=400)
    item_img.place(relx=0.02, rely=0.04)

    def checkimg_function():
        try:
            eachitem_image = customtkinter.CTkImage(Image.open(directory+itemcode_entry.get()+".jpg", mode="r"), size=(400, 420))
            if hasattr(checkimg_function, 'image_label'):
                checkimg_function.image_label.configure(image=eachitem_image)
            else:
                checkimg_function.image_label = customtkinter.CTkLabel(master=item_img, text="", image=eachitem_image)
                checkimg_function.image_label.pack()
        except FileNotFoundError:
            def clear_label():
                file_error.configure(text="")

            file_error = customtkinter.CTkLabel(master=frame,
                                                bg_color="white",
                                                text="Error, make sure your image name is same with item code and using jpg extension.",
                                                font=("TT Commons Medium", 25),
                                                wraplength=450,
                                                justify="left",
                                                text_color="red")
            file_error.place(relx=0.16, rely=0.92, anchor="center")
            addItem.after(2000, clear_label)

    checkimg_button = customtkinter.CTkButton(master=frame,
                                       text="Check Image",
                                       font=("TT Commons Medium", 50),
                                       command=checkimg_function)
    checkimg_button.place(relx=0.162, rely=0.8, anchor="center")

    #item code
    itemcode_label = customtkinter.CTkLabel(master=frame,
                                        text="Item code",
                                        font=("TT Commons Medium", 50))
    itemcode_label.place(relx=0.33, rely=0.04)

    itemcode_entry = customtkinter.CTkEntry(master=frame,
                                        width=540,
                                        font=("TT Commons Medium", 50))
    itemcode_entry.place(relx=0.585, rely=0.04)

    #name
    name_label = customtkinter.CTkLabel(master=frame,
                                        text="Item name",
                                        font=("TT Commons Medium", 50))
    name_label.place(relx=0.33, rely=0.17)

    name_entry = customtkinter.CTkEntry(master=frame,
                                        width=540,
                                        font=("TT Commons Medium", 50))
    name_entry.place(relx=0.585, rely=0.17)
    
    #price
    price_label = customtkinter.CTkLabel(master=frame,
                                        text="Price",
                                        font=("TT Commons Medium", 50))
    price_label.place(relx=0.33, rely=0.30)

    price_entry = customtkinter.CTkEntry(master=frame,
                                           width=540,
                                           border_color="#949ca4",
                                           border_width=2,
                                           font=("TT Commons Medium", 50))
    price_entry.place(relx=0.585, rely=0.30)

    #bloom or addon
    def bloomoraddon_function(choice):
        if choice == "bloom":
            category_label.place(relx=0.33, rely=0.69)
            category_combobox.place(relx=0.585, rely=0.69)
            stock_label2.place_forget()
            stock_combobox.place(relx=0.585, rely=0.56)

        else:
            category_combobox.set("-")
            category_label.place_forget()
            category_combobox.place_forget()
            stock_combobox.place_forget()
            stock_label2.place(relx=0.585, rely=0.56)
    
    bloomoraddon_label = customtkinter.CTkLabel(master=frame,
                                                    text="Type",
                                                    font=("TT Commons Medium", 50))
    bloomoraddon_label.place(relx=0.33, rely=0.43)

    bloomoraddon_var = customtkinter.StringVar(value="add-on")
    bloomoraddon_combobox = customtkinter.CTkComboBox(master=frame,
                                                            height=68,
                                                            width=540,
                                                            font=("TT Commons Medium", 50),
                                                            border_color="#949ca4",
                                                            border_width=2,
                                                            bg_color="white",
                                                            fg_color="white",
                                                            dropdown_font=("TT Commons Medium", 50),
                                                            dropdown_fg_color="white",
                                                            dropdown_hover_color="#cd9ede",
                                                            button_color="#cd9ede",
                                                            button_hover_color="#cd9ede",
                                                            values=["add-on", "bloom"],
                                                            variable=bloomoraddon_var,
                                                            state="readonly",
                                                            command=bloomoraddon_function)
    bloomoraddon_combobox.place(relx=0.585, rely=0.43)

    #category
    category_var = customtkinter.StringVar(value="-")

    category_label = customtkinter.CTkLabel(master=frame,
                                                text="Category",
                                                font=("TT Commons Medium", 50))
        
    category_combobox = customtkinter.CTkComboBox(master=frame,
                                                    height=68,
                                                    width=540,
                                                    font=("TT Commons Medium", 50),
                                                    border_color="#949ca4",
                                                    border_width=2,
                                                    bg_color="white",
                                                    fg_color="white",
                                                    dropdown_font=("TT Commons Medium", 50),
                                                    dropdown_fg_color="white",
                                                    dropdown_hover_color="#cd9ede",
                                                    button_color="#cd9ede",
                                                    button_hover_color="#cd9ede",
                                                    values=["Anniversary", "Birthday", "Condolence", "Grand Opening", "Romantic"],
                                                    state="readonly",
                                                    variable=category_var)

    #stock
    stock_label = customtkinter.CTkLabel(master=frame,
                                                text="Stock",
                                                font=("TT Commons Medium", 50))
    stock_label.place(relx=0.33, rely=0.56)

    stock_label2 = customtkinter.CTkLabel(master=frame,
                                                text="Available",
                                                font=("TT Commons Medium", 50))
    stock_label2.place(relx=0.585, rely=0.56)

    stock_var = customtkinter.StringVar(value="Available")

    stock_combobox = customtkinter.CTkComboBox(master=frame,
                                            height=68,
                                            width=540,
                                            font=("TT Commons Medium", 50),
                                            border_color="#949ca4",
                                            border_width=2,
                                            bg_color="white",
                                            fg_color="white",
                                            dropdown_font=("TT Commons Medium", 50),
                                            dropdown_fg_color="white",
                                            dropdown_hover_color="#cd9ede",
                                            button_color="#cd9ede",
                                            button_hover_color="#cd9ede",
                                            state="readonly",
                                            values=["Available", "Not Available"],
                                            variable=stock_var)
    
    #error label
    error_label = customtkinter.CTkLabel(master = frame,
                                        text="",
                                        text_color="red",
                                        font=("TT Commons Medium", 35),
                                        bg_color="#FFFFFF")
    error_label.place(relx=0.33, rely=0.86)

    #save
    def save_function():
        err = False
        item = database.mst_item("", "", "", "", "", "")
        item.item_code = itemcode_entry.get()
        item.item_name = name_entry.get()
        item.price = price_entry.get()
        item.bloom_or_addon = bloomoraddon_combobox.get()

        if item.bloom_or_addon == "bloom":
            item.category = category_combobox.get()
            item.stock = stock_combobox.get()
        else:
            item.category = "-"
            item.stock = "Available"

        if database.mst_item.check_itemcode(item.item_code):
            error_label.configure(text="*Item code has been used")
            err = True

        elif item.item_code == "" or item.item_name == "" or item.price == "" or item.category == "" or item.stock == "" or (item.bloom_or_addon == "bloom" and item.category == "-"):
            error_label.configure(text="*Data is not complete")
            err = True

        else:
            try:
                if float(price_entry.get()) < 0:
                    error_label.configure(text="*Please input positive number for item's price")
                    err = True
            except ValueError:
                    error_label.configure(text="*Please input positive number for item's price")
                    err = True

        if err == False:
            if item.bloom_or_addon == "bloom":
                txt_reader.additem_txt("Products.txt", item)
            else:
                txt_reader.addaddon_txt("Addons.txt", item)
            database.mst_item.add_item(item)
            addItem.destroy()
            seller_home(user, True)

    save_button = customtkinter.CTkButton(master=frame,
                                         corner_radius=30,
                                         width=200,
                                         text="Save",
                                         font=("TT Commons Medium", 50),
                                         command = save_function)
    save_button.place(relx=0.831, rely=0.845)

    addItem.mainloop()

def txt_add(user):
    txtAdd = customtkinter.CTk()
    txtAdd.geometry("1536 x 790")
    txtAdd.minsize(1536, 790)
    txtAdd.maxsize(1536, 790)
    txtAdd.title("Add Item")
    txtAdd.after(0, lambda: txtAdd.wm_state('zoomed'))

    #background
    img1=customtkinter.CTkImage(Image.open(directory+"plain_background.png", mode="r"), size=(1536, 790))
    l1=customtkinter.CTkLabel(master=txtAdd, image=img1, text="")
    l1.pack()

    #Add item text
    l2=customtkinter.CTkLabel(master=txtAdd,
                              text="Add Item",
                              font=("TT Commons Medium", 55),
                              bg_color="#F8F8FF")
    l2.place(relx=0.015, rely=0)

    #view order button
    def vieworder_function():
        txtAdd.destroy()
        order_table(user)

    vieworder_button = customtkinter.CTkButton(master=txtAdd,
                                               text="View Order",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=vieworder_function)
    vieworder_button.place(relx=0.83, rely=0.02)

    #edit item button
    def edititem_function():
        txtAdd.destroy()
        seller_home(user, False)

    edititem_button = customtkinter.CTkButton(master=txtAdd,
                                               text="Edit Item",
                                               width=180,
                                               font=("TT Commons Medium", 30),
                                               border_color="#000000",
                                               bg_color="#F8F8FF",
                                               fg_color="#cd9ede",
                                               hover_color="#b382c4",
                                               command=edititem_function)
    edititem_button.place(relx=0.705, rely=0.02)

    #manual
    def manual_function():
        txtAdd.destroy()
        add_item(user)

    manual_button = customtkinter.CTkButton(master=txtAdd,
                                         width=180,
                                         bg_color="#F8F8FF",
                                         fg_color="#866492",
                                         hover_color="#674b70",
                                         text="Manually",
                                         font=("TT Commons Medium", 30),
                                         command = manual_function)
    manual_button.place(relx=0.58, rely=0.02)

    #profile button
    def profile_function():
        txtAdd.destroy()
        seller_profile(user)

    profile_image = customtkinter.CTkImage(Image.open(directory+"profile_button.png", mode="r"), size=(50,50))
    profile_button = customtkinter.CTkButton(master=txtAdd,
                                             width=30,
                                             text="",
                                             bg_color="#F8F8FF",
                                             fg_color="#F8F8FF",
                                             hover_color="#F8F8FF",
                                             image=profile_image,
                                             command=profile_function)
    profile_button.place(relx=0.95, rely=0.01)

    
    #format
    format_label = customtkinter.CTkLabel(master=txtAdd,
                                          bg_color="#D4BBDD",
                                          text="Format: item code, item name, price, availability\n*Please name your image as {item code}.jpg and put it in 'Image' folder",
                                          font=("TT Commons Medium", 40))
    format_label.place(relx=0.5, rely=0.56, anchor="center")

    #name
    name_label = customtkinter.CTkLabel(master=txtAdd,
                                        text="File name",
                                        bg_color="#D4BBDD",
                                        font=("TT Commons Medium", 50))
    name_label.place(relx=0.24, rely=0.25)

    name_entry = customtkinter.CTkEntry(master=txtAdd,
                                        width=540,
                                        bg_color="#D4BBDD",
                                        placeholder_text="Addons.txt",
                                        font=("TT Commons Medium", 50))
    name_entry.place(relx=0.41, rely=0.25)
    
    #bloom or addon
    def bloomoraddon_function(choice):
        if choice == "bloom":
            name_entry.configure(placeholder_text="Products.txt")
            format_label.configure(text="Format: item code, item name, category, price, availability\n*Please name your image as {item code}.jpg and put it in 'Image' folder")
        else:
            name_entry.configure(placeholder_text="Addons.txt")
            format_label.configure(text="Format: item code, item name, price, availability\n*Please name your image as {item code}.jpg and put it in 'Image' folder")
    
    bloomoraddon_label = customtkinter.CTkLabel(master=txtAdd,
                                                bg_color="#D4BBDD",
                                                text="Type",
                                                font=("TT Commons Medium", 50))
    bloomoraddon_label.place(relx=0.24, rely=0.38)

    bloomoraddon_var = customtkinter.StringVar(value="add-on")

    bloomoraddon_combobox = customtkinter.CTkComboBox(master=txtAdd,
                                                            height=68,
                                                            width=540,
                                                            font=("TT Commons Medium", 50),
                                                            border_color="#949ca4",
                                                            border_width=2,
                                                            bg_color="#D4BBDD",
                                                            fg_color="white",
                                                            dropdown_font=("TT Commons Medium", 50),
                                                            dropdown_fg_color="white",
                                                            dropdown_hover_color="#cd9ede",
                                                            button_color="#866492",
                                                            button_hover_color="#674b70",
                                                            values=["add-on", "bloom"],
                                                            state="readonly",
                                                            variable = bloomoraddon_var,
                                                            command=bloomoraddon_function)
    bloomoraddon_combobox.place(relx=0.41, rely=0.38)

    #item code error
    codeerror_label = customtkinter.CTkLabel(master=txtAdd,
                                             bg_color="#D4BBDD",
                                             text="",
                                             text_color="red",
                                             font=("TT Commons Medium", 40))
    codeerror_label.place(relx=0.5, rely=0.86, anchor="center")

    #add
    def add_function():
        code_error = False

        file = name_entry.get()
        bloom_or_addon = bloomoraddon_combobox.get()

        if bloom_or_addon == "bloom":
            if file == "":
                file = "Products.txt"

            try:
                item_list = txt_reader.readitem_txt(file)

                for i in range(len(item_list)):
                    code_error = database.mst_item.check_itemcode(item_list[i][0])
                    if code_error == True:
                        break

                if code_error:
                    codeerror_label.configure(text="*Error, the code inside txt file has been used in the item in database.",
                                              text_color="red")
                else:
                    codeerror_label.configure(text="*Successfully added.",
                                            text_color="green")
                    for i in range(len(item_list)):
                        item = database.mst_item("", "", "", "", "", "")
                        item.item_code = item_list[i][0]
                        item.item_name = item_list[i][1]
                        item.category = item_list[i][2]
                        item.price = item_list[i][3]
                        item.stock = item_list[i][4]
                        item.bloom_or_addon = "bloom"
                        database.mst_item.add_item(item)

            except FileNotFoundError:
                def clear_label():
                    file_error.configure(text="")

                file_error = customtkinter.CTkLabel(master=txtAdd,
                                                    bg_color="#D4BBDD",
                                                    text="*Error, no file named "+file+" is found.",
                                                    font=("TT Commons Medium", 40),
                                                    text_color="red")
                file_error.place(relx=0.41, rely=0.17)
                txtAdd.after(2000, clear_label)

        else:
            if file == "":
                file = "Addons.txt"
            
            try:
                item_list = txt_reader.readitem_txt(file)

                for i in range(len(item_list)):
                    code_error = database.mst_item.check_itemcode(item_list[i][0])
                    if code_error == True:
                        break

                if code_error:
                    codeerror_label.configure(text="*Error, the code inside txt file has been used in the item in database.",
                                              text_color="red")
                else:
                    codeerror_label.configure(text="*Successfully added.",
                                            text_color="green")
                    for i in range(len(item_list)):
                        item = database.mst_item("", "", "", "", "", "")
                        item.item_code = item_list[i][0]
                        item.item_name = item_list[i][1]
                        item.category = "-"
                        item.price = item_list[i][2]
                        item.stock = item_list[i][3]
                        item.bloom_or_addon = "add-on"
                        database.mst_item.add_item(item)

            except FileNotFoundError:
                def clear_label():
                    file_error.configure(text="")

                file_error = customtkinter.CTkLabel(master=txtAdd,
                                                    bg_color="#D4BBDD",
                                                    text="*Error, no file named "+file+" is found.",
                                                    font=("TT Commons Medium", 40),
                                                    text_color="red")
                file_error.place(relx=0.41, rely=0.17)
                txtAdd.after(2000, clear_label)

    add_button = customtkinter.CTkButton(master=txtAdd,
                                         corner_radius=30,
                                         width=250,
                                         bg_color="#D4BBDD",
                                         text="Add",
                                         font=("TT Commons Medium", 65),
                                         command = add_function)
    add_button.place(relx=0.5, rely=0.75, anchor="center")

    txtAdd.mainloop()

login_page()