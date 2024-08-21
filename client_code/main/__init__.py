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
      t=self.spin_time_slider.value,
      sl=self.spin_speed_slider.value * min(1, 1 - self.balance_slider.value),
      sr=self.spin_speed_slider.value * min(1, 1 + self.balance_slider.value),
    )

  def single_wheel_turn(self, func_name, d):
      anvil.server.call(
        func_name,
        d,
        t=self.turn_time_slider.value,
        s=self.turn_sens_slider.value,
      )

  def two_wheel_turn(self, func_name):
    anvil.server.call(
      func_name,
      t=self.turn_time_slider.value,
      s=self.turn_sens_slider.value,
    )
  
  def spin_motors_click(self, **event_args):
    self.spin_both("f")

  def spin_both_backward_click(self, **event_args):
    self.spin_both("r")
    
  def leftturn_click(self, **event_args):
    self.two_wheel_turn("left_turn")

  def rightturn_click(self, **event_args):
    self.two_wheel_turn("right_turn")

  def left_forward_click(self, **event_args):
    self.single_wheel_turn("left_only", "f")

  def right_forward_click(self, **event_args):
    self.single_wheel_turn("right_only", "f")

  def left_back_click(self, **event_args):
    self.single_wheel_turn("left_only", "r")

  def right_back_click(self, **event_args):
    self.single_wheel_turn("right_only", "r")
  
  def keydown_handler(self, **event_args):
    key_code = event_args.get('key_code')
    key = event_args.get('key')
    print(key, key_code)
    if key == "w":
      self.spin_both("f")
    elif key == "s":
      self.spin_both("r")
    elif key == "q":
      self.single_wheel_turn("left_only", "f")
    elif key == "e":
      self.single_wheel_turn("right_only", "f")
    elif key == "z":
      self.single_wheel_turn("left_only", "r")
    elif key == "c":
      self.single_wheel_turn("right_only", "r")
    elif key == "a":
      self.two_wheel_turn("left_turn")
    elif key == "d":
      self.two_wheel_turn("right_turn")
    else:
      ...

  def balance_slider_change(self, handle, **event_args):
    self.spin_factor_showval.text = f"{self.balance_slider.value:.2f}"

  def spin_speed_slider_change(self, handle, **event_args):
    self.spin_speed_showval.text = str(int(self.spin_speed_slider.value))

  def turn_sens_slider_change(self, handle, **event_args):
    self.turn_sens_showval.text = str(int(self.turn_sens_slider.value))

  def spin_time_slider_change(self, handle, **event_args):
    self.spin_time_showval.text = f"{self.spin_time_slider.value:.2f}"

  def turn_time_slider_change(self, handle, **event_args):
    self.turn_time_showval.text = f"{self.turn_time_slider.value:.2f}"

