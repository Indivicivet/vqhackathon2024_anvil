from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
from anvil_extras import augment

class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    augment.set_event_handler(self, "keydown", self.keydown_handler)
    
  def spin_motors_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("run1s")

  def leftturn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("left_turn")

  def rightturn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("right_turn")

#augment.set_event_handler(self.text_box, 'keydown', self.text_box_keydown)

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