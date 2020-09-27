from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def home():
    return render_template('index.html')



@app.route("/decoded", methods=["GET", "POST"])
def decoded():
    # msg = list(request.form.values())
    #import os
    # if os.path.exists("static/result/temp.png"):
        #print("YESSSSSS")
    # os.remove("static/result/temp.png")
    msg = [str(i) for i in request.form.values()]
    print(msg)
    x, key = msg[0], msg[1]
    from model import eval
    e = eval()

    ret_message, total_cost_dict, loc_list = e.run(x, key)

    if ret_message == None:
        from error import apology
        return apology("NA TRY AGAIN", 400)
    else:
        camps = []
        total_cost_list = []

        for camp, total_cost in total_cost_dict.items():
            if camp not in loc_list:
                camps.append(camp)
                total_cost_list.append(total_cost)

        return render_template("decoded_msg.html", solution_text=ret_message, camps=camps, total_cost_list=total_cost_list, legend="Cost (Total Distance)")

"""

@app.after_request
def add_header(response):
    print("----------x----------x--------------")
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

"""



@app.route("/ps")
def ps():
    return render_template("ps.html")


if __name__ == "__main__":
    app.run(debug=True)
