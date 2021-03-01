# Mazer  
Mazer is a random maze generator, made with python3 and Flask Framework.

## Heroku app
You can try Mazer here: https://sp-mazer.herokuapp.com/

- choose width and height for the maze.
- seed is optional.
- click the Generate button to generate the labyrinth.
- click the Solution button at the bottom to show the solution path.

## Console mode
Launch console_mode.py to run Mazer in a console.

Console Commands are :
- **quit** : to quit the program.
- **gen** : to generate another maze.
- **solve** : to solve the maze.
- **save** : to create a txt file of the maze (! the previous will be over-written).

## Localhost mode
Fork it, clone it and create a virtual env.
It requires to install the modules from requirement.txt : ```pip install -r requirements.txt```
launch run_app.py and open your web browser at http://localhost:5000 to run Mazer in a web page.
