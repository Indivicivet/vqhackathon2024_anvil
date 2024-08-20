from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def spin_motors_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("run1s")

  def leftturn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("leftturn")

  def rightturn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("rightturn")
