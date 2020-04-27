# King's Defense Server Functions

Welcome to the King's Defense server code ropositery. Here we will create Python code to be the server for the [Scratch project (https://scratch.mit.edu/studios/5805912/)](https://scratch.mit.edu/studios/5805912/). The server will run on a Raspberry Pi 3B+.

Setup
------
1. Install Python v3.8.
1. Install [PyAutoGUI (https://pypi.org/project/PyAutoGUI/)](https://pypi.org/project/PyAutoGUI/). This allows the Python code interact with the scratch project by moving the mouse and typing.
1. Clone the repositery by copying the https or ssh key in GitHub.

Contributing
------
+ Always pull the latest commit before editing.
+ Always push your changes straight after you've finished editing.
+ Use comments where necessary.
+ Want to chat about new features? Do so at https://github.com/users/ScratcherOfWorld/projects/1#column-8490040.

How it Works
------
1. Whenever you buy a card or place a troop a request gets made.
1. The request starts with the id of the request (e.g. Buy card is 4) followed by any paramaters (e.g. the index of the card buying might be 5) with fixed lengths (e.g. 2 so the paramater would be 05).
1. The request is then put into a cloud variable (e.g. serverSend) with the request id and the paramaters (In this case 405).
1. The server is constantly reading the variable and sees your request and your username.
1. The server then processes the request (e.g. Add the card to a list of your cards). If the request needs a return (e.g. Get Coins) then the server sends a message back to the client in a similar way but with the client's encoded username first.
1. The server clears the cloud variable for other requests.

Client send: https://github.com/users/ScratcherOfWorld/projects/1#column-8485755

Server send: https://github.com/users/ScratcherOfWorld/projects/1#column-8485805
