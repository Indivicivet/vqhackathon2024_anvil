from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
from anvil_extras import augment

class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    augment.set_event_handler(self.magic_text_box, "keydown", self.keydown_handler)
    
  def spin_motors_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("both", "f", t=1)

  def leftturn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("left_turn")

  def rightturn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("right_turn")

  def left_forward_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("left_only", "f")

  def right_forward_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("right_only", "f")

  def left_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("left_only", "r")

  def right_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("right_only", "r")
  
  def keydown_handler(self, **event_args):
    key_code = event_args.get('key_code')
    key = event_args.get('key')
    print(key, key_code)
    if key == "w":
      anvil.server.call("both", "f")
    elif key == "s":
      anvil.server.call("both", "r")
    elif key == "q":
      anvil.server.call("left_only", "f")
    elif key == "e":
      anvil.server.call("right_only", "f")
    elif key == "z":
      anvil.server.call("left_only", "r")
    elif key == "c":
      anvil.server.call("right_only", "r")
    elif key == "a":
      anvil.server.call("left_turn")
    elif key == "d":
      anvil.server.call("right_turn")
    elif key == "w":
      anvil.server.call("run1s")
    else:
      ...