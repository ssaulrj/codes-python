class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  pass
  def get_rate(self):
    return (.001 * self.price_of_insured_item)

class HomeInsurance(InsurancePolicy):
  pass
  def get_rate(self):
    return (.00005 * self.price_of_insured_item)
