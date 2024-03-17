import customtkinter

class SilverCalc:
    """A GUI to calculate current spot price of silver.

    Returns:
        None: 
    """
    from price_getter import get_silver_price
    
    price = get_silver_price()

    def __init__(self):
        customtkinter.set_appearance_mode("dark")

        root = customtkinter.CTk()
        root.geometry("380x320")
        root.title("Silver price per Oz calculator")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Title within GUI window
        label = customtkinter.CTkLabel(master=frame,
                                       text="Silver Price Calculator",
                                       font=("Papyrus", 20))
        label.pack(pady=12, padx=10)

        # Tells user what to input
        input_desc = customtkinter.CTkLabel(master=frame
                                            ,text="Enter Oz of silver:")
        input_desc.pack(pady=12, padx=8)

        input_Oz = customtkinter.StringVar()

        # Number of ounces to calculate
        entry1 = customtkinter.CTkEntry(master=frame,
                                        placeholder_text=
                                        "Enter ounces of silver:",
                                        textvariable=input_Oz)
        entry1.pack(pady=12, padx=10)

        # Button calculates total spot price
        button = customtkinter.CTkButton(master=frame,
                                         text="Calculate Spot Price",
                                         command=lambda: 
                                         self.show_spot_price(self.price
                                                              ,input_Oz.get(
                                                              )))
        button.pack(pady=12, padx=10)

        self.spot_label = customtkinter.CTkLabel(master=frame, text="")
        self.spot_label.pack(pady=12, padx=10)

        root.mainloop()
    
    def total_spot(self, price_per_Oz: str, num_of_Oz: int):
        """Calculates the total spot price of silver for inputted 
            silver in Oz.

        Args:
            price_per_Oz (str): The current price of silver
            num_of_Oz (float): number of ounces currently owned

        Returns:
            float: total price in GBP
        """
        return float(price_per_Oz[1:]) * num_of_Oz
    
    def show_spot_price(self, price_per_Oz, num_of_Oz):
        """Shows the spot price on the GUI

        Args:
            price_per_Oz (str): The current price of silver
            num_of_Oz (float): number of ounces currently owned
        """
        # ensures a number of Oz is entered, telling the user if not.
        try:
            num_of_Oz = float(num_of_Oz)
        except ValueError:
            self.spot_label.configure(text = 
                                      f"A number of Oz must be entered!")
        
        total_spot_price = self.total_spot(price_per_Oz, float(num_of_Oz))
        self.spot_label.configure(
            text=f"Total Spot Price: £{total_spot_price:.2f}")

SilverCalc()