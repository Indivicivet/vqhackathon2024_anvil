from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
from anvil_extras import augment

class main(mainTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
  
    augment.set_event_handler(self.magic_text_box, "keydown", self.keydown_handler)
  
  def spin_motors_click(self, **event_args):
    anvil.server.call("both", "f", t=1, s=self.spin_speed_slider.value)

  def spin_both_backward_click(self, **event_args):
    anvil.server.call("both", "r", t=1, s=self.spin_speed_slider.value)
    
  def leftturn_click(self, **event_args):
    anvil.server.call("left_turn", s=self.turn_sens_slider.value)

  def rightturn_click(self, **event_args):
    anvil.server.call("right_turn", s=self.turn_sens_slider.value)

  def left_forward_click(self, **event_args):
    anvil.server.call("left_only", "f", s=self.turn_sens_slider.value)

  def right_forward_click(self, **event_args):
    anvil.server.call("right_only", "f", s=self.turn_sens_slider.value)

  def left_back_click(self, **event_args):
    anvil.server.call("left_only", "r", s=self.turn_sens_slider.value)

  def right_back_click(self, **event_args):
    anvil.server.call("right_only", "r", s=self.turn_sens_slider.value)
  
  def keydown_handler(self, **event_args):
    key_code = event_args.get('key_code')
    key = event_args.get('key')
    print(key, key_code)
    if key == "w":
      anvil.server.call("both", "f", s=self.spin_speed_slider.value)
    elif key == "s":
      anvil.server.call("both", "r", s=self.spin_speed_slider.value)
    elif key == "q":
      anvil.server.call("left_only", "f", s=self.turn_sens_slider.value)
    elif key == "e":
      anvil.server.call("right_only", "f", s=self.turn_sens_slider.value)
    elif key == "z":
      anvil.server.call("left_only", "r", s=self.turn_sens_slider.value)
    elif key == "c":
      anvil.server.call("right_only", "r", s=self.turn_sens_slider.value)
    elif key == "a":
      anvil.server.call("left_turn", s=self.turn_sens_slider.value)
    elif key == "d":
      anvil.server.call("right_turn", s=self.turn_sens_slider.value)
    elif key == "w":
      anvil.server.call("run1s", s=self.turn_sens_slider.value)
    else:
      ...

