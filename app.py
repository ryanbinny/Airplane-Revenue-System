from flask import Flask, render_template, request      #render_template:will tell the compiler to render the templates folder of the project where our html files are located, request: It will tell the server to receive the values given by the user from the frontend ie it acts as the back end to store the values
app = Flask(__name__)

def calc_revenue(economy,business,first_class,distance,aircraft_type):
    rates={'Economy':5,'Business':10,'FirstClass':20}      #dictionary to store the rate values for each class
    base_revenue=(
        economy*distance*rates['Economy']+
        business*distance*rates['Business']+
        first_class*distance*rates['FirstClass']        #this fn will calculate the basic total revenue
    )

    tot_passengers=economy+business+first_class          #total no. of passengers
    surcharge=0
    discount=0
    bonus=0                                             #initially setting all conditions to 0

    if tot_passengers>300:
        rates={k:v*1.10 for k,v in rates.items()}       #1.10=10 percent additional increase

        base_revenue = (
        economy * distance * rates['Economy'] +
        business * distance * rates['Business'] +
        first_class * distance * rates['FirstClass']
    )
        
    if distance>5000:
        discount=0.05*base_revenue                      #5 percent discount

    if aircraft_type == "A380" and tot_passengers>250:
        bonus=100000

    final_revenue=base_revenue-discount+bonus           #the last revenue after the conditions have been applied

    return{
        'base_revenue': base_revenue,
        'surcharge_applied' : tot_passengers>300,          # will return true or false-it is passed to the html code so that it can understand if a surcharge was applied or not
        'discount': discount,
        'bonus':bonus,
        'final_revenue':final_revenue
    }

@app.route('/')                                         #it routes to the home page of the project
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])                  #POST is an http protocol used to send data from the client to the server-used when we have forms-data will not be shown in the url
def result():
    print("FORM DATA:", request.form)
    economy = int(request.form['economy'])
    business = int(request.form['business'])
    first_class = int(request.form['first_class'])
    distance = int(request.form['distance'])
    aircraft = request.form['aircraft']              #flask server is recieving the values in backend which the client has sent
    print("Received values:", economy, business, first_class, distance, aircraft)

    if economy<0 or business<0 or first_class<0 or distance<=0:
        raise ValueError("Invalid input values!")
        
    results=calc_revenue(economy,business,first_class,distance,aircraft)       #fn.call

    return render_template('result.html',**results,      #**results unpacks the dictionary values from results dictionary and returns them
                               economy=economy,business=business,first_class=first_class,distance=distance,aircraft=aircraft)
    
if __name__ == '__main__':
    app.run(debug=True)                          #this sets to automatic debugging




    
