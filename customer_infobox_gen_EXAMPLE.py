# CLASS WILL CREATE CUSTOMER INFO BOX TO SHOW AS EXAMPLE ON THE HELP PAGE
import tkinter as tk
from tkinter import ttk

class CustomerInfoBox(tk.Frame):
    def __init__(self, page3):
        ### General frame for the entry of customer information
        main_frame = tk.Frame(page3, bg='gray15')
        main_frame.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)
        
        ### Drop down list for performance date
        perfDate_Frame = tk.Frame(main_frame, bg='gray15')
        perfDate_Frame.pack(side=tk.LEFT, anchor=tk.N)

        perfDate_Label = tk.Label(perfDate_Frame, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        perfDate_Label.config(bd=0, text='Performance Date:', font='System 12', fg='yellow')
        perfDate_Label.pack(fill=tk.X, anchor=tk.N, padx=10, pady=10)
        
        self.perfDate_opt = tk.StringVar(page3)
        self.perfDate_opt.set("06/10/20")

        perfDate_Optmenu = tk.OptionMenu(perfDate_Frame, self.perfDate_opt, "06/10/20","05/10/20","04/10/20")
        perfDate_Optmenu.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)
        ###
        
        ### Drop down list for FREE seat list.
        seatList_Frame = tk.Frame(main_frame, bg='gray15')
        seatList_Frame.pack(side=tk.LEFT, anchor=tk.N)

        seatList_Label = tk.Label(seatList_Frame, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        seatList_Label.config(bd=0, text='Available Seats:', font='System 12', fg='yellow')
        seatList_Label.pack(fill=tk.X, anchor=tk.N, padx=10, pady=10)

        #Exemplar seating arrangement list.
        seatList = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20']
        
        seatList_var = tk.StringVar(page3)

        # place each seat code into seat listbox to  display the seats as a drop down list
        self.seatList_listbox = tk.Listbox(seatList_Frame, selectmode=tk.SINGLE, exportselection=False)
        for item in seatList:
            self.seatList_listbox.insert(tk.END,item)
        self.seatList_listbox.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)
        ###
        
        ### Customer infobox: where all the customer information will be entered into the system.
        cust_info_canvas_title_frame = tk.Frame(main_frame, bg='gray15')
        cust_info_canvas_title_frame.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        cust_info_canvas_title_label = tk.Label(cust_info_canvas_title_frame, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        cust_info_canvas_title_label.config(bd=0, text='Customer Information:', font='System 12', fg='yellow')
        cust_info_canvas_title_label.pack(fill=tk.X, anchor=tk.N)
        
        cust_infobox_canvas = tk.Canvas(cust_info_canvas_title_frame, width=200, height=200, relief=tk.RIDGE, bd=1, bg='gray15')
        cust_infobox_canvas.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Customer ID Entry field
        cust_infobox_id_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_id_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_id_label = tk.Label(cust_infobox_id_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_id_label.config(bd=0, text='Customer ID: ', font='System 6', fg='yellow')
        cust_infobox_id_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        self.entry_id_var_1 = tk.IntVar(page3)
        cust_infobox_id_entry = tk.Entry(cust_infobox_id_frame)
        cust_infobox_id_entry.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_id_var_1,
                                     font='System 6', fg='yellow', state=tk.DISABLED)
        cust_infobox_id_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # First Name entry field
        cust_infobox_fname_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_fname_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_fname_label = tk.Label(cust_infobox_fname_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_fname_label.config(bd=0, text='First Name: ', font='System 6', fg='yellow')
        cust_infobox_fname_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        self.fname_reg = page3.register(self.fname_validate)
        
        self.entry_fname_var_1 = tk.StringVar(page3)
        self.entry_fname_var_1.set('')
        self.cust_infobox_fname_entry = tk.Entry(cust_infobox_fname_frame)
        self.cust_infobox_fname_entry.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_fname_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(self.fname_reg, '%P'))
        self.cust_infobox_fname_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Surname entry field
        cust_infobox_surname_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_surname_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_surname_label = tk.Label(cust_infobox_surname_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_surname_label.config(bd=0, text='Surname: ', font='System 6', fg='yellow')
        cust_infobox_surname_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        self.surname_reg = page3.register(self.surname_validate)

        self.entry_surname_var_1 = tk.StringVar(page3)
        self.entry_surname_var_1.set('')
        self.cust_infobox_surname_entry = tk.Entry(cust_infobox_surname_frame)
        self.cust_infobox_surname_entry.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_surname_var_1,
                                          font='System 6', fg='yellow', validate="key", validatecommand=(self.surname_reg,"%P"))
        self.cust_infobox_surname_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Phone Number entry field
        cust_infobox_phoneNumber_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_phoneNumber_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_phoneNumber_label = tk.Label(cust_infobox_phoneNumber_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_phoneNumber_label.config(bd=0, text='Phone Number: ', font='System 6', fg='yellow')
        cust_infobox_phoneNumber_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        self.phoneN_reg = page3.register(self.phoneN_validate)

        self.entry_phoneNumber_var_1 = tk.StringVar(page3)
        self.entry_phoneNumber_var_1.set('')
        self.cust_infobox_phoneNumber = tk.Entry(cust_infobox_phoneNumber_frame)
        self.cust_infobox_phoneNumber.config(bd=1, relief=tk.GROOVE, bg='gray15',textvariable=self.entry_phoneNumber_var_1,
                                              font='System 6', fg='yellow', validate="key", validatecommand=(self.phoneN_reg,"%P"))
        self.cust_infobox_phoneNumber.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Customer Type Radiobutton field
        cust_infobox_radiobutton_1_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_radiobutton_1_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_custType_1_label = tk.Label(cust_infobox_radiobutton_1_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_custType_1_label.config(bd=0, text='Customer Type: ', font='System 6', fg='yellow')
        cust_infobox_custType_1_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        self.radio_custType_var_1 = tk.StringVar(page3)
        self.radio_custType_var_1.set('Regular')
        self.cust_infobox_custType_radio_1_1 = tk.Radiobutton(cust_infobox_radiobutton_1_frame, text='Regular', variable=self.radio_custType_var_1, value='Regular',
                                                       font='System 1', fg='yellow', relief=tk.GROOVE, bd=1, bg='gray15', selectcolor='gray15')
        self.cust_infobox_custType_radio_1_2 = tk.Radiobutton(cust_infobox_radiobutton_1_frame, text='Reduced', variable=self.radio_custType_var_1, value='Reduced',
                                                       font='System 1', fg='yellow', relief=tk.GROOVE, bd=1, bg='gray15', selectcolor='gray15')
        self.cust_infobox_custType_radio_1_3 = tk.Radiobutton(cust_infobox_radiobutton_1_frame, text='Special', variable=self.radio_custType_var_1, value='Special',
                                                       font='System 1', fg='yellow', relief=tk.GROOVE, bd=1, bg='gray15', selectcolor='gray15')
        self.cust_infobox_custType_radio_1_1.pack(side=tk.LEFT, anchor=tk.W)
        self.cust_infobox_custType_radio_1_2.pack(side=tk.LEFT, anchor=tk.W)
        self.cust_infobox_custType_radio_1_3.pack(side=tk.LEFT, anchor=tk.W)
        ###

        ### Making Dynamic CustomerID Search Field
        cust_infobox_search_custID_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_search_custID_frame.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X, expand=True)

        cust_infobox_search_custID_label = tk.Label(cust_infobox_search_custID_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_search_custID_label.config(bd=0, text='Search Specific CustomerID: ', font='System 6', fg='yellow')
        cust_infobox_search_custID_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        search_custID_reg = page3.register(self.search_custID_validate)

        self.entry_search_custID_var_1 = tk.StringVar(page3)
        self.entry_search_custID_var_1.set('')

        self.cust_infobox_search_custID_entry = tk.Entry(cust_infobox_search_custID_frame)
        self.cust_infobox_search_custID_entry.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                                     textvariable=self.entry_search_custID_var_1,
                                                     font='System 6', fg='yellow', validate="key",
                                                     validatecommand=(search_custID_reg, "%P"))
        self.cust_infobox_search_custID_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        self.cust_infobox_search_custID_entry.bind("<Return>", self.searchSpecific_Customer)

        # Seat Blocker
        # Blocks seats from being allocated by the user
        cust_infobox_seatblocker_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_seatblocker_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_seatblocker_label = tk.Label(cust_infobox_seatblocker_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_seatblocker_label.config(bd=0, text='Block Seat? ', font='System 6', fg='yellow')
        cust_infobox_seatblocker_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)
        
        self.radio_seatblocker_var_1 = tk.StringVar(page3)
        self.radio_seatblocker_var_1.set('no')

        #All available options (2) as 2 seperate clickable GUI radiobuttons.
        self.cust_infobox_seatblocker_radio_1 = tk.Radiobutton(cust_infobox_seatblocker_frame, text='Yes',
                                                         variable=self.radio_seatblocker_var_1, value='yes',
                                                         font='System 1', fg='yellow', relief=tk.GROOVE, bd=1,
                                                         bg='gray15', selectcolor='gray15', command=self.radioChange)
        self.cust_infobox_seatblocker_radio_2 = tk.Radiobutton(cust_infobox_seatblocker_frame, text='No',
                                                         variable=self.radio_seatblocker_var_1, value='no',
                                                         font='System 1', fg='yellow', relief=tk.GROOVE, bd=1,
                                                         bg='gray15', selectcolor='gray15', command=self.radioChange)

        #2 Variables to store the value which was chosen from the 2.
        self.cust_infobox_seatblocker_radio_1.pack(side=tk.LEFT, anchor=tk.W)
        self.cust_infobox_seatblocker_radio_2.pack(side=tk.LEFT, anchor=tk.W)

        ### Making Enter Information Button.
        enter_info_button_frame = tk.Frame(main_frame, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame.pack(side=tk.BOTTOM)

        enter_info_button_Label = tk.Label(enter_info_button_frame, relief=tk.GROOVE, bg='gray15')
        enter_info_button_Label.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_Label.pack(side=tk.TOP)

        enter_info_button = tk.Button(enter_info_button_frame)
        enter_info_button.config(relief=tk.RAISED, bd=5, text='    Enter Information    ', command=self.addToTreeview)
        enter_info_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)
        ###

        ### Making 'Refresh' Button
        refresh_button_frame = tk.Frame(main_frame, relief=tk.GROOVE, bd=0, bg='gray15')
        refresh_button_frame.pack(side=tk.BOTTOM)

        refresh_button_Label = tk.Label(refresh_button_frame, relief=tk.GROOVE, bg='gray15')
        refresh_button_Label.config(text='Refresh The Table:', font='System 6', fg='yellow')
        refresh_button_Label.pack(side=tk.TOP)

        refresh_button = tk.Button(refresh_button_frame)
        refresh_button.config(relief=tk.RAISED, bd=5, text='    Refresh    ', command=self.refreshTreeview)
        refresh_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)
        ###

        ### Making 'Previous'+'Next' Buttons
        changeID_button_frame = tk.Frame(main_frame, relief=tk.GROOVE, bd=0, bg='gray15')
        changeID_button_frame.pack(side=tk.BOTTOM, anchor=tk.NW)

        prev_button_Label = tk.Label(changeID_button_frame, relief=tk.GROOVE, bg='gray15')
        prev_button_Label.config(text='Change CustomerID:', font='System 6', fg='yellow')
        prev_button_Label.pack(side=tk.TOP, padx=15, pady=15)

        prev_button = tk.Button(changeID_button_frame)
        prev_button.config(relief=tk.RAISED, bd=5, text='Previous', command=self.prevCustomer)
        prev_button.pack(side=tk.LEFT, anchor=tk.NW, padx=15, pady=15)

        next_button = tk.Button(changeID_button_frame)
        next_button.config(relief=tk.RAISED, bd=5, text='  Next  ', command=self.nextCustomer)
        next_button.pack(side=tk.RIGHT, anchor=tk.NE, padx=15, pady=15)
        
        ### Making TreeView Widget to display database information that can be searched and sorted by
        treeview_frame = tk.Frame(page3, relief=tk.GROOVE, bd=0, bg='gray15')
        treeview_frame.pack(side=tk.TOP, padx=10, pady=10)

        treeview_label = tk.Label(treeview_frame, relief=tk.GROOVE, bg='gray15')
        treeview_label.config(text='Search Database:', font='System 6', fg='yellow')
        treeview_label.pack(side=tk.TOP, padx=10, pady=10)
        
        columns = ('Customer ID','Seat ID','First Name','Surname','Phone Number','Status', 'Price')
        treeview = ttk.Treeview(treeview_frame, columns=columns, show='headings')

        # Fake exemplar information to show how the information is displayed in the real system.
        self.customerID=list(range(200))
        self.seatID = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20']
        self.fname = ['John','Marco','Felipe','Victor','Kelly']
        self.surname = ['Stamos','Fernandes','Stelio','Zantor','Silva']
        self.phoneN = ['07888981342','02918541363','98765432109','01234567895','01923874563']
        self.status = ['REGULAR','REDUCED','REDUCED','SPECIAL','REGULAR']
        self.price = ['£10','£5','£5','£0','£10']
        
        treeview.column('Customer ID', width=125)
        treeview.column('Seat ID', width=125)
        treeview.column('First Name', width=125)
        treeview.column('Surname', width=125)
        treeview.column('Phone Number', width=125)
        treeview.column('Status', width=125)
        treeview.column('Price', width=125)

        for i in range(200):
            try:
                treeview.insert('', tk.END, values=(self.customerID[i],self.seatID[i],self.fname[i],
                                                    self.surname[i],self.phoneN[i],self.status[i],self.price[i]))
                treeview.pack()
                i+=1
            except IndexError:
                i+=1
                
        for col in columns:
            treeview.heading(col, text=col, command=lambda _col=col: \
                             self.treeview_sort_column(treeview, _col, False))
        ###

        # Title Header
        tips_header_frame = tk.Frame(page3, relief=tk.GROOVE, bd=1, bg='gray15')
        tips_header_frame.pack(side=tk.TOP, padx=15, pady=15, fill=tk.X)

        # Tips for entering information into the box.
        entry_tips_title = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_title.config(text='Detailed Information Links', font='System 18', fg='yellow')
        entry_tips_title.pack(side=tk.TOP,padx=15)

        cust_infobox_help_button = tk.Button(tips_header_frame)
        cust_infobox_help_button.config(text=' Customer Infobox Staff Guide ', relief=tk.RAISED, bd=5, bg='white',
                                        command=self.customerInfobox_guide)
        cust_infobox_help_button.pack(side=tk.TOP, anchor=tk.NW, pady=15, padx=15)

        cust_treeview_help_button = tk.Button(tips_header_frame)
        cust_treeview_help_button.config(text='Customer TreeView Staff Guide', relief=tk.RAISED, bd=5, bg='white',
                                        command=self.customerTreeView_guide)
        cust_treeview_help_button.pack(side=tk.TOP, anchor=tk.NW, pady=15, padx=15)

        
    def customerInfobox_guide(self):
        top = tk.Toplevel()
        top.title('Customer Infobox Staff Guide')
        top.wm_state('zoomed')
        top.option_add('*Font', 'System 12')
        top.option_add('*Label.Font', 'System 14')
        top.config(bg='gray15')

        tips_header_frame = tk.Frame(top, relief=tk.GROOVE, bd=1, bg='gray15')
        tips_header_frame.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=15, fill=tk.X)
        
        # Tips for entering information into the box.
        entry_tips_title = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_title.config(text='Using the Customer Infobox', font='System 18', fg='yellow')
        entry_tips_title.pack(side=tk.TOP,padx=15)

        entry_tips_label_0_title = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_0_title.config(text='How to book customer successfully!', font='System 16', fg='yellow')
        entry_tips_label_0_title.pack(side=tk.TOP,padx=15)
        
        entry_tips_label_0 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_0.config(text="-Select a Performance Date\n-Select a seat from the 'Available Seats' list\n-Enter the customer's information in the correct, labelled fields\n-Select a customer type based on the customer's age\n-Press the 'Enter Information' button to send the information to the database", font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_0.pack(side=tk.TOP,padx=10, pady=10)
        
        entry_tips_label_1 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_1.config(text='- Under Customer Type, the "Regular" option is for those UNDER 65, but OVER 18.\n"Reduced" is for those OVER 65 AND UNDER 18.\nLastly, "Special" is reserved for VIP, staff or special guests.', font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_1.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_2 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_2.config(text="- If you need to change a customer's seat, you can select their CustomerID and select the desired seat.", font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_2.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_3 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_3.config(text='- Under "Change CustomerID", you may select the "Previous" or "Next" options,\n which allow the staff to cycle through CustomerIDs and their relevant information.', font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_3.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_4 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_4.config(text="- Select a seat and press the 'Block Seat?' Check button to create a blocked seat.", font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_4.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_5 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_5.config(text="- The 'First Name' and 'Surname' entry fields require the first character to be a capital letter. The 'Phone Number' entry field must be 11 characters long.", font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_5.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_6 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_6.config(text='- You may use the "Search for a Specific CustomerID" entry box to find a specific customer on the database.\n Press the <Enter> button on your keyboard to search the given CustomerID', font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_6.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_7 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_7.config(text='- Please use the largest CustomerID that the program automatically gives to fill in information.\n eg. CustomerID 20 is the one show, hence fill that one in, not CustomerID 21.', font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_7.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_8 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_8.config(text='- Start Phone Numbers with 0, NOT +44', font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_8.pack(side=tk.TOP,padx=10, pady=10)

        btn_close = tk.Button(top, relief=tk.RAISED, borderwidth=5, text='   Close   ',
                           command=top.destroy)
        btn_close.pack(padx=10, pady=10, side=tk.BOTTOM)
        
    def customerTreeView_guide(self):
        top = tk.Toplevel()
        top.title('Customer TreeView Staff Guide')
        top.wm_state('zoomed')
        top.option_add('*Font', 'System 12')
        top.option_add('*Label.Font', 'System 14')
        top.config(bg='gray15')
        
        tips_header_frame = tk.Frame(top, relief=tk.GROOVE, bd=1, bg='gray15')
        tips_header_frame.pack(side=tk.TOP, padx=15, pady=15, fill=tk.X)

        # Tips for entering information into the box.
        entry_tips_title = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_title.config(text='Using the Database Table', font='System 18', fg='yellow')
        entry_tips_title.pack(side=tk.TOP,padx=15)
        
        entry_tips_label_0_title = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_0_title.config(text='How to correctly use the TreeView table!', font='System 16', fg='yellow')
        entry_tips_label_0_title.pack(side=tk.TOP,padx=15)

        entry_tips_label_0 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_0.config(text="-The TreeView table is the table on the right side of the User Interface that shows the user what it being stored in the internal database\n-The TreeView shows all information regarding the customers who have booked a seat and any seats that may be blocked.\n- Each heading should be self explanatory, though just to clarify, 6th Oct refers to the date of the performance on the 6th of October, and so on for the other performance dates.", font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_0.pack(side=tk.TOP,padx=10, pady=10)
        
        entry_tips_label_1 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_1.config(text='- Use the "Search the Database" TreeView Section to Search for Customers using the table.', font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_1.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_2 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_2.config(text='- Click the Column headers to sort alphabetically or numerically.', font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_2.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_3 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_3.config(text="- A row with the '-' values indicates a blocked seat.", font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_3.pack(side=tk.TOP,padx=10, pady=10)

        entry_tips_label_4 = tk.Label(tips_header_frame, relief=tk.FLAT, bd=1, bg='gray15')
        entry_tips_label_4.config(text="- The price column is assumed to be in GBP currency (£).", font='System 6', fg='yellow', justify=tk.CENTER)
        entry_tips_label_4.pack(side=tk.TOP,padx=10, pady=10)

        btn_close = tk.Button(top, relief=tk.RAISED, borderwidth=5, text='   Close   ',
                           command=top.destroy)
        btn_close.pack(padx=10, pady=10, side=tk.BOTTOM)
        

    #Validation methods to show staff what can and cannot be entered into the system.
    def fname_validate(self, fname_inp):
        if fname_inp.isalpha():
            return True
        elif fname_inp is "":
            return True
        else:
            return False

    def surname_validate(self, surname_inp):
        if surname_inp.isalpha():
            return True
        elif surname_inp is "":
            return True
        else:
            return False

    def phoneN_validate(self, phoneN_inp):
        if phoneN_inp.isdigit():
            phoneN_inp_lencheck = ''.join(phoneN_inp)
            if phoneN_inp_lencheck[0] != '0':
                return False
            else:
                if len(str(phoneN_inp_lencheck)) <= 11:
                    return True
                else:
                    return False
        elif phoneN_inp is "":
            return True
        elif phoneN_inp is None:
            return True
        else:
            return False

    def search_custID_validate(self, search_custID_inp):
        if search_custID_inp.isdigit():
            search_custID_inp_lencheck = ''.join(search_custID_inp)
            if len(search_custID_inp_lencheck) > 3:
                return False
            else:
                if int(search_custID_inp) > 600:
                    return False
                else:
                    return True
        elif search_custID_inp is "":
            return True
        else:
            return False

    def radioChange(self):
        if self.radio_seatblocker_var_1.get() == "yes":
            self.cust_infobox_fname_entry["state"]= tk.DISABLED
            self.cust_infobox_surname_entry["state"]= tk.DISABLED
            self.cust_infobox_phoneNumber["state"]= tk.DISABLED
            self.cust_infobox_custType_radio_1_1["state"]= tk.DISABLED
            self.cust_infobox_custType_radio_1_2["state"]= tk.DISABLED
            self.cust_infobox_custType_radio_1_3["state"]= tk.DISABLED
        else:
            self.cust_infobox_fname_entry["state"]= tk.NORMAL
            self.cust_infobox_fname_entry["validate"]="key"
            self.cust_infobox_fname_entry["validatecommand"]=(self.fname_reg, '%P')
            
            self.cust_infobox_surname_entry["state"]= tk.NORMAL
            self.cust_infobox_surname_entry["validate"]="key"
            self.cust_infobox_surname_entry["validatecommand"]=(self.surname_reg, '%P')

            self.cust_infobox_phoneNumber["state"]= tk.NORMAL
            self.cust_infobox_phoneNumber["validate"]="key"
            self.cust_infobox_phoneNumber["validatecommand"]=(self.phoneN_reg, '%P')

            self.cust_infobox_custType_radio_1_1["state"]= tk.NORMAL
            self.cust_infobox_custType_radio_1_2["state"]= tk.NORMAL
            self.cust_infobox_custType_radio_1_3["state"]= tk.NORMAL
    
    # Append all information into the treeview table to show the staff how it looks on the real page.
    def addToTreeview(self):
        perfDate = self.perfDate_opt.get()
        seat_selected = self.seatList_listbox.get(self.seatList_listbox.curselection())
        custID_1 = self.entry_id_var_1.get()
        fname_1 = self.entry_fname_var_1.get()
        surname_1 = self.entry_surname_var_1.get()
        phoneN_1 = self.entry_phoneNumber_var_1.get()
        custType_1 = self.radio_custType_var_1.get()

        if custType_1 == 'REGULAR':
            price=10
            self.price.append(price)
        elif custType_1 == 'REDUCED':
            price=5
            self.price.append(price)
        elif custType_1 == 'SPECIAL':
            price=0
            self.price.append(price)

        self.seatID.append(seat_selected)
        self.fname.append(fname_1)
        self.surname.append(surname_1)
        self.phoneN.append(phoneN_1)
        self.status.append(custType_1)

    # Allow staff to become familiar with the sorting methods of the treeview table.
    def treeview_sort_column(self,tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            l.sort(key=lambda t: int(t[0]),reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: \
                   self.treeview_sort_column(tv, col, not reverse))

    ### No real functionality required as what it shows them as a button or text prompt is already enough to convey an idea of what it might do.
    ### Search for a specific customer through CustomerID
    def searchSpecific_Customer(self, *args):
        pass

    ###

    ### Load in Next CustomerID and relevant information along with it.
    def nextCustomer(self):
        pass

    ###

    ### Load in Previous CustomerID and relevant information along with it.
    def prevCustomer(self):
        pass

    ### Refresh Treeview table upon button press.
    def refreshTreeview(self):
        pass

    ###


