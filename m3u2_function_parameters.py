#Make a simple calculator

def addition(num1,num2,num3,num4):
    answer = num1 + num2 + num3 + num4
    return answer

x = addition(5,6,6,5)
print(x)

def website(font, background_color,font_size,font_color):
    print("Font type:",font)
    print("Background color:",background_color)
    print("Font size:",font_size)
    print("Font color",font_color)

website("Arial","White","11","Black")

#website may contain hundreds of variables - not manageable
#have to retain same order of parameters

#see error example below
website("Black","Arial","White","11")

#could use the below instead - can press enter to help readability
website(font_color="Black",
        font="Arial",
        background_color="White",
        font_size="11")

#if defaults are not defined or input, an error is generated

def websiteNew(font="Arial", background_color="White",font_size=11,font_color="Black"):
    print("Font type:",font)
    print("Background color:",background_color)
    print("Font size:",font_size)
    print("Font color",font_color)

websiteNew(background_color="Grey")

#functions use default values entered above unless overridden when function is called

#recommended to add default values especially if others likely to use code/site
