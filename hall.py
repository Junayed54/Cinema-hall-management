class Star_Cinama:
    hall_list = []
    def entry_hall(self, hall):
        flag = 1
        for i in self.hall_list:
            if i[2]==hall.hall_no:
                print("Hall already installed")
                flag=0
                break
        if flag==1:
            self.hall_list.append(hall.new_hall)
            
        
        
        
    


class Hall(Star_Cinama):
    def __init__(self,rows, cols, hall_no):
        self.seats ={} # id: row/cols
        self.show_list = [] #tuple
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.new_hall = (rows, cols, hall_no)
        
    

    def entry_show(self, id, movie_name, time):
        self.id = id
        self.movie_name = movie_name
        self.time = time
        new_show = (id, movie_name, time)
        self.show_list.append(new_show)
        seat_list = [[False]*self.cols for _ in range(self.rows)]
        self.seats[id] = seat_list
    

    def book_seats(self):
        customer_name = input("ENTER CUSTOMER NAME: ")
        phone_number = input("ENTER CUSTOMER PHONE NUMBER: ")
        show_id = input("ENTER SHOW Id: ")
        flag1 = 0
        for id in self.show_list:
            if show_id==id[0]:
                Tickets = input("ENTER NUMBER OF TICKETS: ")

                flag = 0
                seat_booked = []
                for i in range(int(Tickets)):
                    seat = input('ENTER SEAT NO: ')
                    seat_row = ord(seat[0])-65
                    if seat[1]>='0' and seat[1]<='9':
                        seat_col = int(seat[1])
                    else:
                        print("Wrong seat no!")
                        print("")
                        continue
                    if self.seats[show_id][seat_row][seat_col]==False and seat_row<len(self.seats[show_id]) and seat_col<len(self.seats[show_id][0]):
                        self.seats[show_id][seat_row][seat_col] = True
                        flag += 1
                        seat_booked.append(seat)
                    

                    elif self.seats[show_id][seat_row][seat_col]==True and seat_row<len(self.seats[show_id]) and seat_col<len(self.seats[show_id][0]):
                        print("______________________________________")
                        print("")
                        print(f"THESE SEATS WERE BOOKED - {seat}")
                        print("______________________________________")
                        print("")
                    
                    else:
                        print("Seat no. didn't match")
            
                if flag>=1:
                    print("")
                    print("###### TICKET BOOKED SUCCESSFULLY! ######")
                    print("")
                    print("_________________________________________________________________________________________")
                    print("")
                    print(f"NAME: {customer_name}")
                    print(f"PHONE NUMBER:  {phone_number}")
                    print(f'MOVIE NAME: {id[1]: <20}SHOW ID: {id[0]: <10}MOVIE TIME: {id[2]}')
                    seat_booked = tuple(seat_booked)
                    print(f'TICKETS: {tuple(seat_booked)}')
                    print("")
                    print("_________________________________________________________________________________________")
                    print("")
                    flag1 += 1
                    break

        if flag1==0:
            print('________________________________________')
            print("")
            print("Id didn't match with any show!")
            print('________________________________________')
            print("")
            



    
    def view_show_list(self):
        print("Here are the running shows: ")
        Id = 'ID'
        movieName = 'MOVIE NAME'
        time = 'TIME'
        print('___________________________________________________________________________________________________')
        print("")
    
        for show in self.show_list:
            print(f'MOVIE NAME: {show[1]: <30}SHOW ID: {show[0]:<20}TIME: {show[2]}')

        
        print('___________________________________________________________________________________________________')
        print("")

    def view_available_seats(self):
        show_of_id = input("ENTER THE SHOW ID: ")
        flag = 0
        for show in self.show_list:
            if show_of_id==show[0]:
                flag=1
                print("")
                print(f'MOVIE NAME: {show[1]: <20}TIME: {show[2]}')
                print('X for already booked seats')
                print("____________________________________________________")
                print("")
                for key in self.seats:
                    if show_of_id==key:
                        for i, x in enumerate(self.seats[key]):
                            for y, val in enumerate(x):
                                if val==True:
                                    ins = ' X'
                                    print(f'{ins: <11}', end = '')
                                else:
                                    print(f'{chr(65+i)}{y: <10}', end='')
                            print("")
        
                print("____________________________________________________")
                print("")
                break
        if flag==0:
            print("Id didn't match with any show!")
            print("")
                








riya_Mohol = Hall(5, 5, 1377)
new_one = Star_Cinama()
new_one.entry_hall(riya_Mohol)
riya_Mohol.entry_show("1st","DIRILIS ERTTUGRUL", 'Nov 30 2022 10:00 PM')
riya_Mohol.entry_show('2nd', 'DIRILIS USMAN', 'Nov 30 2022 08:00 PM')
newtwo = Hall(5, 5, 1377)
new_one.entry_hall(newtwo)





while True:
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    option = int(input("ENTER OPTION: "))
    if option==1:
        riya_Mohol.view_show_list()
    elif option==2:
        riya_Mohol.view_available_seats()
    elif option==3:
        riya_Mohol.book_seats()
    else:
        "ENTER THE RIGHT OPTION!"
        print("")
        

    