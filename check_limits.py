class BatteryMonitor:
    def __init__(self):
        self.warning_config = {'temperature': True, 'soc': True, 'charge_rate': True}

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val if min_val is not None else value <= max_val

    def is_approaching_limit(self, value, min_val, max_val, tolerance):
        lower_approaching = min_val is not None and min_val <= value < min_val + tolerance
        upper_approaching = max_val - tolerance < value <= max_val
        return lower_approaching or upper_approaching

    def calculate_tolerance(self, value):
        return value * 0.05

    def should_warn(self, limit_type, value, min_val, max_val, tolerance):
        """
        Determines if a warning should be issued for approaching the limit of a given parameter.
        """
        return self.warning_config[limit_type] and self.is_approaching_limit(value, min_val, max_val, tolerance)

    def check_limits(self, value, min_val, max_val, tolerance, limit_type):
        if not self.is_within_range(value, min_val, max_val):
            print(f'{limit_type.capitalize()} is out of range!')
            return False
        if self.should_warn(limit_type, value, min_val, max_val, tolerance):
            print(f'Warning: Approaching {limit_type} limit')
        return True

    def battery_is_ok(self, temperature, soc, charge_rate):
        temp_ok = self.check_limits(temperature, 0, 45, self.calculate_tolerance(45), 'temperature')
        soc_ok = self.check_limits(soc, 20, 80, self.calculate_tolerance(80), 'soc')
        charge_rate_ok = self.check_limits(charge_rate, None, 0.8, self.calculate_tolerance(0.8), 'charge_rate')
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
    monitor.configure_warnings(temperature=False)
