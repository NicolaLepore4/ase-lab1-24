from flask import Flask, request, make_response, jsonify
import random as rnd


app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST

#Endpoint /sub for subtraction which takes a and b as query parameters.
@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a-b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /mul for multiplication which takes a and b as query parameters.
@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a*b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /div for division which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a/b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /mod for modulo which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a%b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /random which takes a and b as query parameters and returns a random number between a and b included. Returns HTTP 400 BAD REQUEST if a is greater than b.
@app.route('/random')
def random():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if (a < b):
        return make_response(jsonify(s = rnd.randint(a,b)), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
    

# /upperwhichgiven the string a it returns it in a JSON all in uppercase.
# /lowerwhichgiven the string a it returns it in a JSON all in lowercase.
# /concatwhichgiven the strings a and b it returns in a JSON the concatenation of them.
# /reducewhichtakes the operator op (one of add, sub, mul, div, upper, lower, concat) and a lst string
 representing a list and apply the operator to all the elements giving the result. For instance, 
/reduce?op=add&lst=[2,1,3,4]returnsa JSON containing {s=10}, meaning 2+1+3+4.
 ▪ /crashwhichterminates the service execution after responding to the client with info about the host and 
the port of the service.
 ▪ /lastwhichreturnsa string representing the last operation requested with success, in the format 
op(args)=res, e.g. add(2.0,3.0)=5.0 or reduce(‘add’,[2,1,3,4])=10 or rand(1,3)=2. It answers with 
HTTP code 404 if no operation was performed.





if __name__ == '__main__':
    app.run(debug=True)