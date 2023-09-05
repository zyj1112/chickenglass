# Chickenglass
It's an improvement on the original [chickenglass](https://github.com/chaoxu/chickenglass) which is the project of the undergraduate innovation and entrepreneurship project given to me by my tutor [Prof. Xu](https://github.com/chaoxu). And there is a blog for why chickenglass is developed and more [information](https://hackmd.io/LoFPSapEQhWjBfCFVfytVQ) about it

# Function
* A blog\notes writing tools for mathematicians
* Convert markdown to html
* Basic structural information system such as headings
* Mathematical symbols and formulas
* Internal and external references
* If the markdown file changes, the output html file can change at any time
* Add some simple graphical interfaces instead of terminal

# Test
* First you should install python requirements and Pandoc
* Make sure to set the appropriate environment variables
* Then you can run the `run_program.py`
* Entering the corresponding page, input your input_dir and output_dir

# RoadMap
* Using Pandoc to Convert markdown to html
* Add Tex macro（The first two parts refer to the code of the chickenglass project, and these codes have provided me with great help）
* Add a "refreshing" plugin(I implemented this function with python's watchgod and time，and you can use livereload)
* Add a simple graphical interface（To be honest, this function is a bit redundant, because we can use the terminal to complete the corresponding things）
