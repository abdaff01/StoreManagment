import tkinter
from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Store:

    def __init__(self,root):
        self.root = root
        self.root.title("Store Management System")
        self.root.geometry("1350x950+0+0")
        self.root.configure(background='powder blue')


        #=================Variables===================

        ProductType = StringVar()
        ProductID = StringVar()
        ProductName = StringVar()
        Category = StringVar()
        Quantity = IntVar()
        ProductSize = StringVar()
        ProductColor = StringVar()
        QualityNote = StringVar()
        SupplierName = StringVar()
        SupplierID = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        ZipCode = StringVar()
        PhoneNumber = IntVar()
        ProductRank = StringVar()

        def iRest():
            ProductType.set("")
            ProductID.set("")
            ProductName.set("")
            Category.set("")
            Quantity.set("")
            ProductSize.set("")
            ProductColor.set("")
            QualityNote.set("")
            SupplierName.set("")
            SupplierID.set("")
            Address1.set("")
            Address2.set("")
            ZipCode.set("")
            PhoneNumber.set("")
            ProductRank.set("")

        def iDelete():
            iRest()
            self.txtDisplayR.delete("1.0", END)

        def iExit():
            iExit = tkinter.messagebox.askyesno("Store Management System", "Confirm if you want to exist")
            if iExit>0:
                root.destroy()
                return

        def iDisplayData():
            self.txtDisplayR.insert(END, "\t"+ ProductType.get()+"\t\t"+ProductID.get()+
                                    "\t"+Category.get()+"\t"+ProductName.get()+"\t"+Quantity.get()
                                    +"\t"+ProductSize.get()+"\t"+ProductColor.get()+"\n")

        def iReceipt():
            self.txtDisplayR.insert(END,'Product Type: \t\t'+ ProductType.get()+"\n")
            self.txtDisplayR.insert(END,'Product ID: \t\t'+ ProductID.get()+"\n")
            self.txtDisplayR.insert(END,'Category: \t\t'+ Category.get()+"\n")
            self.txtDisplayR.insert(END,'Product Name: \t\t'+ ProductName.get()+"\n")
            self.txtDisplayR.insert(END,'Quantity: \t\t'+ Quantity.get()+"\n")
            self.txtDisplayR.insert(END,'Product Size: \t\t'+ ProductSize.get()+"\n")
            self.txtDisplayR.insert(END,'Product Color: \t\t'+ ProductColor.get()+"\n")



        #=============Frame===========================

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=23, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame, width=39,font=('arial', 40, 'bold'), padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Product details:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Supplier details")
        DataFrameRIGHT.pack(side=RIGHT)

        #==========================Widget LEFT=====================#

        self.lblMemberType = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Product Type:",
                                   padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'), state="readonly",
                                          textvariable=ProductType, width=23)
        self.cboMemberType['value'] = ('Product 1', 'Product 2')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)


        self.lblProductID = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Product ID:",
                                   padx=2, pady=2)
        self.lblProductID.grid(row=1, column=0, sticky=W)
        self.txtProductID = Entry(DataFrameLEFT, font=('arial', 12, "bold"),textvariable=ProductID, width=25)
        self.txtProductID.grid(row=1, column=1)

        self.lblCategory = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Category:",
                                  padx=2, pady=2)
        self.lblCategory.grid(row=2, column=0)
        self.txtCategory = Entry(DataFrameLEFT, font=('arial', 12, "bold"),textvariable=Category, width=25)
        self.txtCategory.grid(row=2, column=1)

        self.lblProductName = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Product Name:",
                                  padx=2, pady=2)
        self.lblProductName.grid(row=3, column=0)
        self.txtProductName = Entry(DataFrameLEFT, font=('arial', 12, "bold"),textvariable=ProductName, width=25)
        self.txtProductName.grid(row=3, column=1)

        self.lblQuantity = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Quantity:",
                                  padx=2, pady=2)
        self.lblQuantity.grid(row=4, column=0)
        self.txtQuantity = Entry(DataFrameLEFT, font=('arial', 12, "bold"),textvariable=Quantity, width=25)
        self.txtQuantity.grid(row=4, column=1)

        self.lblSize = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Product Size:",
                                  padx=2, pady=2)
        self.lblSize.grid(row=5, column=0)
        self.txtSize = Entry(DataFrameLEFT, font=('arial', 12, "bold"),textvariable=ProductSize, width=25)
        self.txtSize.grid(row=5, column=1)

        self.lblColor = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Product Color:",
                                  padx=2, pady=2)
        self.lblColor.grid(row=6, column=0)
        self.txtColor = Entry(DataFrameLEFT, font=('arial', 12, "bold"),textvariable=ProductColor, width=25)
        self.txtColor.grid(row=6, column=1)

        self.lblRank = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Product Rank:",
                                  padx=2, pady=2)
        self.lblRank.grid(row=7, column=0)

        self.cboRank = ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'), state="readonly",
                                          textvariable=ProductRank,width=23)
        self.cboRank['value'] = ('Rank A', 'Rank B')
        self.cboRank.current(0)
        self.cboRank.grid(row=7, column=1)

        self.lblQualityNote = Label(DataFrameLEFT, font=('arial', 12, "bold"), text="Quality Note:",
                                  padx=2, pady=2)
        self.lblQualityNote.grid(row=8, column=0)
        self.txtQualityNote = tkinter.Text(DataFrameLEFT, width=25, height=3, font=('arial', 12, "bold"))
        self.txtQualityNote.grid(row=8, column=1)

        #==========================Widget RIGHT=====================#

        self.lblSupplierName = Label(DataFrameRIGHT, font=('arial', 12, "bold"), text="Supplier Name:",
                                  padx=2, pady=2)
        self.lblSupplierName.grid(row=0, column=0)
        self.txtSupplierName = Entry(DataFrameRIGHT, font=('arial', 12, "bold"), width=25)
        self.txtSupplierName.grid(row=0, column=1)

        self.lblSupplierID = Label(DataFrameRIGHT, font=('arial', 12, "bold"), text="Supplier ID:",
                                  padx=2, pady=2)
        self.lblSupplierID.grid(row=1, column=0)
        self.txtSupplierID = Entry(DataFrameRIGHT, font=('arial', 12, "bold"), width=25)
        self.txtSupplierID.grid(row=1, column=1)

        self.lblSupplierAdd1 = Label(DataFrameRIGHT, font=('arial', 12, "bold"), text="Address 1:",
                                  padx=2, pady=2)
        self.lblSupplierAdd1.grid(row=2, column=0)
        self.txtSupplierAdd1 = Entry(DataFrameRIGHT, font=('arial', 12, "bold"), width=25)
        self.txtSupplierAdd1.grid(row=2, column=1)

        self.lblSupplierAdd2 = Label(DataFrameRIGHT, font=('arial', 12, "bold"), text="Address 2:",
                                  padx=2, pady=2)
        self.lblSupplierAdd2.grid(row=3, column=0)
        self.txtSupplierAdd2 = Entry(DataFrameRIGHT, font=('arial', 12, "bold"), width=25)
        self.txtSupplierAdd2.grid(row=3, column=1)

        self.lblZipCode = Label(DataFrameRIGHT, font=('arial', 12, "bold"), text="Postal Code:",
                                  padx=2, pady=2)
        self.lblZipCode.grid(row=4, column=0)
        self.txtZipCode = Entry(DataFrameRIGHT, font=('arial', 12, "bold"), width=25)
        self.txtZipCode.grid(row=4, column=1)

        self.lblPhoneNum = Label(DataFrameRIGHT, font=('arial', 12, "bold"), text="Phone Number:",
                                  padx=2, pady=2)
        self.lblPhoneNum.grid(row=5, column=0)
        self.txtPhoneNum = Entry(DataFrameRIGHT, font=('arial', 12, "bold"), width=25)
        self.txtPhoneNum.grid(row=5, column=1)


        #======================================================

        self.lblLabel = Label(FrameDetail, font=('arial', 10, "bold"), pady=8,
                              text="Product Type\t Product ID\t Category\t Product Name\t "
                                   "Quantity\t Product size\t Product Color")
        self.lblLabel.grid(row=0,column=0)

        self.txtDisplayR = Text(FrameDetail, font=('arial', 12, "bold"), width=141,
                                height=4, padx=2, pady=2)
        self.txtDisplayR.grid(row=1, column=0)

        #==================Button===========================#
        self.btnDisplayData = Button(ButtonFrame, text='Display Data', font=('arial', 12, 'bold'),
                                     width=30, bd=4)
        self.btnDisplayData.grid(row=0, column=0)

        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'),
                                     width=30, bd=4,command=iDelete)
        self.btnDelete.grid(row=0, column=1)

        self.btnRest = Button(ButtonFrame, text='Rest', font=('arial', 12, 'bold'),
                                     width=30, bd=4, command=iRest)
        self.btnRest.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'),
                                     width=30, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=3)




if __name__ =='__main__':
    root = Tk()
    application = Store(root)
    root.mainloop()









