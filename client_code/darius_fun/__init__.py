from ._anvil_designer import darius_funTemplate
from anvil import *
import anvil.server


class darius_fun(darius_funTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
