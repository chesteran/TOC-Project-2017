from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'hello'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'hey bitch'
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'yo whats up'
    def is_going_to_state1to1(self, update):
        text = update.message.text
        return text.lower() == 'how much'
    def is_going_to_state1to2(self, update):
        text = update.message.text
        return text.lower() == 'but you look like a whore'
    def is_going_to_state2to1(self, update):
        text = update.message.text
        return text.lower() == 'dont be so mean'
    def is_going_to_state3to1(self, update):
        text = update.message.text
        return text.lower() == '5000?'
    def on_enter_state1(self, update):
        update.message.reply_text("nice to meet you")
      #  self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("fuck off")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
    def on_enter_state3(self, update):
        update.message.reply_text("whats up")
       # self.go_back(update)
    def on_exit_state3(self, update):
        print('Leaving state3')	
    def on_enter_state1to1(self, update):
        update.message.reply_text("i'm not a bitch")
       # self.go_back(update)
    def on_exit_state1to1(self, update):
        print('Leaving state1to1')
    def on_enter_state1to2(self, update):
        update.message.reply_text("you dirty pig, get away from me")
        self.go_back(update)
    def on_exit_state1to2(self, update):
        print('Leaving state1to2')
    def on_enter_state2to1(self, update):
        update.message.reply_text("i'll call the police")
        self.go_back(update)

    def on_exit_state2to1(self, update):
        print('Leaving state2to1')
    def on_enter_state3to1(self, update):
        update.message.reply_text("i am not cheap!10000!")
        self.go_back(update)

    def on_exit_state3to1(self, update):
        print('Leaving state3to1')