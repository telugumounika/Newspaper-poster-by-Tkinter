#newspaper
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
root= tk.Tk()
root.geometry("900x900")
root.minsize(300,200)
bg = Image.open("background.png")
bg = bg.resize((1600, 900), Image.LANCZOS)

bg_photo = ImageTk.PhotoImage(bg)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
letter=tk.Label(root,text="DAILY NEWS",font=("bold",18),bg="#e9dec1")
letter.pack(side="top",padx=5, pady=5)
head=tk.Label(root,text="Todays Top Headlines- 18 June 2026 ",font=("bold",16),bg="#e9dec1")
head.pack()

news_frame=tk.Frame(root)
news_frame.pack(side="left",padx=20,pady=20)

content=tk.Label(news_frame,text='''IN INDIA NEWS:
1. Prime Minister Narendra Modi addresses VivaTech 2026 in Paris, emphasizing that technology and artificial intelligence should be democratized 
and made accessible for everyone, not just a few nations or companies.
2. JoSAA Counselling 2026: The registration window for engineering admissions to IITs, NITs, IIITs, and other institutes is reaching its 
deadline, with students advised to complete their applications promptly.
3. Education Ministry reviews NEET-UG re-exam preparations. Union Education Minister Dharmendra Pradhan chaired a high-level meeting to 
review arrangements ahead of the upcoming examination.
4. Delhi High Court questions the Centre over the Telegram ban, asking how the rights of millions of users can be curtailed while hearing 
the matter related to NEET-UG information sharing.
5. NSE moves closer to its much-awaited IPO. The National Stock Exchange has filed updated documents, and investors are closely 
watching one of India's biggest potential public offerings.
6. Indian funds in Swiss banks declined by 8 percent in 2025, although customer deposits increased significantly, according to the
latest banking data.
7. PM-Kisan Scheme: The 23rd installment of the PM-Kisan scheme is scheduled for release on June 20, with thousands of crores 
expected to be transferred to eligible farmers.
8. Bhogapuram International Airport (Andhra Pradesh) has announced provisional user development fees, marking another step toward 
the airport's operational launch.
9. Indian stock market: Analysts are watching stocks such as Bharat Electronics (BEL), Canara Bank, TVS Motor, Tata Motors, and 
JSW Steel after fresh brokerage recommendations and market developments.
10. Technology and AI remain a national focus, with discussions on AI policy, semiconductor development, and digital innovation 
continuing alongside India's growing role in global technology initiatives.''',font=("Times New Roman",10),wraplength=850,justify="left",bg="#e9dec1",bd=3,relief="ridge")

content1=tk.Label(news_frame,text='''IN INTERNATIOANL NEWS:
1.The United States and Iran have signed an interim agreement that starts a 60-day negotiation period aimed at reaching a permanent 
peace deal. The agreement includes reopening the Strait of Hormuz to maritime traffic,while broader issues such as sanctions.
2.Ukraine carried out one of its largest drone attacks on Moscow since the war began. Ukrainian President Volodymyr Zelenskyy warned 
that continued attacks on Ukraine would bring stronger responses, while NATO and European leaders discussed additional military .
3.The Bank of England decided to keep its benchmark interest rate at 3.75%, citing uncertainty caused by geopolitical tensions and 
energy markets. The central bank also lowered its inflation forecast while continuing to monitor economic conditions.
4.Artificial Intelligence continues to be a major topic at international technology events, including VivaTech 2026 in Paris. 
Governments and technology companies are discussing AI governance, innovation, ethical development, and international cooperation.
5.Despite diplomatic efforts in the region, military operations and cross-border tensions between Israel and Lebanon remain a concern,
with international leaders urging restraint and humanitarian support.
6. European countries are discussing increased defense spending and closer military cooperation through NATO in response to ongoing security 
concerns related to the war in Ukraine.
7. Oil prices remain under close watch after easing geopolitical tensions in the Middle East. Analysts say developments around the Strait of 
Hormuz continue to influence global energy prices and inflation.
8.The European Union has approved stricter migration policies aimed at improving border management while addressing humanitarian concerns 
and asylum procedures.
9. The World Food Programme has warned that acute hunger could worsen in several global hotspots and has welcomed additional international 
funding to support humanitarian operations.
10.The FIFA World Cup group stage continues today with several important matches, including England vs. Croatia, as teams compete for 
places in the knockout rounds.
''',font=("Georgia",10),wraplength=850,justify="left",bg="#e9dec1",bd=3,relief="ridge")

content.pack(anchor="nw")
content1.pack(anchor="sw")

right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=20, pady=20)

image = Image.open("2.png")
image = image.resize((600, 325), Image.LANCZOS)
photo1 = ImageTk.PhotoImage(image)

label1 = tk.Label(right_frame, image=photo1,bd=3,relief="sunken")
label1.pack(pady=10,anchor="ne",side="top")

image2 = Image.open("5.png")
image2 = image2.resize((600, 325), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(image2)

label2 = tk.Label(right_frame, image=photo2,bd=3,relief="sunken")
label2.pack(pady=10,anchor="se")

created_by=tk.Label(news_frame,text="Developed by : Mounika Ramya  ! Powered by Tkinter ",font=("Times new roman",9))
created_by.pack(side="bottom")
root.mainloop()

