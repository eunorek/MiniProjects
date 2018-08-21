class VendingMachine:
    def __init__(self):
        self.change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔돈":
            return "잔돈은 %d 원입니다" %self.change
        elif cmd == "동전":
            coin = params[0]
            self.change += coin
            return "inserted %d won" %coin
