from pypdf import PdfReader, PdfWriter
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def reading(Pdf_Name,page_no):
        pdf=PdfReader(f"{Pdf_Name}.pdf")
        page_no=pdf.pages[page]
        print(page_no.extract_text())


def merger(pdfs_list,Modified_Pdf_Name):
    merger=PdfWriter()
    for pdf in pdfs_list:
        merger.append(f"{pdf}.pdf")
    with open(f"{Modified_Pdf_Name}.pdf","wb") as f:
        merger.write(f)

def rotate_pdf(rotation,pdf_file_name,modified_Pdf_name):
    reader=PdfReader(f"{pdf_file_name}.pdf")
    writer=PdfWriter()

    for i in range(0,len(reader.pages)):
        pages=reader.pages[i].rotate(rotation)
        writer.add_page(pages)
    with open(f"C:/users/amaar/onedrive/desktop/Pdf Modifier/{modified_Pdf_name}.pdf","wb") as f:
        writer.write(f)

def split_mid(Pdf_Name,Modified_Pdf_Name):
    reader=PdfReader(f"{Pdf_Name}.pdf")
    mid_page=int(len(reader.pages)/2)
    first_half=PdfWriter()
    second_half=PdfWriter()
    for i in range(0,mid_page):
        page=reader.pages[i]
        first_half.add_page(page)
    for i in range(mid_page,len(reader.pages)):
        pages=reader.pages[i]
        second_half.add_page(pages)
    with open(f"{Modified_Pdf_Name}1.pdf","wb") as f:
        first_half.write(f)
    with open(f"{Modified_Pdf_Name}2.pdf","wb") as f:
        second_half.write(f)

def split_user(Pdf_Name,Modified_Pdf_Name):
    reader=PdfReader(f"{Pdf_Name}.pdf")
    writer=PdfWriter()
    print(f"Your given pdf file pages vary from 1 to {len(reader.pages)}")
    start=int(input("\nStarting Page No: "))-1
    end=int(input("Ending Page NO: "))
    for i in range(start,end):
        pages=reader.pages[i]
        writer.add_page(pages)
    with open(f"{Modified_Pdf_Name}.pdf","wb") as f:
        writer.write(f)

def encrypt_pdf(file_name,new_file_name,password):
    reader=PdfReader(f"{file_name}")
    writer=PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open(f"{new_file_name}.pdf","wb") as f:
        writer.write(f)

def decrypt_pdf(file_name,new_file_name,password):
    reader=PdfReader(f"{file_name}.pdf")
    writer=PdfWriter()
    if reader.is_encrypted:
        reader.decrypt(password)
    for page in reader.pages:
        writer.add_page(page)
    with open(f"{new_file_name}.pdf","wb") as f:
        writer.write(f)

string="""This program can perform the following functions:
    1. Read the text of the pdf
    2. Merging the pdf's
    3. Rotating the pages of the pdf
    4. Splitting the pdf
    5. Encryting the pdf
    6. Decrypting the pdf\n"""
print(string)

Operation=int(input("Which operation you want to perform (1-6): "))


if Operation==1:
        Pdf_Name=input("\nEnter the name of the pdf you want to read: ")
        page=int(input("Which page you want to read: "))

        reading(Pdf_Name,page)


elif Operation==2:   
    ask=int(input("\nHow many pdf's you want to merge you can merge upto 5 pdfs: "))
    pdf_list=[]
    match ask:
        case 2:
            for i in range(1,3):
                pdf=input(f"Enter the name of the pdf no. {i}: ")
                pdf_list.append(pdf)
        case 3:     
            for i in range(1,4):
                pdf=input(f"Enter the name of the pdf no. {i}: ")
                pdf_list.append(pdf)

        case 4:
            for i in range(1,5):
                pdf=input(f"Enter the name of the pdf no. {i}: ")
                pdf_list.append(pdf)
        case 5:
            for i in range(1,6):
                pdf=input(f"Enter the name of the pdf no. {i}: ")
                pdf_list.append(pdf)

    Modified_Pdf_Name=input("Enter the name for the modified pdf: ")

    merger(pdf_list,Modified_Pdf_Name)


elif Operation==3:
    pdf_file_name=input(f"\nEnter the name of the pdf file name: ")
    rotation=int(input(f"Rotation; must be the multiple of 90: "))
    modified_pdf_name=input("Name the modified pdf file: ")

    rotate_pdf(rotation,pdf_file_name,modified_pdf_name)


elif Operation==4:
    Pdf_Name=input("\nEnter the name of the pdf file: ")
    Modified_Pdf_Name=input("Enter the name of Modified_Split_Pdf: ")
    ask=input("If you want to split the pdf into half enter 'mid' or enter 'user' for user defined start and end: ")

    if (ask=="mid"):
        split_mid(Pdf_Name,Modified_Pdf_Name)
    if (ask=="user"):
        split_user(Pdf_Name,Modified_Pdf_Name)


elif Operation==5:
    Pdf_Name=input("\nEnter the name of the pdf you want to encrypt or decrypt: ")
    password=input("Enter the password: ")
    New_Pdf_Name=input("Name for the encrypted Pdf: ")

    encrypt_pdf(Pdf_Name,New_Pdf_Name,password)

elif Operation==6:
    Pdf_Name=input("\nEnter the name of the pdf you want to encrypt or decrypt: ")
    password=input("Enter the password: ")
    New_Pdf_Name=input("Name for the decrypted Pdf: ")
    
    decrypt_pdf(Pdf_Name,New_Pdf_Name,password)

else:
    print("Invalid Command")