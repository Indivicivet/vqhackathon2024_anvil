from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
from anvil_extras import augment

class main(mainTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
  
    augment.set_event_handler(self.magic_text_box, "keydown", self.keydown_handler)

  def spin_both(self, d):
    anvil.server.call(
      "both_split",
      d=d,
      t=1,
      sl=self.spin_speed_slider.value * min(1, 1 - self.balance_slider.value),
      sr=self.spin_speed_slider.value * min(1, 1 + self.balance_slider.value),
    )
  
  def spin_motors_click(self, **event_args):
    self.spin_both("f")

  def spin_both_backward_click(self, **event_args):
    self.spin_both("r")
    
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
      self.spin_both("f")
    elif key == "s":
      self.spin_both("r")
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

  def balance_slider_change(self, handle, **event_args):
    self.spin_factor_showval.text = f"{self.balance_slider.value:.2f}"

  def spin_speed_slider_change(self, handle, **event_args):
    self.spin_speed_showval.text = str(int(self.spin_speed_slider.value))

  def turn_sens_slider_change(self, handle, **event_args):
    self.turn_sens_showval.text = str(int(self.turn_sens_slider.value))

  def spin_time_slider_change(self, handle, **event_args):
    self.spin_time

