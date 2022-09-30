from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[{
    "id":1,

    "Contact":u"9987650324",
    "Name":u"Shawn",
    "done":False
},
{
    "id":2,

    "Contact":u"9653075067",
    "Name":u"Jack",
    "done":False
    
}
]
@app.route("/")
def hello_world():
    return"hello world"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400
        )
    Contact={
        "id":tasks[-1]["id"]+1,

        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    tasks.append(Contact)
    return jsonify({
        "status":"success",

        "message":"task add successfuly"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if(__name__=="__main__"):
    app.run(debug=True)