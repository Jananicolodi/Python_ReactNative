from unittest.mock import Mock

json = Mock()

json.load()
json.load()

json.load.assert_called_with()
