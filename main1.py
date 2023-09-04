from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    full_name,set_full_name = use_state("")
    Username,set_Username=use_state("")
    Email,set_Email=use_state("")
    Date_of_birth,set_Date_of_birth=use_state("")
    Gender,set_Gender=use_state("")
    password, set_password = use_state(0)
    Contact_Number,set_Contact_Number = use_state("")  # Set a default country code
    I_am_a,set_I_am_a=use_state("")



    def mysubmit(event):
        newtodo = {"full_name": full_name,"Username":Username,"Email":Email,"password": password,"Date_of_birth":Date_of_birth, "Gender":Gender, "Contact_Number":Contact_Number, "I am a":I_am_a}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  # function call to login function using the submitted data

    # looping data from alltodo to show on web



    list = []
    def handle_event(event):
        print(event)
    
 #adding background image      
    return html.div(
      {"style": 
                    
          { "background-size": "cover",
            "background_image":"url(https://images.unsplash.com/photo-1504333638930-c8787321eee0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80)", 
            "margin": "0px",
            "padding": "50px",
            "size":"1920x1190px",
            "Resolution":"1080",

            }
                    

           },


        ## creating form for submission
    html.form(
        # Heading 1
               {"on submit": mysubmit},
                html.b(html.h1(
                    {"style": {"font-family": "Brush Script MT", "font-size": "90px","alignItems": "center","color":"#FFFFFF"}}
                    ,"Space Rovers",)),
                html.br(), 
                
        #Heading 2
        
                html.b(html.h2(
                    {"style": {"font-family": "Monotype Corsiva", "font-size": "20px","alignItems": "align","color":"hsl(0, 0%, 80%)"}}
                    ,"Let's learn more about SPACE")),

        #Heading 3
        
                    html.b(html.h3(
                    {"style": {"font-family": "Bodoni_MT", "font-size": "40px","alignItems": "center","color":"hsl(0, 0%, 80%)"}}
                    ,'Sign-Up')),
        
        #creating the input features 
        
                html.label(
                    {"style": {"font-family": "Monotype Corsiva", "font-size": "15px","alignItems": "center","color":"#FFFFFF"}}
                    ,"full name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Full name",
                        "on_change": lambda event: full_name(event["target"]["value"]),
                    }
                    ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Monotype Corsiva", "font-size": "15px","color":"#FFFFFF"}}
                    ,"Username"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Username",
                        "on_change": lambda event: set_Username(event["target"]["value"]),
                    }
                    ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Monotype Corsiva", "font-size": "15px","color":"#FFFFFF"}}
                    ,"Email"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Email",
                        "on_change": lambda event: set_Email(event["target"]["value"]),
                    }
                ),
                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Monotype Corsiva", "font-size": "15px","color":"#FFFFFF"}}
                    ,"Date of birth"),
                html.br(),
                html.input(
                    {
                        "type": "date",
                        "placeholder": "Date_of_birth",
                        "on_change": lambda event: set_Date_of_birth(event["target"]["value"]),
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Monotype Corsiva", "font-size": "15px","color":"#FFFFFF"}}
                    ,"Password"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Password",
                        "on_change": lambda event: set_password(event["target"]["value"]),
                    }
                ),
              
              
                html.br(),
                html.p(""),
                html.select(
                    {
                    "on_blur": lambda event: set_Gender(event["target"]["value"]),
                    "style": {
                    "font-family": "Monotype Corsiva",
                    "font-size": "15px",
                    
                    "color": "#000000",
                    "type":"text"
                            },
                    },
               [
                html.option({"value": "", "disabled": "disabled", "selected": "selected"}, "Gender"),
                html.option({"value": "male"}, "Male"),
                html.option({"value": "female"}, "Female"),
                html.option({"value": "other"}, "Other"),
               ],
                ),
                
                html.br(),
                html.p(""),    
                html.label(
                    {
                    "style": {
                    "font-family": "Monotype Corsiva",
                    "font-size": "15px",
                    "color": "#FFFFFF",
                            }
                    },
                 "Contact Number"
                ),
                html.br(),
                html.input(
                    {
                    "type": "text",  #text input for the contact number
                    "placeholder": "Contact Number",
                    "on_change": lambda event: set_Contact_Number(event["target"]["value"]),
                    }
                ),

                html.br(),
                html.p(""),
                html.select(
                    {
                    "on_focus": lambda event: set_I_am_a(event["target"]["value"]),
                    "style": {
                    "font-family": "Monotype Corsiva",
                    "font-size": "15px",
                    
                    "color": "#000000",
                            },
                    },
               [
                html.option({"value": "", "disabled": "disabled", "selected": "selected"}, "I am"),
                html.option({"value": "Student"}, "Student"),
                html.option({"value": "Teacher"}, "Teacher"),
                html.option({"value": "other"}, "Other"),
               ],

                ),
                
                html.br(),
                html.p(""),
                # creating submit button on form
                html.button(
                    {
                        "type": "Sign up",
                        "on_click":event(lambda event:mysubmit(event)),
                    },
                    "Sign up",
                ),
            # add a button
                html.button(
                {
                    "type": "Cancel",
                    "on_click":lambda event: full_name("") and set_Username("") and set_Email("") and set_Date_of_birth and set_password(0) and set_Gender("") and set_I_am_a(""),
                },
                "Cancel",
                ),
                ),
    html.ul(list), 
    )

app = FastAPI()

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI

app=FastAPI()

uri = "mongodb+srv://Admin678:admin678@reactpy-task01.wnveil8.mongodb.net/"
# Create a new client and connect to the server
client=MongoClient(uri, server_api=ServerApi("1"))
DB=client["reactpy"]
collection=DB["main"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



def login(
    login_data: dict,
):  # removed async, since await makes code execution pause for the promise to resolve anyway. doesnt matter.
    full_name= login_data["first_name"]
    Username=login_data["Username"]
    Email=login_data["Email"]
    Date_of_birth=login_data["Date of birth"]
    Gender=login_data["Gender"]
    password = login_data["password"]
    Contact_Number = login_data["Contact Number"]
    I_am_a = login_data["I am a"]
    # Create a document to insert into the collection
    document = {"full_name": full_name,"Username":Username,"Email":Email,"Date_of_birth":Date_of_birth, "password": password,"Gender":Gender, "Contact Number":Contact_Number,"I am a":I_am_a }
    # logger.info('sample log message')
    print(document)

    # Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "Login successful"}

configure(app, MyCrud)