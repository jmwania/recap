import collections

class Binary:
    def __int__(self, value=0):
        if isinstance(value, collections.Sequence):
            if len(value) > 2 and value[0:2] == 'b':
                self._value = int(value, base=2)
            elif len(value) > 2 and value [0:2] =='0x':
            self._value = int(value, base=16)
            else:
                self._value = int(''.join([str(i) for i in value]), base=2)
        else:
            try:
                self._value = int(value)
                if self._value < 0:
                    raise ValueError("Binary cannot acceptnegative numbers. Use SizedBInary instead")
            execept ValueError:

                 raise ValueError("Cannot convert value {} to Binary".format(value))


def __int__(self):
    return self.value
                