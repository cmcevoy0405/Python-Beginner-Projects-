Title: Game Slot Machine
Video Demo: https://www.youtube.com/watch?v=hB6vL5NJarc&ab_channel=Callummcevoy
Description:
The project has drawn inspiration from slot machines found at casinos. It allows the user to input any amount of money they wish. It then allows them to bet on however many lines they wish varying from one to three. The user is then asked how much money they would like to bet on each line therefore allowing them to bet more on certain lines.

 A random 3x3 matrix of symbols is then produced, if a row matches the user wins. Four different Symbols are stored in two dictionaries, one of which assigns the number of times the symbol can appear in the matrix. The rarest symbol can appear four times while the most common can appear ten times. The second dictionary applies a multiplayer to the symbol. The most common symbol has a multiplayer of two and the rarest symbol has a multiplayer of 8.

  If the user wins the amount won is added to their current balance and returned. If not the user is shown their current balance. If the user's balance has fallen below the minium bet of £5 then they are told they cannot continue to play. If the user has sufficient balance they are asked if they would like to play again which will carry over their current balance to the next game.

  Sufficient effort has been taking to control user error by not quitting the program but prompting them again when the input and invalid response.

I have tested three functions in a separate file of which of which i found difficult to mock the inputs. I overcame this by defining functions that mocked input and passed them through.
