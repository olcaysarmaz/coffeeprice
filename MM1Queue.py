from __future__ import division

#MM1 Queue Class
class MM1Queue():
    def __init__(self, arrival_rate, service_rate, expected_service, uniformL, uniformH):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.expected_service = expected_service
        self.uniformL = uniformL
        self.uniformH = uniformH
        
        #Mean service rate
        global mu
        mu = 1 / service_rate
        
        #Mean rate of arrival
        global lambdao
        lambdao = arrival_rate / 60

        #Server utilization
        global rho
        rho = lambdao / mu

    #Returns average number of customers in the system 
    def ls(self):
        return rho / (1 - rho)

    #Returns average number of customers in queue
    def lq(self):
        return rho ** 2 / (1 - rho)

    #Returns average time a customers spends in the system
    def ws(self):
        return 1 / (mu - lambdao)

    #Returns average time a customer spends in the queue
    def wq(self):
        return lambdao / (mu * (mu - lambdao))

#Returns the coffee price per given percentage served
def coffee_price(percentage, uniformL, uniformH):
    return uniformH - (uniformH - uniformL) * percentage

#Returns a stable Q object for given system parameters
def stable_arrival_rate(challenge):

    #Calculate the max arrival rate the system can accommodate
    stable_arrival_rate = 60 * (challenge.expected_service * mu - 1) / challenge.expected_service
    print("Maximum Arrival Rate that the stable system can accommodate: " + str(stable_arrival_rate) + " customers per hour")

    #Create a MM1Queue object for max arrival rate and other system parameters
    stableQ = MM1Queue(stable_arrival_rate, challenge.service_rate, challenge.expected_service, challenge.uniformL , challenge.uniformH)
    
    #Prints coffee price for max arrival rate the system can accommodate
    percentage_serviced = stable_arrival_rate / challenge.arrival_rate
    print ("The coffee price at the stable system is $" + str(round(coffee_price(percentage_serviced, stableQ.uniformL, stableQ.uniformH),2)))

    return stableQ

#Prints optimal coffee price for given problem parameters and stable Q parameter
def optimal_coffee_price(challenge, stable):

    revenue = 0
    optimal_coffee_price = 0

    #calculate coffee price that maximizes the revenue
    for i in range(1, int(stable.arrival_rate)+1):
        percentage = i / challenge.arrival_rate
        coffee_price = challenge.uniformH - (challenge.uniformH - challenge.uniformL) * percentage
        if i * coffee_price >= revenue:
            revenue = i * coffee_price
            optimal_coffee_price = coffee_price
    print("The optimal coffee price is $" + str(round(optimal_coffee_price,2)) + ".")
    
#Challenge parameters (Customer arrival rate, service rate, expected service time, willingness to pay-Uniform lower bound, willingness to pay-Uniform lower bound)
#Change problem parameters here***
challenge = MM1Queue(50, 2, 5, 2, 5)

#Creates a stable arrival object with given parameters and solves the M/M/1 queue
stableQ = stable_arrival_rate(challenge)
print("Average number in System - Ls: " + str(round(stableQ.ls(),2)))
print("Average number in Queue - Lq: " + str(round(stableQ.lq(),2)))
print("Average time in System - Ws: " + str(round(stableQ.ws(),2)))
print("Average time in Queue - Wq: " + str(round(stableQ.wq(),2)))

#Prints the coffee price that maximizes the revenue
optimal_coffee_price(challenge, stableQ)
