import tkinter as tk
from tkinter import ttk
import customer_infobox_gen_EXAMPLE
import sqlite3
from tkinter import messagebox
from tkinter import simpledialog
import string

### Connect to sqlite3 database.
conn = sqlite3.connect('Booking.db')
cursor = conn.cursor()

class Notebook:
    def __init__(self, master):
        #configuration of main window
        master.wm_state('zoomed')
        master.configure(bg='gray15')
        master.title('Auditorium Booking System v1.15.2')
        master.option_add('*Font', 'System 12')
        master.option_add('*Label.Font', 'System 14')

        main_notebook = ttk.Notebook(master)
        main_notebook.pack(expand=True, fill=tk.BOTH)

        # Creating Booking Page
        page1 = tk.Frame(main_notebook)
        main_notebook.add(page1, text="Booking")
        
        frame1_page1 = tk.Frame(page1, relief=tk.FLAT, borderwidth=1, bg='gray15')
        frame1_page1.pack(side=tk.TOP, fill=tk.BOTH)

        logo_header = tk.Label(frame1_page1, relief=tk.GROOVE, borderwidth=1, bg='ghost white')
        logo_header.config(bd=0, text='Auditorium Booking System v1.15.2', font='System 12')
        logo_header.pack(fill=tk.X, anchor=tk.N)

        custInfoTitle = tk.Label(frame1_page1, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        custInfoTitle.config(bd=0, text='Customer Booking', font='System 20')
        custInfoTitle.pack(fill=tk.X, expand=True, side=tk.TOP, anchor=tk.N, pady=20)

        ### General frame for the entry of customer information
        main_frame = tk.Frame(page1, bg='gray15')
        main_frame.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        ### Drop down list for performance date
        perfDate_Frame = tk.Frame(main_frame, bg='gray15')
        perfDate_Frame.pack(side=tk.LEFT, anchor=tk.N)

        perfDate_Label = tk.Label(perfDate_Frame, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        perfDate_Label.config(bd=0, text='Performance Date:', font='System 12', fg='yellow')
        perfDate_Label.pack(fill=tk.X, anchor=tk.N, padx=10, pady=10)

        self.perfDate_opt = tk.StringVar(master)
        self.perfDate_opt.set("06/10/20")
        #Will track the state of the perfDate variable in real-time.
        self.perfDate_opt.trace("w", self.change)

        perfDate_Optmenu = tk.OptionMenu(perfDate_Frame, self.perfDate_opt, "06/10/20", "05/10/20", "04/10/20")
        perfDate_Optmenu.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)
        ###

        ### Drop down listbox that shows all FREE seats.
        seatList_Frame = tk.Frame(main_frame, bg='gray15')
        seatList_Frame.pack(side=tk.LEFT, anchor=tk.N)

        seatList_Label = tk.Label(seatList_Frame, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        seatList_Label.config(bd=0, text='Available Seats:', font='System 12', fg='yellow')
        seatList_Label.pack(fill=tk.X, anchor=tk.N, padx=10, pady=10)

        self.seatList_var = tk.StringVar(master)
        self.seatList_listbox = tk.Listbox(seatList_Frame, selectmode=tk.SINGLE, exportselection=False)
        #Updates the drop down list dependant on if the seat has just been taken.
        self.listboxUpdate()
        ###

        ### Customer Infobox title
        cust_info_canvas_title_frame = tk.Frame(main_frame, bg='gray15')
        cust_info_canvas_title_frame.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        cust_info_canvas_title_label = tk.Label(cust_info_canvas_title_frame, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        cust_info_canvas_title_label.config(bd=0, text='Customer Information:', font='System 12', fg='yellow')
        cust_info_canvas_title_label.pack(fill=tk.X, anchor=tk.N)

        # Customer Canvas box showing all entry boxes for customer information
        cust_infobox_canvas = tk.Canvas(cust_info_canvas_title_frame, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        cust_infobox_canvas.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Customer ID Entry field
        cust_infobox_id_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_id_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_id_label = tk.Label(cust_infobox_id_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_id_label.config(bd=0, text='Customer ID: ', font='System 6', fg='yellow')
        cust_infobox_id_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        #Fetch first customer ID where a customer has not yet been allocated a seat or ticket at all.
        cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE fname=''")
        sixth_seatlist_fetch = cursor.fetchall()
        custID_list = [x[0] for x in sixth_seatlist_fetch]
        custID_latest = custID_list[0]

        #Stores whatever is put into the entry box as a variable here.
        self.entry_id_var_1 = tk.IntVar(page1)
        self.entry_id_var_1.set(custID_latest)

        #Entry box itself
        self.cust_infobox_id_entry = tk.Entry(cust_infobox_id_frame)
        self.cust_infobox_id_entry.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_id_var_1,
                                     font='System 6', fg='yellow', state=tk.DISABLED)
        self.cust_infobox_id_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # First Name entry field
        cust_infobox_fname_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_fname_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_fname_label = tk.Label(cust_infobox_fname_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_fname_label.config(bd=0, text='First Name: ', font='System 6', fg='yellow')
        cust_infobox_fname_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        #Validation method
        self.fname_reg = master.register(self.fname_validate)

        self.entry_fname_var_1 = tk.StringVar(page1)
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

        self.surname_reg = master.register(self.surname_validate)

        self.entry_surname_var_1 = tk.StringVar(page1)
        self.entry_surname_var_1.set('')
        self.cust_infobox_surname_entry = tk.Entry(cust_infobox_surname_frame)
        self.cust_infobox_surname_entry.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_surname_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(self.surname_reg, "%P"))
        self.cust_infobox_surname_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Phone Number entry field
        cust_infobox_phoneNumber_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_phoneNumber_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_phoneNumber_label = tk.Label(cust_infobox_phoneNumber_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_phoneNumber_label.config(bd=0, text='Phone Number: ', font='System 6', fg='yellow')
        cust_infobox_phoneNumber_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        self.phoneN_reg = master.register(self.phoneN_validate)

        self.entry_phoneNumber_var_1 = tk.StringVar(page1)
        self.entry_phoneNumber_var_1.set('')
        self.cust_infobox_phoneNumber = tk.Entry(cust_infobox_phoneNumber_frame)
        self.cust_infobox_phoneNumber.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_phoneNumber_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(self.phoneN_reg, "%P"))
        self.cust_infobox_phoneNumber.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Customer Type Radiobutton field
        cust_infobox_radiobutton_1_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_radiobutton_1_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_custType_1_label = tk.Label(cust_infobox_radiobutton_1_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_custType_1_label.config(bd=0, text='Customer Type: ', font='System 6', fg='yellow')
        cust_infobox_custType_1_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        self.radio_custType_var_1 = tk.StringVar(page1)
        self.radio_custType_var_1.set('REGULAR')

        #All available options (3) as 3 seperate clickable GUI radiobuttons.
        self.cust_infobox_custType_radio_1_1 = tk.Radiobutton(cust_infobox_radiobutton_1_frame, text='Regular',
                                                         variable=self.radio_custType_var_1, value='REGULAR',
                                                         font='System 1', fg='yellow', relief=tk.GROOVE, bd=1,
                                                         bg='gray15', selectcolor='gray15')
        self.cust_infobox_custType_radio_1_2 = tk.Radiobutton(cust_infobox_radiobutton_1_frame, text='Reduced',
                                                         variable=self.radio_custType_var_1, value='REDUCED',
                                                         font='System 1', fg='yellow', relief=tk.GROOVE, bd=1,
                                                         bg='gray15', selectcolor='gray15')
        self.cust_infobox_custType_radio_1_3 = tk.Radiobutton(cust_infobox_radiobutton_1_frame, text='Special',
                                                         variable=self.radio_custType_var_1, value='SPECIAL',
                                                         font='System 1', fg='yellow', relief=tk.GROOVE, bd=1,
                                                         bg='gray15', selectcolor='gray15')

        #3 Variables to store the value which was chosen from the 3.
        self.cust_infobox_custType_radio_1_1.pack(side=tk.LEFT, anchor=tk.W)
        self.cust_infobox_custType_radio_1_2.pack(side=tk.LEFT, anchor=tk.W)
        self.cust_infobox_custType_radio_1_3.pack(side=tk.LEFT, anchor=tk.W)
        ###

        ### Dynamic CustomerID Search Field
        cust_infobox_search_custID_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_search_custID_frame.pack(anchor=tk.S, fill=tk.X, expand=True)

        cust_infobox_search_custID_label = tk.Label(cust_infobox_search_custID_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_search_custID_label.config(bd=0, text='Search Specific CustomerID: ', font='System 6', fg='yellow')
        cust_infobox_search_custID_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        #Validation method
        self.search_custID_reg = master.register(self.search_custID_validate)

        self.entry_search_custID_var_1 = tk.StringVar(page1)
        self.entry_search_custID_var_1.set('')
        
        self.cust_infobox_search_custID_entry = tk.Entry(cust_infobox_search_custID_frame)
        self.cust_infobox_search_custID_entry.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                                     textvariable=self.entry_search_custID_var_1,
                                                     font='System 6', fg='yellow', validate="key",
                                                     validatecommand=(self.search_custID_reg, "%P"))
        self.cust_infobox_search_custID_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        #Allows the user to use their 'Return'/'Enter' key to search for a Customer
        self.cust_infobox_search_custID_entry.bind("<Return>", self.searchSpecific_Customer)

        # Seat Blocker
        # Blocks seats from being allocated by the user
        cust_infobox_seatblocker_frame = tk.Frame(cust_infobox_canvas, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_seatblocker_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        cust_infobox_seatblocker_label = tk.Label(cust_infobox_seatblocker_frame, relief=tk.FLAT, bd=0, bg='gray15')
        cust_infobox_seatblocker_label.config(bd=0, text='Block Seat? ', font='System 6', fg='yellow')
        cust_infobox_seatblocker_label.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)
        
        self.radio_seatblocker_var_1 = tk.StringVar(page1)
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

        #Calls the customerInfoButton_get function to be ran upon the button being pressed.
        enter_info_button = tk.Button(enter_info_button_frame)
        enter_info_button.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.customerInfoButton_get)
        enter_info_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)
        ###
        
        ### Making 'Refresh' Button
        refresh_button_frame = tk.Frame(main_frame, relief=tk.GROOVE, bd=0, bg='gray15')
        refresh_button_frame.pack(side=tk.BOTTOM)

        refresh_button_Label = tk.Label(refresh_button_frame, relief=tk.GROOVE, bg='gray15')
        refresh_button_Label.config(text='Refresh The Table:', font='System 6', fg='yellow')
        refresh_button_Label.pack(side=tk.TOP)
        
        #Calls the refreshTreeview function to be ran upon the button being pressed.
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
        treeview_frame = tk.Frame(page1, relief=tk.GROOVE, bd=0, bg='gray15')
        treeview_frame.pack(side=tk.TOP, padx=10, pady=10)

        treeview_label = tk.Label(treeview_frame, relief=tk.GROOVE, bg='gray15')
        treeview_label.config(text='Search Database:', font='System 6', fg='yellow')
        treeview_label.pack(side=tk.TOP, padx=10, pady=10)

        #Create the columns necessary to display the database in the GUI as a table.
        self.columns = (
            'Customer ID', '6th Oct: Seat ID', '5th Oct: Seat ID', '4th Oct: Seat ID', 'First Name', 'Surname',
            'Phone Number', 'Status', 'Price')
        self.treeview = ttk.Treeview(treeview_frame, columns=self.columns, show='headings')
        # Makes the column titles
        self.treeview.column('Customer ID', width=100)
        self.treeview.column('6th Oct: Seat ID', width=100)
        self.treeview.column('5th Oct: Seat ID', width=100)
        self.treeview.column('4th Oct: Seat ID', width=100)
        self.treeview.column('First Name', width=100)
        self.treeview.column('Surname', width=100)
        self.treeview.column('Phone Number', width=100)
        self.treeview.column('Status', width=100)
        self.treeview.column("Price", width=100)

        # Fetching database for values to place into treeview.
        # This code below fetches all the VALID customerIDs in the database that
        # have a seatID assigned to them on one of the performance days
        cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE SeatID_Sixth!='' OR SeatID_Fifth!='' OR SeatID_Fourth!=''")
        tv_custID_fetch = cursor.fetchall()
        tv_custID_list = [x[0] for x in tv_custID_fetch]
        tv_custID = tv_custID_list

        # Fetches the SeatIDs from all performance days and displays them
        # respectively to their customer and their information, by fetching
        # seatIDs from the database and placing them in the order they appear in
        # the real database.
        cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking")
        tv_6th_seatID_fetch = cursor.fetchall()
        tv_6th_seatID_list = [x[0] for x in tv_6th_seatID_fetch]
        tv_6th_seatID = tv_6th_seatID_list

        cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking")
        tv_5th_seatID_fetch = cursor.fetchall()
        tv_5th_seatID_list = [x[0] for x in tv_5th_seatID_fetch]
        tv_5th_seatID = tv_5th_seatID_list

        cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking")
        tv_4th_seatID_fetch = cursor.fetchall()
        tv_4th_seatID_list = [x[0] for x in tv_4th_seatID_fetch]
        tv_4th_seatID = tv_4th_seatID_list

        cursor.execute("SELECT fname FROM CustomerBooking")
        tv_fname_fetch = cursor.fetchall()
        tv_fname_list = [x[0] for x in tv_fname_fetch]
        tv_fname = tv_fname_list

        cursor.execute("SELECT surname FROM CustomerBooking")
        tv_surname_fetch = cursor.fetchall()
        tv_surname_list = [x[0] for x in tv_surname_fetch]
        tv_surname = tv_surname_list

        cursor.execute("SELECT phoneN FROM CustomerBooking")
        tv_phoneN_fetch = cursor.fetchall()
        tv_phoneN_list = [x[0] for x in tv_phoneN_fetch]
        tv_phoneN = tv_phoneN_list

        cursor.execute("SELECT custType FROM CustomerBooking")
        tv_custType_fetch = cursor.fetchall()
        tv_custType_list = [x[0] for x in tv_custType_fetch]
        tv_custType = tv_custType_list

        cursor.execute("SELECT price FROM CustomerBooking")
        tv_price_fetch = cursor.fetchall()
        tv_price_list = [x[0] for x in tv_price_fetch]
        tv_price = tv_price_list

        # Inserting values into treeview.
        # For however many customerIDs have a seat assigned to them on any given
        # day, the treeview will iterate over each one and insert every
        # customers' information, respective to their given customerID.
        for i in range(len(tv_custID)):
            try:
                self.treeview.insert('', tk.END,
                                     values=(tv_custID[i], tv_6th_seatID[i], tv_5th_seatID[i], tv_4th_seatID[i],
                                             tv_fname[i], tv_surname[i], tv_phoneN[i], tv_custType[i], tv_price[i]))
                i += 1
            except IndexError:
                # Insert an empty string if this error is caught
                self.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', ''))
                i += 1
            self.treeview.pack(pady=2, padx=2)
        # For every column in the columns list, make the column able to be
        # sorted alphabetically or numerically by calling the
        # treeview_sort_column function for every column each time the column
        # heading is pressed.
        for col in self.columns:
            self.treeview.heading(col, text=col,
                                  command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))

        ### MANAGEMENT INFO PANEL
        self.page2 = tk.Frame(main_notebook)
        main_notebook.add(self.page2, text="Management Info")

        frame1_page2 = tk.Frame(self.page2, relief=tk.FLAT, borderwidth=1, bg='gray15')
        frame1_page2.pack(side=tk.TOP, fill=tk.BOTH)

        logo_header_pg2 = tk.Label(frame1_page2, relief=tk.GROOVE, borderwidth=1, bg='ghost white')
        logo_header_pg2.config(bd=0, text='Auditorium Booking System v1.15.2', font='System 12')
        logo_header_pg2.pack(fill=tk.X, expand=True, anchor=tk.N)

        custInfoTitle_pg2 = tk.Label(frame1_page2, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        custInfoTitle_pg2.config(bd=0, text='Management Information', font='System 20')
        custInfoTitle_pg2.pack(fill=tk.X, expand=True, side=tk.TOP, anchor=tk.N, pady=20)

        ### Making Each Frame for the display of what is required
        management_info_frame = tk.Frame(self.page2, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        management_info_frame.pack(padx=15, pady=15, side=tk.TOP, anchor=tk.W, fill=tk.BOTH, expand=True)

        ticketSales_frame = tk.Frame(management_info_frame, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        ticketSales_frame.pack(padx=15, pady=15, side=tk.TOP, anchor=tk.W, expand=True, fill=tk.BOTH)

        ticketSold_title = tk.Label(ticketSales_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        ticketSold_title.config(bd=0, text='Ticket Sales', font='System 25')
        ticketSold_title.pack(fill=tk.X, padx=10, pady=10)

        # Fetches all valid seatIDs on said performance date, that have a
        # customer ID assigned to them. The number of valid seatIDs will be the
        # number of tickets that have been allocated/sold.
        cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking WHERE fname!='' AND fname!='-'")
        no_tickets_sixth_fetch = cursor.fetchall()
        no_tickets_sixth_list = [x[0] for x in no_tickets_sixth_fetch]

        cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking WHERE fname!='' AND fname!='-'")
        no_tickets_fifth_fetch = cursor.fetchall()
        no_tickets_fifth_list = [x[0] for x in no_tickets_fifth_fetch]

        cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking WHERE fname!='' AND fname!='-'")
        no_tickets_fourth_fetch = cursor.fetchall()
        no_tickets_fourth_list = [x[0] for x in no_tickets_fourth_fetch]

        # Checks if the string in the specific field in the database is empty.
        # If it is, it removes the empty string.
        empty_string = ''
        while empty_string in no_tickets_sixth_list:
            no_tickets_sixth_list.remove(empty_string)

        while empty_string in no_tickets_fifth_list:
            no_tickets_fifth_list.remove(empty_string)

        while empty_string in no_tickets_fourth_list:
            no_tickets_fourth_list.remove(empty_string)
        
        # Output the number of tickets sold on the UI.
        self.no_ticketSold = len(no_tickets_sixth_list + no_tickets_fifth_list + no_tickets_fourth_list)
        self.ticketSold_label = tk.Label(ticketSales_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        self.ticketSold_label.config(bd=0, text='No. Tickets Sold: %d' % self.no_ticketSold, font='System 16')
        self.ticketSold_label.pack(fill=tk.X, anchor=tk.N, padx=10, pady=10)

        # The max amount of customers is 600 (200 seats/performance)
        # Hence, 600- number of tickets sold = number of tickets remaining.
        self.no_left2sell = 600 - self.no_ticketSold
        self.ticketLeft2Sell_label = tk.Label(ticketSales_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        self.ticketLeft2Sell_label.config(bd=0, text='No. Tickets Left: %d' % self.no_left2sell, font='System 16')
        self.ticketLeft2Sell_label.pack(fill=tk.X, padx=10, pady=10)

        ### Making 'Refresh' Button
        refresh_management_button = tk.Button(ticketSales_frame)
        refresh_management_button.config(relief=tk.RAISED, bd=5, text='    Refresh    ',
                                         command=self.refreshManagementInfo)
        refresh_management_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)

        refresh_button_management_Label = tk.Label(ticketSales_frame, relief=tk.GROOVE, bg='gray15')
        refresh_button_management_Label.config(text='Refresh All Management Information:', font='System 6', fg='yellow')
        refresh_button_management_Label.pack(side=tk.BOTTOM, anchor=tk.S, padx=15, pady=15)
        ###

        # Collect up all the prices each customer paid that're stored in the
        # database on the 6th.
        cursor.execute("SELECT price FROM CustomerBooking WHERE SeatID_Sixth!=''")
        sixth_revenue_fetch = cursor.fetchall()
        sixth_revenue_list = [x[0] for x in sixth_revenue_fetch]

        # Select the custType that they are classed under as.
        self.sixth_total_revenue = 0
        cursor.execute("SELECT custType FROM CustomerBooking WHERE SeatID_Sixth!=''")
        sixth_custType_fetch = cursor.fetchall()
        sixth_custType_list = [x[0] for x in sixth_custType_fetch]

        # Link the correct price to the respective customer status.
        try:
            for i in range(len(sixth_revenue_list)) and range(len(sixth_custType_list)):
                if sixth_custType_list[i] == "REGULAR":
                    self.sixth_total_revenue += 10

                elif sixth_custType_list[i] == "REDUCED":
                    self.sixth_total_revenue += 5

                elif sixth_custType_list[i] == "SPECIAL":
                    self.sixth_total_revenue += 0

                i += 1

        except TypeError:
            # To handle not iterable TypeError.
            self.sixth_total_revenue = 0

        cursor.execute("SELECT price FROM CustomerBooking WHERE SeatID_Fifth!=''")
        fifth_revenue_fetch = cursor.fetchall()
        fifth_revenue_list = [x[0] for x in fifth_revenue_fetch]

        self.fifth_total_revenue = 0
        cursor.execute("SELECT custType FROM CustomerBooking WHERE SeatID_Fifth!=''")
        fifth_custType_fetch = cursor.fetchall()
        fifth_custType_list = [x[0] for x in fifth_custType_fetch]

        try:
            for i in range(len(fifth_revenue_list)) and range(len(fifth_custType_list)):
                if fifth_custType_list[i] == "REGULAR":
                    self.fifth_total_revenue += 10
                    i += 1
                elif fifth_custType_list[i] == "REDUCED":
                    self.fifth_total_revenue += 5
                    i += 1
                elif fifth_custType_list[i] == "SPECIAL":
                    self.fifth_total_revenue += 0
                    i += 1

        except TypeError:
            self.fifth_total_revenue = 0

        cursor.execute("SELECT price FROM CustomerBooking WHERE SeatID_Fourth!=''")
        fourth_revenue_fetch = cursor.fetchall()
        fourth_revenue_list = [x[0] for x in fourth_revenue_fetch]

        self.fourth_total_revenue = 0
        cursor.execute("SELECT custType FROM CustomerBooking WHERE SeatID_Fourth!=''")
        fourth_custType_fetch = cursor.fetchall()
        fourth_custType_list = [x[0] for x in fourth_custType_fetch]

        try:
            for i in range(len(fourth_revenue_list)) and range(len(fourth_custType_list)):
                if fourth_custType_list[i] == "REGULAR":
                    self.fourth_total_revenue += 10
                    i += 1
                elif fourth_custType_list[i] == "REDUCED":
                    self.fourth_total_revenue += 5
                    i += 1
                elif fourth_custType_list[i] == "SPECIAL":
                    self.fourth_total_revenue += 0
                    i += 1

        except TypeError:
            self.fourth_total_revenue = 0
        # Add up each days' revenue to calculate the total revenue.
        self.total_revenue = self.sixth_total_revenue + self.fifth_total_revenue + self.fourth_total_revenue

        # Build the frame upon which to place the management information.
        revenue_frame = tk.Frame(management_info_frame, relief=tk.GROOVE, borderwidth=1, bg='gray15')
        revenue_frame.pack(padx=15, pady=15, side=tk.TOP, anchor=tk.E, expand=True, fill=tk.BOTH)

        revenue_title = tk.Label(revenue_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        revenue_title.config(bd=0, text='Revenue Stats', font='System 25')
        revenue_title.pack(fill=tk.X, padx=10, pady=10)

        self.sixth_revenue_label = tk.Label(revenue_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        self.sixth_revenue_label.config(bd=0, text='Total Revenue on 6/10/20: £%d' % self.sixth_total_revenue,
                                        font='System 16')
        self.sixth_revenue_label.pack(fill=tk.X, padx=10, pady=10)

        self.fifth_revenue_label = tk.Label(revenue_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        self.fifth_revenue_label.config(bd=0, text='Total Revenue on 5/10/20: £%d' % self.fifth_total_revenue,
                                        font='System 16')
        self.fifth_revenue_label.pack(fill=tk.X, padx=10, pady=10)

        self.fourth_revenue_label = tk.Label(revenue_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        self.fourth_revenue_label.config(bd=0, text='Total Revenue on 4/10/20: £%d' % self.fourth_total_revenue,
                                         font='System 16')
        self.fourth_revenue_label.pack(fill=tk.X, padx=10, pady=10)

        self.total_revenue_label = tk.Label(revenue_frame, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        self.total_revenue_label.config(bd=0, text='Total Compound Revenue: £%d' % self.total_revenue, font='System 16')
        self.total_revenue_label.pack(fill=tk.X, padx=10, pady=10)

        # Help Page
        page3 = tk.Frame(main_notebook)
        main_notebook.add(page3, text="Help")

        frame1_page3 = tk.Frame(page3, relief=tk.FLAT, borderwidth=1, bg='gray15')
        frame1_page3.pack(side=tk.TOP, fill=tk.BOTH)

        logo_header = tk.Label(frame1_page3, relief=tk.GROOVE, borderwidth=1, bg='ghost white')
        logo_header.config(bd=0, text='Auditorium Booking System v1.15.2', font='System 12')
        logo_header.pack(fill=tk.X, expand=True, anchor=tk.N)

        custInfoTitle = tk.Label(frame1_page3, relief=tk.GROOVE, bd=0, bg='gray15', fg='yellow')
        custInfoTitle.config(bd=0, text='Entering Customer Information', font='System 20')
        custInfoTitle.pack(fill=tk.X, expand=True, side=tk.TOP, anchor=tk.N, pady=20)

        # Calls function in a seperate file to show the help page.
        customer_infobox_gen_EXAMPLE.CustomerInfoBox(page3)

    ### Validation Methods
        # If the input returns a True upon going through the validation,
        # that means that it is a valid input
    def fname_validate(self, fname_inp):
        #checks if the input is an alphabetical character
        if fname_inp.isalpha():
            fname_inp_lencheck = ''.join(fname_inp)
            if fname_inp_lencheck[0].isupper() == True:
                if len(str(fname_inp_lencheck)) <= 20:
                    return True
                else:
                    return False   
            else:
                return False
        #checks if input is empty
        elif fname_inp is "":
            return True
        #check if input is a NULL value in the database
        elif fname_inp is None:
            return False
        else:
            return False

    def surname_validate(self, surname_inp):
        if surname_inp.isalpha():
            surname_inp_lencheck = ''.join(surname_inp)
            if surname_inp_lencheck[0].isupper() == True:
                if len(str(surname_inp_lencheck)) <= 20:
                    return True
                else:
                    return False   
            else:
                return False
        elif surname_inp is "":
            return True
        elif surname_inp is None:
            return False
        else:
            return False

    def phoneN_validate(self, phoneN_inp):
        #check if the input is a digit
        self.phoneN_inp = phoneN_inp
        if phoneN_inp.isdigit():
            phoneN_inp_lencheck = ''.join(phoneN_inp)
            #check if the first character entered at the input is a 0
            if phoneN_inp_lencheck[0] != '0':
                return False
            else:
                #check if the length of the phone number is a valid number of 11 digits (including 0 at the start)
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
            #check for a customerID larger than 3 digits (which shouldnt exist since the highest is custID 600)
            if len(search_custID_inp_lencheck) > 3:
                return False
            else:
                #check if the customerID searched for is bigger than 600
                if int(search_custID_inp) > 600:
                    return False
                else:
                    return True
        elif search_custID_inp is "":
            return True
        else:
            return False

    ###

    ### Treeview sorting algorithm
    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            l.sort(key=lambda t: int(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: \
            self.treeview_sort_column(tv, col, not reverse))

    ###           

    ### Detect change in performance date
    def change(self, *args):
        self.listboxUpdate()

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
        

    ###

    ### Search for a specific customer through CustomerID
    def searchSpecific_Customer(self, *args):
        try:
            # Fetch custID in the entry field and then fetch all the other info
            # belonging to that customerID.
            self.entry_search_cust_ID_var_1_fetched = self.entry_search_custID_var_1.get()
            cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE CustomerID=?",
                           (self.entry_search_cust_ID_var_1_fetched,))
            search_sixth_seatlist_fetch = cursor.fetchall()
            search_custID_list = [x[0] for x in search_sixth_seatlist_fetch]
            self.entry_id_var_1.set(search_custID_list[0])

            cursor.execute("SELECT fname FROM CustomerBooking WHERE CustomerID=?",
                           (self.entry_search_cust_ID_var_1_fetched,))
            search_fname_fetch = cursor.fetchall()
            search_fname_list = [x[0] for x in search_fname_fetch]

            #Disables the entry fields if the user passes through a blocked seat.
            if search_fname_list[0] == '-':
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

            # check if the first name is empty.
            if search_fname_list[0] != '':
                search_fname_list[0] = search_fname_list[0]
            else:
                search_fname_list[0] = ""
            # set the entry field to show the first name
            self.entry_fname_var_1.set(search_fname_list[0])

            cursor.execute("SELECT surname FROM CustomerBooking WHERE CustomerID=?",
                           (self.entry_search_cust_ID_var_1_fetched,))
            search_surname_fetch = cursor.fetchall()
            search_surname_list = [x[0] for x in search_surname_fetch]

            # same as above
            if search_surname_list[0] != '':
                search_surname_list[0] = search_surname_list[0]
            else:
                search_surname_list[0] = ""

            self.entry_surname_var_1.set(search_surname_list[0])

            cursor.execute("SELECT phoneN FROM CustomerBooking WHERE CustomerID=?",
                           (self.entry_search_cust_ID_var_1_fetched,))
            search_phoneNumber_fetch = cursor.fetchall()
            search_phoneNumber_list = [x[0] for x in search_phoneNumber_fetch]

            if search_phoneNumber_list[0] != '':
                search_phoneNumber_list[0] = search_phoneNumber_list[0]
            else:
                search_phoneNumber_list[0] = ""

            self.entry_phoneNumber_var_1.set(search_phoneNumber_list[0])

            cursor.execute("SELECT custType FROM CustomerBooking WHERE CustomerID=?",
                           (self.entry_search_cust_ID_var_1_fetched,))
            search_custType_fetch = cursor.fetchall()
            search_custType_list = [x[0] for x in search_custType_fetch]

            if search_custType_list[0] != '':
                search_custType_list[0] = search_custType_list[0]
            else:
                search_custType_list[0] = "REGULAR"

            self.radio_custType_var_1.set(search_custType_list[0])
        # This may be triggered by attempting to display a customerID <0, or a customerID >600.
        except IndexError:
            messagebox.showerror('Illegal CustomerID Error', 'CustomerID beyond this point cannot be found.')

    ###

    ### Load in Next CustomerID and relevant information along with it.
    def nextCustomer(self):
        # ## Grab the next CustomerID along and load up the information onto the entry fields that is fetched from
        # the database.
        try:
            # Fetch the information from the database of the customerID that is currently displayed on the entry field + 1.
            self.next_entry_id_var_1 = int(self.entry_id_var_1.get()) + 1

            cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE CustomerID=?", (self.next_entry_id_var_1,))
            next_sixth_seatlist_fetch = cursor.fetchall()
            next_custID_list = [x[0] for x in next_sixth_seatlist_fetch]
            self.entry_id_var_1.set(next_custID_list[0])

            cursor.execute("SELECT fname FROM CustomerBooking WHERE CustomerID=?", (self.next_entry_id_var_1,))
            next_fname_fetch = cursor.fetchall()
            next_fname_list = [x[0] for x in next_fname_fetch]

            #Disables the entry fields if the user passes through a blocked seat.
            if next_fname_list[0] == '-':
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

            # check if the first name is empty.
            if next_fname_list[0] != '':
                next_fname_list[0] = next_fname_list[0]
            else:
                next_fname_list[0] = ""

            self.entry_fname_var_1.set(next_fname_list[0])

            cursor.execute("SELECT surname FROM CustomerBooking WHERE CustomerID=?", (self.next_entry_id_var_1,))
            next_surname_fetch = cursor.fetchall()
            next_surname_list = [x[0] for x in next_surname_fetch]

            if next_surname_list[0] != '':
                next_surname_list[0] = next_surname_list[0]
            else:
                next_surname_list[0] = ""

            self.entry_surname_var_1.set(next_surname_list[0])

            cursor.execute("SELECT phoneN FROM CustomerBooking WHERE CustomerID=?", (self.next_entry_id_var_1,))
            next_phoneNumber_fetch = cursor.fetchall()
            next_phoneNumber_list = [x[0] for x in next_phoneNumber_fetch]

            if next_phoneNumber_list[0] != '':
                next_phoneNumber_list[0] = next_phoneNumber_list[0]
            else:
                next_phoneNumber_list[0] = ""

            self.entry_phoneNumber_var_1.set(next_phoneNumber_list[0])

            cursor.execute("SELECT custType FROM CustomerBooking WHERE CustomerID=?", (self.next_entry_id_var_1,))
            next_custType_fetch = cursor.fetchall()
            next_custType_list = [x[0] for x in next_custType_fetch]

            if next_custType_list[0] != '':
                next_custType_list[0] = next_custType_list[0]
            else:
                next_custType_list[0] = "REGULAR"

            self.radio_custType_var_1.set(next_custType_list[0])

            self.radio_custType_var_1.set(next_custType_list[0])
        except IndexError:
            messagebox.showerror('Illegal CustomerID Error', 'CustomerID beyond this point cannot be found.')

    ###

    ### Load in Previous CustomerID and relevant information along with it.
    def prevCustomer(self):
        # Grab the previous CustomerID along and load up the information onto the entry fields that is fetched
        # from the database.
        try:
            # Same as above, except -1.
            self.prev_entry_id_var_1 = int(self.entry_id_var_1.get()) - 1

            cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE CustomerID=?", (self.prev_entry_id_var_1,))
            prev_sixth_seatlist_fetch = cursor.fetchall()
            prev_custID_list = [x[0] for x in prev_sixth_seatlist_fetch]
            self.entry_id_var_1.set(prev_custID_list[0])

            cursor.execute("SELECT fname FROM CustomerBooking WHERE CustomerID=?", (self.prev_entry_id_var_1,))
            prev_fname_fetch = cursor.fetchall()
            prev_fname_list = [x[0] for x in prev_fname_fetch]

            #Disables the entry fields if the user passes through a blocked seat.
            if prev_fname_list[0] == '-':
                self.cust_infobox_fname_entry["state"]= tk.DISABLED
                self.cust_infobox_surname_entry["state"]= tk.DISABLED
                self.cust_infobox_phoneNumber["state"]= tk.DISABLED
                self.cust_infobox_custType_radio_1_1["state"]= tk.DISABLED
                self.cust_infobox_custType_radio_1_2["state"]= tk.DISABLED
                self.cust_infobox_custType_radio_1_3["state"]= tk.DISABLED
            else:
                # Re-enable the state of the seats if the customer information that loaded up was not from a blocked seat.
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

            # check if the first name is empty.
            if prev_fname_list[0] != '':
                prev_fname_list[0] = prev_fname_list[0]
            else:
                prev_fname_list[0] = ""
                

            self.entry_fname_var_1.set(prev_fname_list[0])

            cursor.execute("SELECT surname FROM CustomerBooking WHERE CustomerID=?", (self.prev_entry_id_var_1,))
            prev_surname_fetch = cursor.fetchall()
            prev_surname_list = [x[0] for x in prev_surname_fetch]

            if prev_surname_list[0] != '':
                prev_surname_list[0] = prev_surname_list[0]
            else:
                prev_surname_list[0] = ""

            self.entry_surname_var_1.set(prev_surname_list[0])

            cursor.execute("SELECT phoneN FROM CustomerBooking WHERE CustomerID=?", (self.prev_entry_id_var_1,))
            prev_phoneNumber_fetch = cursor.fetchall()
            prev_phoneNumber_list = [x[0] for x in prev_phoneNumber_fetch]

            if prev_phoneNumber_list[0] != '':
                prev_phoneNumber_list[0] = prev_phoneNumber_list[0]
            else:
                prev_phoneNumber_list[0] = ""

            self.entry_phoneNumber_var_1.set(prev_phoneNumber_list[0])

            cursor.execute("SELECT custType FROM CustomerBooking WHERE CustomerID=?", (self.prev_entry_id_var_1,))
            prev_custType_fetch = cursor.fetchall()
            prev_custType_list = [x[0] for x in prev_custType_fetch]

            if prev_custType_list[0] != '':
                prev_custType_list[0] = prev_custType_list[0]
            else:
                prev_custType_list[0] = "REGULAR"

            self.radio_custType_var_1.set(prev_custType_list[0])
        except IndexError:
            messagebox.showerror('Illegal CustomerID Error', 'CustomerID beyond this point cannot be found.')

    ###

    ### Refresh management Info Page to show updated values
    def refreshManagementInfo(self):
        # Fetch all seatIDs from each date where a customer has a seat.
        cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking WHERE fname!='' AND fname!='-'")
        no_tickets_sixth_fetch = cursor.fetchall()
        no_tickets_sixth_list = [x[0] for x in no_tickets_sixth_fetch]
        # The number of seatIDs which have a customer linked to them is equal to
        # the number of seats which have been allocated/sold.

        cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking WHERE fname!='' AND fname!='-'")
        no_tickets_fifth_fetch = cursor.fetchall()
        no_tickets_fifth_list = [x[0] for x in no_tickets_fifth_fetch]

        cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking WHERE fname!='' AND fname!='-'")
        no_tickets_fourth_fetch = cursor.fetchall()
        no_tickets_fourth_list = [x[0] for x in no_tickets_fourth_fetch]

        # Checks if the string in the specific field in the database is empty.
        # If it is, it removes the empty string.
        empty_string = ''
        while empty_string in no_tickets_sixth_list:
            no_tickets_sixth_list.remove(empty_string)

        while empty_string in no_tickets_fifth_list:
            no_tickets_fifth_list.remove(empty_string)

        while empty_string in no_tickets_fourth_list:
            no_tickets_fourth_list.remove(empty_string)

        # Add up the number of tickets sold on each day, to display the total
        # across all 3 days.
        self.no_ticketSold = len(no_tickets_sixth_list + no_tickets_fifth_list + no_tickets_fourth_list)
        # The number of tickets left is equal to the max number of tickets
        # available (600) - the number of tickets sold.
        self.no_left2sell = 600 - self.no_ticketSold

        cursor.execute("SELECT price FROM CustomerBooking WHERE SeatID_Sixth!=''")
        sixth_revenue_fetch = cursor.fetchall()
        sixth_revenue_list = [x[0] for x in sixth_revenue_fetch]

        self.sixth_total_revenue = 0
        cursor.execute("SELECT custType FROM CustomerBooking WHERE SeatID_Sixth!=''")
        sixth_custType_fetch = cursor.fetchall()
        sixth_custType_list = [x[0] for x in sixth_custType_fetch]

        try:
            for i in range(len(sixth_revenue_list)) and range(len(sixth_custType_list)):
                if sixth_custType_list[i] == "REGULAR":
                    self.sixth_total_revenue += 10

                elif sixth_custType_list[i] == "REDUCED":
                    self.sixth_total_revenue += 5

                elif sixth_custType_list[i] == "SPECIAL":
                    self.sixth_total_revenue += 0
                i += 1

        except TypeError:
            # To handle not iterable TypeError.
            self.sixth_total_revenue = 0

        cursor.execute("SELECT price FROM CustomerBooking WHERE SeatID_Fifth!=''")
        fifth_revenue_fetch = cursor.fetchall()
        fifth_revenue_list = [x[0] for x in fifth_revenue_fetch]

        self.fifth_total_revenue = 0
        cursor.execute("SELECT custType FROM CustomerBooking WHERE SeatID_Fifth!=''")
        fifth_custType_fetch = cursor.fetchall()
        fifth_custType_list = [x[0] for x in fifth_custType_fetch]

        try:
            for i in range(len(fifth_revenue_list)) and range(len(fifth_custType_list)):
                if fifth_custType_list[i] == "REGULAR":
                    self.fifth_total_revenue += 10
                    i += 1
                elif fifth_custType_list[i] == "REDUCED":
                    self.fifth_total_revenue += 5
                    i += 1
                elif fifth_custType_list[i] == "SPECIAL":
                    self.fifth_total_revenue += 0
                    i += 1

        except TypeError:
            self.fifth_total_revenue = 0

        cursor.execute("SELECT price FROM CustomerBooking WHERE SeatID_Fourth!=''")
        fourth_revenue_fetch = cursor.fetchall()
        fourth_revenue_list = [x[0] for x in fourth_revenue_fetch]

        self.fourth_total_revenue = 0
        cursor.execute("SELECT custType FROM CustomerBooking WHERE SeatID_Fourth!=''")
        fourth_custType_fetch = cursor.fetchall()
        fourth_custType_list = [x[0] for x in fourth_custType_fetch]

        try:
            for i in range(len(fourth_revenue_list)) and range(len(fourth_custType_list)):
                if fourth_custType_list[i] == "REGULAR":
                    self.fourth_total_revenue += 10
                    i += 1
                elif fourth_custType_list[i] == "REDUCED":
                    self.fourth_total_revenue += 5
                    i += 1
                elif fourth_custType_list[i] == "SPECIAL":
                    self.fourth_total_revenue += 0
                    i += 1

        except TypeError:
            self.fourth_total_revenue = 0

        # Show new values on page
        self.ticketSold_label["text"] = 'No. Tickets Sold: %d' % self.no_ticketSold
        self.no_left2sell = 600 - self.no_ticketSold
        self.ticketLeft2Sell_label["text"] = 'No. Tickets Left: %d' % self.no_left2sell

        self.sixth_revenue_label["text"] = 'Total Revenue on 6/10/20: £%d' % self.sixth_total_revenue
        self.fifth_revenue_label["text"] = 'Total Revenue on 5/10/20: £%d' % self.fifth_total_revenue
        self.fourth_revenue_label["text"] = 'Total Revenue on 4/10/20: £%d' % self.fourth_total_revenue

        self.total_revenue = self.sixth_total_revenue + self.fifth_total_revenue + self.fourth_total_revenue
        self.total_revenue_label["text"] = 'Total Compound Revenue: £%d' % self.total_revenue

    ###

    ### Refresh Treeview table upon button press.
    def refreshTreeview(self):
        # Fetching values from database to place into treeview.

        # Fetching all customerIDs that have a customer linked to them.
        cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE SeatID_Sixth!='' OR SeatID_Fifth!='' OR SeatID_Fourth!=''")
        tv_custID_fetch = cursor.fetchall()
        tv_custID_list = [x[0] for x in tv_custID_fetch]
        tv_custID = tv_custID_list

        cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking")
        tv_6th_seatID_fetch = cursor.fetchall()
        tv_6th_seatID_list = [x[0] for x in tv_6th_seatID_fetch]
        tv_6th_seatID = tv_6th_seatID_list

        cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking")
        tv_5th_seatID_fetch = cursor.fetchall()
        tv_5th_seatID_list = [x[0] for x in tv_5th_seatID_fetch]
        tv_5th_seatID = tv_5th_seatID_list

        cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking")
        tv_4th_seatID_fetch = cursor.fetchall()
        tv_4th_seatID_list = [x[0] for x in tv_4th_seatID_fetch]
        tv_4th_seatID = tv_4th_seatID_list

        cursor.execute("SELECT fname FROM CustomerBooking")
        tv_fname_fetch = cursor.fetchall()
        tv_fname_list = [x[0] for x in tv_fname_fetch]
        tv_fname = tv_fname_list

        cursor.execute("SELECT surname FROM CustomerBooking")
        tv_surname_fetch = cursor.fetchall()
        tv_surname_list = [x[0] for x in tv_surname_fetch]
        tv_surname = tv_surname_list

        cursor.execute("SELECT phoneN FROM CustomerBooking")
        tv_phoneN_fetch = cursor.fetchall()
        tv_phoneN_list = [x[0] for x in tv_phoneN_fetch]
        tv_phoneN = tv_phoneN_list

        cursor.execute("SELECT custType FROM CustomerBooking")
        tv_custType_fetch = cursor.fetchall()
        tv_custType_list = [x[0] for x in tv_custType_fetch]
        tv_custType = tv_custType_list

        cursor.execute("SELECT price FROM CustomerBooking")
        tv_price_fetch = cursor.fetchall()
        tv_price_list = [x[0] for x in tv_price_fetch]
        tv_price = tv_price_list

        # Inserting values into treeview.
        for k in self.treeview.get_children():
            self.treeview.delete(k)

        for i in range(len(tv_custID)):
            try:
                self.treeview.insert('', tk.END,
                                     values=(tv_custID[i], tv_6th_seatID[i], tv_5th_seatID[i], tv_4th_seatID[i],
                                             tv_fname[i], tv_surname[i], tv_phoneN[i], tv_custType[i], tv_price[i]))
                i += 1
            except IndexError:
                self.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', ''))
                i += 1
            self.treeview.pack(pady=2, padx=2)
        for col in self.columns:
            self.treeview.heading(col, text=col,
                                  command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))

    ###

    ### Update the Listbox upon information being entered
    def listboxUpdate(self, *args):
        if self.perfDate_opt.get() == "06/10/20":
            # Fetch the seatIDs which are available to be purchased.
            cursor.execute("SELECT SeatID FROM Seating_SixthOct WHERE StateOfSeat = 'FREE'")
            sixth_seatlist_fetch = cursor.fetchall()
            # Place them into a list.
            sixth_seatlist_list = [x[0] for x in sixth_seatlist_fetch]
            self.seatList_6th = sixth_seatlist_list

            # Clear the table and then insert them into the bottom of the treeview table.
            self.seatList_listbox.delete(0, tk.END)
            for item in self.seatList_6th:
                self.seatList_listbox.insert(tk.END, item)
            self.seatList_listbox.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        elif self.perfDate_opt.get() == "05/10/20":
            cursor.execute("SELECT SeatID FROM Seating_FifthOct WHERE StateOfSeat = 'FREE'")
            fifth_seatlist_fetch = cursor.fetchall()
            fifth_seatlist_list = [x[0] for x in fifth_seatlist_fetch]
            self.seatList_5th = fifth_seatlist_list

            self.seatList_listbox.delete(0, tk.END)
            for item in self.seatList_5th:
                self.seatList_listbox.insert(tk.END, item)
            self.seatList_listbox.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        elif self.perfDate_opt.get() == "04/10/20":
            cursor.execute("SELECT SeatID FROM Seating_FourthOct WHERE StateOfSeat = 'FREE'")
            fourth_seatlist_fetch = cursor.fetchall()
            fourth_seatlist_list = [x[0] for x in fourth_seatlist_fetch]
            self.seatList_4th = fourth_seatlist_list

            self.seatList_listbox.delete(0, tk.END)
            for item in self.seatList_4th:
                self.seatList_listbox.insert(tk.END, item)
            self.seatList_listbox.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)
    ###

    ### Fetch all values from entry boxes and radio buttons on the GUI.
    def customerInfoButton_get(self):
        perfDate = self.perfDate_opt.get()
        blockSeat = self.radio_seatblocker_var_1.get()
        custID = self.entry_id_var_1.get()
        fname = self.entry_fname_var_1.get()
        surname = self.entry_surname_var_1.get()
        phoneN = self.entry_phoneNumber_var_1.get()
        custType = self.radio_custType_var_1.get()
        
        try:
            seat_selected = self.seatList_listbox.get(self.seatList_listbox.curselection())
            # if the user checked the seat to be blocked, then it will replace all the information at that CustomerID to
            # the character '-' to indicate that the seat is blocked.
            if blockSeat == 'yes':
                if perfDate == '06/10/20':
                    # Checks if there is a seat that was replaced and needs to be set to a 'FREE' state.
                    cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                    custID_match_sixth_fetch = cursor.fetchall()
                    custID_match_sixth_list = [x[0] for x in custID_match_sixth_fetch]

                    # If the seat that was selected from the dropdown
                    # does not equal the customerID that is shown in the database...
                    if seat_selected != custID_match_sixth_list[0]:
                        # update the database seatID to be linked to the correct customerID;
                        cursor.execute("UPDATE CustomerBooking SET SeatID_Sixth = ? WHERE CustomerID=?",
                                       (custID_match_sixth_list[0], custID))
                        conn.commit()
                        # Then, update said dates' seat state to 'FREE' on its individual seat list table, so that it becomes available to be purchased again.
                        cursor.execute("UPDATE Seating_SixthOct SET StateOfSeat='FREE' WHERE SeatID=?",
                                       (custID_match_sixth_list[0],))
                        conn.commit()
                        # Update the SeatID in the CustomerBooking table to be equal to the seat selected and custID in the UI.
                        cursor.execute("UPDATE CustomerBooking SET SeatID_Sixth = ? WHERE CustomerID=?",
                                       (seat_selected, custID))
                        conn.commit()
                        # Update the StateOfSeat to be 'TAKEN' in the individual seat list table of the performance date, so that it can be blocked off from being purchased
                        cursor.execute("UPDATE Seating_SixthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                       (seat_selected,))
                        conn.commit()
                    else:
                        # If the above doesn't apply, set the SeatID and CustID in the CustomerBooking table to = the seat selected and custID in the UI.
                        cursor.execute("UPDATE CustomerBooking SET SeatID_Sixth = ? WHERE CustomerID=?",
                                       (seat_selected, custID))
                        conn.commit()
                        # Then, update the SeatID's StateOfSeat in the individual performance dates' seat list table to be 'TAKEN', where it is equal to the seat selected in the UI.
                        cursor.execute("UPDATE Seating_SixthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                       (seat_selected,))
                        conn.commit()

                # same as above for the next two days.
                elif perfDate == '05/10/20':
                    cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                    custID_match_fifth_fetch = cursor.fetchall()
                    custID_match_fifth_list = [x[0] for x in custID_match_fifth_fetch]

                    if seat_selected != custID_match_fifth_list[0]:
                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fifth = ? WHERE CustomerID=?",
                                       (custID_match_fifth_list[0], custID))
                        conn.commit()

                        cursor.execute("UPDATE Seating_FifthOct SET StateOfSeat='FREE' WHERE SeatID=?",
                                       (custID_match_fifth_list[0],))
                        conn.commit()

                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fifth = ? WHERE CustomerID=?",
                                       (seat_selected, custID))
                        conn.commit()

                        cursor.execute("UPDATE Seating_FifthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                       (seat_selected,))
                        conn.commit()
                    else:
                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fifth = ? WHERE CustomerID=?",
                                       (seat_selected, custID))
                        conn.commit()

                        cursor.execute("UPDATE Seating_FifthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                       (seat_selected,))
                        conn.commit()

                elif perfDate == '04/10/20':
                    cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                    custID_match_fourth_fetch = cursor.fetchall()
                    custID_match_fourth_list = [x[0] for x in custID_match_fourth_fetch]

                    if seat_selected != custID_match_fourth_list[0]:
                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fourth = ? WHERE CustomerID=?",
                                       (custID_match_fourth_list[0], custID))
                        conn.commit()

                        cursor.execute("UPDATE Seating_FourthOct SET StateOfSeat='FREE' WHERE SeatID=?",
                                       (custID_match_fourth_list[0],))
                        conn.commit()

                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fourth = ? WHERE CustomerID=?",
                                       (seat_selected, custID))
                        conn.commit()

                        cursor.execute("UPDATE Seating_FourthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                       (seat_selected,))
                        conn.commit()
                    else:
                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fourth = ? WHERE CustomerID=?",
                                       (seat_selected, custID))
                        conn.commit()

                        cursor.execute("UPDATE Seating_FourthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                       (seat_selected,))
                        conn.commit()

                cursor.execute("UPDATE CustomerBooking SET fname='-' WHERE CustomerID=?", (custID,))
                conn.commit()

                cursor.execute("UPDATE CustomerBooking SET surname='-' WHERE CustomerID=?", (custID,))
                conn.commit()

                cursor.execute("UPDATE CustomerBooking SET phoneN='-' WHERE CustomerID=?", (custID,))
                conn.commit()

                cursor.execute("UPDATE CustomerBooking SET custType='-' WHERE CustomerID=?", (custID,))
                conn.commit()

                cursor.execute("UPDATE CustomerBooking SET price='-' WHERE CustomerID=?", (custID,))
                conn.commit()
                
                # Updates the management information and listbox of seats available.
                self.refreshManagementInfo()
                self.listboxUpdate()

                # Fetching database for values to update treeview.
                cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE SeatID_Sixth!='' OR SeatID_Fifth!='' OR SeatID_Fourth!=''")
                tv_custID_fetch = cursor.fetchall()
                tv_custID_list = [x[0] for x in tv_custID_fetch]
                tv_custID = tv_custID_list

                cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking")
                tv_6th_seatID_fetch = cursor.fetchall()
                tv_6th_seatID_list = [x[0] for x in tv_6th_seatID_fetch]
                tv_6th_seatID = tv_6th_seatID_list

                cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking")
                tv_5th_seatID_fetch = cursor.fetchall()
                tv_5th_seatID_list = [x[0] for x in tv_5th_seatID_fetch]
                tv_5th_seatID = tv_5th_seatID_list

                cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking")
                tv_4th_seatID_fetch = cursor.fetchall()
                tv_4th_seatID_list = [x[0] for x in tv_4th_seatID_fetch]
                tv_4th_seatID = tv_4th_seatID_list

                cursor.execute("SELECT fname FROM CustomerBooking")
                tv_fname_fetch = cursor.fetchall()
                tv_fname_list = [x[0] for x in tv_fname_fetch]
                tv_fname = tv_fname_list

                cursor.execute("SELECT surname FROM CustomerBooking")
                tv_surname_fetch = cursor.fetchall()
                tv_surname_list = [x[0] for x in tv_surname_fetch]
                tv_surname = tv_surname_list

                cursor.execute("SELECT phoneN FROM CustomerBooking")
                tv_phoneN_fetch = cursor.fetchall()
                tv_phoneN_list = [x[0] for x in tv_phoneN_fetch]
                tv_phoneN = tv_phoneN_list

                cursor.execute("SELECT custType FROM CustomerBooking")
                tv_custType_fetch = cursor.fetchall()
                tv_custType_list = [x[0] for x in tv_custType_fetch]
                tv_custType = tv_custType_list

                cursor.execute("SELECT price FROM CustomerBooking")
                tv_price_fetch = cursor.fetchall()
                tv_price_list = [x[0] for x in tv_price_fetch]
                tv_price = tv_price_list

                for k in self.treeview.get_children():
                    self.treeview.delete(k)

                for i in range(len(tv_custID)):
                    try:
                        self.treeview.insert('', tk.END,
                                             values=(tv_custID[i], tv_6th_seatID[i], tv_5th_seatID[i], tv_4th_seatID[i],
                                                     tv_fname[i], tv_surname[i], tv_phoneN[i], tv_custType[i], tv_price[i]))
                        i += 1
                    except IndexError:
                        self.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', ''))
                        i += 1
                    self.treeview.pack(pady=2, padx=2)
                for col in self.columns:
                    self.treeview.heading(col, text=col,
                                          command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))
            else:
                if fname == '':
                    # Error caused by anything not being entered.
                    messagebox.showerror('First Name Entry Error', 'Please Enter a First Name')
                elif fname.isalpha() == False:
                    # Error caused by name containing invalid characters.
                    messagebox.showerror('First Name Entry Error', 'Please Enter a Valid First Name')
                    self.cust_infobox_fname_entry.delete(0, tk.END)
                else:
                    if surname == '':
                        # Error caused by anything not being entered.
                        messagebox.showerror('Surname Entry Error', 'Please Enter a Surname')
                        
                    elif surname.isalpha() == False:
                        # Error caused by name containing invalid characters.
                        messagebox.showerror('Surname Entry Error', 'Please Enter a Valid Surname')
                        self.cust_infobox_surname_entry.delete(0, tk.END)
                        
                    else:
                        if phoneN == '':
                            # Error caused by empty string in entry field.
                            messagebox.showerror('Invalid Phone Number','Please enter a Phone Number')
                        elif phoneN.isdigit() == False:
                            # Error caused by characters in phone number not being digits
                            messagebox.showerror('Invalid Phone Number','Please only enter digits into the entry field.')
                            self.cust_infobox_phoneNumber.delete(0, tk.END)
                            
                        elif len(phoneN) != 11:
                            # Error caused by a valid phone number length being entered.
                            messagebox.showerror('Invalid Phone Number',
                                                 'Please Enter a Valid Phone Number.\nPhone Number must start with 0 and '
                                                 'be 11 digits long.')
                        else:
                            if custType =='-':
                                # Error caused by the user not giving a choice of custType
                                messagebox.showerror('Invalid Customer Type','Please select a customer type.')
                            else:
                                # Box Returns
                                # Send this information to the database using UPDATE
                                # to update the database based on the given customer ID.
                                if perfDate == '06/10/20':
                                    # Checks if there is a seat that was replaced and needs to be set to a 'FREE' state.
                                    cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                                    custID_match_sixth_fetch = cursor.fetchall()
                                    custID_match_sixth_list = [x[0] for x in custID_match_sixth_fetch]

                                    # If the seat that was selected from the dropdown
                                    # does not equal the customerID that is shown in the database...
                                    if seat_selected != custID_match_sixth_list[0]:
                                        # update the database seatID to be linked to the correct customerID;
                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Sixth = ? WHERE CustomerID=?",
                                                       (custID_match_sixth_list[0], custID))
                                        conn.commit()
                                        # Then, update said dates' seat state to 'FREE' on its individual seat list table, so that it becomes available to be purchased again.
                                        cursor.execute("UPDATE Seating_SixthOct SET StateOfSeat='FREE' WHERE SeatID=?",
                                                       (custID_match_sixth_list[0],))
                                        conn.commit()
                                        # Update the SeatID in the CustomerBooking table to be equal to the seat selected and custID in the UI.
                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Sixth = ? WHERE CustomerID=?",
                                                       (seat_selected, custID))
                                        conn.commit()
                                        # Update the StateOfSeat to be 'TAKEN' in the individual seat list table of the performance date, so that it can be blocked off from being purchased
                                        cursor.execute("UPDATE Seating_SixthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                                       (seat_selected,))
                                        conn.commit()
                                    else:
                                        # If the above doesn't apply, set the SeatID and CustID in the CustomerBooking table to = the seat selected and custID in the UI.
                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Sixth = ? WHERE CustomerID=?",
                                                       (seat_selected, custID))
                                        conn.commit()
                                        # Then, update the SeatID's StateOfSeat in the individual performance dates' seat list table to be 'TAKEN', where it is equal to the seat selected in the UI.
                                        cursor.execute("UPDATE Seating_SixthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                                       (seat_selected,))
                                        conn.commit()
                                # same as above for the next two days.
                                elif perfDate == '05/10/20':
                                    cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                                    custID_match_fifth_fetch = cursor.fetchall()
                                    custID_match_fifth_list = [x[0] for x in custID_match_fifth_fetch]

                                    if seat_selected != custID_match_fifth_list[0]:
                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fifth = ? WHERE CustomerID=?",
                                                       (custID_match_fifth_list[0], custID))
                                        conn.commit()

                                        cursor.execute("UPDATE Seating_FifthOct SET StateOfSeat='FREE' WHERE SeatID=?",
                                                       (custID_match_fifth_list[0],))
                                        conn.commit()

                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fifth = ? WHERE CustomerID=?",
                                                       (seat_selected, custID))
                                        conn.commit()

                                        cursor.execute("UPDATE Seating_FifthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                                       (seat_selected,))
                                        conn.commit()
                                    else:
                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fifth = ? WHERE CustomerID=?",
                                                       (seat_selected, custID))
                                        conn.commit()

                                        cursor.execute("UPDATE Seating_FifthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                                       (seat_selected,))
                                        conn.commit()

                                elif perfDate == '04/10/20':
                                    cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                                    custID_match_fourth_fetch = cursor.fetchall()
                                    custID_match_fourth_list = [x[0] for x in custID_match_fourth_fetch]

                                    if seat_selected != custID_match_fourth_list[0]:
                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fourth = ? WHERE CustomerID=?",
                                                       (custID_match_fourth_list[0], custID))
                                        conn.commit()

                                        cursor.execute("UPDATE Seating_FourthOct SET StateOfSeat='FREE' WHERE SeatID=?",
                                                       (custID_match_fourth_list[0],))
                                        conn.commit()

                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fourth = ? WHERE CustomerID=?",
                                                       (seat_selected, custID))
                                        conn.commit()

                                        cursor.execute("UPDATE Seating_FourthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                                       (seat_selected,))
                                        conn.commit()
                                    else:
                                        cursor.execute("UPDATE CustomerBooking SET SeatID_Fourth = ? WHERE CustomerID=?",
                                                       (seat_selected, custID))
                                        conn.commit()

                                        cursor.execute("UPDATE Seating_FourthOct SET StateOfSeat='TAKEN' WHERE SeatID=?",
                                                       (seat_selected,))
                                        conn.commit()

                                cursor.execute("UPDATE CustomerBooking SET fname=? WHERE CustomerID=?", (fname, custID))
                                conn.commit()

                                cursor.execute("UPDATE CustomerBooking SET surname=? WHERE CustomerID=?", (surname, custID))
                                conn.commit()

                                cursor.execute("UPDATE CustomerBooking SET phoneN=? WHERE CustomerID=?", (phoneN, custID))
                                conn.commit()

                                cursor.execute("UPDATE CustomerBooking SET custType=? WHERE CustomerID=?", (custType, custID))
                                conn.commit()

                                # Adding up the Customer prices properly.
                                # Fetch the SeatIDs that have a customer who has purchased a seat on any given day.
                                seatID_finder_sixth = cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                                seatID_finder_sixth_fetch = cursor.fetchall()
                                seatID_finder_sixth_list = [x[0] for x in seatID_finder_sixth_fetch]
                                seatID_finder_sixth_found = seatID_finder_sixth_list

                                seatID_finder_fifth = cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                                seatID_finder_fifth_fetch = cursor.fetchall()
                                seatID_finder_fifth_list = [x[0] for x in seatID_finder_fifth_fetch]
                                seatID_finder_fifth_found = seatID_finder_fifth_list

                                seatID_finder_fourth = cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking WHERE CustomerID=?", (custID,))
                                seatID_finder_fourth_fetch = cursor.fetchall()
                                seatID_finder_fourth_list = [x[0] for x in seatID_finder_fourth_fetch]
                                seatID_finder_fourth_found = seatID_finder_fourth_list

                                # Differentiating the different customer status' and assigning them their respective price value
                                price = 0
                                # If the price found on the database is NULL (maybe the customer didnt book on this day, but on another),
                                # then try to find a price on the next day.
                                if seatID_finder_sixth_list[0] != "":
                                    # Add up the prices relative to their respective customer statuses.
                                    if custType == 'REGULAR':
                                        price += 10
                                    elif custType == 'REDUCED':
                                        price += 5
                                    else:
                                        price += 0

                                    if seatID_finder_fifth_list[0] != "":
                                        if custType == 'REGULAR':
                                            price += 10
                                        elif custType == 'REDUCED':
                                            price += 5
                                        else:
                                            price += 0

                                        if seatID_finder_fourth_list[0] != "":
                                            if custType == 'REGULAR':
                                                price += 10
                                            elif custType == 'REDUCED':
                                                price += 5
                                            else:
                                                price += 0
                                        else:
                                            pass
                                    else:
                                        if seatID_finder_fourth_list[0] != "":
                                            if custType == 'REGULAR':
                                                price += 10
                                            elif custType == 'REDUCED':
                                                price += 5
                                            else:
                                                price += 0
                                        else:
                                            pass


                                else:
                                    # If the customer didn't book on the sixth, they may have booked on the fifth. checks that.
                                    if seatID_finder_fifth_list[0] != "":
                                        if custType == 'REGULAR':
                                            price += 10
                                        elif custType == 'REDUCED':
                                            price += 5
                                        else:
                                            price += 0

                                        if seatID_finder_fourth_list[0] != "":
                                            if custType == 'REGULAR':
                                                price += 10
                                            elif custType == 'REDUCED':
                                                price += 5
                                            else:
                                                price += 0
                                        else:
                                            pass

                                    else:
                                        # If they haven't booked on the fourth, that is impossible due to the previous validation check.
                                        if seatID_finder_fourth_list[0] != "":
                                            if custType == 'REGULAR':
                                                price += 10
                                            elif custType == 'REDUCED':
                                                price += 5
                                            else:
                                                price += 0
                                        else:
                                            pass
                                # Updates database according to the checks above.
                                cursor.execute("UPDATE CustomerBooking SET price=? WHERE CustomerID=?", (price, custID))
                                conn.commit()
                                # Updates the management information and listbox of seats available.
                                self.refreshManagementInfo()
                                self.listboxUpdate()
                                
                                # Fetching database for values to update treeview.
                                cursor.execute("SELECT CustomerID FROM CustomerBooking WHERE SeatID_Sixth!='' OR SeatID_Fifth!='' OR SeatID_Fourth!=''")
                                tv_custID_fetch = cursor.fetchall()
                                tv_custID_list = [x[0] for x in tv_custID_fetch]
                                tv_custID = tv_custID_list

                                cursor.execute("SELECT SeatID_Sixth FROM CustomerBooking")
                                tv_6th_seatID_fetch = cursor.fetchall()
                                tv_6th_seatID_list = [x[0] for x in tv_6th_seatID_fetch]
                                tv_6th_seatID = tv_6th_seatID_list

                                cursor.execute("SELECT SeatID_Fifth FROM CustomerBooking")
                                tv_5th_seatID_fetch = cursor.fetchall()
                                tv_5th_seatID_list = [x[0] for x in tv_5th_seatID_fetch]
                                tv_5th_seatID = tv_5th_seatID_list

                                cursor.execute("SELECT SeatID_Fourth FROM CustomerBooking")
                                tv_4th_seatID_fetch = cursor.fetchall()
                                tv_4th_seatID_list = [x[0] for x in tv_4th_seatID_fetch]
                                tv_4th_seatID = tv_4th_seatID_list

                                cursor.execute("SELECT fname FROM CustomerBooking")
                                tv_fname_fetch = cursor.fetchall()
                                tv_fname_list = [x[0] for x in tv_fname_fetch]
                                tv_fname = tv_fname_list

                                cursor.execute("SELECT surname FROM CustomerBooking")
                                tv_surname_fetch = cursor.fetchall()
                                tv_surname_list = [x[0] for x in tv_surname_fetch]
                                tv_surname = tv_surname_list

                                cursor.execute("SELECT phoneN FROM CustomerBooking")
                                tv_phoneN_fetch = cursor.fetchall()
                                tv_phoneN_list = [x[0] for x in tv_phoneN_fetch]
                                tv_phoneN = tv_phoneN_list

                                cursor.execute("SELECT custType FROM CustomerBooking")
                                tv_custType_fetch = cursor.fetchall()
                                tv_custType_list = [x[0] for x in tv_custType_fetch]
                                tv_custType = tv_custType_list

                                cursor.execute("SELECT price FROM CustomerBooking")
                                tv_price_fetch = cursor.fetchall()
                                tv_price_list = [x[0] for x in tv_price_fetch]
                                tv_price = tv_price_list

                                # Inserting values into treeview.
                                for k in self.treeview.get_children():
                                    self.treeview.delete(k)

                                for i in range(len(tv_custID)):
                                    try:
                                        self.treeview.insert('', tk.END,
                                                             values=(tv_custID[i], tv_6th_seatID[i], tv_5th_seatID[i], tv_4th_seatID[i],
                                                                     tv_fname[i], tv_surname[i], tv_phoneN[i], tv_custType[i], tv_price[i]))
                                        i += 1
                                    except IndexError:
                                        self.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', ''))
                                        i += 1
                                    self.treeview.pack(pady=2, padx=2)
                                for col in self.columns:
                                    self.treeview.heading(col, text=col,
                                                          command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))
        # Shows error box if the user has not selected a seat yet.
        except Exception:
            messagebox.showerror('Seat Selection Error', 'Please Select a Seat')

    ###


### Driver Code: Runs code above
def main():
    root = tk.Tk()
    app = Notebook(root)
    root.mainloop


if __name__ == "__main__":
    main()
