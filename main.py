from model import todo_model
from view import todo_view
from controller import todo_controller

if __name__ == "__main__":
    model = todo_model()
    view = todo_view()
    controller = todo_controller(model, view)

    controller.run()
