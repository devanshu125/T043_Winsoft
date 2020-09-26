from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route("/decoded", methods=["GET", "POST"])
def decoded():
    # msg = list(request.form.values())
    msg = [str(i) for i in request.form.values()]
    print(msg)
    x, key = msg[0], msg[1]
    from model import eval
    e = eval()

    ret_message, total_cost_dict, loc_list = e.run(x, key)

    camps = []
    total_cost_list = []

    for camp, total_cost in total_cost_dict.items():
        if camp not in loc_list:
            camps.append(camp)
            total_cost_list.append(total_cost)


    return render_template("decoded_msg.html", solution_text=ret_message, camps=camps, total_cost_list=total_cost_list, legend="Cost (Total Distance)")



@app.route("/ps")
def ps():
    return render_template("ps.html")

@app.route("/simplechart")
def chart():
    return render_template("chart.html")

if __name__ == "__main__":
    app.run(debug=True)
