class BatteryMonitor:
    def __init__(self):
        self.warning_config = {
            'temperature': True,
            'soc': True,
            'charge_rate': True,
        }

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val

    def is_approaching_limit(self, value, min_val, max_val, tolerance):
        return (min_val <= value < min_val + tolerance) or (max_val - tolerance < value <= max_val)

    def calculate_tolerance(self, value):
        return value * 0.05

    def check_temp_limit(self, temperature):
        min_temp = 0
        max_temp = 45
        tolerance = self.calculate_tolerance(max_temp)
        
        if not self.is_within_range(temperature, min_temp, max_temp):
            print('Temperature is out of range!')
            return False
        if self.warning_config['temperature'] and self.is_approaching_limit(temperature, min_temp, max_temp, tolerance):
            print('Warning: Approaching temperature limit')
        return True

    def check_soc_limit(self, soc):
        min_soc = 20
        max_soc = 80
        tolerance = self.calculate_tolerance(max_soc)
        
        if not self.is_within_range(soc, min_soc, max_soc):
            print('SOC is out of range!')
            return False
        if self.warning_config['soc'] and self.is_approaching_limit(soc, min_soc, max_soc, tolerance):
            print('Warning: Approaching SOC limit')
        return True

    def check_charge_rate_limit(self, charge_rate):
        max_charge_rate = 0.8
        tolerance = self.calculate_tolerance(max_charge_rate)
        
        if charge_rate > max_charge_rate:
            print('Charge rate is out of range!')
            return False
        if self.warning_config['charge_rate'] and charge_rate > (max_charge_rate - tolerance):
            print('Warning: Approaching charge rate limit')
        return True

    def battery_is_ok(self, temperature, soc, charge_rate):
        temp_ok = self.check_temp_limit(temperature)
        soc_ok = self.check_soc_limit(soc)
        charge_rate_ok = self.check_charge_rate_limit(charge_rate)
        return temp_ok and soc_ok and charge_rate_ok

    def configure_warnings(self, temperature=True, soc=True, charge_rate=True):
        """
        Configures the warning settings for the battery monitor system. 
        This function allows the user to enable or disable warnings for temperature, state of charge (SOC), and charge rate based on the parameters passed.
        """
        self.warning_config['temperature'] = temperature
        self.warning_config['soc'] = soc
        self.warning_config['charge_rate'] = charge_rate

if __name__ == '__main__':
    monitor = BatteryMonitor()
    monitor.configure_warnings(temperature=False)  # Example configuration to disable temperature warnings
