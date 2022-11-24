class Match:
    def __init__(self,team):
        print("5..4..3..2..1.. Play !!!")
        nlist=team.split('-')
        self.bat=nlist[0]
        self.bowl=nlist[1]
        self.run=0
        self.wicket=0

    def add_run(self,run):
        self.run+=run

    def add_over(self,over):
        if over>=5:
            print(f"Warning! Cannot add {over} over/s (5 over match)")
        else:
            self.over=over
    def print_scoreboard(self):
        return f"Batting Team: {self.bat}\nBowling Team: {self.bowl}\nTotal Runs: {self.run} Wickets: {self.wicket} Overs: {self.over}"

    def add_wicket(self,wicket):
        self.wicket+=wicket









match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())
