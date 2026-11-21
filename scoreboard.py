from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.pu()
        self.goto(y=270, x=0)
        self.score = 0
        with open("data.txt", "r") as f:
            self.high_score = int(f.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Courier", 20, "bold"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as ff:
                ff.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over 😥!!", False, "center", ("Courier", 25, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
