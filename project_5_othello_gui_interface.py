# Shanaya Ukuwela. ID: 56649043

import tkinter
from project_5_othello_game_logic import Othello




class Handle_User_Input:
    def __init__(self):

        self._input_window = tkinter.Tk()
        self._input_window.wm_title("Othello")

        rowlabel = tkinter.Label(self._input_window, text = "Number of Rows", font = ('Helvetica', 12))
        rowlabel.grid(row=0)
        columnlabel = tkinter.Label(self._input_window, text = "Number of Columns", font = ('Helvetica', 12))
        columnlabel.grid(row=1)
        firstplayerlabel = tkinter.Label(self._input_window, text = "First Player", font = ('Helvetica', 12))
        firstplayerlabel.grid(row=2)
        topleftdisclabel = tkinter.Label(self._input_window, text = "Top Left Disc in Center", font = ('Helvetica', 12))
        topleftdisclabel.grid(row=3)
        howtowinlabel = tkinter.Label(self._input_window, text = "How to Win (> or <)", font = ('Helvetica', 12))
        howtowinlabel.grid(row=4)

        self._row = tkinter.Spinbox(self._input_window, values=(4,6,8,10,12,14,16))
        self._row.grid(row=0, column=1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._column = tkinter.Spinbox(self._input_window, values=(4,6,8,10,12,14,16))
        self._column.grid(row=1, column=1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._first_player = tkinter.Spinbox(self._input_window, values=('B','W'))
        self._first_player.grid(row=2,column=1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._top_left = tkinter.Spinbox(self._input_window, values=('B','W'))
        self._top_left.grid(row=3, column=1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._how_to_win = tkinter.Spinbox(self._input_window, values=('<','>'))
        self._how_to_win.grid(row=4, column=1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        ok_button = tkinter.Button(master = self._input_window, text = "OK", command = self.okay).grid(row=5, column=0)
        quit_button = tkinter.Button(master = self._input_window, text = "QUIT", command = self.quit).grid(row=5, column=1, pady=4)

        self._input_window.rowconfigure(0, weight = 1)
        self._input_window.rowconfigure(1, weight = 1)
        self._input_window.rowconfigure(2, weight = 1)
        self._input_window.rowconfigure(3, weight = 1)
        self._input_window.rowconfigure(4, weight = 1)
        self._input_window.columnconfigure(0, weight = 1)
        self._input_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False

        self._input_window.mainloop()

    def quit(self):
        """Closes input window"""
        self._input_window.destroy()

    def okay(self):
        """Closes input window and opens up game board window"""
        self._ok_clicked = True
        self.row = int(self._row.get())
        self.column = int(self._column.get())
        self.first_player = self._first_player.get()
        self.top_left = self._top_left.get()
        self.how_to_win = self._how_to_win.get()

        self._input_window.destroy()

class Board:
    def __init__(self, game, row, column):

        self._game = game
        self._board = game._board
        self._rowlength = row
        self._columnlength = column
        self.row_move = 0
        self.col_move = 0
        
        self._root_window = tkinter.Tk()
        self._root_window.wm_title('Othello')
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 500,
            background = "green")

        self._canvas.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        rules = tkinter.Label(
            self._root_window, text = 'FULL',
            font = ('Helvetica', 20))
        rules.grid(row = 0, column = 0, sticky = tkinter.E)

        title = tkinter.Label(self._root_window, text = 'Welcome to Othello!',
                              font = ('Helvetica', 20))
        title.grid(row = 0, column = 0, sticky = tkinter.N)

        self._score_text = tkinter.StringVar()
        self._score_text.set(self._game.track_discs())

        score = tkinter.Label(
            master = self._root_window, textvariable = self._score_text,
            font = ('Helvetica', 12))
        score.grid(row = 1, column = 0)

        self._turn_text = tkinter.StringVar()
        self._turn_text.set(self._game.display_turn())

        turn = tkinter.Label(
            master = self._root_window, textvariable = self._turn_text,
            font = ('Helvetica', 12))
        turn.grid(row = 2, column = 0)

        self._winner_text = tkinter.StringVar()

        winner = tkinter.Label(
            master = self._root_window, textvariable = self._winner_text,
            font = ('Helvetica', 12))
        winner.grid(row = 3, column = 0)

        play_again_button = tkinter.Button(
            master = self._root_window, text = "Play Again?",
            command = self.play_again)
        play_again_button.grid(row=0, column=0, sticky = tkinter.W)
        self._play_again_clicked = False

        quit_button = tkinter.Button(
            master = self._root_window, text = "Quit",
            command = self.quit)
        quit_button.grid(row = 1, column = 0, sticky = tkinter.W)


        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)


        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)

        

    def start(self) -> None:
        self._root_window.mainloop()

    def play_again(self) -> None:
        self._play_again_clicked = True
        self._root_window.destroy()
        user_interface()

    def quit(self) -> None:
        self._root_window.destroy()


    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_board()

    def _draw_board(self):
        self._canvas.delete(tkinter.ALL)
        
        column_width_frac = 1/self._columnlength
        row_height_frac = 1/self._rowlength

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        for x in range(self._columnlength):
            for y in range(self._rowlength):
                if self._board[y][x] == 'B':
                    x1 = x * column_width_frac
                    y1 = y * row_height_frac
                    x2 = x1 + column_width_frac
                    y2 = y1 + row_height_frac
                    self._canvas.create_rectangle(
                        x1 * canvas_width,
                        y1 * canvas_height,
                        x2 * canvas_width,
                        y2 * canvas_height,
                        fill = 'green')
                    self._canvas.create_oval(
                        x1 * canvas_width,
                        y1 * canvas_height,
                        x2 * canvas_width,
                        y2 * canvas_height,
                        fill = 'black')
                elif self._board[y][x] == 'W':
                    x1 = x * column_width_frac
                    y1 = y * row_height_frac
                    x2 = x1 + column_width_frac
                    y2 = y1 + row_height_frac
                    self._canvas.create_rectangle(
                        x1 * canvas_width,
                        y1 * canvas_height,
                        x2 * canvas_width,
                        y2 * canvas_height,
                        fill = 'green')
                    self._canvas.create_oval(
                        x1 * canvas_width,
                        y1 * canvas_height,
                        x2 * canvas_width,
                        y2 * canvas_height,
                        fill = 'white')
                else:
                    x1 = x * column_width_frac
                    y1 = y * row_height_frac
                    x2 = x1 + column_width_frac
                    y2 = y1 + row_height_frac
                    self._canvas.create_rectangle(
                        x1 * canvas_width,
                        y1 * canvas_height,
                        x2 * canvas_width,
                        y2 * canvas_height,
                        fill = 'green')

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        click_point = (event.x / canvas_width, event.y / canvas_height)

        self.handle_click_row(click_point)
        self.handle_click_column(click_point)
        self._score_text.set(self._game.track_discs())

        try:
            if self._game.any_spaces() == True:
                self._game.reset_all_pieces_to_flip()
                row = self.row_move + 1
                column = self.col_move + 1
                if self._game.is_move_on_board(row,column) == True:
                    self._game.check_all_directions(row, column)
                    if self._game.is_valid_move() == True:
                        self._game.flip_pieces()
                        self._score_text.set(self._game.track_discs())
                        self._draw_board()
                        self._game.switch_turns()
                        if self._game.any_spaces() == False:
                            self._game.switch_turns()
                            if self._game.any_spaces() == False:
                                self._winner_text.set(self._game.who_wins())
                                self._turn_text.set("")
                            else:
                                self._turn_text.set(self._game.display_turn())
                        else:
                            self._turn_text.set(self._game.display_turn())
                elif self._game.is_move_on_board(row,column) == False:
                    pass
            elif self._game.any_spaces() == False:
                self._winner_text.set(self._game.who_wins())
                self._turn_text.set("")
        except:
            if self._game.any_spaces() == False:
                self._winner_text.set(self._game.who_wins())
                self._turn_text.set("")

    def handle_click_row(self, click_point) -> None:
        self.row_move = 0
        self.row_move = int(click_point[1] * self._rowlength)

    def handle_click_column(self, click_point) -> None:
        self.col_move = 0
        self.col_move = int(click_point[0] * self._columnlength)



def user_interface():
    user_input = Handle_User_Input()
    if user_input._ok_clicked == True:
        game = Othello(user_input.row, user_input.column, user_input.first_player, user_input.top_left, user_input.how_to_win)
        game.start_game_board()
        gui_board = Board(game, user_input.row, user_input.column)
        gui_board.start()
    else:
        pass


if __name__=='__main__':
    user_interface()








    
