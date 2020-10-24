'''
@author: Bianca Magyar
Created: Oct 23, 2020
Description: Python program using tkinter to calculate 
             the number of IPs between two IPv4 addresses.
Reference: Codewars

'''

from tkinter import Label, Button, Tk, Entry, CENTER, E, W

#runs GUI to get the input to calculate IPv4 range size
def addressrange():
    
    #calculates the number of IP addresses within a range
    #start: string, starting IP address, included
    #end: string, ending IP address, excluded
    #return an int when valid or -1 for an invalid IP
    def ips_between(start, end):
        import ipaddress
        #try to run if valid
        try: 
            #convert IPv4 addresses to integers to subtract
            ip1 = int(ipaddress.IPv4Address(start))
            ip2 = int(ipaddress.IPv4Address(end))
            
            #check starting IP is smaller than ending IP
            if ip2 >= ip1: return ip2 - ip1
            #enter when ip2 < ip1
            else: return -1
        #enter when invalid IP input by user    
        except: return -1
    
    #action for the submit button
    def submit():
        #get entry data, remove extra whitespace from string, and store
        start = (start_entry.get().strip())
        end = (end_entry.get().strip())
        
        #store number of IP addresses in between starting and ending IP address
        count = ips_between(start, end) 
        result = "Range of IP addresses is %d." % (count)
        if count == -1: result = "Invalid. Please try again."
        
        #set up window to display results
        popup = Tk()
        popup.title("Result")
        popup.iconbitmap("IP.ico")
        popup.geometry("220x90")
        result_label = Label(popup, text=result, justify=CENTER, wraplength=200, font=("Calibri", 12))
        result_label.pack(pady=(25,0))
    
    #set up main window
    root = Tk()
    root.title("IP Addresses")
    root.iconbitmap("IP.ico")
    root.geometry("320x215")
    
    #create label for title
    title_label = Label(root, text="Please enter a starting and an ending IP address to calculate the range of IP addresses in between.", wraplength=300, font=("Calibri", 14))
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)
    
    #create label and entry box to prompt and enter starting IP address
    start_label = Label(root, text="Starting IPv4 address:")
    start_label.grid(row=1, column=0, padx=(0, 10), pady=(10,0), sticky=E)
    start_entry = Entry(root, width=20)
    start_entry.grid(row=1, column=1, pady=(10,0), sticky=W)
    
    #create label and entry box to prompt and enter ending IP address
    end_label = Label(root, text="Ending IPv4 address:")
    end_label.grid(row=2, column=0, padx=(0, 10), pady=(10,0), sticky=E)
    end_entry = Entry(root, width=20)
    end_entry.grid(row=2, column=1, pady=(10,0), sticky=W)
    
    #create button to submit data submit
    submit_button = Button(root, text="Submit", command=submit)
    submit_button.grid(row=3, column=1, padx=(0,0), pady=(10,0), ipadx=38, sticky=W)
  
    root.mainloop()

if __name__ == "__main__":    
    #call program
    addressrange()