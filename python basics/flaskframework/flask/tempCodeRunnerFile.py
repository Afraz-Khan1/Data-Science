
@app.route("/success")
def success():
    return render_template('success.html',result={"phy":56,"chem":60,"maths":40})
