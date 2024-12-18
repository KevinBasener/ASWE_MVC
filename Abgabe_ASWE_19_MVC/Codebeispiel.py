# Model
class Model:
    def __init__(self):
        self.data = "Initial Data"

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

# View
class View:
    def render(self, data):
        print(f"Data: {data}")

    def update(self, data):
        self.render(data)

# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle(self):
        self.view.render(self.model.get_data())

    def update(self, data):
        self.model.set_data(data)
        self.view.update(self.model.get_data())

# Anwendung
if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    # Initiale Anzeige
    controller.handle()

    # Daten aktualisieren
    controller.update("Neue Daten")