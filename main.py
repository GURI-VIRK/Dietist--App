from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatIconButton, MDFlatButton
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivymd.uix.snackbar import Snackbar
import requests
import json

# dropdown1 --activity level
# dropdown 2 --weightgain or fat loss per week
# dropdown 3 ---muscle building or fat loss
# page having name (data) is a breakfast page
# breakfast--simple functiom
# lunch func ends with l
# brunch func ends --b
# snacks func ends-- s
# dinner func ends --d

Window.size = (400, 600)

username_input = """
ScreenManager:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    Mainscreen:
    Dcalories:
    Macro:
    Bmi:
    Bmr:
    Repmax:
    Brunch:
    Lunch:
    Dinner:
    Snacks:
    Data:
    Target:

<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:'&'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.7}
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.5}
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.3,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.7,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:

        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.username_changer() 


    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'

<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'

<Mainscreen>:
    name: 'main'
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            left_action_items: [["arm-flex", lambda x: app.khalifunc()]]
            title: 'DIETist'
            elevation: 10

        MDBottomNavigation:
            text_color_normal: 1, 0, 0, 1
            panel_color: .2, .2, .2, 1

            MDBottomNavigationItem:
                name: 'screen1'
                text: 'Home'
                icon: 'home-flood'

                MDLabel:
                    id:username_info
                    text:'Hello Main'
                    font_style:'H3'
                    halign:'center'
                    theme_text_color: "Custom"
                    text_color: 224, 191, 184,1
                    pos_hint: {"center_x": .5, "center_y": .86}

                MDLabel:
                    text: 'Using DIETist you can design your own diet plan based on calories required by your body ,follow along step by step '
                    font_style:'H5'
                    halign: "center"
                    theme_text_color: "Error"
                    pos_hint: {"center_x": .5, "center_y": .55}

                MDLabel:
                    text: 'Lets begin with the first step by calculating your BMR'
                    font_style:'H6'
                    halign: "center"
                    theme_text_color: "Hint"
                    pos_hint: {"center_x": .5, "center_y": .22}

                MDFillRoundFlatButton:
                    text: "Let\'s Get Started"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.13} 
                    on_release: root.manager.current= "bmr"

            MDBottomNavigationItem:
                name: 'screen2'
                text: ' Health Tools'
                icon: 'tools'

                ScrollView: 
                    GridLayout:
                        padding: dp(10)
                        spacing: dp(10)
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height

                        OneLineAvatarIconListItem:
                            text: "Bmr Calculator"
                            on_press: 
                                root.manager.current= "bmr"
                                root.manager.transition.direction= "left"

                            IconLeftWidget:
                                icon: "arm-flex"

                            IconRightWidget:
                                icon: "menu-right"

                        OneLineAvatarIconListItem:
                            text: "Calories Counter"
                            on_press: 
                                root.manager.current= "dcalories"
                                root.manager.transition.direction= "left"

                            IconLeftWidget:
                                icon: "fire"

                            IconRightWidget:
                                icon: "menu-right"

                        OneLineAvatarIconListItem:
                            text: "Diet Tool and Calorie Count"
                            on_press: 
                                root.manager.current= "dcalories"
                                root.manager.transition.direction= "left"

                            IconLeftWidget:
                                icon: "fruit-watermelon"

                            IconRightWidget:
                                icon: "menu-right"

                        OneLineAvatarIconListItem:
                            text: "Macro Calculator"
                            on_press: 
                                root.manager.current= "macro"
                                root.manager.transition.direction= "left"

                            IconLeftWidget:
                                icon: "arm-flex"

                            IconRightWidget:
                                icon: "menu-right"

                        OneLineAvatarIconListItem:
                            text: "BMI Calculator"
                            on_press: 
                                root.manager.current= "bmi"
                                root.manager.transition.direction= "left"

                            IconLeftWidget:
                                icon: "arm-flex"

                            IconRightWidget:
                                icon: "menu-right"

                        OneLineAvatarIconListItem:
                            text: "1RM Calculator"
                            on_press: 
                                root.manager.current= "repmax"
                                root.manager.transition.direction= "left"

                            IconLeftWidget:
                                icon: "weight-lifter"

                            IconRightWidget:
                                icon: "menu-right"

<Macro>
    name:'macro'
    MDBoxLayout:
        orientation: "vertical" 

        MDToolbar:
            title: "Macro Calculator"
            elevation: 10
            left_action_items: [["home", lambda x: app.vapas3()]]

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDTextField:
        id: calinput
        hint_text: "Your Calories"
        helper_text: "Enter number of Cal only"
        helper_text_mode: "on_focus"
        text: ""
        required: True
        size_hint_x: None
        icon: "google-fit"
        text_color: (1, 0, 0, 1)
        line_color: (1, 0, 0, 1)
        mode: "rectangle"
        height: "49dp"
        pos_hint: {"center_x": .5, "center_y": .59}
        width: 200

    MDFloatingActionButton:
        id: macroright
        disabled: True
        icon: 'arrow-right'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: '58sp'
        on_press : 
            root.manager.current= 'target'
            root.manager.transition.direction = 'left'

    MDFloatingActionButton:
        id: macroleft
        icon: 'arrow-left'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '58sp'
        on_press : 
            root.manager.current= 'dcalories'
            root.manager.transition.direction = 'right'

    MDLabel:
        text: 'Step 3 of 3'
        theme_text_color: "Custom"
        halign: "center"
        text_color: 224, 191, 184,1
        pos_hint: {"center_x": .5, "center_y": .2}

    MDLabel:
        text: 'Now Add foods to your meals'
        theme_text_color: "Custom"
        halign: "center"
        text_color: 224, 191, 184,1
        pos_hint: {"center_x": .5, "center_y": .1}

    MDFillRoundFlatButton:
        text: "Calculate Macros"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3} 
        on_release: app.cal_macro()

<Target>
    name:'target'
    MDBoxLayout:
        orientation: "vertical" 

        MDToolbar:
            title: "Calories Counter"
            elevation: 10
            left_action_items: [["home", lambda x: app.vapas4()]]

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height 

                MDProgressBar:
                    id: prog1
                    value: 0
                    min: 0
                    max: 100

                ThreeLineAvatarIconListItem:
                    id: breakf
                    text: "Breakfast"
                    secondary_text: "click to add food items"
                    tertiary_text: "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
                    on_press: 
                        root.manager.current="data"
                        root.manager.transition.direction = 'left'

                    IconLeftWidget:
                        icon: "food-turkey"

                MDProgressBar:
                    id: prog2
                    value: 0

                ThreeLineAvatarIconListItem:
                    id: brunch
                    text: "Brunch"
                    secondary_text: "click to add food items"
                    tertiary_text: "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
                    on_press: 
                        root.manager.current="brunch"
                        root.manager.transition.direction = 'left'

                    IconLeftWidget:
                        icon: "food-turkey"

                MDProgressBar:
                    id: prog3
                    value: 0

                ThreeLineAvatarIconListItem:
                    id: lunch
                    text: "Lunch"
                    secondary_text: "click to add food items"
                    tertiary_text: "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
                    on_press: 
                        root.manager.current="lunch"
                        root.manager.transition.direction = 'left'

                    IconLeftWidget:
                        icon: "food-turkey" 

                MDProgressBar:
                    id: prog4
                    value: 0

                ThreeLineAvatarIconListItem:
                    id: snacks
                    text: "Snacks"
                    secondary_text: "click to add food items"
                    tertiary_text: "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
                    on_press: 
                        root.manager.current="snacks"
                        root.manager.transition.direction = 'left'

                    IconLeftWidget:
                        icon: "food-turkey"

                MDProgressBar:
                    id: prog5
                    value: 0

                ThreeLineAvatarIconListItem:
                    id: dinner
                    text: "Dinner"
                    secondary_text: "click to add food items"
                    tertiary_text: "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
                    on_press: 
                        root.manager.current="dinner"
                        root.manager.transition.direction = 'left'

                    IconLeftWidget:
                        icon: "food-turkey"       

<Repmax>
    name:'repmax'
    MDBoxLayout:
        orientation: "vertical" 

        MDToolbar:
            title: "1Rep Max Calculator"
            elevation: 10
            left_action_items: [["home", lambda x: app.vapas5()]]

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDLabel:
        id:username_info
        text:'Find the Heaviest Weight You can Lift 4-6 Times and Enter Below:'
        font_style:'H6'
        halign:'center'
        theme_text_color: "Custom"
        text_color: 224, 191, 184,1
        pos_hint: {"center_x": .5, "center_y": .83}

    MDTextField:
        id: weightlifted
        hint_text: "Enter Lifted Weight"
        required: True
        size_hint_x: None
        icon: "weight-kilogram"
        text_color: (1, 0, 0, 1)
        line_color: (1, 0, 0, 1)
        mode: "rectangle"
        height: "49dp"
        pos_hint: {"center_x": .5, "center_y": .53}
        width: 200

    MDFillRoundFlatButton:
        text: "Calculate 1RM"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4} 
        on_release: app.repmax()

<Dcalories>
    name:'dcalories'
    MDBoxLayout:
        orientation: "vertical" 

        MDToolbar:
            title: "Daily Needed Calories"
            elevation: 10
            left_action_items: [["home", lambda x: app.vapas5()]]

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDFloatingActionButton:
        id: dcalright
        disabled: True
        icon: 'arrow-right'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: '58sp'
        on_press : 
            root.manager.current= 'macro'
            root.manager.transition.direction = 'left'

    MDFloatingActionButton:
        id: dcalleft
        icon: 'arrow-left'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '58sp'
        on_press : 
            root.manager.current= 'bmr'
            root.manager.transition.direction = 'right'

    MDLabel:
        text: 'Step 2 of 3'
        theme_text_color: "Custom"
        halign: "center"
        text_color: 224, 191, 184,1
        pos_hint: {"center_x": .5, "center_y": .1}

    MDTextField:
        id: bmrinput
        hint_text: "please enter bmr"
        helper_text: "Enter Bmr number only"
        helper_text_mode: "on_focus"
        text: "Bmr"
        required: True
        size_hint_x: None
        icon: "google-fit"
        text_color: (1, 0, 0, 1)
        line_color: (1, 0, 0, 1)
        mode: "rectangle"
        height: "49dp"
        pos_hint: {"center_x": .5, "center_y": .72}
        width: 200

    MDFillRoundFlatButton:
        text: "Calculate Calories"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3} 
        on_release: app.cal_calories_intake()

<Dropdown1>
    Button:
        text: 'sedentary(little or no exercise)'
        size_hint_y: None
        height: 44
        on_release: root.select('sedentary(little or no exercise)')

    Button:
        text: 'lightly(1-3times a week)'
        size_hint_y: None
        height: 44
        on_release: root.select('lightly(1-3times a week)') 

    Button:
        text: 'moderatly(3-5 times a week)'
        size_hint_y: None
        height: 44
        on_release: root.select('moderatly(3-5 times a week)')

    Button:
        text: 'highly active(6-7 times a week)'
        size_hint_y: None
        height: 44
        on_release: root.select('highly active(6-7 times a week)')

    Button:
        text: 'extremly active(1-2 times a day)'
        size_hint_y: None
        height: 44
        on_release: root.select('extremly active(1-2 times a day)')

<Dropdown2>
    Button:
        text: '0.25 Kg per Week'
        size_hint_y: None
        height: 44
        on_release: root.select('0.25 Kg per Week')

    Button:
        text: '0.5 Kg per Week'
        size_hint_y: None
        height: 44
        on_release: root.select('0.5 Kg per Week') 

    Button:
        text: '0.75 Kg per Week'
        size_hint_y: None
        height: 44
        on_release: root.select('0.75 Kg per Week')

    Button:
        text: '1 Kg per Week'
        size_hint_y: None
        height: 44
        on_release: root.select('1 Kg per Week')

<Dropdown3>
    Button:
        text: 'Muscle Building'
        size_hint_y: None
        height: 44
        on_release: root.select('Muscle Building')

    Button:
        text: 'Fat Loss'
        size_hint_y: None
        height: 44
        on_release: root.select('Fat Loss') 

<Dropdown4>
    Button:
        text: 'Muscle Building'
        size_hint_y: None
        height: 44
        on_release: root.select('Muscle Building')

    Button:
        text: 'Fat Loss'
        size_hint_y: None
        height: 44
        on_release: root.select('Fat Loss')

<Dropdown5>
    Button:
        text: 'Squats'
        size_hint_y: None
        height: 44
        on_release: root.select('Squats')

    Button:
        text: 'Deadlift'
        size_hint_y: None
        height: 44
        on_release: root.select('Deadlift')

    Button:
        text: 'Bench Press'
        size_hint_y: None
        height: 44
        on_release: root.select('Bench Press')

    Button:
        text: 'Overhead Press'
        size_hint_y: None
        height: 44
        on_release: root.select('Overhead Press')

<Bmi>
    name: 'bmi'
    MDBoxLayout:
        orientation: "vertical" 

        MDToolbar:
            title: "Body Mass Index"
            elevation: 10
            left_action_items: [["home", lambda x: app.vapas()]]

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height    

    MDTextFieldRound:
        id: weightbmi
        hint_text: "Enter weight in kilograms"
        helper_text: "Enter only in KG"
        helper_text_mode: "on_focus"
        icon_right: "weight-kilogram"
        icon_right_color: (1,0,1,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.43}
        required: True
        size_hint_x: None
        width:265

    MDTextFieldRound:
        id: heightbmi
        hint_text: "Enter height in centimeters"
        helper_text: "enter height in numbers"
        helper_text_mode: "on_focus"
        icon_right: "human-male-height"
        icon_right_color: (1,0,1,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.54}
        required: True
        size_hint_x: None
        width:265

    MDFillRoundFlatButton:
        text: "Calculate BMI"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3} 
        on_release: app.bmi_cal()



<Bmr>
    name: 'bmr'
    MDBoxLayout:
        orientation: "vertical" 

        MDToolbar:
            title: "Basal Metabolic Rate"
            elevation: 10
            left_action_items: [["home", lambda x: app.vapas()]]

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height    

    MDTextFieldRound:
        id: weight
        hint_text: "Enter weight in kilograms"
        helper_text: ""
        icon_right: "weight-kilogram"
        helper_text_mode: "on_focus"
        icon_right_color: (1,0,1,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        required: True
        size_hint_x: None
        width:265

    MDTextFieldRound:
        id: height
        hint_text: "Enter height in centimeters"
        helper_text: "enter height in numbers"
        helper_text_mode: "on_focus"
        icon_right: "human-male-height"
        icon_right_color: (1,0,1,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        required: True
        size_hint_x: None
        width:265


    MDTextFieldRound:
        id: age
        hint_text: "Enter age in years"
        helper_text: "enter age in numbers"
        helper_text_mode: "on_focus"
        icon_right_color: (1,0,1,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        required: True
        size_hint_x:None
        width:265   

    MDTextFieldRound:            
        id: gender
        hint_text: "Gender male/female"
        helper_text: "enter male or female"
        helper_text_mode: "on_focus"
        icon_right: "gender-male-female"
        icon_right_color: (1,0,1,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        required: True
        size_hint_x:None
        width:265

    MDLabel:
        text: 'Step 1 of 3'
        theme_text_color: "Custom"
        halign: "center"
        text_color: 224, 191, 184,1
        pos_hint: {"center_x": .5, "center_y": .1}

    MDFillRoundFlatButton:
        text: "Calculate BMR"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3} 
        on_release: app.show_data()


    MDFloatingActionButton:
        id: bmrright
        disabled: True
        icon: 'arrow-right'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: '58sp'
        on_press : 
            root.manager.current= 'dcalories'
            root.manager.transition.direction = 'left'                 

    MDFloatingActionButton:
        id: bmrleft
        icon: 'arrow-left'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '58sp'
        on_press : 
            root.manager.current= 'main'
            root.manager.transition.direction = 'right'       

<Data>
    name: 'data'
    BoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDToolbar:
            title: "All Foods"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.vapasb()]] 

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDRectangleFlatButton:
        text: "Reset Breakfast"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 0, 0, 1, 1
        pos_hint:{'center_x': 0.5, 'center_y': 0.04}
        on_press: app.reset()

<Lunch>
    name: 'lunch'
    BoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDToolbar:
            title: "All Foods"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.vapasl()]] 

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDRectangleFlatButton:
        text: "Reset Lunch"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 0, 0, 1, 1
        pos_hint:{'center_x': 0.5, 'center_y': 0.04}
        on_press: app.resetl()

<Dinner>
    name: 'dinner'
    BoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDToolbar:
            title: "All Foods"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.vapasd()]] 

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDRectangleFlatButton:
        text: "Reset Dinner"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 0, 0, 1, 1
        pos_hint:{'center_x': 0.5, 'center_y': 0.04}
        on_press: app.resetd()

<Snacks>
    name: 'snacks'
    BoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDToolbar:
            title: "All Foods"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.vapass()]] 

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDRectangleFlatButton:
        text: "Reset Snacks"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 0, 0, 1, 1
        pos_hint:{'center_x': 0.5, 'center_y': 0.04}
        on_press: app.resets()

<Brunch>
    name: 'brunch'
    BoxLayout:
        orientation: "vertical"
        spacing: dp(10)

        MDToolbar:
            title: "All Foods"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.vapasbr()]] 

        ScrollView: 
            GridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                size_hint_y: None
                height: self.minimum_height

    MDRectangleFlatButton:
        text: "Reset Brunch"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 0, 0, 1, 1
        pos_hint:{'center_x': 0.5, 'center_y': 0.04}
        on_press: app.resetb()

"""


class Bmr(Screen):
    pass


class Content(MDBoxLayout):
    pass


class Data(Screen):
    pass


class Mainscreen(Screen):
    pass


class Target(Screen):
    pass


class Dcalories(Screen):
    pass


class Snacks(Screen):
    pass


class Dropdown1(DropDown):
    pass


class Dropdown2(DropDown):
    pass


class Dropdown3(DropDown):
    pass


class Dropdown4(DropDown):
    pass


class Dropdown5(DropDown):
    pass


class Lunch(Screen):
    pass


class Dinner(Screen):
    pass


class Macro(Screen):
    pass


class Brunch(Screen):
    pass


class Bmi(Screen):
    pass


class Repmax(Screen):
    pass


class WelcomeScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


sm = ScreenManager()

sm.add_widget(Bmr(name='bmr'))
sm.add_widget(Data(name='data'))
sm.add_widget(Dcalories(name='dcalories'))
sm.add_widget(Target(name='target'))
sm.add_widget(Snacks(name='snacks'))
sm.add_widget(Dinner(name='dinner'))
sm.add_widget(Lunch(name='lunch'))
sm.add_widget(Brunch(name='brunch'))
sm.add_widget(Mainscreen(name='main'))
sm.add_widget(Macro(name='macro'))
sm.add_widget(Bmi(name='bmi'))
sm.add_widget(Repmax(name='repmax'))
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))


class DIETist(MDApp):
    def build(self):
        self.url = "https://loginfitapp-default-rtdb.firebaseio.com/.json"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        screen = Screen()

        self.el = [0, 0, 0, 0]
        self.elb = [0, 0, 0, 0]
        self.ell = [0, 0, 0, 0]
        self.els = [0, 0, 0, 0]
        self.eld = [0, 0, 0, 0]

        self.username = Builder.load_string(username_input)
        screen.add_widget(self.username)

        self.table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.48}, size_hint=(0.96, 0.8), check=True,
                                 rows_num=63,
                                 column_data=[
                                     ("Qty", dp(30)),
                                     ("Food Item", dp(30)),
                                     ('Calories', dp(30)),
                                     ('Carbs', dp(30)),
                                     ('Protein', dp(30)),
                                     ('Fat', dp(30))],
                                 row_data=[
                                     ("1 Cup", "Oats",
                                      '307', '55',
                                      '11', '5'),
                                     ("3/4 Cup", "Oats",
                                      '225', '41',
                                      '7', '4'),
                                     ("1/2 Cup", "Oats",
                                      '150', '28',
                                      '5', '2.5'),
                                     ("1/4 Cup", "Oats",
                                      '90', '13.5',
                                      '2.5', '1.2'),
                                     ("1 Cup", "Brown rice", '216', '45', '5', '1.8'),
                                     ("3/4 Cup", "Brown rice", '164', '33.3', '3.7', '1.3'),
                                     ("1/2 Cup", "Brown rice", '108', '23', '3', '0.9'),
                                     ("1/4 Cup", "Brown rice", '54', '11.1', '1.26', '0.4'),
                                     ("1 pc", "Brown bread",
                                      '75', '56',
                                      '13', '4.3'),
                                     ("1/2 pc", "Brown bread",
                                      '37', '22.2',
                                      '4.1', '1.5'),
                                     ("100g", "Sweet potato", '86', '20g', '1.6g', '0.1g'),
                                     ("1 pc", "wheat roti",
                                      ' 71 ', '15',
                                      '3', '0.4'),
                                     ("1/2 pc", "wheat roti",
                                      '35.5 ', '7.5',
                                      '1.5', '0.2'),
                                     ("100g", "Wheat pasta", '124', '72', '13.2', '2.5'),
                                     ("1 Cup", "Wheat pasta", '145', '37', '7.5', '0.8'),
                                     ("3/4 Cup", "Wheat pasta", '108', '27.7', '5.6', '0.6'),
                                     ("1/2 Cup", "Wheat pasta", '72', '18.5', '3.7', '0.4'),
                                     ("1/4 Cup", "Wheat pasta", '43', '9.2', '1.9', '0.2'),
                                     ("1 pc", "Banana",
                                      '105', '27',
                                      '1.3', '0.4'),
                                     ("1/2 pc", "Banana",
                                      '53', '13.5',
                                      '0.7', '0.2'),
                                     ("1 pc", "Apple", '95', '25.1', '0.5', '0.3'),
                                     ("1/2 pc", "Apple", '48', '12.5', '0.2', '0.1'),
                                     ("1 pc", "Mango",
                                      '201', '50',
                                      '2.8', '1.3'),
                                     ("1/2 pc", "Mango",
                                      '65', '25',
                                      '1.4', '0.6'),
                                     ("1 pc", "Pear", '102', '15', '0.4', '0.1'),
                                     ("1/2 pc", "Pear", '51', '7.5', '0.2', '0.05'),
                                     ("100g", "Bajra dalia",
                                      '378', '67',
                                      '12', '5'),
                                     ("1 Cup", "Bajra dalia",
                                      '207', '41',
                                      '6', '1.7'),
                                     ("3/4 Cup", "Bajra dalia",
                                      ' 138 ', '30.7',
                                      '4.5', '1.2'),
                                     ("1 Cup", "White chickpeas", '267', '44.7', '14.4', '4.2'),
                                     ("3/4 Cup", "White chickpeas", '214', '33.5', '10.8', '3.1'),
                                     ("1/2 Cup", "White chickpeas", '107', '22.3', '7.2', '2.1'),
                                     ("1/4 Cup", "White chickpeas", '74', '11.1', '3.6', '1.05'),
                                     ("1 Cup", "Kidney beans",
                                      '215', '110',
                                      '43', '1.5'),
                                     ("3/4 Cup", "Kidney beans",
                                      '161', '82.5',
                                      '32.2', '1.1'),
                                     ("1/2 Cup", "Kidney beans",
                                      '107', '55',
                                      '21.5', '0.75'),
                                     ("1/4 Cup", "Kidney beans",
                                      '53', '27.5',
                                      '10.7', '0.3'),
                                     ("1/2Cup", "Black chickpeas ", '147', '24.5', '1.3', '0.4'),
                                     ("1/4Cup", "Black chickpeas ", '73', '12.2', '3.9', '0.1'),
                                     ("1 Cup", "Black chickpeas ", '295', '49', '15.7', '4.9'),
                                     ("100g", "Broccoli",
                                      '34', '6.6',
                                      '2.8', '0.3'),
                                     ("100g", "Spinach", '23', '3.6', '2.9', '0.3'),
                                     ("100g", "Chicken",
                                      '239', '0',
                                      '27', '14'),
                                     ("100g", "Fish", '206', '0', '22', '12'),
                                     ("1 pc", "Eggs",
                                      '18', '0.2',
                                      '3.6', '0'),
                                     ("100g", "Mutton", '294', '0', '25', '21'),
                                     ("240ml", "Milk",
                                      '105', '12',
                                      '8', '2'),
                                     ("100g", "Yogurt", '59', '3.6', '10', '0.4'),
                                     ("100g", "Paneer",
                                      '242', '6.1',
                                      '19.1', '26.9'),
                                     ("100g", "Tofu", '76', '1.9', '8', '4.8'),
                                     ("1 Cup", "Peanuts", '828', '23.5', '37.6', '71.8'),
                                     ("1/2 Cup", "Peanuts", '414', '11.8', '18.8', '35.5'),
                                     ("1/4 Cup", "Peanuts", '207', '5.9', '9.4', '17.9'),
                                     ("1 pc", "Almonds",
                                      '6.94', '0.2',
                                      '0.2', '0.6'),
                                     ("100g", "Cashews", '553', '30', '18', '44'),
                                     ("100g", "Walnuts",
                                      '654', '14',
                                      '15', '65'),
                                     ("1 tbsp", "Peanut butter", '94', '3', '4', '8'),
                                     ("1 tbsp", "Flex seeds",
                                      '37', '2',
                                      '1.3', '3'),
                                     ("100g", "Chia seeds", '486', '42', '17', '31'),
                                     ("1 tbsp", "Sunflower seeds",
                                      '51', '2',
                                      '2', '5'),
                                     ("100g", "Salmon fish", '208', '0', '20', '13'),
                                     ("100g", "Egg boiled",
                                      '77', '0.6',
                                      '6', '5'),
                                     ("1 tbsp", "Olive oil", '119', '0', '0', '14')])

        self.table.bind(on_check_press=self.check_press)

        self.username.get_screen('data').add_widget(self.table)

        self.tablel = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.48}, size_hint=(0.96, 0.8), check=True,
                                  rows_num=63,
                                  column_data=[
                                      ("Qty", dp(30)),
                                      ("Food Item", dp(30)),
                                      ('Calories', dp(30)),
                                      ('Carbs', dp(30)),
                                      ('Protein', dp(30)),
                                      ('Fat', dp(30))],
                                  row_data=[
                                      ("1 Cup", "Oats",
                                       '307', '55',
                                       '11', '5'),
                                      ("3/4 Cup", "Oats",
                                       '225', '41',
                                       '7', '4'),
                                      ("1/2 Cup", "Oats",
                                       '150', '28',
                                       '5', '2.5'),
                                      ("1/4 Cup", "Oats",
                                       '90', '13.5',
                                       '2.5', '1.2'),
                                      ("1 Cup", "Brown rice", '216', '45', '5', '1.8'),
                                      ("3/4 Cup", "Brown rice", '164', '33.3', '3.7', '1.3'),
                                      ("1/2 Cup", "Brown rice", '108', '23', '3', '0.9'),
                                      ("1/4 Cup", "Brown rice", '54', '11.1', '1.26', '0.4'),
                                      ("1 pc", "Brown bread",
                                       '75', '56',
                                       '13', '4.3'),
                                      ("1/2 pc", "Brown bread",
                                       '37', '22.2',
                                       '4.1', '1.5'),
                                      ("100g", "Sweet potato", '86', '20g', '1.6g', '0.1g'),
                                      ("1 pc", "wheat roti",
                                       ' 71 ', '15',
                                       '3', '0.4'),
                                      ("1/2 pc", "wheat roti",
                                       '35.5 ', '7.5',
                                       '1.5', '0.2'),
                                      ("100g", "Wheat pasta", '124', '72', '13.2', '2.5'),
                                      ("1 Cup", "Wheat pasta", '145', '37', '7.5', '0.8'),
                                      ("3/4 Cup", "Wheat pasta", '108', '27.7', '5.6', '0.6'),
                                      ("1/2 Cup", "Wheat pasta", '72', '18.5', '3.7', '0.4'),
                                      ("1/4 Cup", "Wheat pasta", '43', '9.2', '1.9', '0.2'),
                                      ("1 pc", "Banana",
                                       '105', '27',
                                       '1.3', '0.4'),
                                      ("1/2 pc", "Banana",
                                       '53', '13.5',
                                       '0.7', '0.2'),
                                      ("1 pc", "Apple", '95', '25.1', '0.5', '0.3'),
                                      ("1/2 pc", "Apple", '48', '12.5', '0.2', '0.1'),
                                      ("1 pc", "Mango",
                                       '201', '50',
                                       '2.8', '1.3'),
                                      ("1/2 pc", "Mango",
                                       '65', '25',
                                       '1.4', '0.6'),
                                      ("1 pc", "Pear", '102', '15', '0.4', '0.1'),
                                      ("1/2 pc", "Pear", '51', '7.5', '0.2', '0.05'),
                                      ("100g", "Bajra dalia",
                                       '378', '67',
                                       '12', '5'),
                                      ("1 Cup", "Bajra dalia",
                                       '207', '41',
                                       '6', '1.7'),
                                      ("3/4 Cup", "Bajra dalia",
                                       ' 138 ', '30.7',
                                       '4.5', '1.2'),
                                      ("1 Cup", "White chickpeas", '267', '44.7', '14.4', '4.2'),
                                      ("3/4 Cup", "White chickpeas", '214', '33.5', '10.8', '3.1'),
                                      ("1/2 Cup", "White chickpeas", '107', '22.3', '7.2', '2.1'),
                                      ("1/4 Cup", "White chickpeas", '74', '11.1', '3.6', '1.05'),
                                      ("1 Cup", "Kidney beans",
                                       '215', '110',
                                       '43', '1.5'),
                                      ("3/4 Cup", "Kidney beans",
                                       '161', '82.5',
                                       '32.2', '1.1'),
                                      ("1/2 Cup", "Kidney beans",
                                       '107', '55',
                                       '21.5', '0.75'),
                                      ("1/4 Cup", "Kidney beans",
                                       '53', '27.5',
                                       '10.7', '0.3'),
                                      ("1/2Cup", "Black chickpeas ", '147', '24.5', '1.3', '0.4'),
                                      ("1/4Cup", "Black chickpeas ", '73', '12.2', '3.9', '0.1'),
                                      ("1 Cup", "Black chickpeas ", '295', '49', '15.7', '4.9'),
                                      ("100g", "Broccoli",
                                       '34', '6.6',
                                       '2.8', '0.3'),
                                      ("100g", "Spinach", '23', '3.6', '2.9', '0.3'),
                                      ("100g", "Chicken",
                                       '239', '0',
                                       '27', '14'),
                                      ("100g", "Fish", '206', '0', '22', '12'),
                                      ("1 pc", "Eggs",
                                       '18', '0.2',
                                       '3.6', '0'),
                                      ("100g", "Mutton", '294', '0', '25', '21'),
                                      ("240ml", "Milk",
                                       '105', '12',
                                       '8', '2'),
                                      ("100g", "Yogurt", '59', '3.6', '10', '0.4'),
                                      ("100g", "Paneer",
                                       '242', '6.1',
                                       '19.1', '26.9'),
                                      ("100g", "Tofu", '76', '1.9', '8', '4.8'),
                                      ("1 Cup", "Peanuts", '828', '23.5', '37.6', '71.8'),
                                      ("1/2 Cup", "Peanuts", '414', '11.8', '18.8', '35.5'),
                                      ("1/4 Cup", "Peanuts", '207', '5.9', '9.4', '17.9'),
                                      ("1 pc", "Almonds",
                                       '6.94', '0.2',
                                       '0.2', '0.6'),
                                      ("100g", "Cashews", '553', '30', '18', '44'),
                                      ("100g", "Walnuts",
                                       '654', '14',
                                       '15', '65'),
                                      ("1 tbsp", "Peanut butter", '94', '3', '4', '8'),
                                      ("1 tbsp", "Flex seeds",
                                       '37', '2',
                                       '1.3', '3'),
                                      ("100g", "Chia seeds", '486', '42', '17', '31'),
                                      ("1 tbsp", "Sunflower seeds",
                                       '51', '2',
                                       '2', '5'),
                                      ("100g", "Salmon fish", '208', '0', '20', '13'),
                                      ("100g", "Egg boiled",
                                       '77', '0.6',
                                       '6', '5'),
                                      ("1 tbsp", "Olive oil", '119', '0', '0', '14')])

        self.tablel.bind(on_check_press=self.check_pressl)

        self.username.get_screen('lunch').add_widget(self.tablel)

        self.tableb = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.48}, size_hint=(0.96, 0.8), check=True,
                                  rows_num=65,
                                  column_data=[
                                      ("Qty", dp(30)),
                                      ("Food Item", dp(30)),
                                      ('Calories', dp(30)),
                                      ('Carbs', dp(30)),
                                      ('Protein', dp(30)),
                                      ('Fat', dp(30))],
                                  row_data=[
                                      ("1 Cup", "Oats",
                                       '307', '55',
                                       '11', '5'),
                                      ("3/4 Cup", "Oats",
                                       '225', '41',
                                       '7', '4'),
                                      ("1/2 Cup", "Oats",
                                       '150', '28',
                                       '5', '2.5'),
                                      ("1/4 Cup", "Oats",
                                       '90', '13.5',
                                       '2.5', '1.2'),
                                      ("1 Cup", "Brown rice", '216', '45', '5', '1.8'),
                                      ("3/4 Cup", "Brown rice", '164', '33.3', '3.7', '1.3'),
                                      ("1/2 Cup", "Brown rice", '108', '23', '3', '0.9'),
                                      ("1/4 Cup", "Brown rice", '54', '11.1', '1.26', '0.4'),
                                      ("1 pc", "Brown bread",
                                       '75', '56',
                                       '13', '4.3'),
                                      ("1/2 pc", "Brown bread",
                                       '37', '22.2',
                                       '4.1', '1.5'),
                                      ("100g", "Sweet potato", '86', '20g', '1.6g', '0.1g'),
                                      ("1 pc", "wheat roti",
                                       ' 71 ', '15',
                                       '3', '0.4'),
                                      ("1/2 pc", "wheat roti",
                                       '35.5 ', '7.5',
                                       '1.5', '0.2'),
                                      ("100g", "Wheat pasta", '124', '72', '13.2', '2.5'),
                                      ("1 Cup", "Wheat pasta", '145', '37', '7.5', '0.8'),
                                      ("3/4 Cup", "Wheat pasta", '108', '27.7', '5.6', '0.6'),
                                      ("1/2 Cup", "Wheat pasta", '72', '18.5', '3.7', '0.4'),
                                      ("1/4 Cup", "Wheat pasta", '43', '9.2', '1.9', '0.2'),
                                      ("1 pc", "Banana",
                                       '105', '27',
                                       '1.3', '0.4'),
                                      ("1/2 pc", "Banana",
                                       '53', '13.5',
                                       '0.7', '0.2'),
                                      ("1 pc", "Apple", '95', '25.1', '0.5', '0.3'),
                                      ("1/2 pc", "Apple", '48', '12.5', '0.2', '0.1'),
                                      ("1 pc", "Mango",
                                       '201', '50',
                                       '2.8', '1.3'),
                                      ("1/2 pc", "Mango",
                                       '65', '25',
                                       '1.4', '0.6'),
                                      ("1 pc", "Pear", '102', '15', '0.4', '0.1'),
                                      ("1/2 pc", "Pear", '51', '7.5', '0.2', '0.05'),
                                      ("100g", "Bajra dalia",
                                       '378', '67',
                                       '12', '5'),
                                      ("1 Cup", "Bajra dalia",
                                       '207', '41',
                                       '6', '1.7'),
                                      ("3/4 Cup", "Bajra dalia",
                                       ' 138 ', '30.7',
                                       '4.5', '1.2'),
                                      ("1 Cup", "White chickpeas", '267', '44.7', '14.4', '4.2'),
                                      ("3/4 Cup", "White chickpeas", '214', '33.5', '10.8', '3.1'),
                                      ("1/2 Cup", "White chickpeas", '107', '22.3', '7.2', '2.1'),
                                      ("1/4 Cup", "White chickpeas", '74', '11.1', '3.6', '1.05'),
                                      ("1 Cup", "Kidney beans",
                                       '215', '110',
                                       '43', '1.5'),
                                      ("3/4 Cup", "Kidney beans",
                                       '161', '82.5',
                                       '32.2', '1.1'),
                                      ("1/2 Cup", "Kidney beans",
                                       '107', '55',
                                       '21.5', '0.75'),
                                      ("1/4 Cup", "Kidney beans",
                                       '53', '27.5',
                                       '10.7', '0.3'),
                                      ("1/2Cup", "Black chickpeas ", '147', '24.5', '1.3', '0.4'),
                                      ("1/4Cup", "Black chickpeas ", '73', '12.2', '3.9', '0.1'),
                                      ("1 Cup", "Black chickpeas ", '295', '49', '15.7', '4.9'),
                                      ("100g", "Broccoli",
                                       '34', '6.6',
                                       '2.8', '0.3'),
                                      ("100g", "Spinach", '23', '3.6', '2.9', '0.3'),
                                      ("100g", "Chicken",
                                       '239', '0',
                                       '27', '14'),
                                      ("100g", "Fish", '206', '0', '22', '12'),
                                      ("1 pc", "Eggs",
                                       '18', '0.2',
                                       '3.6', '0'),
                                      ("100g", "Mutton", '294', '0', '25', '21'),
                                      ("240ml", "Milk",
                                       '105', '12',
                                       '8', '2'),
                                      ("100g", "Yogurt", '59', '3.6', '10', '0.4'),
                                      ("100g", "Paneer",
                                       '242', '6.1',
                                       '19.1', '26.9'),
                                      ("100g", "Tofu", '76', '1.9', '8', '4.8'),
                                      ("1 Cup", "Peanuts", '828', '23.5', '37.6', '71.8'),
                                      ("1/2 Cup", "Peanuts", '414', '11.8', '18.8', '35.5'),
                                      ("1/4 Cup", "Peanuts", '207', '5.9', '9.4', '17.9'),
                                      ("1 pc", "Almonds",
                                       '6.94', '0.2',
                                       '0.2', '0.6'),
                                      ("100g", "Cashews", '553', '30', '18', '44'),
                                      ("100g", "Walnuts",
                                       '654', '14',
                                       '15', '65'),
                                      ("1 tbsp", "Peanut butter", '94', '3', '4', '8'),
                                      ("1 tbsp", "Flex seeds",
                                       '37', '2',
                                       '1.3', '3'),
                                      ("100g", "Chia seeds", '486', '42', '17', '31'),
                                      ("1 tbsp", "Sunflower seeds",
                                       '51', '2',
                                       '2', '5'),
                                      ("100g", "Salmon fish", '208', '0', '20', '13'),
                                      ("100g", "Egg boiled",
                                       '77', '0.6',
                                       '6', '5'),
                                      ("1 tbsp", "Olive oil", '119', '0', '0', '14')])

        self.tableb.bind(on_check_press=self.check_pressb)

        self.username.get_screen('brunch').add_widget(self.tableb)

        self.tables = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.48}, size_hint=(0.96, 0.8), check=True,
                                  rows_num=63,
                                  column_data=[
                                      ("Qty", dp(30)),
                                      ("Food Item", dp(30)),
                                      ('Calories', dp(30)),
                                      ('Carbs', dp(30)),
                                      ('Protein', dp(30)),
                                      ('Fat', dp(30))],
                                  row_data=[
                                      ("1 Cup", "Oats",
                                       '307', '55',
                                       '11', '5'),
                                      ("3/4 Cup", "Oats",
                                       '225', '41',
                                       '7', '4'),
                                      ("1/2 Cup", "Oats",
                                       '150', '28',
                                       '5', '2.5'),
                                      ("1/4 Cup", "Oats",
                                       '90', '13.5',
                                       '2.5', '1.2'),
                                      ("1 Cup", "Brown rice", '216', '45', '5', '1.8'),
                                      ("3/4 Cup", "Brown rice", '164', '33.3', '3.7', '1.3'),
                                      ("1/2 Cup", "Brown rice", '108', '23', '3', '0.9'),
                                      ("1/4 Cup", "Brown rice", '54', '11.1', '1.26', '0.4'),
                                      ("1 pc", "Brown bread",
                                       '75', '56',
                                       '13', '4.3'),
                                      ("1/2 pc", "Brown bread",
                                       '37', '22.2',
                                       '4.1', '1.5'),
                                      ("100g", "Sweet potato", '86', '20g', '1.6g', '0.1g'),
                                      ("1 pc", "wheat roti",
                                       ' 71 ', '15',
                                       '3', '0.4'),
                                      ("1/2 pc", "wheat roti",
                                       '35.5 ', '7.5',
                                       '1.5', '0.2'),
                                      ("100g", "Wheat pasta", '124', '72', '13.2', '2.5'),
                                      ("1 Cup", "Wheat pasta", '145', '37', '7.5', '0.8'),
                                      ("3/4 Cup", "Wheat pasta", '108', '27.7', '5.6', '0.6'),
                                      ("1/2 Cup", "Wheat pasta", '72', '18.5', '3.7', '0.4'),
                                      ("1/4 Cup", "Wheat pasta", '43', '9.2', '1.9', '0.2'),
                                      ("1 pc", "Banana",
                                       '105', '27',
                                       '1.3', '0.4'),
                                      ("1/2 pc", "Banana",
                                       '53', '13.5',
                                       '0.7', '0.2'),
                                      ("1 pc", "Apple", '95', '25.1', '0.5', '0.3'),
                                      ("1/2 pc", "Apple", '48', '12.5', '0.2', '0.1'),
                                      ("1 pc", "Mango",
                                       '201', '50',
                                       '2.8', '1.3'),
                                      ("1/2 pc", "Mango",
                                       '65', '25',
                                       '1.4', '0.6'),
                                      ("1 pc", "Pear", '102', '15', '0.4', '0.1'),
                                      ("1/2 pc", "Pear", '51', '7.5', '0.2', '0.05'),
                                      ("100g", "Bajra dalia",
                                       '378', '67',
                                       '12', '5'),
                                      ("1 Cup", "Bajra dalia",
                                       '207', '41',
                                       '6', '1.7'),
                                      ("3/4 Cup", "Bajra dalia",
                                       ' 138 ', '30.7',
                                       '4.5', '1.2'),
                                      ("1 Cup", "White chickpeas", '267', '44.7', '14.4', '4.2'),
                                      ("3/4 Cup", "White chickpeas", '214', '33.5', '10.8', '3.1'),
                                      ("1/2 Cup", "White chickpeas", '107', '22.3', '7.2', '2.1'),
                                      ("1/4 Cup", "White chickpeas", '74', '11.1', '3.6', '1.05'),
                                      ("1 Cup", "Kidney beans",
                                       '215', '110',
                                       '43', '1.5'),
                                      ("3/4 Cup", "Kidney beans",
                                       '161', '82.5',
                                       '32.2', '1.1'),
                                      ("1/2 Cup", "Kidney beans",
                                       '107', '55',
                                       '21.5', '0.75'),
                                      ("1/4 Cup", "Kidney beans",
                                       '53', '27.5',
                                       '10.7', '0.3'),
                                      ("1/2Cup", "Black chickpeas ", '147', '24.5', '1.3', '0.4'),
                                      ("1/4Cup", "Black chickpeas ", '73', '12.2', '3.9', '0.1'),
                                      ("1 Cup", "Black chickpeas ", '295', '49', '15.7', '4.9'),
                                      ("100g", "Broccoli",
                                       '34', '6.6',
                                       '2.8', '0.3'),
                                      ("100g", "Spinach", '23', '3.6', '2.9', '0.3'),
                                      ("100g", "Chicken",
                                       '239', '0',
                                       '27', '14'),
                                      ("100g", "Fish", '206', '0', '22', '12'),
                                      ("1 pc", "Eggs",
                                       '18', '0.2',
                                       '3.6', '0'),
                                      ("100g", "Mutton", '294', '0', '25', '21'),
                                      ("240ml", "Milk",
                                       '105', '12',
                                       '8', '2'),
                                      ("100g", "Yogurt", '59', '3.6', '10', '0.4'),
                                      ("100g", "Paneer",
                                       '242', '6.1',
                                       '19.1', '26.9'),
                                      ("100g", "Tofu", '76', '1.9', '8', '4.8'),
                                      ("1 Cup", "Peanuts", '828', '23.5', '37.6', '71.8'),
                                      ("1/2 Cup", "Peanuts", '414', '11.8', '18.8', '35.5'),
                                      ("1/4 Cup", "Peanuts", '207', '5.9', '9.4', '17.9'),
                                      ("1 pc", "Almonds",
                                       '6.94', '0.2',
                                       '0.2', '0.6'),
                                      ("100g", "Cashews", '553', '30', '18', '44'),
                                      ("100g", "Walnuts",
                                       '654', '14',
                                       '15', '65'),
                                      ("1 tbsp", "Peanut butter", '94', '3', '4', '8'),
                                      ("1 tbsp", "Flex seeds",
                                       '37', '2',
                                       '1.3', '3'),
                                      ("100g", "Chia seeds", '486', '42', '17', '31'),
                                      ("1 tbsp", "Sunflower seeds",
                                       '51', '2',
                                       '2', '5'),
                                      ("100g", "Salmon fish", '208', '0', '20', '13'),
                                      ("100g", "Egg boiled",
                                       '77', '0.6',
                                       '6', '5'),
                                      ("1 tbsp", "Olive oil", '119', '0', '0', '14')])

        self.tables.bind(on_check_press=self.check_presss)

        self.username.get_screen('snacks').add_widget(self.tables)

        self.tabled = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.48}, size_hint=(0.96, 0.8), check=True,
                                  rows_num=63,
                                  column_data=[
                                      ("Qty", dp(30)),
                                      ("Food Item", dp(30)),
                                      ('Calories', dp(30)),
                                      ('Carbs', dp(30)),
                                      ('Protein', dp(30)),
                                      ('Fat', dp(30))],
                                  row_data=[
                                      ("1 Cup", "Oats",
                                       '307', '55',
                                       '11', '5'),
                                      ("3/4 Cup", "Oats",
                                       '225', '41',
                                       '7', '4'),
                                      ("1/2 Cup", "Oats",
                                       '150', '28',
                                       '5', '2.5'),
                                      ("1/4 Cup", "Oats",
                                       '90', '13.5',
                                       '2.5', '1.2'),
                                      ("1 Cup", "Brown rice", '216', '45', '5', '1.8'),
                                      ("3/4 Cup", "Brown rice", '164', '33.3', '3.7', '1.3'),
                                      ("1/2 Cup", "Brown rice", '108', '23', '3', '0.9'),
                                      ("1/4 Cup", "Brown rice", '54', '11.1', '1.26', '0.4'),
                                      ("1 pc", "Brown bread",
                                       '75', '56',
                                       '13', '4.3'),
                                      ("1/2 pc", "Brown bread",
                                       '37', '22.2',
                                       '4.1', '1.5'),
                                      ("100g", "Sweet potato", '86', '20g', '1.6g', '0.1g'),
                                      ("1 pc", "wheat roti",
                                       ' 71 ', '15',
                                       '3', '0.4'),
                                      ("1/2 pc", "wheat roti",
                                       '35.5 ', '7.5',
                                       '1.5', '0.2'),
                                      ("100g", "Wheat pasta", '124', '72', '13.2', '2.5'),
                                      ("1 Cup", "Wheat pasta", '145', '37', '7.5', '0.8'),
                                      ("3/4 Cup", "Wheat pasta", '108', '27.7', '5.6', '0.6'),
                                      ("1/2 Cup", "Wheat pasta", '72', '18.5', '3.7', '0.4'),
                                      ("1/4 Cup", "Wheat pasta", '43', '9.2', '1.9', '0.2'),
                                      ("1 pc", "Banana",
                                       '105', '27',
                                       '1.3', '0.4'),
                                      ("1/2 pc", "Banana",
                                       '53', '13.5',
                                       '0.7', '0.2'),
                                      ("1 pc", "Apple", '95', '25.1', '0.5', '0.3'),
                                      ("1/2 pc", "Apple", '48', '12.5', '0.2', '0.1'),
                                      ("1 pc", "Mango",
                                       '201', '50',
                                       '2.8', '1.3'),
                                      ("1/2 pc", "Mango",
                                       '65', '25',
                                       '1.4', '0.6'),
                                      ("1 pc", "Pear", '102', '15', '0.4', '0.1'),
                                      ("1/2 pc", "Pear", '51', '7.5', '0.2', '0.05'),
                                      ("100g", "Bajra dalia",
                                       '378', '67',
                                       '12', '5'),
                                      ("1 Cup", "Bajra dalia",
                                       '207', '41',
                                       '6', '1.7'),
                                      ("3/4 Cup", "Bajra dalia",
                                       ' 138 ', '30.7',
                                       '4.5', '1.2'),
                                      ("1 Cup", "White chickpeas", '267', '44.7', '14.4', '4.2'),
                                      ("3/4 Cup", "White chickpeas", '214', '33.5', '10.8', '3.1'),
                                      ("1/2 Cup", "White chickpeas", '107', '22.3', '7.2', '2.1'),
                                      ("1/4 Cup", "White chickpeas", '74', '11.1', '3.6', '1.05'),
                                      ("1 Cup", "Kidney beans",
                                       '215', '110',
                                       '43', '1.5'),
                                      ("3/4 Cup", "Kidney beans",
                                       '161', '82.5',
                                       '32.2', '1.1'),
                                      ("1/2 Cup", "Kidney beans",
                                       '107', '55',
                                       '21.5', '0.75'),
                                      ("1/4 Cup", "Kidney beans",
                                       '53', '27.5',
                                       '10.7', '0.3'),
                                      ("1/2Cup", "Black chickpeas ", '147', '24.5', '1.3', '0.4'),
                                      ("1/4Cup", "Black chickpeas ", '73', '12.2', '3.9', '0.1'),
                                      ("1 Cup", "Black chickpeas ", '295', '49', '15.7', '4.9'),
                                      ("100g", "Broccoli",
                                       '34', '6.6',
                                       '2.8', '0.3'),
                                      ("100g", "Spinach", '23', '3.6', '2.9', '0.3'),
                                      ("100g", "Chicken",
                                       '239', '0',
                                       '27', '14'),
                                      ("100g", "Fish", '206', '0', '22', '12'),
                                      ("1 pc", "Eggs",
                                       '18', '0.2',
                                       '3.6', '0'),
                                      ("100g", "Mutton", '294', '0', '25', '21'),
                                      ("240ml", "Milk",
                                       '105', '12',
                                       '8', '2'),
                                      ("100g", "Yogurt", '59', '3.6', '10', '0.4'),
                                      ("100g", "Paneer",
                                       '242', '6.1',
                                       '19.1', '26.9'),
                                      ("100g", "Tofu", '76', '1.9', '8', '4.8'),
                                      ("1 Cup", "Peanuts", '828', '23.5', '37.6', '71.8'),
                                      ("1/2 Cup", "Peanuts", '414', '11.8', '18.8', '35.5'),
                                      ("1/4 Cup", "Peanuts", '207', '5.9', '9.4', '17.9'),
                                      ("1 pc", "Almonds",
                                       '6.94', '0.2',
                                       '0.2', '0.6'),
                                      ("100g", "Cashews", '553', '30', '18', '44'),
                                      ("100g", "Walnuts",
                                       '654', '14',
                                       '15', '65'),
                                      ("1 tbsp", "Peanut butter", '94', '3', '4', '8'),
                                      ("1 tbsp", "Flex seeds",
                                       '37', '2',
                                       '1.3', '3'),
                                      ("100g", "Chia seeds", '486', '42', '17', '31'),
                                      ("1 tbsp", "Sunflower seeds",
                                       '51', '2',
                                       '2', '5'),
                                      ("100g", "Salmon fish", '208', '0', '20', '13'),
                                      ("100g", "Egg boiled",
                                       '77', '0.6',
                                       '6', '5'),
                                      ("1 tbsp", "Olive oil", '119', '0', '0', '14')])

        self.tabled.bind(on_check_press=self.check_pressd)

        self.username.get_screen('dinner').add_widget(self.tabled)

        self.mainbutton = MDRectangleFlatIconButton(
            text="-------------------Select Activity Level -------------------------",
            icon="google-fit",
            text_color=(1, 0, 0, 1),
            line_color=(1, 0, 0, 1),
            pos_hint={'center_x': .5, 'center_y': .6}
        )

        self.mainbutton2 = MDRectangleFlatIconButton(
            text="Weight loss/Weight gain per week",
            icon="google-fit",
            text_color=(1, 0, 0, 1),
            md_bg_color=self.theme_cls.primary_color,
            line_color=(1, 0, 0, 1),
            pos_hint={"center_x": .5, "center_y": .4},
        )

        self.mainbutton3 = MDRectangleFlatIconButton(
            text="-----Fitness Goal  -----",
            icon="google-fit",
            text_color=(1, 0, 0, 1),
            line_color=(1, 0, 0, 1),
            pos_hint={"center_x": .5, "center_y": .5},
        )

        # macro calculator da button
        self.mainbutton4 = MDRectangleFlatIconButton(
            text="-----Fitness Goal  -----",
            icon="arm-flex",
            text_color=(1, 0, 0, 1),
            line_color=(1, 0, 0, 1),
            pos_hint={"center_x": .5, "center_y": .43},
        )

        # exercise select button
        self.mainbutton5 = MDRectangleFlatIconButton(
            text="-----Select Exercise -----",
            icon="arm-flex",
            text_color=(1, 0, 0, 1),
            line_color=(1, 0, 0, 1),
            pos_hint={"center_x": .5, "center_y": .65},
        )

        self.username.get_screen('dcalories').add_widget(self.mainbutton)
        self.username.get_screen('dcalories').add_widget(self.mainbutton2)
        self.username.get_screen('dcalories').add_widget(self.mainbutton3)
        self.username.get_screen('macro').add_widget(self.mainbutton4)
        self.username.get_screen('repmax').add_widget(self.mainbutton5)

        self.dropdown1 = Dropdown1()

        self.dropdown1.bind(on_select=self.select_text1)

        self.mainbutton.bind(on_release=self.dropdown1.open)

        self.dropdown2 = Dropdown2()

        self.dropdown2.bind(on_select=self.select_text2)

        self.mainbutton2.bind(on_release=self.dropdown2.open)

        self.dropdown3 = Dropdown3()

        self.dropdown3.bind(on_select=self.select_text3)

        self.mainbutton3.bind(on_release=self.dropdown3.open)

        self.dropdown4 = Dropdown4()

        self.dropdown4.bind(on_select=self.select_text4)

        self.mainbutton4.bind(on_release=self.dropdown4.open)

        self.dropdown5 = Dropdown5()

        self.dropdown5.bind(on_select=self.select_text5)

        self.mainbutton5.bind(on_release=self.dropdown5.open)

        return screen

    def select_text1(self, instance, x):
        self.mainbutton.text = x

    def select_text2(self, instance, x):
        self.mainbutton2.text = x

    def select_text3(self, instance, x):
        self.mainbutton3.text = x

    def select_text4(self, instance, x):
        self.mainbutton4.text = x

    def select_text5(self, instance, x):
        self.mainbutton5.text = x

    def bmr(self, height, weight, age, gender):
        if str(gender).lower() == "male":
            a = 88.362
            b = 13.397 * float(weight)
            c = 4.799 * float(height)
            d = 5.677 * float(age)
            bmr_men = a + b + c - d
            # bmr_for_men = 88.362 + (13.397 * weight) + (4.799 * height) – (5.677 * age )
            return round(bmr_men, 2)

        elif str(gender).lower() == "female":
            a = 447.593
            b = 9.247 * float(weight)
            c = 3.098 * float(height)
            d = 4.330 * float(age)
            bmr_women = a + b + c - d
            # bmr_for_men = 447.593 + (9.247 x weight) + (3.098 x height) – (4.330 x age)
            return round(bmr_women, 2)
        else:
            return ('Enter male or female')

    def show_data(self):
        if str(self.username.get_screen('bmr').ids.height.text) == "" and \
                str(self.username.get_screen('bmr').ids.weight.text) == "" and \
                str(self.username.get_screen('bmr').ids.age.text) == "" and \
                str(self.username.get_screen('bmr').ids.gender.text) is "":
            check_str = 'please enter Height ,Weight, Age and Gender'

        elif str(self.username.get_screen('bmr').ids.height.text) is "":
            check_str = 'please enter weight'

        elif str(self.username.get_screen('bmr').ids.weight.text) is "":
            check_str = 'please enter weight'

        elif str(self.username.get_screen('bmr').ids.age.text) is "":
            check_str = 'please enter your age'

        elif str(self.username.get_screen('bmr').ids.gender.text) is "":
            check_str = 'please enter Gender(Male or Female)'

        elif str(self.username.get_screen('bmr').ids.gender.text).lower() != "male" and str(
                self.username.get_screen('bmr').ids.gender.text).lower() != "female":
            check_str = 'please enter Gender(Male or Female)'

        else:
            check_str = str(self.bmr(float(self.username.get_screen('bmr').ids.height.text),
                                     float(self.username.get_screen('bmr').ids.weight.text),
                                     float(self.username.get_screen('bmr').ids.age.text),
                                     str(self.username.get_screen('bmr').ids.gender.text)))

        self.dialog = MDDialog(title='Calculated BMR',
                               text=check_str,
                               size_hint=(0.8, 1), auto_dismiss=True,
                               buttons=[
                                   MDRaisedButton(text='Close', md_bg_color=(0, 0, 0, 1), on_release=self.close_dialog),
                                   MDRaisedButton(text='more', md_bg_color=(0, 0, 0, 1))]
                               )
        self.dialog.open()

        self.username.get_screen('dcalories').ids.bmrinput.text = check_str

        try:
            if type(float(check_str)) == type(1.2):
                self.username.get_screen('bmr').ids.bmrright.disabled = False
        except:
            self.username.get_screen('bmr').ids.bmrright.disabled = True

    def signup(self):
        signupEmail = self.username.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.username.get_screen('signupscreen').ids.signup_password.text
        signupUsername1 = self.username.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername1.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername1.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialogu = MDDialog(title='Invalid Username', text='Please enter username without space',
                                    size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername1}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.username.get_screen('loginscreen').manager.current = 'loginscreen'

    auth = 'LNCKjE0S7ZU4WDY11KPZP9tKPGCRG8OyQUdd3PHo'

    def login(self):
        loginEmail = self.username.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.username.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username1 = data[supported_loginEmail]['Username']
            self.login_check = True
            self.username.get_screen('main').manager.current = 'main'
        else:
            print("user no longer exists")

    def close_username_dialog(self, obj):
        self.dialogu.dismiss()

    def username_changer(self):
        if self.login_check:
            self.username.get_screen('main').ids.username_info.text = f"welcome {self.username1}"

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def close_dialog1(self, obj):
        self.dialog1.dismiss()

    # dailog bmi
    def close_dialogbmi(self, obj):
        self.dialogbmi.dismiss()

    # macro dialog
    def close_dialogm(self, obj):
        self.dialogm.dismiss()

    # repmax dialog
    def close_dialogrep(self, obj):
        self.dialogrep.dismiss()

    def theme_changer(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    # breakfast(data)
    def check_press(self, instance_table, current_row):
        row = current_row
        ed = [0, 0, 0, 0]
        ed[0] = float(row[2])
        ed[1] = float(row[3])
        ed[2] = float(row[4])
        ed[3] = float(row[5])

        for i in range(0, 4):
            self.el[i] = round((self.el[i] + ed[i]), 2)

            self.username.get_screen(
                'target').ids.breakf.tertiary_text = f'Cal:{self.el[0]},C: {self.el[1]},P: {self.el[2]},F: {self.el[3]}'

            self.progbar(self.el[0], self.dcal)

    # breakfast
    def progbar(self, selcal, total_cal):
        a = float(selcal)
        b = float(total_cal) / 5
        res = round((a / float(b)) * 100, 2)
        if res > 100:
            self.snackbar1 = Snackbar(
                text="Calories exceeds than required",
                snackbar_x="10dp",
                snackbar_y="10dp",
            )
            self.snackbar1.open()
            self.username.get_screen('target').ids.prog1.value = 100
        else:
            self.username.get_screen('target').ids.prog1.value = res

    # brunch
    def progbar2(self, selcal, total_cal):
        a = float(selcal)
        b = float(total_cal) / 5
        res2 = round((a / float(b)) * 100, 2)
        if res2 > 100:
            self.snackbar2 = Snackbar(
                text="Calories exceeds than required",
                snackbar_x="10dp",
                snackbar_y="10dp",
            )
            self.snackbar2.open()
            self.username.get_screen('target').ids.prog2.value = 100
        else:
            self.username.get_screen('target').ids.prog2.value = res2

    # brunch
    def check_pressb(self, instance_table, current_row):
        row = current_row
        edb = [0, 0, 0, 0]
        edb[0] = float(row[2])
        edb[1] = float(row[3])
        edb[2] = float(row[4])
        edb[3] = float(row[5])

        for i in range(0, 4):
            self.elb[i] = round((self.elb[i] + edb[i]), 2)

            self.username.get_screen(
                'target').ids.brunch.tertiary_text = f'Cal:{self.elb[0]},C: {self.elb[1]},P: {self.elb[2]},F: {self.elb[3]}'

            self.progbar2(self.elb[0], self.dcal)

    # lunch
    def check_pressl(self, instance_table, current_row):
        row = current_row
        ed = [0, 0, 0, 0]
        ed[0] = float(row[2])
        ed[1] = float(row[3])
        ed[2] = float(row[4])
        ed[3] = float(row[5])

        for i in range(0, 4):
            self.ell[i] = round((self.ell[i] + ed[i]), 2)

            self.username.get_screen(
                'target').ids.lunch.tertiary_text = f'Cal:{self.ell[0]},C: {self.ell[1]},P: {self.ell[2]},F: {self.ell[3]}'

            self.progbar3(self.ell[0], self.dcal)

    # lunch
    def progbar3(self, selcal, total_cal):
        a = float(selcal)
        b = float(total_cal) / 5
        res3 = round((a / float(b)) * 100, 2)
        if res3 > 100:
            self.snackbar3 = Snackbar(
                text="Calories exceeds than required",
                snackbar_x="10dp",
                snackbar_y="10dp",
            )
            self.snackbar3.open()
            self.username.get_screen('target').ids.prog3.value = 100
        else:
            self.username.get_screen('target').ids.prog3.value = res3

    # dinner
    def check_pressd(self, instance_table, current_row):
        row = current_row
        ed = [0, 0, 0, 0]
        ed[0] = float(row[2])
        ed[1] = float(row[3])
        ed[2] = float(row[4])
        ed[3] = float(row[5])

        for i in range(0, 4):
            self.eld[i] = round((self.eld[i] + ed[i]), 2)
            print(self.eld)

            self.username.get_screen(
                'target').ids.dinner.tertiary_text = f'Cal:{self.eld[0]},C: {self.eld[1]},P: {self.eld[2]},F: {self.eld[3]}'

            self.progbar5(self.eld[0], self.dcal)

    # dinner
    def progbar5(self, selcal, total_cal):
        a = float(selcal)
        b = float(total_cal) / 5
        res5 = round((a / float(b)) * 100, 2)
        if res5 > 100:
            self.snackbar5 = Snackbar(
                text="Calories exceeds than required",
                snackbar_x="10dp",
                snackbar_y="10dp",
            )
            self.snackbar5.open()
            self.username.get_screen('target').ids.prog5.value = 100
        else:
            self.username.get_screen('target').ids.prog5.value = res5

    # snacks
    def check_presss(self, instance_table, current_row):
        row = current_row
        ed = [0, 0, 0, 0]
        ed[0] = float(row[2])
        ed[1] = float(row[3])
        ed[2] = float(row[4])
        ed[3] = float(row[5])

        for i in range(0, 4):
            self.els[i] = round((self.els[i] + ed[i]), 2)
            print(self.els)

            self.username.get_screen(
                'target').ids.snacks.tertiary_text = f'Cal:{self.els[0]},C: {self.els[1]},P: {self.els[2]},F: {self.els[3]}'

            self.progbar4(self.els[0], self.dcal)

    # snacks
    def progbar4(self, selcal, total_cal):
        a = float(selcal)
        b = float(total_cal) / 5
        res4 = round((a / float(b)) * 100, 2)
        if res4 > 100:
            self.snackbar4 = Snackbar(
                text="Calories exceeds than required",
                snackbar_x="10dp",
                snackbar_y="10dp",
            )
            self.snackbar4.open()
            self.username.get_screen('target').ids.prog4.value = 100
        else:
            self.username.get_screen('target').ids.prog4.value = res4

    def screen_swipe(self):
        self.username.get_screen('bmr').manager.current = 'dcalories'
        self.username.get_screen('bmr').manager.transition.direction = 'left'

    def callback(self, instance, value):
        pass

    def vapas(self):
        self.username.get_screen('bmr').manager.current = 'main'
        self.username.get_screen('bmr').manager.transition.direction = 'right'

    # breakfast
    def vapasb(self):
        self.username.get_screen('data').manager.current = 'target'
        self.username.get_screen('data').manager.transition.direction = 'right'

    def vapasbr(self):
        self.username.get_screen('brunch').manager.current = 'target'
        self.username.get_screen('brunch').manager.transition.direction = 'right'

    def vapasl(self):
        self.username.get_screen('lunch').manager.current = 'target'
        self.username.get_screen('lunch').manager.transition.direction = 'right'

    def vapass(self):
        self.username.get_screen('snacks').manager.current = 'target'
        self.username.get_screen('snacks').manager.transition.direction = 'right'

    def vapasd(self):
        self.username.get_screen('dinner').manager.current = 'target'
        self.username.get_screen('dinner').manager.transition.direction = 'right'

    def vapas4(self):
        self.username.get_screen('target').manager.current = 'main'
        self.username.get_screen('target').manager.transition.direction = 'right'

    def vapas3(self):
        self.username.get_screen('macro').manager.current = 'main'
        self.username.get_screen('macro').manager.transition.direction = 'right'

    def vapas5(self):
        self.username.get_screen('dcalories').manager.current = 'main'
        self.username.get_screen('dcalories').manager.transition.direction = 'right'

    def cal_calories_intake(self):

        self.dcal = str(
            self.calories_intake(self.username.get_screen('dcalories').ids.bmrinput.text, str(self.mainbutton.text),
                                 str(self.mainbutton2.text), str(self.mainbutton3.text)))
        self.dialog1 = MDDialog(title='Calories per Day',
                                text=self.dcal,
                                size_hint=(0.8, 1), auto_dismiss=True,
                                buttons=[
                                    MDRaisedButton(text='Close', md_bg_color=(0, 0, 0, 1),
                                                   on_release=self.close_dialog1),
                                    MDRaisedButton(text='more', md_bg_color=(0, 0, 0, 1))]
                                )
        self.dialog1.open()

        self.username.get_screen('macro').ids.calinput.text = self.dcal

        try:
            if type(float(self.dcal)) == type(1.2):
                self.username.get_screen('dcalories').ids.dcalright.disabled = False
        except:
            self.username.get_screen('dcalories').ids.dcalright.disabled = True

    def calories_intake(self, bmr, activity, aim, goal):
        # very lightly
        if str(activity) == "sedentary(little or no exercise)":
            maincal = float(bmr) * 1.2
            if str(goal) == 'Muscle Building':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) + 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) + 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) + 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) + 1000
                else:
                    return 'enter valid input'

            elif str(goal) == 'Fat Loss':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) - 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) - 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) - 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) - 1000
                else:
                    return 'enter valid input'

        # lightly
        if str(activity) == "lightly(1-3times a week)":
            maincal = float(bmr) * 1.375
            if str(goal) == 'Muscle Building':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) + 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) + 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) + 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) + 1000
                else:
                    return 'enter valid input'

            elif str(goal) == 'Fat Loss':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) - 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) - 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) - 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) - 1000
                else:
                    return 'enter valid input'

        # moderatly
        if str(activity) == "moderatly(3-5 times a week)":
            maincal = float(bmr) * 1.55
            if str(goal) == 'Muscle Building':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) + 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) + 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) + 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) + 1000
                else:
                    return 'enter valid input'

            elif str(goal) == 'Fat Loss':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) - 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) - 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) - 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) - 1000
                else:
                    return 'enter valid input'

        # highly
        if str(activity) == "highly active(6-7 times a week)":
            maincal = float(bmr) * 1.725
            if str(goal) == 'Muscle Building':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) + 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) + 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) + 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) + 1000
                else:
                    return 'enter valid input'

            elif str(goal) == 'Fat Loss':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) - 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) - 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) - 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) - 1000
                else:
                    return 'enter valid input'

        # extremly
        if str(activity) == "extremly active(1-2 times a day)":
            maincal = float(bmr) * 1.9
            if str(goal) == 'Muscle Building':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) + 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) + 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) + 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) + 1000
                else:
                    return 'enter valid input'

            elif str(goal) == 'Fat Loss':
                if str(aim) == '0.25 Kg per Week':
                    return round(maincal) - 250
                elif str(aim) == '0.5 Kg per Week':
                    return round(maincal) - 500
                elif str(aim) == '0.75 Kg per Week':
                    return round(maincal) - 750
                elif str(aim) == '1 Kg per Week':
                    return round(maincal) - 1000
                else:
                    return 'enter valid input'

        else:
            return 'Error 404'

    def reset(self):
        self.username.get_screen('target').ids.breakf.tertiary_text = "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
        self.username.get_screen('data').manager.current = "target"
        self.username.get_screen('data').manager.transition.direction = 'right'
        self.el = [0, 0, 0, 0]
        self.username.get_screen('target').ids.prog1.value = 0

    def resetb(self):
        self.username.get_screen('target').ids.brunch.tertiary_text = "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
        self.username.get_screen('brunch').manager.current = "target"
        self.username.get_screen('brunch').manager.transition.direction = 'right'
        self.elb = [0, 0, 0, 0]
        self.username.get_screen('target').ids.prog2.value = 0

    def resetl(self):
        self.username.get_screen('target').ids.lunch.tertiary_text = "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
        self.username.get_screen('lunch').manager.current = "target"
        self.username.get_screen('lunch').manager.transition.direction = 'right'
        self.ell = [0, 0, 0, 0]
        self.username.get_screen('target').ids.prog3.value = 0

    def resets(self):
        self.username.get_screen('target').ids.snacks.tertiary_text = "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
        self.username.get_screen('snacks').manager.current = "target"
        self.username.get_screen('snacks').manager.transition.direction = 'right'
        self.els = [0, 0, 0, 0]
        self.username.get_screen('target').ids.prog4.value = 0

    def resetd(self):
        self.username.get_screen('target').ids.dinner.tertiary_text = "Cal: 00,Carb: 0,Pro: 0,Fat: 0"
        self.username.get_screen('dinner').manager.current = "target"
        self.username.get_screen('dinner').manager.transition.direction = 'right'
        self.eld = [0, 0, 0, 0]
        self.username.get_screen('target').ids.prog5.value = 0

    def khalifunc(self):
        pass

    def cal_macro(self):
        mac = self.macrof(self.username.get_screen('macro').ids.calinput.text, self.mainbutton4.text)
        # macro dailog
        self.dialogm = MDDialog(title='Macro Breakdown',
                                text=mac,
                                size_hint=(0.8, 1), auto_dismiss=True,
                                buttons=[
                                    MDRaisedButton(text='Close', md_bg_color=(0, 0, 0, 1),
                                                   on_release=self.close_dialogm)]
                                )
        self.dialogm.open()

        try:
            if type(float(mac)) == type("d"):
                self.username.get_screen('macro').ids.macroright.disabled = True
        except:
            self.username.get_screen('macro').ids.macroright.disabled = False

    def macrof(self, cal, goal):
        if str(goal).lower() == "fat loss":
            p = round((0.45 * float(cal)) / 4)
            c = round((0.30 * float(cal)) / 4)
            f = round((0.25 * float(cal)) / 9)
            return f'Carbs({c})  Protein({p})  Fat({f})'

        else:
            c = round((0.48 * float(cal)) / 4)
            p = round((0.31 * float(cal)) / 4)
            f = round((0.21 * float(cal)) / 9)
            return f'Carbs({c})  Protein({p})  Fat({f})'

    def bmi_cal(self):
        bmi = '........'
        if str(self.username.get_screen('bmi').ids.heightbmi.text) == "" and \
                str(self.username.get_screen('bmi').ids.weightbmi.text) == "":
            bmi = 'please enter Height ,Weight, Age and Gender'

        elif str(self.username.get_screen('bmi').ids.heightbmi.text) is "":
            bmi = 'please enter weight'

        elif str(self.username.get_screen('bmi').ids.weightbmi.text) is "":
            bmi = 'please enter weight'
        else:
            try:
                if type(float(self.username.get_screen('bmi').ids.heightbmi.text)) == type(1.1) and type(
                        float(self.username.get_screen('bmi').ids.weightbmi.text)) == type(1.1):
                    v = str(self.bmif(float(self.username.get_screen('bmi').ids.heightbmi.text),
                                      float(self.username.get_screen('bmi').ids.weightbmi.text)))

                    if float(v) < 18.5:
                        bmi = f"you are UnderWeight with BMI ({v})"

                    elif float(v) >= 18.5 and float(v) <= 24.9:
                        bmi = f"you have Healthy Weight with BMI ({v})"

                    elif float(v) >= 14.9 and float(v) <= 29.9:
                        bmi = f"you are OverWeight with BMI ({v})"

                    else:
                        bmi = f"you are Obese with BMI ({v})"

            except:
                bmi = "please enter numbers only"

        self.dialogbmi = MDDialog(title='YOUR BMI',
                                  text=bmi,
                                  size_hint=(0.8, 1), auto_dismiss=True,
                                  buttons=[
                                      MDRaisedButton(text='Close', md_bg_color=(0, 0, 0, 1),
                                                     on_release=self.close_dialogbmi)]
                                  )
        self.dialogbmi.open()

    def bmif(self, height, weight):
        return round((((weight / height) / height) * 10000), 1)

    def repmax(self):
        if self.username.get_screen('repmax').ids.weightlifted.text == "":
            rm = "please enter Lifted Weight"

        elif type(float(self.username.get_screen('repmax').ids.weightlifted.text)) == type(1.1):
            rm = str(self.repformula(self.mainbutton5.text, self.username.get_screen('repmax').ids.weightlifted.text))

        else:
            rm = "Enter number only"

        self.dialogrep = MDDialog(title='YOUR 1RM is',
                                  text=rm,
                                  size_hint=(0.8, 1), auto_dismiss=True,
                                  buttons=[
                                      MDRaisedButton(text='Close', md_bg_color=(0, 0, 0, 1),
                                                     on_release=self.close_dialogrep)]
                                  )
        self.dialogrep.open()

    def repformula(self, ex, weight):
        if str(ex) == "Deadlift" or str(ex) == "Squats":
            return round((float(weight) * 1.09703) + 14.2546, 1)

        else:
            return round((float(weight) * 1.1307) + 0.6998, 1)

    # def on_start(self):
    #     data=[]
    #     with open('dinner.json', 'w') as dinner:
    #         json.dump(data, dinner, indent=2)
    #     with open('breakfast.json', 'w') as breakf:
    #         json.dump(data, breakf, indent=2)
    #     with open('lunch.json', 'w') as lunch:
    #         json.dump(data, lunch, indent=2)


DIETist().run()
# DIETist().on_start()