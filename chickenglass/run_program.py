from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__, template_folder=r'C:\Users\Lenovo\Desktop\chickenglass')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_program", methods=["POST"])
def run_program():
    data = request.get_json()
    project_dir = data["projectDir"]
    output_dir = data["outputDir"]

    # 调用你的Python程序并运行
    try:
        result = subprocess.check_output(["python", "chickenglass.py", project_dir, output_dir], stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"运行程序时发生错误：{e.output}", 500

if __name__ == "__main__":
    app.run(debug=True)